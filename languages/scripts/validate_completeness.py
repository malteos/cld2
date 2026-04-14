#!/usr/bin/env python3
"""Check that every language folder has the expected files and meets minimum
content thresholds.

Thresholds (defaults):
  overview.md, grammar.md, characteristics.md, differences.md -> >= MIN_MD_CHARS
  vocabulary.json -> contains a "words" list with >= tier target (high=10000, mid=5000, low=1000)
  examples/ -> at least MIN_EXAMPLES files, each >= MIN_EXAMPLE_CHARS

Exit code is non-zero if any language fails. Prints a report with one row per
language, summarised at the end.

Usage:
    python languages/scripts/validate_completeness.py
    python languages/scripts/validate_completeness.py --summary   # short mode
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LANG_LIST = ROOT / "languages" / "language_list.json"
LANG_DIR = ROOT / "languages"

MIN_MD_CHARS = 400         # TODO placeholder is ~120 chars, so anything above this indicates real content
MIN_EXAMPLES = 10
MIN_EXAMPLE_CHARS = 100
TIER_VOCAB = {"high": 10000, "mid": 5000, "low": 1000}

MD_FILES = ["overview.md", "grammar.md", "characteristics.md", "differences.md"]


def md_complete(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="replace")
    if "<!-- TODO" in text:
        return False
    return len(text) >= MIN_MD_CHARS


def vocab_count(path: Path) -> int:
    if not path.exists():
        return 0
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return 0
    return len(data.get("words", []))


def count_examples(examples_dir: Path) -> tuple[int, int]:
    if not examples_dir.exists():
        return (0, 0)
    total = 0
    long_enough = 0
    for p in sorted(examples_dir.glob("*.txt")):
        total += 1
        if p.stat().st_size >= MIN_EXAMPLE_CHARS:
            long_enough += 1
    return (total, long_enough)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--summary", action="store_true", help="short output")
    ap.add_argument("--json", action="store_true", help="emit JSON report")
    args = ap.parse_args()

    data = json.loads(LANG_LIST.read_text(encoding="utf-8"))
    rows = []
    for entry in data["languages"]:
        code, folder, tier = entry["code"], entry["folder"], entry["tier"]
        ldir = LANG_DIR / folder
        md_status = {m: md_complete(ldir / m) for m in MD_FILES}
        vocab = vocab_count(ldir / "vocabulary.json")
        vocab_target = TIER_VOCAB[tier]
        ex_total, ex_long = count_examples(ldir / "examples")
        ok = (
            all(md_status.values())
            and vocab >= vocab_target
            and ex_long >= MIN_EXAMPLES
        )
        rows.append({
            "code": code,
            "folder": folder,
            "tier": tier,
            "md_ok": sum(md_status.values()),
            "md_total": len(MD_FILES),
            "vocab": vocab,
            "vocab_target": vocab_target,
            "examples": ex_total,
            "examples_ok": ex_long,
            "ok": ok,
        })

    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return 0 if all(r["ok"] for r in rows) else 1

    if not args.summary:
        hdr = f"{'code':<4} {'folder':<12} {'tier':<4} {'md':>5} {'vocab':>8} {'ex':>5}  {'status':<6}"
        print(hdr)
        print("-" * len(hdr))
        for r in rows:
            status = "OK" if r["ok"] else "MISS"
            print(f"{r['code']:<4} {r['folder']:<12} {r['tier']:<4} "
                  f"{r['md_ok']}/{r['md_total']:<3} "
                  f"{r['vocab']:>4}/{r['vocab_target']:<4} "
                  f"{r['examples_ok']:>2}/{r['examples']:<3} "
                  f"{status}")

    completed = sum(1 for r in rows if r["ok"])
    print(f"\n{completed}/{len(rows)} languages meet all thresholds.")
    return 0 if completed == len(rows) else 1


if __name__ == "__main__":
    sys.exit(main())
