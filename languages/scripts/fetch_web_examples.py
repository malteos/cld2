#!/usr/bin/env python3
"""Rebuild `examples/*.txt` for every language from non-benchmark websites.

Pipeline per language:
    1. Wipe the existing `examples/` directory (previous contents were
       seeded from CommonLID / FLORES+; both are evaluation benchmarks).
    2. Try the primary source — `wikimedia/wikipedia` HuggingFace dump —
       which covers ~95 of our 109 languages and gives long paragraph-level
       passages cheaply.
    3. Supplement / fall back to live WebFetch of the curated URLs in
       `sources_catalog.py` (government sites, news, cultural portals,
       religious publications translated into the language, etc.).
    4. Append a "Sources" section to `overview.md` with the exact list of
       URLs that contributed to this language's examples.

Never used:
    - CommonLID (commoncrawl/CommonLID)
    - FLORES+ (openlanguagedata/flores_plus)
    - MADLAD-400, OPUS-100, WMT test sets, Tatoeba — see
      `check_contamination.py` for the full banned-sources list.

Usage
-----
    source .venv/bin/activate
    python languages/scripts/fetch_web_examples.py --all
    python languages/scripts/fetch_web_examples.py --lang eng,deu
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[2]
LANG_LIST = ROOT / "languages" / "language_list.json"
LANG_DIR = ROOT / "languages"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sources_catalog import SOURCES  # noqa: E402

WP_DATE = "20231101"
USER_AGENT = (
    "cld2-lang-kb/0.1 (+https://github.com/malteos/cld2; research; "
    "contact via github issues) python-requests"
)
HEADERS = {"User-Agent": USER_AGENT, "Accept-Language": "*"}


def load_language_list() -> list[dict]:
    return json.loads(LANG_LIST.read_text(encoding="utf-8"))["languages"]


# ---------------------------------------------------------------------------
# Wikipedia HF dump (primary source)
# ---------------------------------------------------------------------------

# Cached listing of all parquet shards per Wikipedia edition.
_WP_SHARD_CACHE: dict[str, list[str]] | None = None


def _wiki_shard_index() -> dict[str, list[str]]:
    global _WP_SHARD_CACHE
    if _WP_SHARD_CACHE is not None:
        return _WP_SHARD_CACHE
    from huggingface_hub import HfApi
    api = HfApi()
    info = api.dataset_info("wikimedia/wikipedia")
    idx: dict[str, list[str]] = {}
    prefix = f"{WP_DATE}."
    for s in info.siblings:
        name = s.rfilename
        if prefix not in name or not name.endswith(".parquet"):
            continue
        first = name.split("/")[0]  # e.g. "20231101.en"
        sub = first[len(prefix):]
        idx.setdefault(sub, []).append(name)
    for k in idx:
        idx[k].sort()
    _WP_SHARD_CACHE = idx
    return idx


def download_wiki_parquet(subdomain: str) -> Path | None:
    """Download the first shard of the given Wikipedia edition. Returns
    the local path or None if no edition exists under that subdomain."""
    from huggingface_hub import hf_hub_download
    from huggingface_hub.utils import EntryNotFoundError
    shards = _wiki_shard_index().get(subdomain, [])
    if not shards:
        return None
    try:
        return Path(hf_hub_download(
            repo_id="wikimedia/wikipedia",
            filename=shards[0],
            repo_type="dataset",
        ))
    except EntryNotFoundError:
        return None
    except Exception as exc:  # noqa: BLE001
        print(f"  [warn] hf fetch {shards[0]}: {exc}", file=sys.stderr)
        return None


def iter_wiki_articles(parquet_path: Path, max_articles: int = 2000):
    """Stream articles from a Wikipedia parquet shard without loading the
    whole shard into RAM (English's shard-0 is multi-hundred MB)."""
    import pyarrow.parquet as pq
    pf = pq.ParquetFile(parquet_path)
    seen = 0
    for batch in pf.iter_batches(batch_size=256, columns=["title", "text"]):
        titles = batch.column("title").to_pylist()
        texts = batch.column("text").to_pylist()
        for t, x in zip(titles, texts):
            if seen >= max_articles:
                return
            if t and x and isinstance(x, str):
                yield t, x
                seen += 1


# ---------------------------------------------------------------------------
# Live web-fetch (secondary source)
# ---------------------------------------------------------------------------

_HTML_TAG = re.compile(r"<[^>]+>")
_SCRIPT_STYLE = re.compile(r"<(script|style|nav|header|footer|noscript|svg|form|aside)[^>]*>.*?</\1>", re.I | re.S)
_WHITESPACE = re.compile(r"\s+")


def strip_html(html: str) -> str:
    html = _SCRIPT_STYLE.sub(" ", html)
    text = _HTML_TAG.sub(" ", html)
    text = text.replace("&nbsp;", " ").replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    text = text.replace("&quot;", '"').replace("&#39;", "'").replace("&apos;", "'")
    return _WHITESPACE.sub(" ", text).strip()


def fetch_url(url: str, timeout: int = 8) -> str | None:
    try:
        r = requests.get(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
        if r.status_code != 200:
            return None
        # Some sites serve UTF-8 but forget to declare it; trust apparent encoding.
        if not r.encoding or r.encoding.lower() in ("iso-8859-1",):
            r.encoding = r.apparent_encoding or "utf-8"
        return r.text
    except Exception as exc:  # noqa: BLE001
        print(f"    [warn] fetch failed {url}: {type(exc).__name__}: {str(exc)[:80]}", file=sys.stderr)
        return None


def extract_article_links(html: str, base_url: str, max_links: int = 8) -> list[str]:
    """Return up to `max_links` in-domain links pointing to article-like
    pages. News homepages are mostly navigation; actual paragraph content
    lives one click down. We follow links on the same origin whose path
    looks like an article slug."""
    from urllib.parse import urljoin, urlparse
    base = urlparse(base_url)
    seen: set[str] = set()
    out: list[str] = []
    for m in re.finditer(r'href\s*=\s*"([^"#?]+)"', html, flags=re.I):
        href = m.group(1)
        if href.startswith(("mailto:", "javascript:", "tel:")):
            continue
        full = urljoin(base_url, href)
        p = urlparse(full)
        if p.netloc != base.netloc:
            continue
        path = p.path
        # Heuristic: article-like paths have >=2 segments and end with slug.
        segs = [s for s in path.split("/") if s]
        if len(segs) < 2:
            continue
        last = segs[-1]
        if not any(c.isalpha() for c in last) or "." in last and not last.endswith((".html", ".htm", ".php")):
            continue
        if full in seen:
            continue
        seen.add(full)
        out.append(full)
        if len(out) >= max_links:
            break
    return out


_NAV_MARKERS = re.compile(
    r"\b(?:accueil|menu|rubriques|plus d[ae']?\s*infos?|abonnement|"
    r"suivez[\- ]nous|tous droits r[eé]serv|mentions l[eé]gales|"
    r"cookies?|newsletter|home|subscribe|newsletter|privacy policy|"
    r"terms of (?:service|use)|login|sign\s?up|search|archives?|"
    r"directory|footer)\b", re.I)


def _is_cjk_or_thai_dominant(text: str) -> bool:
    """True if the text is mostly CJK, Thai, Lao, or Khmer — scripts that
    don't use spaces between words. Different heuristics apply."""
    n = sum(1 for c in text
            if 0x3040 <= ord(c) <= 0x9FFF
            or 0xAC00 <= ord(c) <= 0xD7AF
            or 0x0E00 <= ord(c) <= 0x0EFF
            or 0x1780 <= ord(c) <= 0x17FF)
    return n > 0.4 * max(1, len(text))


_SCRIPT_RANGES = [
    ("Latin",  (0x0041, 0x024F)),
    ("Cyrl",   (0x0400, 0x04FF)),
    ("Grek",   (0x0370, 0x03FF)),
    ("Arab",   (0x0600, 0x06FF)),
    ("Hebr",   (0x0590, 0x05FF)),
    ("Deva",   (0x0900, 0x097F)),
    ("Beng",   (0x0980, 0x09FF)),
    ("Guru",   (0x0A00, 0x0A7F)),
    ("Gujr",   (0x0A80, 0x0AFF)),
    ("Orya",   (0x0B00, 0x0B7F)),
    ("Taml",   (0x0B80, 0x0BFF)),
    ("Telu",   (0x0C00, 0x0C7F)),
    ("Knda",   (0x0C80, 0x0CFF)),
    ("Mlym",   (0x0D00, 0x0D7F)),
    ("Thai",   (0x0E00, 0x0E7F)),
    ("CJK",    (0x3040, 0x9FFF)),
    ("Hang",   (0xAC00, 0xD7AF)),
]

_DIGEST_SMELL = re.compile(
    r"\b(?:\d+ (?:hrs?|mins?|hours?|minutes?|days?|weeks?|months?) ago|"
    r"read more|click here|see more|full story|continue reading|"
    r"copyright \d{4}|all rights reserved|privacy policy|terms of use)\b",
    re.I)


def _count_scripts(text: str) -> int:
    present = set()
    for c in text:
        cp = ord(c)
        for name, (lo, hi) in _SCRIPT_RANGES:
            if lo <= cp <= hi:
                present.add(name)
                break
    return len(present)


def _looks_like_prose(text: str) -> bool:
    """Reject nav/menu strings, site chrome, and multi-script language
    menus. Real article paragraphs have:
      - sentence-ending punctuation at a reasonable density
      - one dominant script (with limited loan-script tokens)
      - no overt UI / digest markers
    """
    # CJK / Thai / Lao / Khmer: skip the Latin word-boundary heuristics.
    if _is_cjk_or_thai_dominant(text):
        if len(text) < 120:
            return False
        if _NAV_MARKERS.search(text) or _DIGEST_SMELL.search(text):
            return False
        # Still reject if text mixes >3 scripts (typical of language menus).
        if _count_scripts(text) > 3:
            return False
        return True

    # Sentence-ending punctuation: real prose has several per paragraph.
    words = text.split()
    if len(words) < 10:
        return False
    n_end = sum(text.count(p) for p in (".", "!", "?", "…", "。", "！", "？", "؟"))
    if n_end / len(words) < 0.02:
        return False
    # Word-length heuristic for space-separated scripts.
    avg = sum(len(w) for w in words) / len(words)
    if avg < 3.2:
        return False
    # UI-copy smell: lots of short Title Case tokens concatenated.
    title_short = sum(1 for w in words if w[:1].isupper() and len(w) < 8)
    if title_short > 0.55 * len(words) and len(words) > 8:
        return False
    # Cross-script contamination: language menus list dozens of languages.
    if _count_scripts(text) > 3:
        return False
    # News-digest smell (timestamps, "read more", copyright).
    if len(text) < 1200 and _DIGEST_SMELL.search(text):
        return False
    # Common navigation marker presence in a short string is disqualifying.
    if len(text) < 600 and _NAV_MARKERS.search(text):
        return False
    return True


def extract_paragraphs(html: str, min_chars: int = 300) -> list[str]:
    """Pull `<p>` / `<article>` text chunks and strip HTML. Filters out
    navigation boilerplate, cookie notices, and UI menus."""
    paras = re.findall(r"<p[^>]*>(.*?)</p>", html, flags=re.I | re.S)
    # Also consider <article> and <div class=...content...> blocks when
    # the site ships dense article bodies that aren't wrapped in <p>.
    paras += re.findall(r"<(?:article|section)[^>]*>(.*?)</(?:article|section)>",
                        html, flags=re.I | re.S)
    out: list[str] = []
    seen: set[str] = set()
    for p in paras:
        text = strip_html(p).strip()
        if len(text) < min_chars or " " not in text:
            continue
        if not _looks_like_prose(text):
            continue
        # Dedupe — nav/header text repeats on every sub-page.
        key = text[:120]
        if key in seen:
            continue
        seen.add(key)
        out.append(text)
    return out


# ---------------------------------------------------------------------------
# Per-language driver
# ---------------------------------------------------------------------------

def split_into_passages(text: str, min_chars: int, max_chars: int = 1500) -> list[str]:
    passages: list[str] = []
    paragraphs = re.split(r"\n\s*\n", text)
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if min_chars <= len(p) <= max_chars:
            passages.append(p)
        elif len(p) > max_chars:
            # split long ones by sentence approximation
            buf, total = [], 0
            for sent in re.split(r"(?<=[\.\?!])\s+", p.replace("\n", " ")):
                sent = sent.strip()
                if not sent:
                    continue
                buf.append(sent)
                total += len(sent) + 1
                if total >= min_chars:
                    passages.append(" ".join(buf))
                    buf, total = [], 0
            if buf and total >= min_chars:
                passages.append(" ".join(buf))
    return passages


def build_examples(entry: dict, target_count: int, min_chars: int) -> tuple[list[dict], list[str]]:
    """Interleave passages from Wikipedia and curated live URLs so every
    language ends up with contributions from multiple sources where
    possible. Returns (used_sources, example_passages)."""
    code = entry["code"]
    cat = SOURCES.get(code)
    used: list[dict] = []
    passages: list[str] = []

    wp_sub = cat.get("wikipedia") if cat else None
    non_wiki_sources = [s for s in (cat.get("sources", []) if cat else [])
                        if not (wp_sub and s["url"].startswith(f"https://{wp_sub}.wikipedia.org"))]

    # Rough quota: half to Wikipedia, half to live web. When one side is
    # absent, give its share to the other.
    if wp_sub and non_wiki_sources:
        wiki_quota = target_count // 2
    elif wp_sub:
        wiki_quota = target_count
    else:
        wiki_quota = 0
    web_quota = target_count - wiki_quota

    # --- 1. Pull from Wikipedia up to its quota ---------------------------
    if wp_sub:
        parquet = download_wiki_parquet(wp_sub)
        if parquet is not None:
            taken_titles: list[str] = []
            for title, body in iter_wiki_articles(parquet, max_articles=3000):
                if len(taken_titles) >= wiki_quota:
                    break
                for p in split_into_passages(body, min_chars):
                    if len(taken_titles) >= wiki_quota:
                        break
                    passages.append(f"# Source: Wikipedia article \"{title}\" "
                                    f"(https://{wp_sub}.wikipedia.org/)\n\n{p}")
                    taken_titles.append(title)
            if taken_titles:
                used.append({
                    "url": f"https://{wp_sub}.wikipedia.org/",
                    "via": f"wikimedia/wikipedia {WP_DATE}",
                    "type": "cultural",
                    "articles_used": len(taken_titles),
                    "articles_sample": taken_titles[:3],
                })

    # --- 2. Pull from each curated live URL -------------------------------
    per_src = max(1, web_quota // max(len(non_wiki_sources), 1)) if non_wiki_sources else 0
    # For low-resource languages where the homepage has little paragraph
    # text, fall back to following article links one level deep.
    for src in non_wiki_sources:
        if len(passages) >= target_count:
            break
        url = src["url"]
        html = fetch_url(url)
        if html is None:
            continue
        got = extract_paragraphs(html, min_chars=min_chars)
        # If the homepage yielded little (typical for nav-heavy news sites),
        # crawl a few in-domain article links one step down.
        if len(got) < per_src:
            relaxed_min = max(200, min_chars // 2)
            for link in extract_article_links(html, url, max_links=5):
                if len(got) >= per_src * 3:
                    break
                sub_html = fetch_url(link)
                if sub_html is None:
                    continue
                got.extend(extract_paragraphs(sub_html, min_chars=relaxed_min))
                time.sleep(0.3)
        if not got:
            continue
        n_before = len(passages)
        for p in got[:per_src]:
            if len(passages) >= target_count:
                break
            passages.append(f"# Source: {url} ({src.get('description','')})\n\n{p}")
        used.append({
            "url": url,
            "via": "live WebFetch",
            "type": src.get("type", "?"),
            "description": src.get("description", ""),
            "paragraphs_used": len(passages) - n_before,
        })
        time.sleep(0.4)

    # --- 3. If we're under quota, top up from Wikipedia with more articles
    if len(passages) < target_count and wp_sub:
        parquet = download_wiki_parquet(wp_sub)
        if parquet is not None:
            extra_taken: list[str] = []
            seen_already = {p.splitlines()[0] for p in passages}
            for title, body in iter_wiki_articles(parquet, max_articles=4000):
                if len(passages) >= target_count:
                    break
                hdr = f'# Source: Wikipedia article "{title}" (https://{wp_sub}.wikipedia.org/)'
                if hdr in seen_already:
                    continue
                for p in split_into_passages(body, min_chars):
                    if len(passages) >= target_count:
                        break
                    passages.append(f"{hdr}\n\n{p}")
                    extra_taken.append(title)
            # update the wiki entry's article count if we already logged it
            for u in used:
                if u.get("via", "").startswith("wikimedia/wikipedia"):
                    u["articles_used"] = u.get("articles_used", 0) + len(extra_taken)
                    break

    return used, passages


def wipe_examples(folder: Path) -> None:
    ex = folder / "examples"
    if ex.exists():
        for p in ex.iterdir():
            if p.is_file():
                p.unlink()
    ex.mkdir(parents=True, exist_ok=True)


def write_examples(folder: Path, passages: list[str]) -> None:
    ex = folder / "examples"
    for i, p in enumerate(passages, start=1):
        (ex / f"{i:02d}.txt").write_text(p + "\n", encoding="utf-8")


def update_overview_sources(folder: Path, entry: dict, used: list[dict]) -> None:
    """Append / replace a `## Sources` section in overview.md listing every
    URL whose text contributed to this language's examples directory."""
    path = folder / "overview.md"
    if not path.exists():
        return
    body = path.read_text(encoding="utf-8")
    # strip any previous Sources section
    body = re.sub(r"\n## Sources\n[\s\S]*?(?=\n## |\Z)", "", body).rstrip()

    cat = SOURCES.get(entry["code"], {})
    all_candidates = list(cat.get("sources", []))

    lines = ["", "", "## Sources"]
    lines.append("")
    lines.append("Examples and vocabulary for this language folder are drawn "
                 "**only** from non-benchmark websites (Wikipedia, government, "
                 "news, cultural / religious organisations). CommonLID, "
                 "FLORES+, MADLAD-400, OPUS-100, WMT, and Tatoeba are off-limits "
                 "per the contamination policy.")
    lines.append("")
    if used:
        lines.append("### Contributed content")
        lines.append("")
        for u in used:
            bits = [f"`{u['url']}`"]
            if u.get("description"):
                bits.append(u["description"])
            bits.append(f"_{u.get('via','?')}_")
            lines.append("- " + " — ".join(bits))
    else:
        lines.append("_No fetch yielded content for this language. Placeholders "
                     "in `examples/` must be filled manually from original "
                     "websites._")
    if all_candidates:
        lines.append("")
        lines.append("### Catalogued source candidates")
        lines.append("")
        for s in all_candidates:
            lines.append(f"- `{s['url']}` — {s.get('description','')} "
                         f"({s.get('type','?')})")
    lines.append("")

    path.write_text(body + "\n" + "\n".join(lines), encoding="utf-8")


def parse_langs(arg: str | None, all_flag: bool, langs: list[dict]) -> list[dict]:
    if all_flag or not arg:
        return langs
    want = {c.strip() for c in arg.split(",") if c.strip()}
    return [l for l in langs if l["code"] in want]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", help="comma-separated ISO-639-3 codes")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--count", type=int, default=12, help="target example passages per language")
    ap.add_argument("--min-chars", type=int, default=400)
    args = ap.parse_args()

    entries = parse_langs(args.lang, args.all, load_language_list())
    if not entries:
        entries = load_language_list()

    manifest: dict[str, dict] = {}
    for entry in entries:
        code = entry["code"]
        folder = LANG_DIR / entry["folder"]
        wipe_examples(folder)
        used, passages = build_examples(entry, args.count, args.min_chars)
        write_examples(folder, passages)
        update_overview_sources(folder, entry, used)
        manifest[code] = {
            "folder": entry["folder"],
            "passages_written": len(passages),
            "sources_used": used,
        }
        print(f"  {code:<4} wrote={len(passages):>2} sources={len(used)}")

    (LANG_DIR / "sources_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[info] manifest written to languages/sources_manifest.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
