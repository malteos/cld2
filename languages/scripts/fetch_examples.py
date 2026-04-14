#!/usr/bin/env python3
"""Supplement per-language `examples/` directories with real text from FLORES+.

The CommonLID dataset pre-seeds ~15 short web snippets per language via
`generate_skeleton.py`. For languages where those snippets are very short, we
append longer multi-sentence passages built from the FLORES+ dev/devtest split
on HuggingFace (`openlanguagedata/flores_plus`).

FLORES+ rows are standalone sentences. We concatenate consecutive sentences
into passages of at least `--min-chars` characters so each `examples/XX.txt`
has enough context for typological reference.

Usage:
    source .venv/bin/activate
    python languages/scripts/fetch_examples.py --all --count 5
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LANG_LIST = ROOT / "languages" / "language_list.json"
LANG_DIR = ROOT / "languages"


def flores_sentences(folder: str) -> list[str]:
    """Return a list of sentence strings from FLORES+ for this folder, or []."""
    from huggingface_hub import hf_hub_download
    from huggingface_hub.utils import EntryNotFoundError
    out: list[str] = []
    for split in ("dev", "devtest"):
        try:
            path = hf_hub_download(
                repo_id="openlanguagedata/flores_plus",
                filename=f"{split}/{folder}.jsonl",
                repo_type="dataset",
            )
        except EntryNotFoundError:
            continue
        except Exception as exc:  # noqa: BLE001
            print(f"  [warn] flores fetch {folder}/{split}: {exc}", file=sys.stderr)
            continue
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                txt = (rec.get("text") or "").strip()
                if txt:
                    out.append(txt)
    return out


def chunk_into_passages(sentences: list[str], min_chars: int, max_chars: int = 1500) -> list[str]:
    passages: list[str] = []
    buf: list[str] = []
    buf_len = 0
    for s in sentences:
        buf.append(s)
        buf_len += len(s) + 1
        if buf_len >= min_chars:
            passages.append(" ".join(buf))
            buf = []
            buf_len = 0
        if len(buf) > 1 and buf_len >= max_chars:
            passages.append(" ".join(buf))
            buf = []
            buf_len = 0
    if buf:
        passages.append(" ".join(buf))
    return passages


def next_index(examples_dir: Path) -> int:
    highest = 0
    for p in examples_dir.glob("*.txt"):
        if p.stem.isdigit():
            highest = max(highest, int(p.stem))
    return highest + 1


def count_long_enough(examples_dir: Path, min_chars: int) -> int:
    if not examples_dir.exists():
        return 0
    return sum(1 for p in examples_dir.glob("*.txt") if p.stat().st_size >= min_chars)


def supplement_language(entry: dict, target_long: int, min_chars: int) -> int:
    folder = LANG_DIR / entry["folder"]
    examples_dir = folder / "examples"
    examples_dir.mkdir(parents=True, exist_ok=True)
    existing_long = count_long_enough(examples_dir, min_chars)
    if existing_long >= target_long:
        return 0

    sentences = flores_sentences(entry["folder"])
    if not sentences:
        return 0

    passages = chunk_into_passages(sentences, min_chars)
    idx = next_index(examples_dir)
    written = 0
    for p in passages:
        if existing_long + written >= target_long:
            break
        if len(p) < min_chars:
            continue
        out = examples_dir / f"{idx:02d}.txt"
        out.write_text(p + "\n", encoding="utf-8")
        idx += 1
        written += 1
    return written


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", help="comma-separated ISO-639-3 codes")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--target-long", type=int, default=10,
                    help="desired count of long (>= min-chars) example files")
    ap.add_argument("--min-chars", type=int, default=500)
    args = ap.parse_args()

    langs = json.loads(LANG_LIST.read_text(encoding="utf-8"))["languages"]
    if args.all:
        targets = langs
    elif args.lang:
        want = {c.strip() for c in args.lang.split(",") if c.strip()}
        targets = [l for l in langs if l["code"] in want]
    else:
        print("No languages selected (--lang or --all).", file=sys.stderr)
        return 2

    for entry in targets:
        added = supplement_language(entry, args.target_long, args.min_chars)
        print(f"  {entry['code']:<4} ({entry['folder']:<12}) +{added} examples")

    return 0


if __name__ == "__main__":
    sys.exit(main())
