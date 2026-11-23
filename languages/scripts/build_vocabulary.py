#!/usr/bin/env python3
"""Build frequency-ranked vocabularies (~10k words) from real corpus statistics.

Sources (in order of preference):
  1. wordfreq (https://github.com/rspeer/wordfreq) -- multi-source frequencies
     (Wikipedia, subtitles, news, web text, Reddit/Twitter). Data: CC-BY-SA 4.0.
  2. FrequencyWords (https://github.com/hermitdave/FrequencyWords) -- OpenSubtitles
     2016/2018 frequency lists. Content: CC-BY-SA 4.0.

Existing AI-written vocabulary entries (with translation / pos) are merged in by word.

Usage:
    .venv/bin/python languages/scripts/build_vocabulary.py ces_Latn slk_Latn ...
    .venv/bin/python languages/scripts/build_vocabulary.py --chalis
"""
import argparse
import json
import os
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from translit import sr_lat2cyr  # noqa: E402

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FW_URL = "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/{year}/{lang}/{lang}_50k.txt"

# code -> (source, source_lang, postprocess)
SOURCES = {
    "ces_Latn": ("wordfreq", "cs", None),
    "slk_Latn": ("wordfreq", "sk", None),
    "spa_Latn": ("wordfreq", "es", None),
    "cat_Latn": ("wordfreq", "ca", None),
    "por_Latn": ("wordfreq", "pt", None),
    "glg_Latn": ("frequencywords", "gl", None),
    "dan_Latn": ("wordfreq", "da", None),
    "nob_Latn": ("wordfreq", "nb", None),
    "nld_Latn": ("wordfreq", "nl", None),
    "bul_Cyrl": ("wordfreq", "bg", None),
    "mkd_Cyrl": ("wordfreq", "mk", None),
    "rus_Cyrl": ("wordfreq", "ru", None),
    "srp_Cyrl": ("frequencywords", "sr", "sr_lat2cyr"),
    "kaz_Cyrl": ("frequencywords2016", "kk", None),
    "vie_Latn": ("wordfreq", "vi", None),
    "eng_Latn": ("wordfreq", "en", None),
    "ukr_Cyrl": ("wordfreq", "uk", None),
}
CHALIS = list(SOURCES)


def from_wordfreq(lang, n):
    import wordfreq
    words = wordfreq.top_n_list(lang, n * 2, wordlist="best")
    out = []
    for w in words:
        if not any(ch.isalpha() for ch in w):
            continue
        out.append({"word": w, "zipf": round(wordfreq.zipf_frequency(w, lang), 2)})
        if len(out) >= n:
            break
    return out, f"wordfreq ({lang})"


def from_frequencywords(lang, n, year="2018"):
    url = FW_URL.format(year=year, lang=lang)
    with urllib.request.urlopen(url, timeout=60) as r:
        lines = r.read().decode("utf-8").splitlines()
    out = []
    for line in lines:
        parts = line.rsplit(" ", 1)
        if len(parts) != 2 or not any(ch.isalpha() for ch in parts[0]):
            continue
        out.append({"word": parts[0], "count": int(parts[1])})
        if len(out) >= n:
            break
    return out, f"FrequencyWords OpenSubtitles {year} ({lang})"


def build(code, n):
    src, lang, post = SOURCES[code]
    if src == "wordfreq":
        entries, label = from_wordfreq(lang, n)
    elif src == "frequencywords2016":
        entries, label = from_frequencywords(lang, n, "2016")
    else:
        entries, label = from_frequencywords(lang, n)

    if post == "sr_lat2cyr":
        # OpenSubtitles Serbian is mostly Latin script; keep both forms.
        seen, conv = set(), []
        for e in entries:
            cyr = sr_lat2cyr(e["word"])
            if cyr in seen:
                continue
            seen.add(cyr)
            conv.append({**e, "word": cyr, "latin": e["word"]})
        entries = conv
        label += " transliterated Latin->Cyrillic"

    path = os.path.join(BASE, code, "vocabulary.json")
    old = {}
    if os.path.exists(path):
        try:
            for e in json.load(open(path, encoding="utf-8")):
                if isinstance(e, dict) and e.get("word") and (e.get("translation") or e.get("pos")):
                    old[e["word"]] = e
        except Exception:
            pass

    for i, e in enumerate(entries, 1):
        e["rank"] = i
        if e["word"] in old:
            for k in ("translation", "pos"):
                if old[e["word"]].get(k):
                    e[k] = old[e["word"]][k]
        e["source"] = label
    # key order: rank, word first
    entries = [{"rank": e.pop("rank"), "word": e.pop("word"), **e} for e in entries]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=0)
    print(f"{code}: {len(entries)} words from {label} (+{sum('translation' in e for e in entries)} glossed)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("codes", nargs="*")
    ap.add_argument("--chalis", action="store_true")
    ap.add_argument("-n", type=int, default=10000)
    a = ap.parse_args()
    for code in (CHALIS if a.chalis else a.codes):
        build(code, a.n)


if __name__ == "__main__":
    main()
