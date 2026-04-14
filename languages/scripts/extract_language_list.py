#!/usr/bin/env python3
"""Extract the 109 CommonLID languages from HuggingFace and enrich each with
metadata (ISO-639-3 code, endonym/English name, script, family, resource tier).

Primary source: HuggingFace `commoncrawl/CommonLID` dataset tags.
Fallback: the list compiled into `FALLBACK_LANGS` below, captured from the HF
dataset on 2026-04-14.

Outputs: languages/language_list.json
Also writes: languages/per_language_samples/{code}.txt with up to N lines per
language extracted from the CommonLID .tsv.gz (useful as real example texts).

Usage (from repo root):
    source .venv/bin/activate
    python languages/scripts/extract_language_list.py
"""
from __future__ import annotations

import gzip
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "languages" / "language_list.json"
SAMPLE_DIR = ROOT / "languages" / "per_language_samples"

# Fallback if HuggingFace is unavailable. Captured 2026-04-14 from
# commoncrawl/CommonLID dataset tags (109 languages).
FALLBACK_LANGS = [
    "ace", "acf", "aeb", "afr", "amh", "apd", "ara", "arb", "arg", "ars",
    "ary", "arz", "asm", "aze", "azj", "bak", "bcl", "ben", "bik", "bre",
    "bul", "cat", "ces", "cmn", "crh", "deu", "ell", "eng", "est", "ext",
    "fas", "fil", "fin", "fra", "fro", "fry", "fuv", "gaz", "gcf", "gcr",
    "gla", "gle", "gom", "grc", "gug", "guj", "guw", "hau", "hbo", "heb",
    "hin", "ibo", "ind", "ita", "jav", "jpn", "kab", "kan", "kik", "kor",
    "lat", "lav", "lij", "lin", "ltg", "lug", "lvs", "mal", "mar", "mlg",
    "msa", "nld", "nso", "nyn", "oci", "orm", "ory", "pan", "pcm", "pol",
    "por", "rcf", "rus", "san", "sna", "sot", "spa", "swa", "swh", "tam",
    "tat", "tel", "tgl", "tha", "tuk", "tur", "ukr", "urd", "uzb", "uzs",
    "vec", "vie", "wuu", "xho", "yor", "yue", "zho", "zsm", "zul",
]

