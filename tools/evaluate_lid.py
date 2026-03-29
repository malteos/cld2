#!/usr/bin/env python3
"""
CommonLID Evaluation Tool for CLD2

Loads the CommonLID benchmark, runs CLD2 on each text sample via the
tools/cld2_detect CLI, and reports macro F1 + micro F1 metrics.

Output format (grep-friendly, matching benchmark.cc style):
    ---
    samples: 373230
    languages: 109
    coverage: 0.7615
    macro_f1: 0.4523
    micro_f1: 0.7891

Usage:
    python3 tools/evaluate_lid.py [--data data/commonlid/commonlid.tsv.gz]
                                  [--output data/commonlid/results/]
                                  [--limit N]
"""

import argparse
import gzip
import json
import os
import subprocess
import sys
from collections import Counter

# CLD2 code -> ISO 639-3 mapping
# CLD2 uses a mix of ISO 639-1 (2-letter) and some 3-letter codes.
# CommonLID uses ISO 639-3 (3-letter) codes.
CLD2_TO_ISO639_3 = {
    "en": "eng", "da": "dan", "nl": "nld", "fi": "fin", "fr": "fra",
    "de": "deu", "iw": "heb", "it": "ita", "ja": "jpn", "ko": "kor",
    "no": "nor", "pl": "pol", "pt": "por", "ru": "rus", "es": "spa",
    "sv": "swe", "zh": "zho", "cs": "ces", "el": "ell", "is": "isl",
    "lv": "lav", "lt": "lit", "ro": "ron", "hu": "hun", "et": "est",
    "bg": "bul", "hr": "hrv", "sr": "srp", "ga": "gle", "gl": "glg",
    "tl": "tgl", "tr": "tur", "uk": "ukr", "hi": "hin", "mk": "mkd",
    "bn": "ben", "id": "ind", "la": "lat", "ms": "msa", "ml": "mal",
    "cy": "cym", "ne": "nep", "te": "tel", "sq": "sqi", "ta": "tam",
    "be": "bel", "jw": "jav", "oc": "oci", "ur": "urd", "bh": "bho",
    "gu": "guj", "th": "tha", "ar": "ara", "ca": "cat", "eo": "epo",
    "eu": "eus", "ia": "ina", "kn": "kan", "pa": "pan", "gd": "gla",
    "sw": "swh", "sl": "slv", "mr": "mar", "mt": "mlt", "vi": "vie",
    "fy": "fry", "sk": "slk", "zh-Hant": "zho", "fo": "fao", "or": "ory",
    "su": "sun", "uz": "uzb", "am": "amh", "az": "aze", "ka": "kat",
    "ti": "tir", "fa": "fas", "bs": "bos", "si": "sin", "nn": "nno",
    "xh": "xho", "zu": "zul", "gn": "grn", "st": "sot", "tk": "tuk",
    "ky": "kir", "br": "bre", "tw": "twi", "yi": "yid", "so": "som",
    "ug": "uig", "ku": "kur", "mn": "mon", "hy": "hye", "lo": "lao",
    "sd": "snd", "rm": "roh", "af": "afr", "lb": "ltz", "my": "mya",
    "km": "khm", "bo": "bod", "dv": "div", "chr": "chr", "syr": "syr",
    "lif": "lif", "as": "asm", "co": "cos", "ie": "ile",
    "kk": "kaz", "ln": "lin", "ps": "pus", "qu": "que", "sn": "sna",
    "tg": "tgk", "tt": "tat", "to": "ton", "yo": "yor", "mi": "mri",
    "wo": "wol", "ab": "abk", "aa": "aar", "ay": "aym", "ba": "bak",
    "bi": "bis", "dz": "dzo", "fj": "fij", "kl": "kal", "ha": "hau",
    "ht": "hat", "ik": "ipk", "iu": "iku", "ks": "kas", "rw": "kin",
    "mg": "mlg", "na": "nau", "om": "orm", "rn": "run", "sm": "smo",
    "sg": "sag", "sa": "san", "ss": "ssw", "ts": "tso", "tn": "tsn",
    "vo": "vol", "za": "zha", "kha": "kha", "sco": "sco", "lg": "lug",
    "gv": "glv", "sr-ME": "cnr", "ak": "aka", "ig": "ibo", "mfe": "mfe",
    "haw": "haw", "ceb": "ceb", "ee": "ewe", "gaa": "gaa", "hmn": "hmn",
    "kri": "kri", "loz": "loz", "lua": "lua", "luo": "luo", "new": "new",
    "ny": "nya", "os": "oss", "pam": "pam", "nso": "nso", "raj": "raj",
    "crs": "crs", "tum": "tum", "ve": "ven", "war": "war",
    # New languages added to CLD2
    "arg": "arg",  # Aragonese
    "vec": "vec",  # Venetian
    "bik": "bik",  # Bikol
    "acf": "acf",  # Saint Lucian Creole French
    "crh": "crh",  # Crimean Tatar
    "rcf": "rcf",  # Réunion Creole French
    "gom": "gom",  # Goan Konkani
    "bcl": "bcl",  # Central Bikol
    "lij": "lij",  # Ligurian
    "kab": "kab",  # Kabyle
    "gcr": "gcr",  # Guianese Creole French
    "kik": "kik",  # Kikuyu
    "ltg": "ltg",  # Latgalian
    "fuv": "fuv",  # Nigerian Fulfulde
    "gcf": "gcf",  # Guadeloupean Creole French
    "ext": "ext",  # Extremaduran
    "nyn": "nyn",  # Nyankore
    "guw": "guw",  # Gun
    "pcm": "pcm",  # Nigerian Pidgin
    "ace": "ace",  # Acehnese
    # Special
    "un": "und",  # unknown
    "xxx": "xxx",  # ignore
}

