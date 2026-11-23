# Plan: Language Knowledge Base for CommonLID Benchmark

## Context

CLD2 (Compact Language Detector 2) needs a comprehensive language knowledge base for the ~109 languages in the [CommonLID benchmark](https://huggingface.co/datasets/commoncrawl/CommonLID). This data will support future In-Context Typological (ICT) language identification, where detailed linguistic knowledge (grammar descriptions, typological features, example texts, function words) helps identify languages.

**Key constraint**: No changes to the main CLD2 codebase. All work goes in a new `languages/` folder. Code is only written to collect/format data. Python uses `.venv` with `uv`.

**Branch**: `claude/language-knowledge-base-QaCwG`

---

## Phase 1: Infrastructure & Language List Extraction

### 1.1 Set up Python environment
```bash
cd /home/user/cld2
uv venv .venv
source .venv/bin/activate
uv pip install datasets requests pyyaml beautifulsoup4
```

### 1.2 Extract CommonLID language list
- Write `languages/scripts/extract_language_list.py`
- Primary: Load CommonLID from HuggingFace `datasets` library, extract unique language labels
- Fallback: Compile comprehensive list from training knowledge (used because HF access is blocked in the sandbox)
- Output: `languages/language_list.json` with per-language metadata (ISO code, script, name, family, resource level)

### 1.3 Create folder structure
- `languages/README.md` — project overview and data source documentation
- `languages/PROGRESS.md` — auto-generated tracking table
- `languages/scripts/` — data collection and formatting scripts
- `languages/{lang_code}/` — one subfolder per language (using FLORES-200 style `iso639-3_Script` codes)

### 1.4 Create helper scripts
- `scripts/generate_skeleton.py` — creates all language folder structures
- `scripts/validate_completeness.py` — checks files exist and meet minimum thresholds
- `scripts/build_progress.py` — regenerates PROGRESS.md from filesystem state
- `scripts/fetch_vocabulary.py` — fetches word lists from Wiktionary/Wikipedia APIs
- `scripts/fetch_examples.py` — fetches example texts from Wikipedia API

---

## Phase 2: Knowledge Base Content Generation (per language)

For each of the ~109 languages, create these files using subagents:

### Per-language files

| File | Content | Source |
|------|---------|--------|
| `overview.md` | Family, ISO codes, script, speakers, regions, writing system | AI knowledge |
| `grammar.md` | Word order, morphology, phonology, case system, verb conjugation, syntax | AI knowledge + WALS data |
| `characteristics.md` | LID features: unique chars/diacritics, function words (top 50), n-gram patterns, character frequencies | AI knowledge |
| `differences.md` | Comparison with confusable/related languages, diagnostic features for LID | AI knowledge, referencing CLD2 close-sets |
| `vocabulary.json` | Frequency-ranked word list (~10k target) with translations | AI knowledge (starter ~1-2k) + API scripts |
| `examples/*.txt` | 10+ texts of 100+ words each, different domains | AI knowledge + Wikipedia fetch via subagents |

### Processing strategy
- **Use subagents** to research and generate content for each language
- Process languages in groups by family/confusability (e.g., all Romance languages together so `differences.md` is consistent)
- Group ordering: high-resource confusable groups first, then remaining high-resource, then mid/low-resource
- Each subagent handles 3-10 languages at a time, running in parallel where possible

### CLD2 confusable groups to prioritize (from `internal/lang_script.cc:258-308`)
1. Indonesian / Malay
2. Tibetan / Dzongkha
3. Czech / Slovak
4. Zulu / Xhosa
5. Bosnian / Croatian / Serbian / Montenegrin
6. Hindi / Marathi / Bihari / Nepali
7. Norwegian / Norwegian Nynorsk / Danish
8. Galician / Spanish / Portuguese
9. Kinyarwanda / Rundi

---

## Phase 3: Vocabulary & Example Text Enrichment

After initial generation, use subagents with WebFetch/WebSearch to:
1. **Expand vocabulary** — Fetch Wiktionary frequency lists, Wikipedia word extraction
2. **Add real example texts** — Fetch Wikipedia articles in target language, extract plain text
3. **Add typological features** — Fetch WALS/Grambank data where available

Tiered vocabulary targets:
- High-resource languages: 10k words
- Mid-resource: 5k words
- Low-resource: 1-2k words

---

## Phase 4: Validation & Tracking

- Run `validate_completeness.py` to check all languages meet thresholds
- Update `PROGRESS.md` with per-language completion status
- Fill gaps for low-resource languages where possible

---

## Phase 5: Commit, Push & PR

- Commit all changes to `claude/language-knowledge-base-QaCwG`
- Push to remote
- Create PR to the repository

---

## Folder Structure

```
languages/
├── README.md                    # Project overview
├── PROGRESS.md                  # Per-language completion tracking
├── language_list.json           # Master language list with metadata
├── scripts/
│   ├── extract_language_list.py
│   ├── generate_skeleton.py
│   ├── validate_completeness.py
│   ├── build_progress.py
│   ├── fetch_vocabulary.py
│   └── fetch_examples.py
├── eng_Latn/                    # Example: English
│   ├── overview.md
│   ├── grammar.md
│   ├── characteristics.md
│   ├── differences.md
│   ├── vocabulary.json
│   └── examples/
│       ├── 01.txt
│       ├── 02.txt
│       └── ... (10+ files)
├── deu_Latn/                    # Example: German
│   └── ...
└── ... (one folder per language)
```

---

## Sandbox Constraints (discovered during Phase 1)

- Bash has no direct internet access (`curl` exits with 56).
- HuggingFace API / `datasets.load_dataset_builder("commoncrawl/CommonLID")` returns 403 Forbidden in this environment.
- arXiv HTML and Common Crawl blog pages also return 403 via WebFetch.
- Subagent `WebFetch` / `WebSearch` tools work for many sites (Wikipedia, Wiktionary).
- **Implication**: The CommonLID 109-language list will be compiled from training knowledge for this pass; the extraction script is retained so the list can be verified/refreshed in an environment with HF access.

---

## User Preferences Captured

- **Vocabulary**: Generate starter vocabulary from AI knowledge AND provide Python scripts to expand via Wiktionary/Wikipedia APIs.
- **Example texts**: Generate some from AI knowledge, supplement with real texts fetched by subagents where possible.
- **Language list**: Try HuggingFace `datasets` library first, fall back to a compiled list.

---

## Critical Files (read-only reference)
- `/home/user/cld2/internal/generated_language.cc` — CLD2 language enum + name/code tables
- `/home/user/cld2/internal/lang_script.cc:258-308` — CLD2 confusable language groups
- `/home/user/cld2/CLAUDE.md` — Project conventions (.venv, uv)

## Verification
1. Run `python languages/scripts/validate_completeness.py` — all languages should show required files
2. Check `languages/PROGRESS.md` — all languages marked complete
3. Spot-check 5-10 languages manually: verify grammar accuracy, vocabulary count, example text count/length
4. Verify confusable groups have bidirectionally consistent `differences.md`
