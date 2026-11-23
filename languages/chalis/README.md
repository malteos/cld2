# CHALIS knowledge base

Language knowledge for the **CHALIS** benchmark: *Challenging Language Identification Samples*
(Tichý & Libovický, 2026, [arXiv:2606.06088](https://arxiv.org/abs/2606.06088); data:
[`michal-tichy/CHALIS`](https://huggingface.co/datasets/michal-tichy/CHALIS), CC BY-NC 4.0;
evaluation integration: [commoncrawl/commonlid-eval#32](https://github.com/commoncrawl/commonlid-eval/pull/32)).

CHALIS targets two failure modes of language identification (LID):

1. **Cousin languages**: closely related pairs that share most of their high-frequency vocabulary.
2. **Non-standard orthography**: transliteration, stripped diacritics, homoglyphs, spaced letters and leetspeak.

Gold labels are ISO 639-3 codes, taken from the `<iso639_3>_<Script>` label with the script part removed.
For example, Arabic-script Kazakh is scored as `kaz`.

## Sections and languages

| CHALIS section | Texts | Gold languages | What makes it hard | Where to look |
|---|---|---|---|---|
| `single` | 2,894 | ces slk spa cat por glg dan nob nld | cousin pairs | `<code>/differences.md`, `<code>/chalis.md`, [`discriminators.md`](discriminators.md) |
| `cyrillic_to_english` | 6,000 | bul mkd rus srp (and unlabelled ukr) | Cyrillic typed in Latin letters with English-style spelling | `<code>/variants/romanized_en/`, `<code>/chalis.md`, `discriminators/*_roman.tsv` |
| `cyrillic_to_czech` | 1,500 | rus | Russian typed with Czech orthography (ž č š ch ja ju) | `rus_Cyrl/variants/romanized_cs/`, `rus_Cyrl/chalis.md` |
| `arabic` | 1,500 | kaz | Kazakh in Arabic script (tote jazuw) | `kaz_Cyrl/variants/arabic_script/`, `kaz_Cyrl/chalis.md` |
| `diacritics` | 4,500 | ces slk vie | diacritics and tone marks removed | `<code>/variants/no_diacritics/`, `discriminators/ces-slk_nodiac.tsv` |
| `homoglyphs` | 4,500 | ces slk eng | Latin letters replaced by Cyrillic or Greek look-alikes | `<code>/variants/homoglyphs/`, `eng_Latn/chalis.md` |
| `antspeak` | 1,500 | eng | l e t t e r s separated by spaces | `eng_Latn/variants/antspeak/` |
| `leetspeak` | 1,500 | eng | 1337 substitutions | `eng_Latn/variants/leetspeak/` |

Section sizes are from commonlid-eval PR #32 (pinned dataset revision `e4fa744`). In total the sections use 16
distinct gold languages. Ukrainian is included in this knowledge base as a distractor.

| Code | Language | Vocabulary (real frequency data) | Real example texts |
|---|---|---|---|
| ces_Latn | Czech | 10,000 (wordfreq) | 12 (UD FicTree) |
| slk_Latn | Slovak | 10,000 (wordfreq) | 12 (UD SNK) |
| spa_Latn | Spanish | 10,000 (wordfreq) | 12 (UD AnCora) |
| cat_Latn | Catalan | 10,000 (wordfreq) | 12 (UD AnCora) |
| por_Latn | Portuguese | 10,000 (wordfreq) | 12 (UD Bosque) |
| glg_Latn | Galician | 10,000 (FrequencyWords/OpenSubtitles) | 12 (UD CTG) |
| dan_Latn | Danish | 10,000 (wordfreq) | 12 (UD DDT) |
| nob_Latn | Norwegian Bokmål | 10,000 (wordfreq) | 12 (UD Bokmaal) |
| nld_Latn | Dutch | 10,000 (wordfreq) | 12 (UD Alpino) |
| bul_Cyrl | Bulgarian | 10,000 (wordfreq) | 12 (UD BTB) |
| mkd_Cyrl | Macedonian | 10,000 (wordfreq) | 9 (UD MTB) + 1 synthetic |
| rus_Cyrl | Russian | 10,000 (wordfreq) | 12 (UD SynTagRus) |
| srp_Cyrl | Serbian | 9,506 (FrequencyWords, Latin→Cyrillic) | 12 (UD SET, Latin→Cyrillic) |
| kaz_Cyrl | Kazakh | 3,402 (FrequencyWords 2016) | 12 (UD KTB) |
| vie_Latn | Vietnamese | 10,000 (wordfreq) | 12 (UD VTB) |
| eng_Latn | English | 10,000 (wordfreq) | 12 (UD EWT) |
| ukr_Cyrl | Ukrainian (distractor) | 10,000 (wordfreq) | 12 (UD IU) |

## Per-language files

Each language folder (`languages/<code>/`) contains:

- `overview.md`, `grammar.md`, `characteristics.md`, `differences.md`: LLM-written descriptions
  based on the vocabulary and example data. They should be reviewed by native speakers.
- `chalis.md`: a practical identification guide for this language under CHALIS conditions, covering cousin cues,
  noisy-orthography cues, a decision checklist and worked snippets.
- `vocabulary.json`: up to 10k frequency-ranked words (`rank`, `word`, `zipf` or `count`, `source`). Serbian
  entries also carry the original Latin-script form (`latin`).
- `examples/ud_NN.txt`: authentic passages of at least 100 words from Universal Dependencies treebanks, with
  provenance and licences listed in `examples/SOURCES.md`. Files named `NN.txt` without the `ud_` prefix are
  written by an LLM and are synthetic.
- `variants/<kind>/`: the top 3,000 words and four example passages after a CHALIS-style transformation. The
  transformation is deterministic and applied to real text; these are not CHALIS items.

Cross-language files in this folder:

- [`discriminators.md`](discriminators.md) plus `discriminators/*.tsv`: frequent words of one language that do not
  occur in its cousin's 10k list. These are given for standard, diacritic-free (`_nodiac`) and romanized (`_roman`)
  forms.

## Data sources and licences

| Source | Used for | Licence |
|---|---|---|
| [wordfreq](https://github.com/rspeer/wordfreq) 3.x | vocabularies | data CC BY-SA 4.0 |
| [FrequencyWords](https://github.com/hermitdave/FrequencyWords) (OpenSubtitles 2016/2018) | gl, sr, kk vocabularies | content CC BY-SA 4.0 |
| [Universal Dependencies](https://universaldependencies.org/) treebanks (test splits) | example texts | per treebank (CC BY / BY-SA / BY-NC-SA); see `examples/SOURCES.md` |

## Regenerating

All scripts use the repository `.venv` and need network access to PyPI and raw.githubusercontent.com:

```bash
uv pip install --python .venv/bin/python wordfreq
.venv/bin/python languages/scripts/build_vocabulary.py --chalis       # 10k vocabularies
.venv/bin/python languages/scripts/fetch_ud_examples.py --chalis      # real example passages
.venv/bin/python languages/scripts/build_chalis_variants.py           # variants and discriminators
python3 languages/scripts/build_progress.py                           # refresh PROGRESS.md
```

## Known limitations

- The Kazakh Arabic-script variant comes from a simplified rule-based converter (`scripts/translit.py`). Real tote
  jazuw differs in loanwords and in where the hamza sign goes.
- The English-style romanization follows a single convention. Real users mix several (e.g. `ya`/`ja`, `kh`/`h`/`x`,
  `sh`/`w`, and digits such as `4` for `ч` or `6` for `ш`), so treat the variant files as indicative, not exhaustive.
- Serbian vocabulary and examples come from Latin-script sources transliterated to Cyrillic. The source tokens may
  include some Croatian or Bosnian forms.
- The Kazakh vocabulary is small (3.4k words, from subtitles).
- The prose documents were written by an LLM and have not been reviewed by native speakers.
