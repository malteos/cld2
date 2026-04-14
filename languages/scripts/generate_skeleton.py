#!/usr/bin/env python3
"""Create the per-language folder skeleton.

For each language in `language_list.json`, create `languages/<folder>/`
containing placeholder files:
    overview.md
    grammar.md
    characteristics.md
    differences.md
    vocabulary.json           (empty skeleton: {"words": []})
    examples/                 (pre-seeded from per_language_samples if present)

The script is idempotent: existing non-empty files are never overwritten. Files
that are absent or empty get a YAML-front-matter-plus-TODO placeholder so that
`validate_completeness.py` can later distinguish "missing" from "unstarted".

Usage:
    python languages/scripts/generate_skeleton.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[2]
LANG_LIST = ROOT / "languages" / "language_list.json"
SAMPLE_DIR = ROOT / "languages" / "per_language_samples"
LANG_DIR = ROOT / "languages"


def placeholder_md(title: str, lang_name: str, code: str, notes: str = "") -> str:
    banner = "<!-- TODO: replace placeholder with full content -->"
    return dedent(f"""\
        # {title}: {lang_name} ({code})

        {banner}

        {notes}
        """)


def split_sample_file(sample_path: Path, out_dir: Path, min_chars: int = 150) -> int:
    """Write one example file per reasonably-long line from the sample.

    Returns the number of example files written.
    """
    if not sample_path.exists():
        return 0
    out_dir.mkdir(parents=True, exist_ok=True)
    lines = [l.rstrip("\n") for l in sample_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    written = 0
    for idx, line in enumerate(lines, start=1):
        target = out_dir / f"{idx:02d}.txt"
        if target.exists() and target.stat().st_size > 0:
            continue
        if len(line) < min_chars:
            # still write short samples; they're better than nothing, but keep flagged
            pass
        target.write_text(line + "\n", encoding="utf-8")
        written += 1
    return written


def ensure_file(path: Path, content_fn):
    """Write content_fn() only when the file is missing or empty."""
    if path.exists() and path.stat().st_size > 0:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content_fn(), encoding="utf-8")
    return True


def main() -> int:
    data = json.loads(LANG_LIST.read_text(encoding="utf-8"))
    created = 0
    for entry in data["languages"]:
        code = entry["code"]
        folder = entry["folder"]
        name = entry["name"]
        lang_dir = LANG_DIR / folder
        lang_dir.mkdir(parents=True, exist_ok=True)

        examples_dir = lang_dir / "examples"
        written = split_sample_file(SAMPLE_DIR / f"{code}.txt", examples_dir)
        created += written

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
                        "note": "TODO: populate frequency-ranked vocabulary (see scripts/fetch_vocabulary.py)",
                    }, ensure_ascii=False, indent=2))

    print(f"[info] skeleton generated; wrote {created} new example files across {len(data['languages'])} languages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
