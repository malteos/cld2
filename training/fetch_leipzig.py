#!/usr/bin/env python3
"""Fetch training corpora from the Leipzig Corpora Collection and write
train/eval TSVs in the format the CLD2 trainer expects.

Each Leipzig corpus is a tar.gz containing <name>-sentences.txt with lines
"<id>\t<sentence>". We concatenate sentences into documents of a few
hundred bytes (CLD2 is a document classifier, not a sentence classifier),
and split them 90/10 into train/eval.

Example:
  fetch_leipzig.py --out data \
      --corpus en=eng_news_2023_10K --corpus de=deu_news_2023_10K \
      --corpus cv=chv_wikipedia_2021_10K

Downloads are cached in <out>/cache/.
"""

import argparse
import io
import random
import sys
import tarfile
import urllib.request
from pathlib import Path

BASE = "https://downloads.wortschatz-leipzig.de/corpora/"


def fetch(corpus: str, cache: Path) -> bytes:
    cache.mkdir(parents=True, exist_ok=True)
    f = cache / f"{corpus}.tar.gz"
    if not f.exists():
        url = BASE + f"{corpus}.tar.gz"
        print(f"downloading {url}", file=sys.stderr)
        with urllib.request.urlopen(url, timeout=120) as r:
            f.write_bytes(r.read())
    return f.read_bytes()


def sentences(tgz: bytes):
    with tarfile.open(fileobj=io.BytesIO(tgz), mode="r:gz") as tf:
        for m in tf.getmembers():
            if m.name.endswith("-sentences.txt"):
                data = tf.extractfile(m).read().decode("utf-8", "replace")
                for line in data.split("\n"):
                    parts = line.split("\t", 1)
                    if len(parts) == 2 and parts[1].strip():
                        yield parts[1].strip()
                return
    raise RuntimeError("no -sentences.txt member found")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", action="append", required=True,
                    metavar="code=leipzig_name",
                    help="e.g. en=eng_news_2023_10K (repeatable)")
    ap.add_argument("--out", default="training/data", help="output directory")
    ap.add_argument("--doc_bytes", type=int, default=600,
                    help="approximate bytes per training document")
    ap.add_argument("--eval_fraction", type=float, default=0.10)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    train_f = (out / "train.tsv").open("w", encoding="utf-8")
    eval_f = (out / "eval.tsv").open("w", encoding="utf-8")
    for spec in args.corpus:
        code, _, corpus = spec.partition("=")
        if not corpus:
            sys.exit(f"error: bad --corpus {spec}, want code=leipzig_name")
        sents = list(sentences(fetch(corpus, out / "cache")))
        rng.shuffle(sents)
        # Pack sentences into documents of ~doc_bytes
        docs = []
        cur = []
        cur_len = 0
        for s in sents:
            s = s.replace("\t", " ")
            cur.append(s)
            cur_len += len(s.encode()) + 1
            if cur_len >= args.doc_bytes:
                docs.append(" ".join(cur))
                cur, cur_len = [], 0
        if cur:
            docs.append(" ".join(cur))
        n_eval = max(1, int(len(docs) * args.eval_fraction))
        for i, d in enumerate(docs):
            (eval_f if i < n_eval else train_f).write(f"{code}\t{d}\n")
        print(f"{code}: {len(sents)} sentences -> {len(docs)} docs "
              f"({n_eval} eval)", file=sys.stderr)
    train_f.close()
    eval_f.close()
    print(f"wrote {out}/train.tsv and {out}/eval.tsv", file=sys.stderr)


if __name__ == "__main__":
    main()