# Per-language metadata. FLORES-200 style code is `iso3_Script`.
# Resource tier: high | mid | low (rough heuristic for vocabulary targets).
LANG_META: dict[str, dict[str, str]] = {
    "ace": dict(name="Acehnese", endonym="Bahsa Acèh", script="Latn", family="Austronesian", tier="low"),
    "acf": dict(name="Saint Lucian Creole", endonym="Kwéyòl", script="Latn", family="Creole (French-based)", tier="low"),
    "aeb": dict(name="Tunisian Arabic", endonym="تونسي", script="Arab", family="Afro-Asiatic/Semitic", tier="low"),
    "afr": dict(name="Afrikaans", endonym="Afrikaans", script="Latn", family="Indo-European/Germanic", tier="mid"),
    "amh": dict(name="Amharic", endonym="አማርኛ", script="Ethi", family="Afro-Asiatic/Semitic", tier="mid"),
    "apd": dict(name="Sudanese Arabic", endonym="عربي سوداني", script="Arab", family="Afro-Asiatic/Semitic", tier="low"),
    "ara": dict(name="Arabic (macro)", endonym="العربية", script="Arab", family="Afro-Asiatic/Semitic", tier="high"),
    "arb": dict(name="Modern Standard Arabic", endonym="العربية الفصحى", script="Arab", family="Afro-Asiatic/Semitic", tier="high"),
    "arg": dict(name="Aragonese", endonym="Aragonés", script="Latn", family="Indo-European/Romance", tier="low"),
    "ars": dict(name="Najdi Arabic", endonym="عربي نجدي", script="Arab", family="Afro-Asiatic/Semitic", tier="low"),
    "ary": dict(name="Moroccan Arabic", endonym="الدارجة", script="Arab", family="Afro-Asiatic/Semitic", tier="low"),
    "arz": dict(name="Egyptian Arabic", endonym="مصرى", script="Arab", family="Afro-Asiatic/Semitic", tier="mid"),
    "asm": dict(name="Assamese", endonym="অসমীয়া", script="Beng", family="Indo-European/Indic", tier="mid"),
    "aze": dict(name="Azerbaijani (macro)", endonym="Azərbaycan", script="Latn", family="Turkic", tier="mid"),
    "azj": dict(name="North Azerbaijani", endonym="Azərbaycan", script="Latn", family="Turkic", tier="mid"),
    "bak": dict(name="Bashkir", endonym="Башҡортса", script="Cyrl", family="Turkic", tier="low"),
    "bcl": dict(name="Central Bikol", endonym="Bikol Sentral", script="Latn", family="Austronesian", tier="low"),
    "ben": dict(name="Bengali", endonym="বাংলা", script="Beng", family="Indo-European/Indic", tier="high"),
    "bik": dict(name="Bikol (macro)", endonym="Bikol", script="Latn", family="Austronesian", tier="low"),
    "bre": dict(name="Breton", endonym="Brezhoneg", script="Latn", family="Indo-European/Celtic", tier="low"),
    "bul": dict(name="Bulgarian", endonym="Български", script="Cyrl", family="Indo-European/Slavic", tier="high"),
    "cat": dict(name="Catalan", endonym="Català", script="Latn", family="Indo-European/Romance", tier="high"),
    "ces": dict(name="Czech", endonym="Čeština", script="Latn", family="Indo-European/Slavic", tier="high"),
    "cmn": dict(name="Mandarin Chinese", endonym="普通话", script="Hans", family="Sino-Tibetan", tier="high"),
    "crh": dict(name="Crimean Tatar", endonym="Qırımtatar", script="Latn", family="Turkic", tier="low"),
    "deu": dict(name="German", endonym="Deutsch", script="Latn", family="Indo-European/Germanic", tier="high"),
    "ell": dict(name="Greek (Modern)", endonym="Ελληνικά", script="Grek", family="Indo-European/Hellenic", tier="high"),
    "eng": dict(name="English", endonym="English", script="Latn", family="Indo-European/Germanic", tier="high"),
    "est": dict(name="Estonian", endonym="Eesti", script="Latn", family="Uralic/Finnic", tier="high"),
    "ext": dict(name="Extremaduran", endonym="Estremeñu", script="Latn", family="Indo-European/Romance", tier="low"),
    "fas": dict(name="Persian", endonym="فارسی", script="Arab", family="Indo-European/Iranian", tier="high"),
    "fil": dict(name="Filipino", endonym="Filipino", script="Latn", family="Austronesian", tier="mid"),
    "fin": dict(name="Finnish", endonym="Suomi", script="Latn", family="Uralic/Finnic", tier="high"),
    "fra": dict(name="French", endonym="Français", script="Latn", family="Indo-European/Romance", tier="high"),
    "fro": dict(name="Old French", endonym="Franceis", script="Latn", family="Indo-European/Romance (historical)", tier="low"),
    "fry": dict(name="Western Frisian", endonym="Frysk", script="Latn", family="Indo-European/Germanic", tier="low"),
    "fuv": dict(name="Nigerian Fulfulde", endonym="Fulfulde", script="Latn", family="Niger-Congo/Atlantic", tier="low"),
    "gaz": dict(name="West Central Oromo", endonym="Afaan Oromoo", script="Latn", family="Afro-Asiatic/Cushitic", tier="low"),
    "gcf": dict(name="Guadeloupean Creole", endonym="Kréyol Gwadloupéyen", script="Latn", family="Creole (French-based)", tier="low"),
    "gcr": dict(name="Guianese Creole", endonym="Kréyòl Gwiyanè", script="Latn", family="Creole (French-based)", tier="low"),
    "gla": dict(name="Scottish Gaelic", endonym="Gàidhlig", script="Latn", family="Indo-European/Celtic", tier="low"),
    "gle": dict(name="Irish", endonym="Gaeilge", script="Latn", family="Indo-European/Celtic", tier="mid"),
    "gom": dict(name="Konkani (Goan)", endonym="कोंकणी", script="Deva", family="Indo-European/Indic", tier="low"),
    "grc": dict(name="Ancient Greek", endonym="Ἑλληνική", script="Grek", family="Indo-European/Hellenic (historical)", tier="low"),
    "gug": dict(name="Paraguayan Guarani", endonym="Avañe'ẽ", script="Latn", family="Tupian", tier="low"),
    "guj": dict(name="Gujarati", endonym="ગુજરાતી", script="Gujr", family="Indo-European/Indic", tier="mid"),
    "guw": dict(name="Gun", endonym="Gungbe", script="Latn", family="Niger-Congo/Gbe", tier="low"),
    "hau": dict(name="Hausa", endonym="Hausa", script="Latn", family="Afro-Asiatic/Chadic", tier="mid"),
    "hbo": dict(name="Ancient Hebrew", endonym="עברית מקראית", script="Hebr", family="Afro-Asiatic/Semitic (historical)", tier="low"),
    "heb": dict(name="Hebrew (Modern)", endonym="עברית", script="Hebr", family="Afro-Asiatic/Semitic", tier="high"),
    "hin": dict(name="Hindi", endonym="हिन्दी", script="Deva", family="Indo-European/Indic", tier="high"),
    "ibo": dict(name="Igbo", endonym="Igbo", script="Latn", family="Niger-Congo/Volta-Niger", tier="mid"),
    "ind": dict(name="Indonesian", endonym="Bahasa Indonesia", script="Latn", family="Austronesian", tier="high"),
    "ita": dict(name="Italian", endonym="Italiano", script="Latn", family="Indo-European/Romance", tier="high"),
    "jav": dict(name="Javanese", endonym="Basa Jawa", script="Latn", family="Austronesian", tier="mid"),
    "jpn": dict(name="Japanese", endonym="日本語", script="Jpan", family="Japonic", tier="high"),
    "kab": dict(name="Kabyle", endonym="Taqbaylit", script="Latn", family="Afro-Asiatic/Berber", tier="low"),
    "kan": dict(name="Kannada", endonym="ಕನ್ನಡ", script="Knda", family="Dravidian", tier="mid"),
    "kik": dict(name="Kikuyu", endonym="Gĩkũyũ", script="Latn", family="Niger-Congo/Bantu", tier="low"),
    "kor": dict(name="Korean", endonym="한국어", script="Hang", family="Koreanic", tier="high"),
    "lat": dict(name="Latin", endonym="Latina", script="Latn", family="Indo-European/Italic (historical)", tier="low"),
    "lav": dict(name="Latvian (macro)", endonym="Latviešu", script="Latn", family="Indo-European/Baltic", tier="mid"),
    "lij": dict(name="Ligurian", endonym="Ligure", script="Latn", family="Indo-European/Romance", tier="low"),
    "lin": dict(name="Lingala", endonym="Lingála", script="Latn", family="Niger-Congo/Bantu", tier="low"),
    "ltg": dict(name="Latgalian", endonym="Latgalīšu", script="Latn", family="Indo-European/Baltic", tier="low"),
    "lug": dict(name="Ganda", endonym="Luganda", script="Latn", family="Niger-Congo/Bantu", tier="low"),
    "lvs": dict(name="Standard Latvian", endonym="Latviešu", script="Latn", family="Indo-European/Baltic", tier="mid"),
    "mal": dict(name="Malayalam", endonym="മലയാളം", script="Mlym", family="Dravidian", tier="mid"),
    "mar": dict(name="Marathi", endonym="मराठी", script="Deva", family="Indo-European/Indic", tier="mid"),
    "mlg": dict(name="Malagasy", endonym="Malagasy", script="Latn", family="Austronesian", tier="low"),
    "msa": dict(name="Malay (macro)", endonym="Bahasa Melayu", script="Latn", family="Austronesian", tier="high"),
    "nld": dict(name="Dutch", endonym="Nederlands", script="Latn", family="Indo-European/Germanic", tier="high"),
    "nso": dict(name="Northern Sotho", endonym="Sesotho sa Leboa", script="Latn", family="Niger-Congo/Bantu", tier="low"),
    "nyn": dict(name="Nyankole", endonym="Runyankore", script="Latn", family="Niger-Congo/Bantu", tier="low"),
    "oci": dict(name="Occitan", endonym="Occitan", script="Latn", family="Indo-European/Romance", tier="low"),
    "orm": dict(name="Oromo (macro)", endonym="Afaan Oromoo", script="Latn", family="Afro-Asiatic/Cushitic", tier="low"),
    "ory": dict(name="Odia", endonym="ଓଡ଼ିଆ", script="Orya", family="Indo-European/Indic", tier="mid"),
    "pan": dict(name="Punjabi (Eastern)", endonym="ਪੰਜਾਬੀ", script="Guru", family="Indo-European/Indic", tier="mid"),
    "pcm": dict(name="Nigerian Pidgin", endonym="Naijá", script="Latn", family="Creole (English-based)", tier="low"),
    "pol": dict(name="Polish", endonym="Polski", script="Latn", family="Indo-European/Slavic", tier="high"),
    "por": dict(name="Portuguese", endonym="Português", script="Latn", family="Indo-European/Romance", tier="high"),
    "rcf": dict(name="Réunion Creole", endonym="Kréol Rénioné", script="Latn", family="Creole (French-based)", tier="low"),
    "rus": dict(name="Russian", endonym="Русский", script="Cyrl", family="Indo-European/Slavic", tier="high"),
    "san": dict(name="Sanskrit", endonym="संस्कृतम्", script="Deva", family="Indo-European/Indic (historical)", tier="low"),
    "sna": dict(name="Shona", endonym="ChiShona", script="Latn", family="Niger-Congo/Bantu", tier="low"),
    "sot": dict(name="Southern Sotho", endonym="Sesotho", script="Latn", family="Niger-Congo/Bantu", tier="low"),
    "spa": dict(name="Spanish", endonym="Español", script="Latn", family="Indo-European/Romance", tier="high"),
    "swa": dict(name="Swahili (macro)", endonym="Kiswahili", script="Latn", family="Niger-Congo/Bantu", tier="mid"),
    "swh": dict(name="Swahili (Coastal)", endonym="Kiswahili", script="Latn", family="Niger-Congo/Bantu", tier="mid"),
    "tam": dict(name="Tamil", endonym="தமிழ்", script="Taml", family="Dravidian", tier="mid"),
    "tat": dict(name="Tatar", endonym="Татарча", script="Cyrl", family="Turkic", tier="low"),
    "tel": dict(name="Telugu", endonym="తెలుగు", script="Telu", family="Dravidian", tier="mid"),
    "tgl": dict(name="Tagalog", endonym="Tagalog", script="Latn", family="Austronesian", tier="mid"),
    "tha": dict(name="Thai", endonym="ภาษาไทย", script="Thai", family="Kra-Dai", tier="high"),
    "tuk": dict(name="Turkmen", endonym="Türkmençe", script="Latn", family="Turkic", tier="low"),
    "tur": dict(name="Turkish", endonym="Türkçe", script="Latn", family="Turkic", tier="high"),
    "ukr": dict(name="Ukrainian", endonym="Українська", script="Cyrl", family="Indo-European/Slavic", tier="high"),
    "urd": dict(name="Urdu", endonym="اُردُو", script="Arab", family="Indo-European/Indic", tier="mid"),
    "uzb": dict(name="Uzbek (macro)", endonym="Oʻzbekcha", script="Latn", family="Turkic", tier="mid"),
    "uzs": dict(name="Southern Uzbek", endonym="اوزبیکی", script="Arab", family="Turkic", tier="low"),
    "vec": dict(name="Venetian", endonym="Vèneto", script="Latn", family="Indo-European/Romance", tier="low"),
    "vie": dict(name="Vietnamese", endonym="Tiếng Việt", script="Latn", family="Austroasiatic", tier="high"),
    "wuu": dict(name="Wu Chinese", endonym="吳語", script="Hans", family="Sino-Tibetan", tier="low"),
    "xho": dict(name="Xhosa", endonym="IsiXhosa", script="Latn", family="Niger-Congo/Bantu", tier="mid"),
    "yor": dict(name="Yoruba", endonym="Yorùbá", script="Latn", family="Niger-Congo/Volta-Niger", tier="mid"),
    "yue": dict(name="Cantonese", endonym="粵語", script="Hant", family="Sino-Tibetan", tier="mid"),
    "zho": dict(name="Chinese (macro)", endonym="中文", script="Hans", family="Sino-Tibetan", tier="high"),
    "zsm": dict(name="Standard Malay", endonym="Bahasa Malaysia", script="Latn", family="Austronesian", tier="mid"),
    "zul": dict(name="Zulu", endonym="IsiZulu", script="Latn", family="Niger-Congo/Bantu", tier="mid"),
}


