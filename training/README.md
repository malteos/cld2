# Training CLD2 on new languages

Google never released the training pipeline for CLD2 (`postproc-cld2`,
run over Google-internal ngram MapReduce output). This directory contains
a reverse-engineered replacement that trains the non-CJK scoring tables
from scratch, from plain `(language code, text)` pairs, and supports
adding languages CLD2 has never heard of.

Verified end to end: trained on 8 Leipzig 10K corpora (en, de, fr, es,
it, ru + **Chuvash `cv`** and **Silesian `szl`**, which stock CLD2 does
not know), the rebuilt detector scores **100%** on 1,486 held-out ~600-byte
documents and **99.7%** on ~10-word fragments. Stock tables score 79.5%
on the same set (0% for cv/szl, which they cannot represent).

## Quick start

```bash
# 1. fetch corpora (Leipzig Corpora Collection), 90/10 train/eval split
python3 training/fetch_leipzig.py --out training/data \
    --corpus en=eng_news_2023_10K --corpus de=deu_news_2023_10K \
    --corpus fr=fra_news_2023_10K --corpus es=spa_news_2023_10K \
    --corpus it=ita_news_2023_10K --corpus ru=rus_news_2023_10K \
    --corpus cv=chv_wikipedia_2021_10K --corpus szl=szl_wikipedia_2021_10K

# 2. register new languages, build, train, evaluate
python3 training/train.py \
    --train training/data/train.tsv --eval training/data/eval.tsv \
    --register cv:CHUVASH:Cyrillic --register szl:SILESIAN:Latin
```

Training data format: one document per line, `code<TAB>utf8 text`.
Any corpus works; `fetch_leipzig.py` is just a convenience. A few hundred
KB per language is enough for a usable model; more is better. **Include
every language you want detectable** — the tables only know the languages
they were trained on, and anything else will be misattributed or unknown.

The output `training/output/cld2_generated_trained.cc` is a drop-in
replacement for these four files in any CLD2 build:

```
internal/cld2_generated_quadchrome_2.cc
internal/cld2_generated_deltaoctachrome.cc
internal/cld2_generated_distinctoctachrome.cc
internal/cld_generated_score_quad_octa_2.cc
```

(Keep linking the CJK files — `cld_generated_cjk_uni_prop_80.cc`,
`cld2_generated_cjk_compatible.cc`, `cld_generated_cjk_delta_bi_4.cc`,
`generated_distinct_bi_0.cc` — they are independent of these tables.)

## Files

| File | Purpose |
|---|---|
| `generate_cld2_tables.cc` | The trainer: TSV in, generated table `.cc` out |
| `register_language.py` | Claims a spare `Language` enum slot + per-script number for a new language and rewrites `internal/generated_language.cc/.h` |
| `train.py` | Orchestrates register → build → train → build eval → evaluate |
| `eval_detect.cc` | Accuracy/confusion report over a held-out TSV |
| `fetch_leipzig.py` | Downloads Leipzig Corpora Collection 10K corpora into train/eval TSVs |

## How CLD2's tables work (reverse-engineered)

CLD2 scores text with a Naive-Bayes-style accumulation over hashed
character ngrams. Everything below was recovered from the runtime code
(`internal/cldutil*.cc`, `scoreonescriptspan.cc`) and the headers of the
original generated files, which record the `postproc-cld2` command lines.

**Text normalization.** `ScriptScanner::GetOneScriptSpanLower`
(`getonescriptspan.cc`) strips HTML tags/entities, splits the input into
single-script spans of letters/marks, collapses every non-letter run to
one ASCII space, and lowercases. Spans arrive padded: one leading space,
`" \0"`-style trailing spaces. The trainer feeds its corpus through this
exact code.

**Gram extraction.** For "RTypeMany" scripts (Latin, Cyrillic, Arabic,
Hebrew, Devanagari, Bengali, Tibetan, Ethiopic) the runtime samples
quadgrams with a stride of ~2 characters plus an ASCII-vowel skip
(`GetQuadHits`), and whole words truncated to 8 characters
(`GetOctaHits`). Both keep a 2-entry repeat filter. The trainer
replicates these loops verbatim so the trained counts match what the
runtime will look up. Scripts with one dominant language ("RTypeOne",
e.g. Greek, Thai) never consult these tables — the script itself decides —
and Han uses a separate CJK path this trainer does not regenerate.

**Hashing.** Quadgrams hash to 32 bits with `QuadHashV2`, words to 40
bits with `OctaHash40` (`cldutil_shared.cc`); leading/trailing spaces set
indicator bits. A fingerprint maps to a hash bucket via
`QuadFPJustHash`/`OctaFPJustHash`: bucket = `(fp + (fp >> 12)) &
(nbuckets - 1)`, key = masked high bits.

