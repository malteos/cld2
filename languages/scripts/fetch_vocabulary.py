#!/usr/bin/env python3
"""Build `vocabulary.json` for one or more languages from real multilingual
corpora available on HuggingFace.

Sources (in order):
    1. The CommonLID TSV itself — every line tagged with this language.
    2. FLORES+ dev/devtest splits for the same `iso_Script` combination — clean
       sentence-level text.

Tokenisation is Unicode-aware and lowercased. Output is frequency-ranked,
truncated to the tier target (high=10k, mid=5k, low=1k).

Script-writing-system tokenization notes:
    - For CJK scripts (Hans/Hant/Jpan/Hang) we keep single-character tokens
      because whitespace tokenisation is meaningless.
    - For Thai/Lao we fall back to character n-gram frequencies.
    - Otherwise we use a `[\\w'\\-]+` regex that understands Unicode letters.

Usage:
    source .venv/bin/activate
    python languages/scripts/fetch_vocabulary.py --all
    python languages/scripts/fetch_vocabulary.py --lang eng,deu --max-words 5000
"""
from __future__ import annotations

import argparse
import gzip
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LANG_LIST = ROOT / "languages" / "language_list.json"
LANG_DIR = ROOT / "languages"

TIER_VOCAB = {"high": 10000, "mid": 5000, "low": 1000}

CJK_SCRIPTS = {"Hans", "Hant", "Jpan", "Hang"}  # whitespace-free
NO_WORD_BOUNDARY_SCRIPTS = {"Thai"}             # Thai/Lao: use char n-grams

# Unicode-aware word regex. Matches letters (incl. Arabic, Devanagari etc.),
# apostrophes, and internal hyphens.
TOKEN_RE = re.compile(r"[^\W\d_](?:[\w'\-]*[^\W\d_])?", re.UNICODE)


def normalise(token: str) -> str:
    return unicodedata.normalize("NFC", token).lower()


def tokenise(text: str, script: str) -> list[str]:
    if script in CJK_SCRIPTS:
        # Keep runs of CJK characters as 1-char tokens; drop ASCII punctuation/digits.
        return [c for c in text if _is_cjk(c)]
    if script in NO_WORD_BOUNDARY_SCRIPTS:
        # Character 3-grams (decent proxy for Thai where there are no spaces).
        txt = "".join(c for c in text if _is_thai_letter(c))
        return [txt[i:i + 3] for i in range(len(txt) - 2)]
    out = []
    for m in TOKEN_RE.finditer(text):
        t = normalise(m.group(0)).strip("'-")
        if len(t) >= 2:
            out.append(t)
    return out


def _is_cjk(c: str) -> bool:
    cp = ord(c)
    return (
        0x3040 <= cp <= 0x30FF   # Hiragana/Katakana
        or 0x3400 <= cp <= 0x9FFF  # CJK Unified
        or 0xAC00 <= cp <= 0xD7AF  # Hangul
        or 0xF900 <= cp <= 0xFAFF  # CJK Compat
        or 0x20000 <= cp <= 0x2FFFF
    )


def _is_thai_letter(c: str) -> bool:
    cp = ord(c)
    return 0x0E00 <= cp <= 0x0E7F and unicodedata.category(c).startswith("L")


def load_language_list() -> list[dict]:
    return json.loads(LANG_LIST.read_text(encoding="utf-8"))["languages"]


# ---- data sources ---------------------------------------------------------

def commonlid_tsv() -> Path:
    from huggingface_hub import hf_hub_download
    return Path(hf_hub_download(
        repo_id="commoncrawl/CommonLID",
        filename="commonlid_20251209.tsv.gz",
        repo_type="dataset",
    ))


def flores_file(folder: str) -> Path | None:
    """Return a local path to the FLORES+ dev+devtest text for this folder, or
    None if FLORES doesn't carry it."""
    from huggingface_hub import hf_hub_download
    from huggingface_hub.utils import EntryNotFoundError
    import requests
    texts = []
    for split in ("dev", "devtest"):
        try:
            p = Path(hf_hub_download(
                repo_id="openlanguagedata/flores_plus",
                filename=f"{split}/{folder}.jsonl",
                repo_type="dataset",
            ))
            texts.append(p)
        except (EntryNotFoundError, requests.HTTPError):
            continue
        except Exception as exc:  # noqa: BLE001 - tolerate transient errors
            print(f"  [warn] flores fetch {folder}/{split}: {exc}", file=sys.stderr)
    if not texts:
        return None
    return texts  # list[Path]


def iter_commonlid_text(path: Path, wanted: set[str]):
    """Yield text for rows tagged with any of the codes in `wanted`."""
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as f:
        f.readline()  # header
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 3:
                continue
            if parts[1] in wanted:
                yield parts[1], parts[0]


def iter_flores_text(paths):
    for p in paths:
        with open(p, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                txt = rec.get("text")
                if txt:
                    yield txt


# ---- main -----------------------------------------------------------------

def build_vocab_for(entries: list[dict], commonlid_path: Path, max_override: int | None):
    # Bucket counters per code.
    counters: dict[str, Counter] = {e["code"]: Counter() for e in entries}
    scripts: dict[str, str] = {e["code"]: e["script"] for e in entries}

    # Pass 1: one linear scan of the CommonLID TSV.
    wanted = set(counters.keys())
    for code, text in iter_commonlid_text(commonlid_path, wanted):
        counters[code].update(tokenise(text, scripts[code]))

    # Pass 2: FLORES+ (per language).
    for entry in entries:
        paths = flores_file(entry["folder"])
        if not paths:
            continue
        for txt in iter_flores_text(paths):
            counters[entry["code"]].update(tokenise(txt, entry["script"]))

    # Write out.
    for entry in entries:
        code = entry["code"]
        folder = LANG_DIR / entry["folder"]
        target = max_override or TIER_VOCAB[entry["tier"]]
        vocab_path = folder / "vocabulary.json"
        data = json.loads(vocab_path.read_text(encoding="utf-8"))
        counter = counters[code]
        ranked = [(w, c) for w, c in counter.most_common(target)]
        data["words"] = [{"word": w, "count": c} for w, c in ranked]
        data.pop("note", None)
        data["source"] = "CommonLID TSV + FLORES+ (dev+devtest)"
        data["total_tokens"] = sum(counter.values())
        data["unique_tokens"] = len(counter)
        vocab_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  {code:<4} words={len(ranked):>5}/{target} unique={len(counter):>6} tokens={sum(counter.values()):>7}")


def parse_langs(arg: str | None, all_flag: bool, langs: list[dict]) -> list[dict]:
    if all_flag:
        return langs
    if not arg:
        return []
    want = {c.strip() for c in arg.split(",") if c.strip()}
    return [l for l in langs if l["code"] in want]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", help="comma-separated ISO-639-3 codes")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--max-words", type=int, default=None)
    args = ap.parse_args()

    langs = load_language_list()
    targets = parse_langs(args.lang, args.all, langs)
    if not targets:
        print("No languages selected (--lang or --all).", file=sys.stderr)
        return 2

    print(f"[info] downloading CommonLID TSV…", flush=True)
    path = commonlid_tsv()
    print(f"[info] scanning {len(targets)} language(s)")
    build_vocab_for(targets, path, args.max_words)
    return 0


if __name__ == "__main__":
    sys.exit(main())