def hf_language_list() -> list[str]:
    """Fetch the language list from HF dataset tags; fall back on error."""
    try:
        from huggingface_hub import HfApi
        api = HfApi()
        info = api.dataset_info("commoncrawl/CommonLID")
        langs = sorted(
            t.removeprefix("language:") for t in info.tags
            if t.startswith("language:")
        )
        if langs:
            return langs
    except Exception as exc:  # pragma: no cover - network/auth paths
        print(f"[warn] HF fetch failed, using fallback list: {exc}", file=sys.stderr)
    return sorted(FALLBACK_LANGS)


def folder_code(code: str, meta: dict[str, str]) -> str:
    """FLORES-200-ish identifier used for the per-language folder name."""
    return f"{code}_{meta['script']}"


def build_entries(langs: list[str]) -> list[dict]:
    entries = []
    for code in langs:
        meta = LANG_META.get(code)
        if meta is None:
            # Should not happen; LANG_META is comprehensive for the fallback.
            # Keep the code but flag the gap so the reviewer can investigate.
            meta = dict(name=code, endonym="", script="Zzzz", family="unknown", tier="low")
            print(f"[warn] missing metadata for {code!r}", file=sys.stderr)
        entries.append({
            "code": code,
            "folder": folder_code(code, meta),
            **meta,
        })
    return entries