# CommonLID uses some macro/variant codes. Map them to canonical forms
# that CLD2 could possibly match.
COMMONLID_ALIASES = {
    # Arabic variants -> CLD2 detects "ar" which maps to "ara"
    "arb": "ara",   # Standard Arabic -> Arabic
    "arz": "ara",   # Egyptian Arabic -> Arabic
    "ary": "ara",   # Moroccan Arabic -> Arabic
    "ars": "ara",   # Najdi Arabic -> Arabic
    "aeb": "ara",   # Tunisian Arabic -> Arabic
    "apd": "ara",   # Sudanese Arabic -> Arabic
    # Chinese variants
    "cmn": "zho",   # Mandarin -> Chinese
    "wuu": "zho",   # Wu Chinese -> Chinese
    "yue": "zho",   # Cantonese -> Chinese
    # Malay/Indonesian variants
    "zsm": "msa",   # Standard Malay -> Malay
    # Swahili variants
    "swa": "swh",   # Swahili (macro) -> Swahili
    # Azerbaijani variants
    "azj": "aze",   # North Azerbaijani -> Azerbaijani
    # Latvian variants
    "lvs": "lav",   # Standard Latvian -> Latvian
    # Uzbek variants
    "uzs": "uzb",   # Southern Uzbek -> Uzbek
    # Oromo variants
    "gaz": "orm",   # West Central Oromo -> Oromo
    # Fulah variants
    "fuv": "fuv",   # Nigerian Fulfulde (no CLD2 mapping)
    # Others that map to CLD2-known languages
    "hbo": "heb",   # Ancient Hebrew -> Hebrew
    "fro": "fra",   # Old French -> French
    "grc": "ell",   # Ancient Greek -> Greek
    "fil": "tgl",   # Filipino -> Tagalog
    "gug": "grn",   # Paraguayan Guaraní -> Guaraní (CLD2: gn)
}

# Set of ISO 639-3 codes that CLD2 can detect
CLD2_SUPPORTED = set(CLD2_TO_ISO639_3.values()) - {"und", "xxx"}


def load_commonlid(path, limit=None):
    """Load CommonLID TSV.gz file. Returns list of (text, lang_code) tuples."""
    samples = []
    with gzip.open(path, 'rt', encoding='utf-8') as f:
        header = next(f)  # skip header
        for i, line in enumerate(f):
            if limit and i >= limit:
                break
            parts = line.split('\t')
            if len(parts) >= 2:
                text = parts[0]
                tag = parts[1].strip()
                if len(tag) == 3 and tag.isalpha() and tag.islower():
                    samples.append((text, tag))
    return samples


