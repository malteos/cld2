# Language Knowledge Base for CommonLID (109 languages)

This folder is a curated knowledge base for the **109 languages** covered by the
[CommonLID benchmark](https://huggingface.co/datasets/commoncrawl/CommonLID).
It is intended to support future In-Context Typological (ICT) language
identification: each language has a small dossier of grammatical, lexical, and
orthographic information that a language-ID prompt can draw on.

No CLD2 C/C++ code is modified. All content lives here.

## Contents

- `language_list.json` — authoritative list of the 109 CommonLID languages with
  ISO-639-3 codes, scripts, language families, and resource tiers.
- `PROGRESS.md` — auto-generated completion tracker (regenerate with
  `python scripts/build_progress.py`).
- `{iso3}_{Script}/` — one folder per language, FLORES-200-style code:
  - `overview.md` — family, ISO codes, script, speakers, regions.
  - `grammar.md` — word order, morphology, phonology, syntax summary.
  - `characteristics.md` — LID-relevant features: unique characters, top
    function words, n-gram patterns, frequency signals.
  - `differences.md` — diagnostic features vs. close/confusable languages.
  - `vocabulary.json` — frequency-ranked word list (JSON).
  - `examples/*.txt` — real text samples (seeded from CommonLID and FLORES+).
- `per_language_samples/{code}.txt` — raw extracted sample lines per language
  (intermediate artefact; not part of the knowledge base).
- `scripts/` — tooling (see below).

## Scripts

All scripts assume you've activated `.venv`:

```bash
source .venv/bin/activate
```

| Script | Purpose |
|--------|---------|
| `scripts/extract_language_list.py` | Fetch the 109-language list from HuggingFace dataset tags and pre-slice sample lines per language. |
| `scripts/generate_skeleton.py` | Create per-language folders with placeholder markdown and pre-seeded example files. |
| `scripts/fetch_vocabulary.py` | Build `vocabulary.json` from the CommonLID TSV and FLORES+ dev/devtest split. |
| `scripts/fetch_examples.py` | Append longer example passages from FLORES+ where the CommonLID seed snippets are too short. |
| `scripts/validate_completeness.py` | Check every language meets its tier thresholds (md content, vocab size, long-enough example count). |
| `scripts/build_progress.py` | Regenerate `PROGRESS.md`. |

## Data sources

- **CommonLID** (`commoncrawl/CommonLID` on HuggingFace) — primary source for
  real-world web text and the canonical 109-language label set.
- **FLORES+** (`openlanguagedata/flores_plus` on HuggingFace) — supplementary
  clean sentence-level text for languages where CommonLID has few annotated
  lines. FLORES+ uses the same `iso639-3_Script` folder convention.
- **Written knowledge** — `overview.md`, `grammar.md`, `characteristics.md`, and
  `differences.md` are curated prose; they condense typological knowledge into
  a form useful for in-context LID prompting.

## Tier targets

Vocabulary size target depends on the resource tier assigned in
`language_list.json`:

- `high` — 10,000 words
- `mid` — 5,000 words
- `low` — 1,000 words

When CommonLID + FLORES+ don't have enough text to hit the target, the script
truncates to whatever is available; the remaining words are the full unique
token set for the language.

## Rebuilding from scratch

```bash
source .venv/bin/activate
python languages/scripts/extract_language_list.py   # pulls dataset + samples
python languages/scripts/generate_skeleton.py       # creates folders + seed examples
python languages/scripts/fetch_vocabulary.py --all  # frequency-ranked vocab
python languages/scripts/fetch_examples.py  --all   # supplement with FLORES+
python languages/scripts/build_progress.py          # regenerate PROGRESS.md
python languages/scripts/validate_completeness.py   # sanity check
```

## Sandbox caveats

- Wikipedia / Wiktionary public APIs are blocked by the sandbox egress policy.
- HuggingFace Hub is available (HF_TOKEN is read-only; suitable for gated
  dataset access). CommonLID and FLORES+ are both fetched via
  `huggingface_hub`.
- That's why vocabulary/example enrichment relies on HF datasets rather than
  live Wikipedia — the mechanism still works if Wikipedia access is restored
  in another environment.
