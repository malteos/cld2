#!/usr/bin/env python3
"""Create the per-language folder skeleton.

For each language in `language_list.json`, create `languages/<folder>/`
containing placeholder files:
    overview.md
    grammar.md
    characteristics.md
    differences.md
    vocabulary.json           (empty skeleton: {"words": []})
    examples/                 (empty; populated by fetch_web_examples.py)

The script is idempotent: existing non-empty files are never overwritten.
Files that are absent or empty get a YAML-front-matter-plus-TODO placeholder
so that `validate_completeness.py` can distinguish "missing" from "unstarted".

**Non-seeding policy**: earlier revisions of this script pre-filled
`examples/*.txt` from a `per_language_samples/` directory that had been
sliced out of the CommonLID TSV. That was train-test leakage and is now
prohibited. Example files are produced exclusively by
`fetch_web_examples.py`, which pulls from Wikipedia and curated
non-benchmark websites.

Usage:
    python languages/scripts/generate_skeleton.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[2]
LANG_LIST = ROOT / "languages" / "language_list.json"
LANG_DIR = ROOT / "languages"


def placeholder_md(title: str, lang_name: str, code: str, notes: str = "") -> str:
    banner = "<!-- TODO: replace placeholder with full content -->"
    return dedent(f"""\
        # {title}: {lang_name} ({code})

        {banner}

        {notes}
        """)


def ensure_file(path: Path, content_fn):
    if path.exists() and path.stat().st_size > 0:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content_fn(), encoding="utf-8")
    return True


def main() -> int:
    data = json.loads(LANG_LIST.read_text(encoding="utf-8"))
    for entry in data["languages"]:
        code = entry["code"]
        folder = entry["folder"]
        name = entry["name"]
        lang_dir = LANG_DIR / folder
        lang_dir.mkdir(parents=True, exist_ok=True)
        (lang_dir / "examples").mkdir(parents=True, exist_ok=True)

        ensure_file(lang_dir / "overview.md",
                    lambda: placeholder_md("Overview", name, code,
                                            "Family, ISO codes, script, speaker count, regions, orthography."))
        ensure_file(lang_dir / "grammar.md",
                    lambda: placeholder_md("Grammar", name, code,
                                            "Word order, morphology, phonology, case, conjugation, syntax."))
        ensure_file(lang_dir / "characteristics.md",
                    lambda: placeholder_md("LID Characteristics", name, code,
                                            "Unique chars/diacritics, top 50 function words, n-gram patterns, frequency."))
        ensure_file(lang_dir / "differences.md",
                    lambda: placeholder_md("Differences from confusable languages", name, code,
                                            "Diagnostic features that distinguish this language from close neighbours."))
        ensure_file(lang_dir / "vocabulary.json",
                    lambda: json.dumps({
                        "code": code,
                        "name": name,
                        "words": [],
                        "note": "TODO: populate via scripts/fetch_web_vocabulary.py",
                    }, ensure_ascii=False, indent=2))

    print(f"[info] skeleton ready for {len(data['languages'])} languages "
          f"(examples/ are empty — run fetch_web_examples.py next)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
