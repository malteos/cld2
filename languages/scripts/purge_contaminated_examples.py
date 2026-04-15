#!/usr/bin/env python3
"""Remove `examples/*.txt` files that overlap with CommonLID or FLORES+ and
re-fetch replacement passages from a different part of the same source site.

Why this is needed
------------------
Wikipedia is a legitimate, non-benchmark source website — but CommonLID was
built from Common Crawl, which crawls Wikipedia heavily. Some Wikipedia
paragraphs therefore appear verbatim in both our `examples/` and in the
CommonLID TSV. That is train–test leakage even though the source site itself
is outside the benchmark list. The fix is to check each candidate passage
against CommonLID and FLORES+ before keeping it.

Workflow
--------
1. Load CommonLID (via HF, requires HF_TOKEN) and FLORES+ line sets.
2. For every `examples/*.txt`, flag any 80-char substring that also appears
   in the benchmark lines for that language.
3. Delete flagged files.
4. Re-run `fetch_web_examples.py` for the affected languages, this time
   passing the same benchmark-line sets as a filter so candidate passages
   are rejected before they're written.

Usage
-----
    source .venv/bin/activate
    set -a && source .env && set +a
    python languages/scripts/purge_contaminated_examples.py --all
    python languages/scripts/purge_contaminated_examples.py --lang xho,sna
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[2]
LANG_LIST = ROOT / "languages" / "language_list.json"
LANG_DIR = ROOT / "languages"
SUBSTRING_WINDOW = 80
MIN_SIGNIFICANT_LINE = 20

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sources_catalog import SOURCES  # noqa: E402
from fetch_web_examples import (  # noqa: E402
    download_wiki_parquet, iter_wiki_articles, split_into_passages,
    fetch_url, extract_paragraphs, extract_article_links,
    update_overview_sources, WP_DATE,
)


def load_language_list() -> list[dict]:
    return json.loads(LANG_LIST.read_text(encoding="utf-8"))["languages"]


def _download_commonlid() -> Path | None:
    try:
        from huggingface_hub import hf_hub_download
        return Path(hf_hub_download(
            repo_id="commoncrawl/CommonLID",
            filename="commonlid_20251209.tsv.gz",
            repo_type="dataset",
            token=os.environ.get("HF_TOKEN"),
        ))
    except Exception as exc:  # noqa: BLE001
        print(f"[warn] cannot fetch CommonLID: {exc}", file=sys.stderr)
        return None


def _download_flores_for(folder: str) -> set[str]:
    lines: set[str] = set()
    try:
        from huggingface_hub import hf_hub_download
        from huggingface_hub.utils import EntryNotFoundError
    except Exception:
        return lines
    for split in ("dev", "devtest"):
        try:
            p = hf_hub_download(
                repo_id="openlanguagedata/flores_plus",
                filename=f"{split}/{folder}.jsonl",
                repo_type="dataset",
                token=os.environ.get("HF_TOKEN"),
            )
        except EntryNotFoundError:
            continue
        except Exception:
            continue
        with open(p, "r", encoding="utf-8") as f:
            for ln in f:
                try:
                    rec = json.loads(ln)
                except json.JSONDecodeError:
                    continue
                txt = (rec.get("text") or "").strip()
                if len(txt) >= MIN_SIGNIFICANT_LINE:
                    lines.add(txt)
    return lines


def load_commonlid_buckets() -> dict[str, set[str]]:
    path = _download_commonlid()
    if path is None:
        return {}
    buckets: dict[str, set[str]] = defaultdict(set)
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as f:
        f.readline()
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 3:
                continue
            text, code = parts[0].strip(), parts[1].strip()
            if len(text) >= MIN_SIGNIFICANT_LINE:
                buckets[code].add(text)
    return dict(buckets)


def passage_contaminated(passage: str, bench_lines: set[str]) -> bool:
    """True if any 80-char window of `passage` appears in any line of
    bench_lines. Short-circuits on first match."""
    for line in bench_lines:
        if len(line) < SUBSTRING_WINDOW:
            continue
        for i in range(len(passage) - SUBSTRING_WINDOW + 1):
            if passage[i:i + SUBSTRING_WINDOW] in line:
                return True
    return False


def safe_wiki_passages(sub: str, target: int, min_chars: int,
                      bench_lines: set[str], max_articles: int = 5000) -> list[tuple[str, str]]:
    """Stream Wikipedia articles and return up to `target` (title, passage)
    pairs whose passages do NOT overlap with bench_lines."""
    out: list[tuple[str, str]] = []
    parquet = download_wiki_parquet(sub)
    if parquet is None:
        return out
    for title, body in iter_wiki_articles(parquet, max_articles=max_articles):
        if len(out) >= target:
            break
        for p in split_into_passages(body, min_chars):
            if len(out) >= target:
                break
            if passage_contaminated(p, bench_lines):
                continue
            out.append((title, p))
    return out


def safe_web_passages(urls: list[dict], target: int, min_chars: int,
                      bench_lines: set[str]) -> list[tuple[dict, str]]:
    out: list[tuple[dict, str]] = []
    for src in urls:
        if len(out) >= target:
            break
        url = src["url"]
        html = fetch_url(url)
        if html is None:
            continue
        candidates = extract_paragraphs(html, min_chars=min_chars)
        if len(candidates) < 3:
            for link in extract_article_links(html, url, max_links=5):
                sub_html = fetch_url(link)
                if sub_html is None:
                    continue
                candidates.extend(extract_paragraphs(sub_html, min_chars=max(200, min_chars // 2)))
                time.sleep(0.3)
        for p in candidates:
            if len(out) >= target:
                break
            if passage_contaminated(p, bench_lines):
                continue
            out.append((src, p))
        time.sleep(0.3)
    return out


def refresh_language(entry: dict, bench_lines: set[str], target: int,
                     min_chars: int) -> dict:
    code = entry["code"]
    folder = LANG_DIR / entry["folder"]
    ex_dir = folder / "examples"
    if ex_dir.exists():
        for p in ex_dir.glob("*.txt"):
            p.unlink()
    ex_dir.mkdir(parents=True, exist_ok=True)

    cat = SOURCES.get(code, {})
    wp_sub = cat.get("wikipedia")
    non_wiki = [s for s in cat.get("sources", [])
                if not (wp_sub and s["url"].startswith(f"https://{wp_sub}.wikipedia.org"))]

    wiki_quota = target // 2 if non_wiki else target
    web_quota = target - wiki_quota

    used: list[dict] = []
    passages: list[str] = []

    if wp_sub:
        wiki = safe_wiki_passages(wp_sub, wiki_quota, min_chars, bench_lines)
        for title, p in wiki:
            passages.append(
                f"# Source: Wikipedia article \"{title}\" "
                f"(https://{wp_sub}.wikipedia.org/)\n\n{p}"
            )
        if wiki:
            used.append({
                "url": f"https://{wp_sub}.wikipedia.org/",
                "via": f"wikimedia/wikipedia {WP_DATE}",
                "type": "cultural",
                "articles_used": len(wiki),
                "articles_sample": [t for t, _ in wiki[:3]],
            })

    web = safe_web_passages(non_wiki, web_quota, min_chars, bench_lines)
    for src, p in web:
        passages.append(f"# Source: {src['url']} ({src.get('description','')})\n\n{p}")
    for src in {s["url"]: s for s, _ in web}.values():
        used.append({
            "url": src["url"],
            "via": "live WebFetch",
            "type": src.get("type", "?"),
            "description": src.get("description", ""),
        })

    # Top up from Wikipedia if short
    if len(passages) < target and wp_sub:
        remaining = target - len(passages)
        taken_titles = {pp.splitlines()[0] for pp in passages}
        more = safe_wiki_passages(wp_sub, remaining * 3, min_chars, bench_lines,
                                  max_articles=8000)
        added = 0
        for title, p in more:
            if added >= remaining:
                break
            hdr = f'# Source: Wikipedia article "{title}" (https://{wp_sub}.wikipedia.org/)'
            if hdr in taken_titles:
                continue
            passages.append(f"{hdr}\n\n{p}")
            added += 1

    for i, p in enumerate(passages, start=1):
        (ex_dir / f"{i:02d}.txt").write_text(p + "\n", encoding="utf-8")

    update_overview_sources(folder, entry, used)

    return {
        "folder": entry["folder"],
        "passages_written": len(passages),
        "sources_used": used,
    }


def parse_langs(arg: str | None, all_flag: bool, langs: list[dict]) -> list[dict]:
    if all_flag or not arg:
        return langs
    want = {c.strip() for c in arg.split(",") if c.strip()}
    return [l for l in langs if l["code"] in want]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", help="comma-separated ISO-639-3 codes")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--count", type=int, default=12)
    ap.add_argument("--min-chars", type=int, default=400)
    ap.add_argument("--report", help="path to a contamination_report.json to target only affected languages")
    args = ap.parse_args()

    entries = parse_langs(args.lang, args.all, load_language_list())
    if not entries:
        entries = load_language_list()
    if args.report:
        report = json.loads(Path(args.report).read_text(encoding="utf-8"))
        affected = {c for c, d in report["per_language"].items() if d.get("hits")}
        entries = [e for e in entries if e["code"] in affected]
        print(f"[info] targeting {len(entries)} languages from report")

    print("[info] loading CommonLID …", flush=True)
    commonlid = load_commonlid_buckets()
    manifest_update: dict[str, dict] = {}
    for entry in entries:
        code = entry["code"]
        bench = set(commonlid.get(code, set()))
        bench |= _download_flores_for(entry["folder"])
        res = refresh_language(entry, bench, args.count, args.min_chars)
        manifest_update[code] = res
        print(f"  {code:<4} wrote={res['passages_written']:>2} bench_lines={len(bench):>6}")

    # merge into existing manifest
    mpath = LANG_DIR / "sources_manifest.json"
    existing = {}
    if mpath.exists():
        try:
            existing = json.loads(mpath.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            existing = {}
    existing.update(manifest_update)
    mpath.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
