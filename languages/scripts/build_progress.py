#!/usr/bin/env python3
"""Build PROGRESS.md from filesystem state."""
import json
import os
from datetime import datetime, timezone

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    lang_list_path = os.path.join(base_dir, "language_list.json")
    with open(lang_list_path) as f:
        languages = json.load(f)

    rows = []
    complete = 0
    for lang in languages:
        code = lang["code"]
        lang_dir = os.path.join(base_dir, code)
        def has(fn):
            p = os.path.join(lang_dir, fn)
            return os.path.exists(p) and os.path.getsize(p) > 50
        overview = "done" if has("overview.md") else "-"
        grammar = "done" if has("grammar.md") else "-"
        chars = "done" if has("characteristics.md") else "-"
        diffs = "done" if has("differences.md") else "-"
        vocab_count = 0
        vocab_path = os.path.join(lang_dir, "vocabulary.json")
        if os.path.exists(vocab_path):
            try:
                with open(vocab_path) as vf:
                    vocab_count = len(json.load(vf))
            except Exception:
                pass
        examples_dir = os.path.join(lang_dir, "examples")
        example_count = 0
        if os.path.isdir(examples_dir):
            example_count = len([f for f in os.listdir(examples_dir) if f.endswith(".txt")])
        all_done = all(x == "done" for x in [overview, grammar, chars, diffs]) and vocab_count >= 100 and example_count >= 10
        status = "COMPLETE" if all_done else "PARTIAL" if overview == "done" else "EMPTY"
        if status == "COMPLETE":
            complete += 1
        rows.append(f"| {lang['name']} | `{code}` | {overview} | {grammar} | {chars} | {diffs} | {vocab_count:,} | {example_count} | {status} |")

    total = len(languages)
    pct = round(100 * complete / total) if total else 0
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        f"# Language Knowledge Base Progress",
        f"",
        f"Generated: {now}",
        f"Total languages: {total}",
        f"Complete: {complete} / {total} ({pct}%)",
        f"",
        f"| Language | Code | Overview | Grammar | Characteristics | Differences | Vocab | Examples | Status |",
        f"|----------|------|----------|---------|-----------------|-------------|-------|----------|--------|",
    ] + rows

    progress_path = os.path.join(base_dir, "PROGRESS.md")
    with open(progress_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote {progress_path}: {complete}/{total} complete ({pct}%)")

if __name__ == "__main__":
    main()
