#!/usr/bin/env python3
"""Fetch vocabulary/word frequency lists from Wiktionary and Wikipedia APIs.

Usage:
    python fetch_vocabulary.py <lang_code> [--merge]

Requires internet access. Fetches from:
- Wiktionary frequency lists (Appendix pages)
- Wikipedia: extracts most common words from random articles
"""
import json
import os
import re
import sys
from collections import Counter

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


def fetch_wikipedia_words(wiki_code, num_articles=50):
    """Fetch random Wikipedia articles and extract word frequencies."""
    words = Counter()
    session = requests.Session()
    for _ in range(num_articles):
        try:
            resp = session.get(
                f"https://{wiki_code}.wikipedia.org/w/api.php",
                params={"action": "query", "list": "random", "rnnamespace": 0,
                        "rnlimit": 1, "format": "json"},
                timeout=10,
            )
            pages = resp.json().get("query", {}).get("random", [])
            if not pages:
                continue
            title = pages[0]["title"]
            resp2 = session.get(
                f"https://{wiki_code}.wikipedia.org/w/api.php",
                params={"action": "query", "titles": title, "prop": "extracts",
                        "explaintext": True, "format": "json"},
                timeout=10,
            )
            pages2 = resp2.json().get("query", {}).get("pages", {})
            for page in pages2.values():
                text = page.get("extract", "")
                for word in re.findall(r"\b\w+\b", text.lower()):
                    if len(word) > 1:
                        words[word] += 1
        except Exception:
            continue
    return words


def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_vocabulary.py <lang_code> [--merge]")
        sys.exit(1)

    lang_code = sys.argv[1]
    merge = "--merge" in sys.argv
    iso = lang_code.split("_")[0]
    wiki_code = ISO_TO_WIKI.get(iso)

    if not wiki_code:
        print(f"No Wikipedia code mapping for {iso}. Skipping.")
        sys.exit(0)

    print(f"Fetching vocabulary for {lang_code} from {wiki_code}.wikipedia.org...")
    words = fetch_wikipedia_words(wiki_code)
    print(f"Extracted {len(words)} unique words from Wikipedia")

    vocab = [{"rank": i + 1, "word": w, "frequency": c}
             for i, (w, c) in enumerate(words.most_common(10000))]

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    vocab_path = os.path.join(base_dir, lang_code, "vocabulary.json")

    if merge and os.path.exists(vocab_path):
        with open(vocab_path) as f:
            existing = json.load(f)
        existing_words = {e["word"] for e in existing}
        new_entries = [v for v in vocab if v["word"] not in existing_words]
        combined = existing + new_entries
        for i, entry in enumerate(combined):
            entry["rank"] = i + 1
        vocab = combined
        print(f"Merged: {len(vocab)} total words")

    with open(vocab_path, "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=1)
    print(f"Wrote {len(vocab)} words to {vocab_path}")


if __name__ == "__main__":
    main()
