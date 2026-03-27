#!/usr/bin/env python3
"""CLD2 Benchmark Tool

Measures language detection speed on HTML pages extracted from Common Crawl WARC files.
Designed to be reusable across CLD2 variants for tracking performance improvements.

Usage:
    python benchmark_cld2.py --warc <path> [OPTIONS]
"""

import argparse
import csv
import os
import statistics
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


def extract_html_pages(warc_path: str, num_pages: int) -> list:
    """Extract HTML page bodies from WARC file.

    Returns list of (html_bytes, content_length) tuples.
    Only selects HTTP 200 responses with text/html content type.
    """
    from warcio.archiveiterator import ArchiveIterator

    pages = []
    with open(warc_path, "rb") as f:
        for record in ArchiveIterator(f):
            if len(pages) >= num_pages:
                break
            if record.rec_type != "response":
                continue
            if not record.http_headers:
                continue
            if record.http_headers.get_statuscode() != "200":
                continue
            content_type = record.http_headers.get_header("Content-Type") or ""
            if "text/html" not in content_type:
                continue
            content = record.content_stream().read()
            pages.append((content, len(content)))
    return pages


def load_cached_pages(cache_dir: str, num_pages: int) -> list | None:
    """Load pages from cache directory. Returns None if cache is insufficient."""
    cache_path = Path(cache_dir)
    if not cache_path.exists():
        return None
    cached_files = sorted(cache_path.glob("*.html"))
    if len(cached_files) < num_pages:
        return None
    pages = []
    for f in cached_files[:num_pages]:
        content = f.read_bytes()
        pages.append((content, len(content)))
    print(f"Loaded {len(pages)} pages from cache: {cache_dir}")
    return pages


def save_to_cache(pages: list, cache_dir: str):
    """Save extracted pages to cache directory."""
    cache_path = Path(cache_dir)
    cache_path.mkdir(parents=True, exist_ok=True)
    for i, (content, _) in enumerate(pages):
        (cache_path / f"{i:04d}.html").write_bytes(content)
    print(f"Cached {len(pages)} pages to {cache_dir}")


def benchmark_cld2(pages: list) -> list:
    """Run CLD2 detection on each page, returning per-page timing results."""
    import pycld2

    results = []
    for i, (html_bytes, content_length) in enumerate(pages):
        try:
            text = html_bytes.decode("utf-8", errors="replace")
        except Exception:
            text = html_bytes.decode("latin-1", errors="replace")

        t0 = time.perf_counter_ns()
        try:
            is_reliable, text_bytes_found, details = pycld2.detect(text)
            lang_name = details[0][0] if details else "UNKNOWN"
            lang_code = details[0][1] if details else "un"
            percent = details[0][2] if details else 0
            score = details[0][3] if details else 0.0
        except Exception as e:
            is_reliable = False
            lang_name = f"ERROR:{type(e).__name__}"
            lang_code = "un"
            percent = 0
            score = 0.0
        t1 = time.perf_counter_ns()

        time_ms = (t1 - t0) / 1_000_000
        results.append(
            {
                "sample_id": i,
                "content_length": content_length,
                "time_ms": time_ms,
                "detected_language": lang_name,
                "language_code": lang_code,
                "is_reliable": is_reliable,
                "percent": percent,
                "score": score,
            }
        )
    return results


def compute_aggregates(per_page_results: list, experiment_name: str) -> dict:
    """Compute aggregate statistics from per-page results."""
    times = [r["time_ms"] for r in per_page_results]
    total_bytes = sum(r["content_length"] for r in per_page_results)
    sorted_times = sorted(times)

    return {
        "experiment_name": experiment_name,
        "total_time_ms": f"{sum(times):.3f}",
        "mean_time_ms": f"{statistics.mean(times):.3f}",
        "median_time_ms": f"{statistics.median(times):.3f}",
        "p95_time_ms": f"{sorted_times[int(len(times) * 0.95)]:.3f}",
        "p99_time_ms": f"{sorted_times[int(len(times) * 0.99)]:.3f}",
        "num_pages": len(per_page_results),
        "total_bytes": total_bytes,
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


AGGREGATE_FIELDS = [
    "experiment_name",
    "total_time_ms",
    "mean_time_ms",
    "median_time_ms",
    "p95_time_ms",
    "p99_time_ms",
    "num_pages",
    "total_bytes",
    "timestamp",
]


def write_results(aggregate: dict, results_file: str):
    """Append aggregate results to TSV file, creating header if needed."""
    os.makedirs(os.path.dirname(results_file), exist_ok=True)
    file_exists = os.path.exists(results_file) and os.path.getsize(results_file) > 0

    with open(results_file, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=AGGREGATE_FIELDS, delimiter="\t")
        if not file_exists:
            writer.writeheader()
        writer.writerow(aggregate)


PREDICTION_FIELDS = [
    "sample_id",
    "detected_language",
    "language_code",
    "is_reliable",
    "percent",
    "score",
]


def write_predictions(per_page_results: list, experiment_dir: str):
    """Write per-page predictions to TSV file."""
    os.makedirs(experiment_dir, exist_ok=True)
    pred_path = os.path.join(experiment_dir, "predictions.tsv")

    with open(pred_path, "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=PREDICTION_FIELDS, delimiter="\t", extrasaction="ignore"
        )
        writer.writeheader()
        writer.writerows(per_page_results)
    print(f"Predictions written to {pred_path}")


def main():
    parser = argparse.ArgumentParser(description="CLD2 Benchmark Tool")
    parser.add_argument("--warc", required=True, help="Path to WARC file")
    parser.add_argument(
        "--num-pages", type=int, default=1000, help="Number of HTML pages to test"
    )
    parser.add_argument(
        "--experiment", default="pycld2-baseline", help="Experiment name"
    )
    parser.add_argument(
        "--results-file",
        default="./data/benchmark/results.csv",
        help="Aggregate results TSV path",
    )
    parser.add_argument(
        "--cache-dir",
        default="./data/benchmark/cache/",
        help="Cache directory for extracted HTML",
    )
    args = parser.parse_args()

    # Load from cache or extract from WARC
    pages = load_cached_pages(args.cache_dir, args.num_pages)
    if pages is None:
        print(f"Extracting {args.num_pages} HTML pages from {args.warc}...")
        pages = extract_html_pages(args.warc, args.num_pages)
        print(f"Extracted {len(pages)} pages, total {sum(cl for _, cl in pages):,} bytes")
        save_to_cache(pages, args.cache_dir)

    if len(pages) < args.num_pages:
        print(
            f"Warning: only {len(pages)} pages available (requested {args.num_pages})"
        )

    # Benchmark
    print(f"Running CLD2 benchmark ({args.experiment})...")
    per_page_results = benchmark_cld2(pages)

    # Aggregate
    aggregate = compute_aggregates(per_page_results, args.experiment)

    print(f"\n--- Results: {args.experiment} ---")
    for k, v in aggregate.items():
        print(f"  {k}: {v}")

    # Write outputs
    write_results(aggregate, args.results_file)
    print(f"\nAggregate appended to {args.results_file}")

    experiment_dir = os.path.join(
        os.path.dirname(args.results_file), "experiments", args.experiment
    )
    write_predictions(per_page_results, experiment_dir)


if __name__ == "__main__":
    main()
