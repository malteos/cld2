#!/usr/bin/env python3
"""Build real example texts (>=100 words each) from Universal Dependencies treebanks.

UD treebanks contain authentic sentences (news, fiction, web, Wikipedia, ...).
Consecutive sentences of the same document (``# newdoc``) are joined into passages
of at least ``--min-words`` words. Files are written to ``<code>/examples/ud_NN.txt``
and provenance is recorded in ``<code>/examples/SOURCES.md``.

Usage:
    .venv/bin/python languages/scripts/fetch_ud_examples.py --chalis
    .venv/bin/python languages/scripts/fetch_ud_examples.py srp_Cyrl --count 12
"""
import argparse
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from translit import sr_lat2cyr  # noqa: E402

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = "https://raw.githubusercontent.com/UniversalDependencies/{repo}/master/{file}"

# code -> list of (repo, file, license, genre); post-processing key optional
TREEBANKS = {
    "ces_Latn": [("UD_Czech-FicTree", "cs_fictree-ud-test.conllu", "CC BY-NC-SA 4.0", "fiction"),
                 ("UD_Czech-CAC", "cs_cac-ud-test.conllu", "CC BY-SA 4.0", "mixed (news, science, admin)")],
    "slk_Latn": [("UD_Slovak-SNK", "sk_snk-ud-test.conllu", "CC BY-SA 4.0", "mixed (fiction, news, web)")],
    "spa_Latn": [("UD_Spanish-AnCora", "es_ancora-ud-test.conllu", "CC BY 4.0", "news")],
    "cat_Latn": [("UD_Catalan-AnCora", "ca_ancora-ud-test.conllu", "CC BY 4.0", "news")],
    "por_Latn": [("UD_Portuguese-Bosque", "pt_bosque-ud-test.conllu", "CC BY-SA 4.0", "news (PT and BR)")],
    "glg_Latn": [("UD_Galician-CTG", "gl_ctg-ud-test.conllu", "CC BY 3.0", "news, science, fiction")],
    "dan_Latn": [("UD_Danish-DDT", "da_ddt-ud-test.conllu", "CC BY-SA 4.0", "mixed (news, magazines)")],
    "nob_Latn": [("UD_Norwegian-Bokmaal", "no_bokmaal-ud-test.conllu", "CC BY-SA 4.0", "news, blogs, reports")],
    "nld_Latn": [("UD_Dutch-Alpino", "nl_alpino-ud-test.conllu", "CC BY-SA 4.0", "news")],
    "bul_Cyrl": [("UD_Bulgarian-BTB", "bg_btb-ud-test.conllu", "CC BY-NC-SA 3.0", "news, fiction, legal")],
    "mkd_Cyrl": [("UD_Macedonian-MTB", "mk_mtb-ud-test.conllu", "CC BY-SA 4.0", "fiction")],
    "rus_Cyrl": [("UD_Russian-SynTagRus", "ru_syntagrus-ud-test.conllu", "CC BY-SA 4.0", "news, fiction, popular science")],
    "srp_Cyrl": [("UD_Serbian-SET", "sr_set-ud-test.conllu", "CC BY-SA 4.0", "news (SETimes), Latin script transliterated to Cyrillic", "sr_lat2cyr")],
    "kaz_Cyrl": [("UD_Kazakh-KTB", "kk_ktb-ud-test.conllu", "CC BY-SA 4.0", "Wikipedia, fiction, news")],
    "vie_Latn": [("UD_Vietnamese-VTB", "vi_vtb-ud-test.conllu", "CC BY-SA 4.0", "news, fiction"),
                 ("UD_Vietnamese-VTB", "vi_vtb-ud-train.conllu", "CC BY-SA 4.0", "news, fiction")],
    "eng_Latn": [("UD_English-EWT", "en_ewt-ud-test.conllu", "CC BY-SA 4.0", "web (blogs, reviews, email, Q&A)")],
    "ukr_Cyrl": [("UD_Ukrainian-IU", "uk_iu-ud-test.conllu", "CC BY-NC-SA 4.0", "fiction, news, legal, letters")],
}
POST = {"sr_lat2cyr": sr_lat2cyr}


def detok(s):
    """Undo tokenizer spacing found in some treebanks (e.g. Vietnamese VTB)."""
    s = re.sub(r"\s+([.,:;!?%)\]])", r"\1", s)
    s = re.sub(r"([(\[])\s+", r"\1", s)
    s = re.sub(r'"\s*(.*?)\s*"', r'"\1"', s)
    return s


def read_docs(text):
    """Yield lists of sentence texts grouped by document (or paragraph runs)."""
    doc = []
    for line in text.splitlines():
        if line.startswith("# newdoc") and doc:
            yield doc
            doc = []
        else:
            m = re.match(r"# text\s*=\s*(.*)", line)
            if m:
                doc.append(detok(m.group(1).strip()))
    if doc:
        yield doc


def passages(docs, min_words, max_words):
    for doc in docs:
        buf, n = [], 0
        for sent in doc:
            buf.append(sent)
            n += len(sent.split())
            if n >= max_words:
                yield " ".join(buf)
                buf, n = [], 0
        if n >= min_words:
            yield " ".join(buf)


def build(code, count, min_words, max_words):
    exdir = os.path.join(BASE, code, "examples")
    os.makedirs(exdir, exist_ok=True)
    out, prov = [], []
    for spec in TREEBANKS[code]:
        repo, fname, lic, genre = spec[:4]
        post = POST.get(spec[4]) if len(spec) > 4 else None
        url = RAW.format(repo=repo, file=fname)
        with urllib.request.urlopen(url, timeout=120) as r:
            text = r.read().decode("utf-8")
        docs = list(read_docs(text))
        # If the treebank has no doc boundaries, chunk the whole stream.
        if len(docs) == 1:
            docs = [docs[0]]
        for p in passages(docs, min_words, max_words):
            if len(out) >= count:
                break
            out.append(post(p) if post else p)
            prov.append((repo, fname, lic, genre, url))
        if len(out) >= count:
            break

    for old in os.listdir(exdir):
        if old.startswith("ud_") and old.endswith(".txt"):
            os.remove(os.path.join(exdir, old))
    lines = [f"# Example text sources ({code})", "",
             "Files `ud_NN.txt` are authentic text from Universal Dependencies treebanks "
             "(consecutive sentences of one document joined into passages). Other `NN.txt` files, "
             "if present, were written by an LLM and are synthetic.", "",
             "| File | Words | Treebank | Genre | License |", "|---|---|---|---|---|"]
    for i, (p, (repo, fname, lic, genre, url)) in enumerate(zip(out, prov), 1):
        fn = f"ud_{i:02d}.txt"
        with open(os.path.join(exdir, fn), "w", encoding="utf-8") as f:
            f.write(p + "\n")
        lines.append(f"| {fn} | {len(p.split())} | [{repo}]({url}) | {genre} | {lic} |")
    with open(os.path.join(exdir, "SOURCES.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"{code}: {len(out)} passages")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("codes", nargs="*")
    ap.add_argument("--chalis", action="store_true")
    ap.add_argument("--count", type=int, default=12)
    ap.add_argument("--min-words", type=int, default=110)
    ap.add_argument("--max-words", type=int, default=220)
    a = ap.parse_args()
    for code in (list(TREEBANKS) if a.chalis else a.codes):
        build(code, a.count, a.min_words, a.max_words)


if __name__ == "__main__":
    main()
