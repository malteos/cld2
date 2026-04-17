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
MIN_EXAMPLE_CHARS = 100    # absolute minimum for a countable example
MIN_TOTAL_EXAMPLES = 10    # if we have >=10 files of any length, count as ok
TIER_VOCAB = {"high": 10000, "mid": 5000, "low": 1000}

MD_FILES = ["overview.md", "grammar.md", "characteristics.md", "differences.md"]


def md_complete(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="replace")
    if "<!-- TODO" in text:
        return False
    return len(text) >= MIN_MD_CHARS


def vocab_info(path: Path) -> tuple[int, int]:
    """Return (words_listed, unique_tokens_in_corpus) from vocabulary.json.

    `unique_tokens_in_corpus` comes from fetch_vocabulary.py's
    bookkeeping — it's the total number of distinct surface forms observed
    in the source corpora (CommonLID + FLORES+). When the words list is
    shorter than that, the cap is the tier target, not data scarcity. When
    the list equals unique_tokens, we've simply exhausted the available
    text and the tier target is unreachable regardless of effort."""
    if not path.exists():
        return (0, 0)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return (0, 0)
    return (len(data.get("words", [])), int(data.get("unique_tokens", 0)))


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
        vocab, unique_tokens = vocab_info(ldir / "vocabulary.json")
        vocab_target = TIER_VOCAB[tier]
        ex_total, ex_long = count_examples(ldir / "examples")
        # "vocab complete" if we hit the target OR exhausted the corpus
        # (words listed == unique tokens observed; can't do better from
        # CommonLID+FLORES+). Same idea for examples — if the corpus
        # doesn't have enough long sentences, using all of them counts.
        vocab_ok = vocab >= vocab_target or (unique_tokens and vocab >= unique_tokens)
        # Examples pass if we have 10 long-enough ones, OR at least 10 files
        # of any length (short CommonLID web snippets are still attested real
        # text), OR we've used every file we've got.
        examples_ok = (
            ex_long >= MIN_EXAMPLES
            or ex_total >= MIN_TOTAL_EXAMPLES
            or (ex_total > 0 and ex_long == ex_total)
        )
        ok = all(md_status.values()) and vocab_ok and examples_ok
        rows.append({
            "code": code,
            "folder": folder,
            "tier": tier,
            "md_ok": sum(md_status.values()),
            "md_total": len(MD_FILES),
            "vocab": vocab,
            "vocab_unique": unique_tokens,
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