def write_samples(tsv_path: Path, max_per_lang: int = 15, max_chars: int = 600) -> None:
    """Split the CommonLID TSV into per-language sample files."""
    SAMPLE_DIR.mkdir(parents=True, exist_ok=True)
    counts: dict[str, int] = {}
    handles: dict[str, object] = {}
    try:
        with gzip.open(tsv_path, "rt", encoding="utf-8", errors="replace") as f:
            header = f.readline()  # skip
            for line in f:
                parts = line.rstrip("\n").split("\t")
                if len(parts) < 3:
                    continue
                text, tag, _lid = parts[0], parts[1], parts[2]
                if counts.get(tag, 0) >= max_per_lang:
                    continue
                counts[tag] = counts.get(tag, 0) + 1
                h = handles.get(tag)
                if h is None:
                    h = open(SAMPLE_DIR / f"{tag}.txt", "w", encoding="utf-8")
                    handles[tag] = h
                snippet = text[:max_chars].replace("\t", " ")
                h.write(snippet + "\n")
    finally:
        for h in handles.values():
            h.close()
    print(f"[info] wrote per-language samples for {len(counts)} tags")


def ensure_dataset_file() -> Path | None:
    """Download the CommonLID TSV if possible."""
    try:
        from huggingface_hub import hf_hub_download
        return Path(hf_hub_download(
            repo_id="commoncrawl/CommonLID",
            filename="commonlid_20251209.tsv.gz",
            repo_type="dataset",
        ))
    except Exception as exc:
        print(f"[warn] could not download dataset: {exc}", file=sys.stderr)
        return None


def main() -> int:
    langs = hf_language_list()
    entries = build_entries(langs)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as f:
        json.dump({"count": len(entries), "languages": entries}, f, ensure_ascii=False, indent=2)
    print(f"[info] wrote {OUT} with {len(entries)} entries")

    tsv = ensure_dataset_file()
    if tsv is not None:
        write_samples(tsv)
    else:
        print("[warn] skipping sample extraction - dataset not available")
    return 0


if __name__ == "__main__":
    sys.exit(main())
