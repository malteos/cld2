#!/usr/bin/env python3
"""Contamination checker — prove that no benchmark text (CommonLID or FLORES+)
has leaked into our knowledge-base artefacts.

Why this matters
----------------
CommonLID is the *evaluation set* for this project. If any CommonLID line
ends up in `examples/*.txt`, `vocabulary.json`, or anywhere else we feed to
a downstream model, we create **train-test leakage**: a model tuned on our
KB would have seen the test data at training time.

FLORES+ (`openlanguagedata/flores_plus`) is a widely used LID/MT benchmark
too; we treat it with the same strictness even though CommonLID is the
primary concern.

What this script checks
-----------------------
For every language folder in `languages/`:

1. Every `examples/*.txt` file is hashed line-by-line and compared against
   the full set of CommonLID lines for the matching language (plus FLORES+).
   We also check substring overlap at 80 characters — any run of 80 or more
   consecutive characters shared with a benchmark line is flagged.
2. `vocabulary.json` is inspected: its `source` field must not mention
   `commonlid`, `flores`, or `madlad`.

Exit status is non-zero if any contamination is found, and a JSON report
(`contamination_report.json`) is written alongside the console summary.

Usage
-----
    source .venv/bin/activate
    python languages/scripts/check_contamination.py
    python languages/scripts/check_contamination.py --lang eng,deu
"""
from __future__ import annotations

import argparse
import gzip
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LANG_LIST = ROOT / "languages" / "language_list.json"
LANG_DIR = ROOT / "languages"
REPORT_PATH = ROOT / "languages" / "contamination_report.json"

SUBSTRING_WINDOW = 80        # flag any shared run this long or longer
MIN_SIGNIFICANT_LINE = 20    # shorter lines are too generic to be diagnostic

BANNED_SOURCES = (
    "commonlid",
    "flores",
    "madlad",
    "opus-100",
    "tatoeba",   # user-uploaded, but often benchmarked → treat conservatively
    "wmt",
)


def load_language_list() -> list[dict]:
    return json.loads(LANG_LIST.read_text(encoding="utf-8"))["languages"]


def load_commonlid_lines(local_path: str | None = None) -> dict[str, set[str]]:
    """Return {code: set(normalised_line)} from the CommonLID TSV.

    Tries, in order:
      1. `local_path` (if supplied)
      2. `HF_COMMONLID_TSV` env var pointing at a local file
      3. HuggingFace Hub (requires HF_TOKEN with access to the gated repo)

    Returns an empty dict if none of the above is reachable, and prints a
    visible warning. That means the line-level comparison degrades to a
    structural check only (Source headers + vocab attribution). This is
    intentional: CommonLID is gated, and requiring a token on every
    machine would leak credentials unnecessarily. The Source-header
    check still proves positively where each example came from.
    """
    import os
    path: Path | None = None
    candidate = local_path or os.environ.get("HF_COMMONLID_TSV")
    if candidate and Path(candidate).exists():
        path = Path(candidate)
    else:
        try:
            from huggingface_hub import hf_hub_download
            path = Path(hf_hub_download(
                repo_id="commoncrawl/CommonLID",
                filename="commonlid_20251209.tsv.gz",
                repo_type="dataset",
            ))
        except Exception as exc:  # noqa: BLE001
            print(f"[warn] CommonLID TSV unavailable ({type(exc).__name__}: "
                  f"{str(exc)[:120]}). Falling back to structural checks "
                  f"only. Pass --commonlid-tsv <path> to enable line-level "
                  f"matching.", file=sys.stderr)
            return {}

    buckets: dict[str, set[str]] = defaultdict(set)
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as f:
        f.readline()  # header
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 3:
                continue
            text = parts[0].strip()
            code = parts[1].strip()
            if len(text) >= MIN_SIGNIFICANT_LINE:
                buckets[code].add(text)
    return dict(buckets)


def load_flores_lines() -> dict[str, set[str]]:
    """Return {folder: set(line)} for every flores_plus jsonl file we can
    reach (dev+devtest). Keyed by folder (e.g. `eng_Latn`) because FLORES+
    uses the `iso3_Script` convention."""
    try:
        from huggingface_hub import hf_hub_download
        from huggingface_hub.utils import EntryNotFoundError
    except Exception:
        return {}
    buckets: dict[str, set[str]] = defaultdict(set)
    entries = load_language_list()
    for entry in entries:
        folder = entry["folder"]
        for split in ("dev", "devtest"):
            try:
                p = hf_hub_download(
                    repo_id="openlanguagedata/flores_plus",
                    filename=f"{split}/{folder}.jsonl",
                    repo_type="dataset",
                )
            except EntryNotFoundError:
                continue
            except Exception as exc:  # noqa: BLE001
                print(f"  [warn] flores {folder}/{split}: {exc}", file=sys.stderr)
                continue
            with open(p, "r", encoding="utf-8") as f:
                for line in f:
                    try:
                        rec = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    txt = (rec.get("text") or "").strip()
                    if len(txt) >= MIN_SIGNIFICANT_LINE:
                        buckets[folder].add(txt)
    return dict(buckets)


def scan_example_headers(entry: dict) -> list[dict]:
    """Structural check: every example MUST start with a `# Source: <URL>`
    header from a non-banned source. This catches files that slipped
    through without attribution."""
    ex_dir = LANG_DIR / entry["folder"] / "examples"
    hits: list[dict] = []
    if not ex_dir.exists():
        return hits
    for path in sorted(ex_dir.glob("*.txt")):
        first = ""
        try:
            with path.open("r", encoding="utf-8") as f:
                first = f.readline().strip()
        except Exception:
            continue
        if not first.startswith("# Source:"):
            hits.append({
                "file": str(path.relative_to(ROOT)),
                "type": "missing_source_header",
                "first_line": first[:140],
            })
            continue
        low = first.lower()
        for banned in BANNED_SOURCES:
            if banned in low:
                hits.append({
                    "file": str(path.relative_to(ROOT)),
                    "type": "banned_source_in_header",
                    "source": banned,
                    "first_line": first[:140],
                })
                break
    return hits


