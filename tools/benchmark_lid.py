#!/usr/bin/env python3
"""
Benchmark prediction speed for language identification models on CommonLID text.

Measures wall-clock time for each model to classify N text samples.
Reports samples/second and total time for fair comparison.

Usage:
    python3 tools/benchmark_lid.py [--limit 10000]
"""

import argparse
import gzip
import subprocess
import sys
import time


def load_samples(path, limit):
    """Load text samples from CommonLID TSV.gz."""
    samples = []
    with gzip.open(path, 'rt', encoding='utf-8') as f:
        next(f)  # skip header
        for i, line in enumerate(f):
            if limit and i >= limit:
                break
            parts = line.split('\t')
            if len(parts) >= 2:
                samples.append(parts[0])
    return samples


def bench_cld2(texts, binary="tools/cld2_detect"):
    """Benchmark CLD2 via CLI binary."""
    input_text = "\n".join(t.replace("\n", " ").replace("\r", " ") for t in texts)
    # Warmup
    subprocess.run([binary], input=input_text[:10000], capture_output=True,
                   text=True, timeout=60)
    t0 = time.perf_counter()
    subprocess.run([binary], input=input_text, capture_output=True,
                   text=True, timeout=600)
    t1 = time.perf_counter()
    return t1 - t0


def bench_fasttext(texts, model_name):
    """Benchmark a fasttext model."""
    from huggingface_hub import hf_hub_download
    import fasttext

    configs = {
        "glotlid": ("cis-lmu/glotlid", "model.bin"),
        "openlid-v3": ("HPLT/OpenLID-v3", "openlid-v3.bin"),
    }
    repo_id, filename = configs[model_name]
    path = hf_hub_download(repo_id=repo_id, filename=filename)
    model = fasttext.load_model(path)

    cleaned = [t.replace("\n", " ").replace("\r", " ") for t in texts]
    # Warmup
    model.predict(cleaned[:100])
    t0 = time.perf_counter()
    model.predict(cleaned)
    t1 = time.perf_counter()
    return t1 - t0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/evaluation/commonlid.tsv.gz")
    parser.add_argument("--limit", type=int, default=10000)
    parser.add_argument("--binary", default="tools/cld2_detect")
    args = parser.parse_args()

    print(f"Loading {args.limit} samples...", file=sys.stderr)
    texts = load_samples(args.data, args.limit)
    n = len(texts)
    print(f"Loaded {n} samples", file=sys.stderr)

    # Compile CLD2
    subprocess.run(["make", "tools/cld2_detect"], capture_output=True, text=True)

    results = []

    # CLD2
    print("Benchmarking CLD2...", file=sys.stderr)
    dt = bench_cld2(texts, args.binary)
    results.append(("cld2", dt))
    print(f"  CLD2: {dt:.3f}s ({n/dt:.0f} samples/s)", file=sys.stderr)

    # GlotLID
    print("Benchmarking GlotLID...", file=sys.stderr)
    dt = bench_fasttext(texts, "glotlid")
    results.append(("glotlid", dt))
    print(f"  GlotLID: {dt:.3f}s ({n/dt:.0f} samples/s)", file=sys.stderr)

    # OpenLID-v3
    print("Benchmarking OpenLID-v3...", file=sys.stderr)
    dt = bench_fasttext(texts, "openlid-v3")
    results.append(("openlid-v3", dt))
    print(f"  OpenLID-v3: {dt:.3f}s ({n/dt:.0f} samples/s)", file=sys.stderr)

    # Print results
    print(f"\n{'model':<15} {'time_s':>8} {'samples_per_s':>14} {'us_per_sample':>14}")
    print("-" * 55)
    for name, dt in results:
        sps = n / dt
        us = dt / n * 1e6
        print(f"{name:<15} {dt:>8.3f} {sps:>14.0f} {us:>14.1f}")


if __name__ == "__main__":
    main()
