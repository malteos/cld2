# Language Knowledge Base for CommonLID Benchmark

Comprehensive linguistic knowledge base for ~109 languages in the [CommonLID benchmark](https://huggingface.co/datasets/commoncrawl/CommonLID), designed to support In-Context Typological (ICT) language identification.

## Structure

Each language has a subfolder named `{iso639-3}_{Script}` containing:

| File | Description |
|------|-------------|
| `overview.md` | Language classification, speakers, regions, writing system |
| `grammar.md` | Word order, morphology, phonology, syntax, typological features |
| `characteristics.md` | LID-relevant features: unique characters, function words, n-gram patterns |
| `differences.md` | How to distinguish from confusable/related languages |
| `vocabulary.json` | Frequency-ranked word list (target: 10,000 entries) |
| `examples/` | At least 10 texts of 100+ words each, covering different domains |

## Data Sources

- **AI knowledge** — initial generation of overviews, grammar, characteristics, differences
- **Wiktionary** — vocabulary expansion via frequency lists
- **Wikipedia** — real example texts in target languages
- **WALS / Grambank** — typological feature data

## Language List

See [`language_list.json`](language_list.json) for the master list of all languages with metadata.

## Progress

See [`PROGRESS.md`](PROGRESS.md) for per-language completion status.

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/extract_language_list.py` | Extract language list from HuggingFace dataset |
| `scripts/generate_skeleton.py` | Create folder structure for all languages |
| `scripts/validate_completeness.py` | Check all languages have required files |
| `scripts/build_progress.py` | Regenerate PROGRESS.md from filesystem state |
| `scripts/fetch_vocabulary.py` | Fetch word lists from Wiktionary/Wikipedia APIs |
| `scripts/fetch_examples.py` | Fetch example texts from Wikipedia API |

## CLD2 Confusable Language Groups

These language pairs/groups are particularly hard to distinguish and get priority attention in `differences.md`:

1. Indonesian / Malay
2. Tibetan / Dzongkha
3. Czech / Slovak
4. Zulu / Xhosa
5. Bosnian / Croatian / Serbian
6. Hindi / Marathi / Nepali
7. Norwegian Bokmal / Norwegian Nynorsk / Danish
8. Galician / Spanish / Portuguese
9. Kinyarwanda / Rundi