def normalize_commonlid_code(code):
    """Normalize a CommonLID ISO 639-3 code to a canonical form."""
    return COMMONLID_ALIASES.get(code, code)


def run_cld2(texts, binary="tools/cld2_detect"):
    """Run CLD2 on a list of texts via the CLI binary.
    Returns list of CLD2 language codes."""
    # Feed all texts via stdin, one per line
    # Replace newlines in text with spaces to keep line-per-sample format
    input_text = "\n".join(t.replace("\n", " ").replace("\r", " ") for t in texts)
    proc = subprocess.run(
        [binary],
        input=input_text,
        capture_output=True,
        text=True,
        timeout=600
    )
    if proc.returncode != 0:
        print(f"ERROR: cld2_detect failed: {proc.stderr}", file=sys.stderr)
        sys.exit(1)

    results = []
    for line in proc.stdout.strip().split("\n"):
        parts = line.split("\t")
        if len(parts) >= 1:
            cld2_code = parts[0]
            iso3 = CLD2_TO_ISO639_3.get(cld2_code, "und")
            results.append(iso3)
        else:
            results.append("und")
    return results


def compute_metrics(true_labels, pred_labels):
    """Compute macro F1, micro F1, per-language P/R/F1."""
    all_langs = sorted(set(true_labels) | set(pred_labels))

    per_lang = {}
    total_tp = total_fp = total_fn = 0

    for lang in all_langs:
        if lang == "und":
            continue
        tp = sum(1 for t, p in zip(true_labels, pred_labels) if t == lang and p == lang)
        fp = sum(1 for t, p in zip(true_labels, pred_labels) if t != lang and p == lang)
        fn = sum(1 for t, p in zip(true_labels, pred_labels) if t == lang and p != lang)

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

        n_true = sum(1 for t in true_labels if t == lang)
        per_lang[lang] = {
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "tp": tp, "fp": fp, "fn": fn,
            "n_samples": n_true,
            "supported": lang in CLD2_SUPPORTED,
        }
        total_tp += tp
        total_fp += fp
        total_fn += fn

    # Only compute macro F1 over ground-truth languages (not spurious predictions)
    gt_langs = sorted(set(true_labels) - {"und"})
    macro_f1 = sum(per_lang.get(l, {}).get("f1", 0) for l in gt_langs) / len(gt_langs) if gt_langs else 0
    micro_p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0
    micro_r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0
    micro_f1 = 2 * micro_p * micro_r / (micro_p + micro_r) if (micro_p + micro_r) > 0 else 0

    supported_langs = sum(1 for l in gt_langs if l in CLD2_SUPPORTED)
    coverage = supported_langs / len(gt_langs) if gt_langs else 0

    return {
        "macro_f1": macro_f1,
        "micro_f1": micro_f1,
        "micro_precision": micro_p,
        "micro_recall": micro_r,
        "coverage": coverage,
        "n_gt_languages": len(gt_langs),
        "n_supported": supported_langs,
        "per_lang": per_lang,
    }


