#!/usr/bin/env python3
"""Validate completeness of language knowledge base files."""
import json
import os
import sys

REQUIRED_FILES = ["overview.md", "grammar.md", "characteristics.md", "differences.md", "vocabulary.json"]
MIN_SIZES = {"overview.md": 200, "grammar.md": 500, "characteristics.md": 300, "differences.md": 200}
MIN_VOCAB = 100
MIN_EXAMPLES = 10
MIN_EXAMPLE_WORDS = 100

def validate_language(base_dir, code):
    lang_dir = os.path.join(base_dir, code)
    issues = []
    stats = {"overview": False, "grammar": False, "characteristics": False,
             "differences": False, "vocab_count": 0, "example_count": 0}

    for f in REQUIRED_FILES:
        path = os.path.join(lang_dir, f)
        if not os.path.exists(path):
            issues.append(f"Missing {f}")
            continue
        size = os.path.getsize(path)
        if f in MIN_SIZES and size < MIN_SIZES[f]:
            issues.append(f"{f} too small ({size} bytes, need {MIN_SIZES[f]})")
        else:
            key = f.replace(".md", "").replace(".json", "")
            if key in stats:
                stats[key] = True

    vocab_path = os.path.join(lang_dir, "vocabulary.json")
    if os.path.exists(vocab_path):
        try:
            with open(vocab_path) as vf:
                vocab = json.load(vf)
                stats["vocab_count"] = len(vocab)
                if len(vocab) < MIN_VOCAB:
                    issues.append(f"Vocabulary too small ({len(vocab)}, need {MIN_VOCAB})")
        except json.JSONDecodeError:
            issues.append("vocabulary.json is invalid JSON")

    examples_dir = os.path.join(lang_dir, "examples")
    if os.path.isdir(examples_dir):
        examples = [f for f in os.listdir(examples_dir) if f.endswith(".txt")]
        stats["example_count"] = len(examples)
        if len(examples) < MIN_EXAMPLES:
            issues.append(f"Too few examples ({len(examples)}, need {MIN_EXAMPLES})")
        for ex in examples:
            with open(os.path.join(examples_dir, ex)) as ef:
                words = len(ef.read().split())
                if words < MIN_EXAMPLE_WORDS:
                    issues.append(f"Example {ex} too short ({words} words, need {MIN_EXAMPLE_WORDS})")
    else:
        issues.append("Missing examples/ directory")

    return stats, issues

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    lang_list_path = os.path.join(base_dir, "language_list.json")
    with open(lang_list_path) as f:
        languages = json.load(f)

    total = len(languages)
    complete = 0
    partial = 0
    results = []

    for lang in languages:
        code = lang["code"]
        stats, issues = validate_language(base_dir, code)
        status = "COMPLETE" if not issues else "PARTIAL" if stats["overview"] else "EMPTY"
        if status == "COMPLETE":
            complete += 1
        elif status == "PARTIAL":
            partial += 1
        results.append({"lang": lang, "stats": stats, "issues": issues, "status": status})

    print(f"\nLanguage Knowledge Base Validation")
    print(f"{'='*60}")
    print(f"Total: {total} | Complete: {complete} | Partial: {partial} | Empty: {total - complete - partial}")
    print()

    for r in results:
        icon = {"COMPLETE": "[OK]", "PARTIAL": "[..] ", "EMPTY": "[  ]"}[r["status"]]
        lang = r["lang"]
        stats = r["stats"]
        print(f"{icon} {lang['code']:12s} {lang['name']:25s} vocab={stats['vocab_count']:5d} examples={stats['example_count']:2d}")
        if r["issues"] and "--verbose" in sys.argv:
            for issue in r["issues"]:
                print(f"     ! {issue}")

if __name__ == "__main__":
    main()
