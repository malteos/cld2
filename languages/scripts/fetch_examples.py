#!/usr/bin/env python3
"""Fetch example texts from Wikipedia for a given language.

Usage:
    python fetch_examples.py <lang_code> [--count 10]

Requires internet access.
"""
import json
import os
import re
import sys

import requests

ISO_TO_WIKI = {
    "eng": "en", "fra": "fr", "deu": "de", "spa": "es", "por": "pt",
    "ita": "it", "nld": "nl", "rus": "ru", "pol": "pl", "ces": "cs",
    "swe": "sv", "dan": "da", "fin": "fi", "hun": "hu", "ron": "ro",
    "tur": "tr", "ell": "el", "bul": "bg", "ukr": "uk", "cat": "ca",
    "hrv": "hr", "slk": "sk", "slv": "sl", "lit": "lt", "lvs": "lv",
    "est": "et", "isl": "is", "nob": "no", "nno": "nn", "heb": "he",
    "arb": "ar", "pes": "fa", "hin": "hi", "ben": "bn", "tam": "ta",
    "tel": "te", "mar": "mr", "urd": "ur", "tha": "th", "vie": "vi",
    "ind": "id", "msa": "ms", "jpn": "ja", "kor": "ko", "zho": "zh",
    "kat": "ka", "hye": "hy", "amh": "am", "swh": "sw", "afr": "af",
    "tgl": "tl", "mal": "ml", "kan": "kn", "guj": "gu", "pan": "pa",
    "mya": "my", "khm": "km", "lao": "lo", "sin": "si", "npi": "ne",
    "eus": "eu", "glg": "gl", "cym": "cy", "gle": "ga", "bos": "bs",
    "srp": "sr", "mkd": "mk", "bel": "be", "kaz": "kk", "uzn": "uz",
    "azj": "az", "mon": "mn", "yor": "yo", "hau": "ha", "ibo": "ig",
    "som": "so", "als": "sq", "mlt": "mt",
}

MIN_WORDS = 100


def fetch_examples(wiki_code, count=10, max_attempts=50):
    """Fetch random Wikipedia articles with at least MIN_WORDS words."""
    examples = []
    session = requests.Session()
    attempts = 0
    while len(examples) < count and attempts < max_attempts:
        attempts += 1
        try:
            resp = session.get(
                f"https://{wiki_code}.wikipedia.org/w/api.php",
                params={"action": "query", "list": "random", "rnnamespace": 0,
                        "rnlimit": 5, "format": "json"},
                timeout=10,
            )
            pages = resp.json().get("query", {}).get("random", [])
            for page in pages:
                if len(examples) >= count:
                    break
                title = page["title"]
                resp2 = session.get(
                    f"https://{wiki_code}.wikipedia.org/w/api.php",
                    params={"action": "query", "titles": title, "prop": "extracts",
                            "explaintext": True, "format": "json"},
                    timeout=10,
                )
                pages2 = resp2.json().get("query", {}).get("pages", {})
                for p in pages2.values():
                    text = p.get("extract", "").strip()
                    text = re.sub(r"\n{3,}", "\n\n", text)
                    word_count = len(text.split())
                    if word_count >= MIN_WORDS:
                        examples.append({"title": title, "text": text, "word_count": word_count})
        except Exception:
            continue
    return examples


def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_examples.py <lang_code> [--count 10]")
        sys.exit(1)

    lang_code = sys.argv[1]
    count = 10
    if "--count" in sys.argv:
        idx = sys.argv.index("--count")
        count = int(sys.argv[idx + 1])

    iso = lang_code.split("_")[0]
    wiki_code = ISO_TO_WIKI.get(iso)
    if not wiki_code:
        print(f"No Wikipedia code mapping for {iso}. Skipping.")
        sys.exit(0)

    print(f"Fetching {count} examples for {lang_code} from {wiki_code}.wikipedia.org...")
    examples = fetch_examples(wiki_code, count)
    print(f"Got {len(examples)} examples")

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    examples_dir = os.path.join(base_dir, lang_code, "examples")
    os.makedirs(examples_dir, exist_ok=True)

    for i, ex in enumerate(examples, 1):
        slug = re.sub(r"[^\w]", "_", ex["title"].lower())[:40]
        filename = f"{i:02d}_{slug}.txt"
        filepath = os.path.join(examples_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(ex["text"])
        print(f"  Wrote {filepath} ({ex['word_count']} words)")


if __name__ == "__main__":
    main()