def main():
    parser = argparse.ArgumentParser(description="Evaluate CLD2 on CommonLID")
    parser.add_argument("--data", default="data/commonlid/commonlid.tsv.gz",
                        help="Path to CommonLID TSV.gz file")
    parser.add_argument("--output", default="data/commonlid/results",
                        help="Output directory for detailed results")
    parser.add_argument("--binary", default="tools/cld2_detect",
                        help="Path to cld2_detect binary")
    parser.add_argument("--limit", type=int, default=None,
                        help="Limit number of samples (for testing)")
    parser.add_argument("--batch-size", type=int, default=50000,
                        help="Batch size for piping to cld2_detect")
    args = parser.parse_args()

    # Recompile cld2_detect
    print("Compiling cld2_detect...", file=sys.stderr)
    ret = subprocess.run(["make", "tools/cld2_detect"], capture_output=True, text=True)
    if ret.returncode != 0:
        print(f"Compilation failed:\n{ret.stderr}", file=sys.stderr)
        sys.exit(1)
    print("Compilation OK", file=sys.stderr)

    # Load data
    print(f"Loading CommonLID from {args.data}...", file=sys.stderr)
    samples = load_commonlid(args.data, limit=args.limit)
    print(f"Loaded {len(samples)} samples", file=sys.stderr)

    # Normalize ground truth labels
    true_labels = [normalize_commonlid_code(tag) for _, tag in samples]
    texts = [text for text, _ in samples]

    # Run CLD2 in batches
    print(f"Running CLD2 on {len(texts)} samples...", file=sys.stderr)
    pred_labels = []
    for i in range(0, len(texts), args.batch_size):
        batch = texts[i:i + args.batch_size]
        batch_preds = run_cld2(batch, binary=args.binary)
        pred_labels.extend(batch_preds)
        print(f"  Processed {min(i + args.batch_size, len(texts))}/{len(texts)}", file=sys.stderr)

    assert len(pred_labels) == len(true_labels), \
        f"Mismatch: {len(pred_labels)} predictions vs {len(true_labels)} labels"

    # Compute metrics
    print("Computing metrics...", file=sys.stderr)
    metrics = compute_metrics(true_labels, pred_labels)

    # Print summary (grep-friendly format)
    print("---")
    print(f"samples: {len(samples)}")
    print(f"languages: {metrics['n_gt_languages']}")
    print(f"coverage: {metrics['coverage']:.4f}")
    print(f"macro_f1: {metrics['macro_f1']:.4f}")
    print(f"micro_f1: {metrics['micro_f1']:.4f}")

    # Write detailed results
    os.makedirs(args.output, exist_ok=True)

    # Per-language TSV
    per_lang_path = os.path.join(args.output, "per_language.tsv")
    with open(per_lang_path, "w") as f:
        f.write("lang\tn_samples\tsupported\tprecision\trecall\tf1\ttp\tfp\tfn\n")
        for lang in sorted(metrics["per_lang"].keys(),
                          key=lambda l: -metrics["per_lang"][l]["n_samples"]):
            m = metrics["per_lang"][lang]
            f.write(f"{lang}\t{m['n_samples']}\t{'yes' if m['supported'] else 'no'}\t"
                    f"{m['precision']:.4f}\t{m['recall']:.4f}\t{m['f1']:.4f}\t"
                    f"{m['tp']}\t{m['fp']}\t{m['fn']}\n")
    print(f"Per-language results: {per_lang_path}", file=sys.stderr)

    # Summary JSON
    summary_path = os.path.join(args.output, "summary.json")
    summary = {k: v for k, v in metrics.items() if k != "per_lang"}
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Summary: {summary_path}", file=sys.stderr)

    # Confusion pairs (top misclassifications)
    confusion = Counter()
    for t, p in zip(true_labels, pred_labels):
        if t != p:
            confusion[(t, p)] += 1
    confusion_path = os.path.join(args.output, "confusion.tsv")
    with open(confusion_path, "w") as f:
        f.write("true_lang\tpred_lang\tcount\n")
        for (t, p), count in confusion.most_common(200):
            f.write(f"{t}\t{p}\t{count}\n")
    print(f"Confusion matrix: {confusion_path}", file=sys.stderr)

    # Print worst-performing supported languages
    print("\nPer-language breakdown (supported languages):", file=sys.stderr)
    print(f"{'lang':<8} {'n':>6} {'P':>6} {'R':>6} {'F1':>6}", file=sys.stderr)
    for lang in sorted(metrics["per_lang"].keys(),
                      key=lambda l: metrics["per_lang"][l]["f1"]):
        m = metrics["per_lang"][lang]
        if m["supported"] and m["n_samples"] > 0:
            print(f"{lang:<8} {m['n_samples']:>6} {m['precision']:>6.3f} "
                  f"{m['recall']:>6.3f} {m['f1']:>6.3f}", file=sys.stderr)


if __name__ == "__main__":
    main()
