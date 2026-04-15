#!/usr/bin/env python3
"""Rebuild `vocabulary.json` for every language from non-benchmark text.

The previous vocabulary was built from CommonLID + FLORES+, both evaluation
benchmarks. That's train-test leakage. This replacement draws exclusively
from the `wikimedia/wikipedia` HuggingFace dump (a mirror of Wikipedia,
itself a website — not a LID benchmark).

Falls back to the paragraphs already written to `examples/*.txt` if the
Wikipedia edition is missing or empty (those paragraphs were just produced
from the same non-benchmark web sources by `fetch_web_examples.py`).

Tokenisation matches the old script: Unicode-aware word regex for
alphabetic scripts, single-character tokens for CJK, character 3-grams
for Thai. Output is frequency-ranked and capped at the tier target
(high=10k, mid=5k, low=1k).

Usage
-----
    source .venv/bin/activate
    python languages/scripts/fetch_web_vocabulary.py --all
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LANG_LIST = ROOT / "languages" / "language_list.json"
LANG_DIR = ROOT / "languages"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sources_catalog import SOURCES  # noqa: E402
from fetch_web_examples import (  # noqa: E402
    download_wiki_parquet, iter_wiki_articles, WP_DATE,
)

TIER_VOCAB = {"high": 10000, "mid": 5000, "low": 1000}
CJK_SCRIPTS = {"Hans", "Hant", "Jpan", "Hang"}
NO_WORD_BOUNDARY_SCRIPTS = {"Thai"}

TOKEN_RE = re.compile(r"[^\W\d_](?:[\w'\-]*[^\W\d_])?", re.UNICODE)


def _is_cjk(c: str) -> bool:
    cp = ord(c)
    return (
        0x3040 <= cp <= 0x30FF
        or 0x3400 <= cp <= 0x9FFF
        or 0xAC00 <= cp <= 0xD7AF
        or 0xF900 <= cp <= 0xFAFF
        or 0x20000 <= cp <= 0x2FFFF
    )


def _is_thai_letter(c: str) -> bool:
    cp = ord(c)
    return 0x0E00 <= cp <= 0x0E7F and unicodedata.category(c).startswith("L")


def tokenise(text: str, script: str) -> list[str]:
    if script in CJK_SCRIPTS:
        return [c for c in text if _is_cjk(c)]
    if script in NO_WORD_BOUNDARY_SCRIPTS:
        t = "".join(c for c in text if _is_thai_letter(c))
        return [t[i:i + 3] for i in range(len(t) - 2)]
    out = []
    for m in TOKEN_RE.finditer(text):
        tok = unicodedata.normalize("NFC", m.group(0)).lower().strip("'-")
        if len(tok) >= 2:
            out.append(tok)
    return out


def load_language_list() -> list[dict]:
    return json.loads(LANG_LIST.read_text(encoding="utf-8"))["languages"]


def build_counter_from_wiki(sub: str, script: str, max_articles: int) -> Counter:
    counter: Counter = Counter()
    parquet = download_wiki_parquet(sub)
    if parquet is None:
        return counter
    for _, body in iter_wiki_articles(parquet, max_articles=max_articles):
        counter.update(tokenise(body, script))
    return counter


def build_counter_from_examples(folder: Path, script: str) -> Counter:
    counter: Counter = Counter()
    ex = folder / "examples"
    if not ex.exists():
        return counter
    for p in ex.glob("*.txt"):
        counter.update(tokenise(p.read_text(encoding="utf-8", errors="replace"), script))
    return counter


def write_vocab(entry: dict, counter: Counter, sources_note: str) -> tuple[int, int]:
    folder = LANG_DIR / entry["folder"]
    path = folder / "vocabulary.json"
    tier_target = TIER_VOCAB[entry["tier"]]
    ranked = counter.most_common(tier_target)
    data = {
        "code": entry["code"],
        "name": entry["name"],
        "script": entry["script"],
        "tier": entry["tier"],
        "tier_target": tier_target,
        "source": sources_note,  # NOT commonlid / flores / madlad
        "total_tokens": sum(counter.values()),
        "unique_tokens": len(counter),
        "words": [{"word": w, "count": c} for w, c in ranked],
    }
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return (len(ranked), len(counter))


def parse_langs(arg: str | None, all_flag: bool, langs: list[dict]) -> list[dict]:
    if all_flag or not arg:
        return langs
    want = {c.strip() for c in arg.split(",") if c.strip()}
    return [l for l in langs if l["code"] in want]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", help="comma-separated ISO-639-3 codes")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--max-articles", type=int, default=2000,
                    help="cap on Wikipedia articles scanned per language")
    args = ap.parse_args()

    entries = parse_langs(args.lang, args.all, load_language_list())
    if not entries:
        entries = load_language_list()

    for entry in entries:
        code = entry["code"]
        script = entry["script"]
        cat = SOURCES.get(code, {})
        sub = cat.get("wikipedia")
        counter: Counter = Counter()
        notes: list[str] = []
        if sub:
            wiki_counter = build_counter_from_wiki(sub, script, args.max_articles)
            counter.update(wiki_counter)
            if wiki_counter:
                notes.append(f"Wikipedia ({sub}.wikipedia.org) via wikimedia/wikipedia {WP_DATE}")
        ex_counter = build_counter_from_examples(LANG_DIR / entry["folder"], script)
        counter.update(ex_counter)
        if ex_counter and "examples/" not in " ".join(notes):
            notes.append("examples/*.txt (live WebFetch of curated non-benchmark URLs)")
        source_note = "; ".join(notes) if notes else "UNAVAILABLE — needs manual curation"
        listed, unique = write_vocab(entry, counter, source_note)
        print(f"  {code:<4} listed={listed:>5}/{TIER_VOCAB[entry['tier']]:<5} "
              f"unique={unique:>6} tokens={sum(counter.values()):>8}  [{source_note}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
