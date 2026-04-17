#!/usr/bin/env python3
"""Discover non-benchmark source websites per language via Wikidata SPARQL.

For each of the 109 CommonLID languages, runs a SPARQL query against
`query.wikidata.org` to find items that are (newspaper|news media|radio|
television|publisher|news agency) AND have an official website (P856) AND
list the target language (P407). Prints a human-readable catalogue block
and can optionally merge suggestions directly into `sources_catalog.py`.

Why this matters
----------------
Hand-curating source URLs per language doesn't scale past ~50 languages
and systematically under-covers low-resource languages. Wikidata already
knows which newspapers publish in Tigrinya, Fulfulde, Acehnese, etc.;
asking it by SPARQL is cheaper and more accurate than guessing.

Usage
-----
    source .venv/bin/activate
    python languages/scripts/discover_sources_wikidata.py --lang pcm,gcf,ace
    python languages/scripts/discover_sources_wikidata.py --all --print-only
    python languages/scripts/discover_sources_wikidata.py --all --emit suggestions.py
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.parse
from pathlib import Path
from typing import Any

import requests

ROOT = Path(__file__).resolve().parents[2]
LANG_LIST = ROOT / "languages" / "language_list.json"

SPARQL_ENDPOINT = "https://query.wikidata.org/sparql"
USER_AGENT = (
    "cld2-lang-kb-discovery/0.1 (+https://github.com/malteos/cld2; "
    "research; discovers non-benchmark text sources via Wikidata)"
)

# ISO-639-3 → list of Wikidata P218/P220 language codes (639-1, 639-3, others).
# Wikidata's P220 stores 639-3; P218 stores 639-1. Queries work fine against
# the 639-3 code P220, which is what we use here.

# Media / publisher Wikidata item IDs that we treat as in-scope:
MEDIA_CLASSES = [
    "Q11032",     # newspaper
    "Q1193236",   # news media
    "Q1110794",   # daily newspaper
    "Q1153191",   # online newspaper
    "Q1002697",   # periodical
    "Q41298",     # magazine
    "Q14752",     # radio station
    "Q1616075",   # television station
    "Q192283",    # news agency
    "Q2085381",   # publisher
    "Q1057474",   # broadcaster
    "Q4830453",   # business (for state / cultural institutions)
    "Q3918",      # university
]


def load_language_list() -> list[dict]:
    return json.loads(LANG_LIST.read_text(encoding="utf-8"))["languages"]


def sparql_query(query: str) -> list[dict]:
    r = requests.get(
        SPARQL_ENDPOINT,
        params={"query": query, "format": "json"},
        headers={"User-Agent": USER_AGENT, "Accept": "application/sparql-results+json"},
        timeout=60,
    )
    r.raise_for_status()
    data = r.json()
    return data["results"]["bindings"]


def _mk_union(classes: list[str]) -> str:
    return "\n         UNION ".join(
        f"{{ ?item wdt:P31/wdt:P279* wd:{cls}. }}" for cls in classes)


def query_media_by_language(lang_code: str, limit: int = 40) -> list[dict]:
    """Primary query: media items whose `language of work or name` (P407)
    resolves to a language whose ISO-639-3 (P220) is the target code."""
    classes_union = _mk_union(MEDIA_CLASSES)
    query = f"""
SELECT DISTINCT ?item ?itemLabel ?typeLabel ?url ?countryLabel WHERE {{
  {{
     {classes_union}
  }}
  ?item wdt:P856 ?url .
  ?item wdt:P407 ?language .
  ?language wdt:P220 "{lang_code}" .
  OPTIONAL {{ ?item wdt:P31 ?type . }}
  OPTIONAL {{ ?item wdt:P17 ?country . }}
  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en,[AUTO_LANGUAGE]" }}
}} LIMIT {limit}
"""
    return _run_query(query, lang_code, "by-language")


def query_media_by_country(lang_code: str, limit: int = 40) -> list[dict]:
    """Fallback: media items in a country (P17) whose official language
    (P37) is the target. Catches newspapers whose language of work is
    unrecorded but whose country makes them a plausible source."""
    classes_union = _mk_union(MEDIA_CLASSES)
    query = f"""
