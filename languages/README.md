# Language Knowledge Base for CommonLID (109 languages)

This folder is a curated knowledge base for the **109 languages** covered by the
[CommonLID benchmark](https://huggingface.co/datasets/commoncrawl/CommonLID).
It is intended to support future In-Context Typological (ICT) language
identification: each language has a small dossier of grammatical, lexical, and
orthographic information that a language-ID prompt can draw on.

No CLD2 C/C++ code is modified. All content lives here.

## Contamination policy (read first)

CommonLID is the **evaluation set** for this project. Neither it, nor any
other LID / MT benchmark, may appear in `examples/`, `vocabulary.json`, or
anywhere else that a model sees at prompting time. Read
[`CONTAMINATION_POLICY.md`](CONTAMINATION_POLICY.md) before extending this
knowledge base. A contamination check (`scripts/check_contamination.py`)
verifies that the pipeline produces zero line-level overlap against
CommonLID and FLORES+.

## Contents

- `language_list.json` — authoritative list of the 109 CommonLID languages with
  ISO-639-3 codes, scripts, language families, and resource tiers.
- `PROGRESS.md` — auto-generated completion tracker (regenerate with
  `python scripts/build_progress.py`).
- `CONTAMINATION_POLICY.md` — what we may and may not source from, and why.
- `sources_manifest.json` — per-language record of the URLs that contributed
  to `examples/` on the last refresh. Regenerated on every fetch.
- `{iso3}_{Script}/` — one folder per language, FLORES-200-style code:
  - `overview.md` — family, ISO codes, script, speakers, regions, plus a
    `## Sources` section listing the websites consulted.
  - `grammar.md` — word order, morphology, phonology, syntax summary.
  - `characteristics.md` — LID-relevant features: unique characters, top
    function words, n-gram patterns, frequency signals.
  - `differences.md` — diagnostic features vs. close/confusable languages.
  - `vocabulary.json` — frequency-ranked word list built from non-benchmark
    text (Wikipedia + curated web sources).
  - `examples/*.txt` — real text samples. Each file carries a
    `# Source: <URL>` header naming the origin.
- `scripts/` — tooling (see below).

## Scripts

All scripts assume you've activated `.venv`:

```bash
source .venv/bin/activate
```

| Script | Purpose |
|--------|---------|
| `scripts/extract_language_list.py` | Fetch the 109-language list from the HF dataset's tag metadata (does **not** read the TSV). |
| `scripts/generate_skeleton.py` | Create per-language folders with placeholder markdown. Examples/ is left empty — fill it with the next script. |
| `scripts/sources_catalog.py` | Per-language catalogue of non-benchmark source websites (Wikipedia + government + news + cultural + civil-society + select religious). |
| `scripts/fetch_web_examples.py` | Rebuild `examples/*.txt` from the Wikipedia HF dump and live WebFetch of the curated URL catalogue. Writes a `## Sources` block into each `overview.md`. |
| `scripts/fetch_web_vocabulary.py` | Rebuild `vocabulary.json` from Wikipedia (primary) and the refreshed `examples/*.txt` (secondary). |
| `scripts/check_contamination.py` | Scan every example and vocabulary file against CommonLID + FLORES+ for exact line or ≥80-char substring overlap. Also enforces that every example carries an attributed source header. |
| `scripts/validate_completeness.py` | Check every language meets its tier thresholds (markdown content, vocab size, long-enough example count). |
| `scripts/build_progress.py` | Regenerate `PROGRESS.md`. |

## Data sources (non-benchmark only)

- **Wikipedia** via the `wikimedia/wikipedia` HuggingFace dump. Each example
  carries the article title and the edition URL.
- **Government / state** websites (Rijksoverheid, Bundesregierung, lamoncloa,
  Gov.ie, Karnataka.gov.in, …).
- **News publishers** in the target language (BBC language services, DW,
  Al Jazeera, Tuoi Tre, Pravda, Isolezwe, Dinamani, …).
- **Cultural institutions** (academies, literature portals).
- **Civil society** (UN language editions, UNESCO, UNHCR).
- **Religious** translations — used sparingly as a fallback for low-resource
  languages without news / government coverage (jw.org for some creoles,
  Sefaria for Biblical Hebrew, Vatican Latin archives).

All chosen URLs are recorded in `scripts/sources_catalog.py`.

### Banned

- `commoncrawl/CommonLID`, `openlanguagedata/flores_plus`,
  `allenai/MADLAD-400`, `Helsinki-NLP/opus-100`, WMT test sets, Tatoeba.
- See `CONTAMINATION_POLICY.md` for the full list and reasoning.

## Tier targets

Vocabulary size target depends on the resource tier assigned in
`language_list.json`:

- `high` — 10,000 words
- `mid` — 5,000 words
- `low` — 1,000 words

When a language's Wikipedia edition + curated URLs don't yield enough text
to hit the target, the script truncates to whatever is available. The
validator treats "exhausted unique tokens" as satisfied.

## Rebuilding from scratch

```bash
source .venv/bin/activate
set -a && source .env && set +a                                   # HF_TOKEN, etc.
python languages/scripts/extract_language_list.py                 # 109-code list
python languages/scripts/generate_skeleton.py                     # empty skeletons
python languages/scripts/fetch_web_examples.py    --all           # live web examples
python languages/scripts/fetch_web_vocabulary.py  --all           # wiki vocab
python languages/scripts/check_contamination.py   --all           # PROVE clean
python languages/scripts/build_progress.py                        # PROGRESS.md
python languages/scripts/validate_completeness.py                 # tier sanity
```

## Environment notes

- `HF_TOKEN` in `.env` (read-only) is required to download the CommonLID
  TSV for the contamination check. Examples and vocabulary themselves do
  not use CommonLID — only the checker does, and only to prove non-overlap.
- Arbitrary public websites are reachable in this environment. Individual
  curated URLs occasionally fail (DNS, SSL, rate limits); the fetcher
  tolerates this and proceeds with remaining sources.
- Low-resource languages routinely produce fewer than 12 example passages
  because their web presence is thin. This is recorded in
  `sources_manifest.json` and is acceptable — real-text scarcity is the
  honest result, not a bug to paper over.