**Table format** (`cld2tablesummary.h`). A `CLD2TableSummary` is a 4-way
associative hash table of 16-byte `IndirectProbBucket4` buckets. Each
32-bit slot packs `hashkey | indirect_subscript` under `kCLDTableKeyMask`
(quad tables: `0xffff0000` = 16-bit key + 16-bit subscript; octa tables:
`0xfffff000`). The subscript indexes the shared value pool `kCLDTableInd`:
subscripts `< kCLDTableSizeOne` address one 32-bit langprob (up to 3
languages); larger subscripts `s` address the pair at `2s - SizeOne`
(up to 6 languages). Identical langprob combinations are deduplicated.

**Langprob encoding.** One langprob word =
`(lang3 << 24) | (lang2 << 16) | (lang1 << 8) | prob_byte`. Languages are
8-bit *per-script numbers* (`PerScriptNumber`, two independent number
spaces: Latin-script and everything-else; `FromPerScriptNumber` resolves
them against the span's script at lookup time). The `prob_byte` indexes
`kLgProbV2Tbl` (240 entries), which expands to three quantized log2
probabilities in 1..12. Packing uses the original offline code
`ProbPackV2`/`FindBestProb3Match` (`cldutil_offline.cc`), which survives
in the repo even though the trainer around it was never released.

**Quantization used by this trainer.** For each ngram and language,
`p = count / total_ngrams(language, script)`, and
`qprob = clamp(1..12, 12 + log2(p) - pref_log2)` with `pref_log2 = -9`
by default (`--pref_log2`), i.e. a relative frequency of 1/512 earns the
maximum score. At detection time the runtime sums qprobs per language
over each chunk (`ProcessProbV2Tote`), so this is naive Bayes with
per-language-normalized emission frequencies.

**Distinct words.** Strongly language-pure words (default: ≥90% of
occurrences in one language, ≥4 occurrences) go into the distinct-octa
table as single-language entries with qprob 2–4 by purity, mirroring the
`lang.un.un_N00` entries in the original tables. They add per-chunk boosts
(`AddDistinctBoost2`).

**Delta-octa table.** The original pipeline stored per-word corrections
relative to quad-only scoring (`--wrt=` in the original command lines,
`DoWordScore` in `cldutil_offline.cc`). This trainer emits an empty
(always-miss) table there; quads + distinct words already carry the
accuracy above. This is the main known gap vs. Google's pipeline.

**Expected-score table.** `kAvgDeltaOctaScore[lang * 4 + script4]`
(script4: Latn/Cyrl/Arab/other) holds the score per 1KB a genuine
document of that language should earn; the runtime compares actual vs.
expected for reliability (`ReliabilityExpected`, ratio ≤ 1.5 → 100%).
The trainer calibrates it in a second pass over the corpus with the
freshly built tables. A zero entry means "always reliable", the safe
default for untrained languages.

**Bucket allocation.** Like the original (`--flatmap --rr_alloc
--freq_alloc` stats blocks in the generated files), candidates whose
`(bucket, key)` collide are merged, then each bucket keeps its 4
highest-count entries; overflow is dropped and reported. Bucket count is
auto-sized to ~60% fill (`--quad_buckets`/`--octa_buckets` to override).

## Adding a new language

`register_language.py --code xx --name NEWLANG --script Latin` rewrites
`internal/generated_language.cc`:

- claims a spare `Language` slot (the `X_NN` placeholders, e.g. cv → 81)
  and a spare per-script number in the right number space,
- fills `kLanguageToName/CName/Code/Scripts/PLang`,
  `kPLangToLanguageLatn|Othr`, and the sorted `kNameToLanguage` /
  `kCodeToLanguage` lookup arrays.

It is idempotent; revert with `git checkout internal/generated_language.*`.
The public `Language` enum identifier stays `X_NN` (binary layout is
frozen), but `LanguageCode()`/`LanguageName()`/`GetLanguageFromName()`
all speak the new code/name, and `ExtDetectLanguageSummary` returns the
new language. This repo has `cv` (CHUVASH, slot 81) and `szl` (SILESIAN,
slot 82) registered as working examples.

## Limitations

- **Non-CJK only.** Chinese/Japanese/Korean keep their original tables;
  training new Han-script languages is not supported.
- **RTypeMany scripts only.** A new language in an RTypeOne script
  (e.g. Greek script) would require flipping that script's recognition
  type — not automated here.
- **Closed world.** Detection quality is only meaningful among the
  trained languages; the original 80+-language coverage is replaced, not
  extended in place (train with all languages you care about).
- **No delta-octa table** (see above), and no distinct word *pairs*.
- The `--indirectbits`-style probability tuning knobs of the original
  are reduced to `--pref_log2`, `--max_langs`, `--min_count`,
  `--distinct_*`; the defaults reproduce sensible tables.
- Tables are little-endian, like all of CLD2.