SELECT DISTINCT ?item ?itemLabel ?typeLabel ?url ?countryLabel WHERE {{
  {{
     {classes_union}
  }}
  ?item wdt:P856 ?url .
  ?item wdt:P17 ?country .
  ?country wdt:P37 ?language .
  ?language wdt:P220 "{lang_code}" .
  OPTIONAL {{ ?item wdt:P31 ?type . }}
  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en,[AUTO_LANGUAGE]" }}
}} LIMIT {limit}
"""
    return _run_query(query, lang_code, "by-country")


def _run_query(query: str, lang_code: str, tag: str) -> list[dict]:
    try:
        rows = sparql_query(query)
    except requests.HTTPError as exc:
        print(f"  [warn] SPARQL {tag} error for {lang_code}: {exc}", file=sys.stderr)
        return []
    except Exception as exc:  # noqa: BLE001
        print(f"  [warn] SPARQL {tag} error for {lang_code}: {exc}", file=sys.stderr)
        return []
    out: list[dict] = []
    for row in rows:
        name = row.get("itemLabel", {}).get("value") or "?"
        url = row.get("url", {}).get("value") or ""
        kind = row.get("typeLabel", {}).get("value") or ""
        country = row.get("countryLabel", {}).get("value") or ""
        if not url.startswith("http"):
            continue
        # Filter obvious noise: mediawiki installs, social media links, etc.
        for bad in ("wikipedia.org", "mediawiki.org", "youtube.com",
                    "facebook.com", "twitter.com", "instagram.com",
                    "tiktok.com", "pinterest.com", "linkedin.com"):
            if bad in url:
                break
        else:
            out.append({
                "name": name,
                "url": url,
                "kind": kind,
                "country": country,
                "source_query": tag,
            })
    return out


def query_media_for_language(lang_code: str, limit: int = 40) -> list[dict]:
    """Return media items for the language, combining the P407-direct
    query and the P17/P37 fallback. Deduplicated by URL."""
    a = query_media_by_language(lang_code, limit=limit)
    b = query_media_by_country(lang_code, limit=limit)
    seen: set[str] = set()
    out: list[dict] = []
    for row in a + b:
        if row["url"] in seen:
            continue
        seen.add(row["url"])
        out.append(row)
    return out


def categorise(kind: str) -> str:
    k = (kind or "").lower()
    if any(t in k for t in ("newspaper", "daily", "magazine", "periodical",
                             "news agency", "news media")):
        return "news"
    if "radio" in k or "broadcast" in k:
        return "news"
    if "television" in k:
        return "news"
    if "publisher" in k or "publishing" in k:
        return "cultural"
    if "university" in k or "school" in k:
        return "education"
    if "government" in k or "ministry" in k or "agency" in k:
        return "gov"
    return "cultural"


def format_entry(row: dict) -> str:
    typ = categorise(row["kind"])
    desc = row["name"]
    if row.get("country"):
        desc = f"{desc} ({row['country']})"
    # escape quotes
    desc = desc.replace('"', "'")
    return f'        {{"url": "{row["url"]}", "type": "{typ}", "description": "{desc}"}},'


def parse_langs(arg: str | None, all_flag: bool, langs: list[dict]) -> list[dict]:
    if all_flag or not arg:
        return langs
    want = {c.strip() for c in arg.split(",") if c.strip()}
    return [l for l in langs if l["code"] in want]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", help="comma-separated ISO-639-3 codes")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--limit", type=int, default=40)
    ap.add_argument("--emit", help="write Python dict-suggestions to this file "
                                    "(otherwise just prints to stdout)")
    ap.add_argument("--print-only", action="store_true")
    args = ap.parse_args()

    entries = parse_langs(args.lang, args.all, load_language_list())
    if not entries:
        entries = load_language_list()

    suggestions: dict[str, list[dict]] = {}
    for entry in entries:
        code = entry["code"]
        print(f"  {code:<4} querying …", flush=True)
        rows = query_media_for_language(code, limit=args.limit)
        if rows:
            suggestions[code] = rows
            print(f"        -> {len(rows)} candidates")
        else:
            print(f"        -> no results")
        time.sleep(1.0)  # be polite to query.wikidata.org

    if args.emit:
        with open(args.emit, "w", encoding="utf-8") as f:
            f.write('"""Wikidata-discovered source suggestions. Merge manually '
                    'into sources_catalog.py after review."""\n\n')
            f.write("SUGGESTIONS = {\n")
            for code, rows in suggestions.items():
                f.write(f'    "{code}": [\n')
                for r in rows:
                    f.write(format_entry(r) + "\n")
                f.write("    ],\n")
            f.write("}\n")
        print(f"[info] wrote suggestions to {args.emit}")
    elif args.print_only or not suggestions:
        for code, rows in suggestions.items():
            print(f"\n=== {code} ({len(rows)} candidates) ===")
            for r in rows:
                print(f"  [{categorise(r['kind']):<9}] {r['url']:<60} {r['name']} ({r.get('country','?')})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