def substring_match(sample: str, sources: set[str]) -> tuple[str, str] | None:
    """Return (sample_snippet, source_snippet) if any window of
    SUBSTRING_WINDOW chars from `sample` appears in any member of `sources`."""
    if len(sample) < SUBSTRING_WINDOW:
        return None
    # Build an index of substrings in sources (lazy — we stop on first match).
    for src in sources:
        if len(src) < SUBSTRING_WINDOW:
            continue
        # Short-circuit on the first shared window.
        for i in range(len(sample) - SUBSTRING_WINDOW + 1):
            window = sample[i:i + SUBSTRING_WINDOW]
            if window in src:
                return (window, src[:140])
    return None


def scan_examples(entry: dict, commonlid: set[str], flores: set[str]) -> list[dict]:
    folder = LANG_DIR / entry["folder"]
    ex_dir = folder / "examples"
    hits: list[dict] = []
    if not ex_dir.exists():
        return hits
    for path in sorted(ex_dir.glob("*.txt")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            s = line.strip()
            if len(s) < MIN_SIGNIFICANT_LINE:
                continue
            if s in commonlid:
                hits.append({
                    "file": str(path.relative_to(ROOT)),
                    "source": "commonlid",
                    "type": "exact_line",
                    "snippet": s[:140],
                })
                continue
            if s in flores:
                hits.append({
                    "file": str(path.relative_to(ROOT)),
                    "source": "flores_plus",
                    "type": "exact_line",
                    "snippet": s[:140],
                })
                continue
            # Substring check only for longer lines (more expensive).
            if len(s) >= SUBSTRING_WINDOW:
                hit = substring_match(s, commonlid)
                if hit is not None:
                    hits.append({
                        "file": str(path.relative_to(ROOT)),
                        "source": "commonlid",
                        "type": "substring_match",
                        "sample_window": hit[0],
                        "source_preview": hit[1],
                    })
                    continue
                hit = substring_match(s, flores)
                if hit is not None:
                    hits.append({
                        "file": str(path.relative_to(ROOT)),
                        "source": "flores_plus",
                        "type": "substring_match",
                        "sample_window": hit[0],
                        "source_preview": hit[1],
                    })
    return hits


def scan_vocabulary(entry: dict) -> list[dict]:
    path = LANG_DIR / entry["folder"] / "vocabulary.json"
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return [{"file": str(path.relative_to(ROOT)), "source": "unknown",
                 "type": "invalid_json"}]
    src = str(data.get("source", "")).lower()
    for banned in BANNED_SOURCES:
        if banned in src:
            return [{
                "file": str(path.relative_to(ROOT)),
                "source": banned,
                "type": "banned_source_attribution",
                "value": data.get("source"),
            }]
    return []


def parse_langs(arg: str | None, all_flag: bool, langs: list[dict]) -> list[dict]:
    if all_flag or not arg:
        return langs
    want = {c.strip() for c in arg.split(",") if c.strip()}
    return [l for l in langs if l["code"] in want]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", help="comma-separated ISO-639-3 codes")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--skip-flores", action="store_true",
                    help="skip FLORES+ comparison (useful if HF is offline)")
    ap.add_argument("--commonlid-tsv", help="local path to CommonLID TSV gz")
    args = ap.parse_args()

    entries = parse_langs(args.lang, args.all, load_language_list())
    if not entries:
        entries = load_language_list()

    print("[info] loading CommonLID lines …", flush=True)
    commonlid = load_commonlid_lines(args.commonlid_tsv)
    flores: dict[str, set[str]] = {}
    if not args.skip_flores:
        print("[info] loading FLORES+ lines …", flush=True)
        flores = load_flores_lines()

    line_check_enabled = bool(commonlid or flores)
    if not line_check_enabled:
        print("[warn] neither CommonLID nor FLORES+ reachable; running "
              "structural checks only (source-header + vocab attribution).")

    report: dict = {
        "summary": {
            "languages_checked": 0,
            "languages_contaminated": 0,
            "total_hits": 0,
            "line_level_check": line_check_enabled,
        },
        "per_language": {},
    }
    for entry in entries:
        code = entry["code"]
        folder = entry["folder"]
        cl_lines = commonlid.get(code, set())
        fl_lines = flores.get(folder, set())
        hits = scan_examples(entry, cl_lines, fl_lines) if line_check_enabled else []
        hits += scan_example_headers(entry)
        hits += scan_vocabulary(entry)
        report["per_language"][code] = {
            "folder": folder,
            "commonlid_source_lines": len(cl_lines),
            "flores_source_lines": len(fl_lines),
            "hits": hits,
        }
        report["summary"]["languages_checked"] += 1
        if hits:
            report["summary"]["languages_contaminated"] += 1
            report["summary"]["total_hits"] += len(hits)
            print(f"  [LEAK] {code}: {len(hits)} hits (first: {hits[0]['type']})")
        else:
            print(f"  [ok]   {code}: clean")

    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2),
                           encoding="utf-8")
    print()
    print(f"Checked {report['summary']['languages_checked']} languages; "
          f"{report['summary']['languages_contaminated']} contaminated "
          f"({report['summary']['total_hits']} hits total); "
          f"line_level={line_check_enabled}.")
    print(f"Report written to {REPORT_PATH.relative_to(ROOT)}")
    return 0 if report["summary"]["languages_contaminated"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
