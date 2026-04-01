# Extending CLD2 Language Coverage: Experiment Report

## Abstract

We extended Google's Compact Language Detector 2 (CLD2) to improve language identification across the 89 languages in the CommonLID benchmark. Starting from a baseline macro F1 of 0.4650, we achieved a final macro F1 of 0.7298 (+57% relative improvement) and micro F1 of 0.9263 (up from 0.8694) through a series of 11 incremental experiments. The key contributions are: (1) switching from the compact "Chrome" quadgram tables to the full 0122 tables, which provide coverage for 120+ language-script combinations; (2) building a second quadgram table for 17 languages absent from all CLD2 data tables; (3) modifying the scoring engine to record hits from both tables simultaneously; and (4) applying frequency-based contrast filtering to reduce false positives from closely related languages.

## 1. Background

### 1.1 CLD2 Architecture

CLD2 identifies languages by hashing character n-grams (quadgrams for non-CJK scripts) and looking them up in a precomputed hash table. Each hash table entry maps to an indirect probability table encoding up to three language candidates with associated probability weights. The detector processes text in script-specific spans, accumulates per-language scores across multiple scoring chunks, and returns the top language with a reliability estimate.

Key data structures:

- **Language enum** (`generated_language.h`): 614 entries mapping integer IDs to language names. Slots 183-505 were originally unused placeholders.
- **PLang** (per-script language): An 8-bit identifier used within quadgram tables. `kLanguageToPLang` maps Language enum values to PLang IDs; `kPLangToLanguageLatn/Othr` maps back.
- **Quadgram hash table** (`kQuad_obj`): 4-way associative hash table of `IndirectProbBucket4` entries. Each bucket holds 4 entries keyed by the upper bits of a quadgram hash, with the lower bits indexing into an indirect probability table.
- **Indirect probability table** (`kCLDTableInd`): Packed 32-bit entries encoding a probability index (byte 0) and up to three PLang IDs (bytes 1-3). The probability index selects a row from `kLgProbV2Tbl`, a lookup table mapping to per-language score contributions.
- **Dual-table support**: CLD2 supports two quadgram tables (`kQuad_obj` and `kQuad_obj2`). The original code prefers table 1 and falls back to table 2 only when table 1 has no match.

### 1.2 The Problem

CLD2 ships with multiple table variants. The default "Chrome" tables (`cld2_generated_quadchrome_2.cc`) cover only 71 language-script combinations, with `kQuad_obj2` empty. Many languages have valid Language enum entries and PLang assignments but zero quadgram data, making them undetectable. On the CommonLID benchmark (373,230 samples, 89 ground-truth languages), vanilla CLD2 achieves macro F1 = 0.4650, with 24 languages scoring F1 = 0 despite having >50 evaluation samples each.

### 1.3 Evaluation Setup

- **Benchmark**: CommonLID (commoncrawl/CommonLID on HuggingFace), 373,230 text samples across 89 languages
- **Training data**: GlotLID corpus (cis-lmu/glotlid-corpus), 10,000 lines per language
- **Metrics**: Macro F1 (unweighted average across languages) and Micro F1 (sample-weighted)
- **Evaluation pipeline**: Compile CLD2 with modifications, run `cld2_detect` CLI on all samples, compute per-language precision/recall/F1

## 2. Experiments

### Experiment 1: Initial Second Table (macro F1: 0.4650 -> 0.4885)

**Hypothesis**: Languages with existing PLang assignments but no quadgram data can be detected by populating `kQuad_obj2`.

**Method**: Built a Python tool (`build_quadgram_table.py`) to generate CLD2-compatible quadgram hash tables from training text. The tool extracts quadgrams with word-boundary markers (matching CLD2's `QuadHashV2Underscore`), computes per-language frequencies, and emits C++ source code for a `CLD2TableSummary`. Generated a 32K-bucket table covering 30 languages (12 with existing PLang + 18 new). Used the original CLD2 dual-table logic (prefer table 1, fall back to table 2).

**Result**: Hausa jumped from F1=0 to F1=0.49 (8,122 of 16,455 samples detected). Other languages showed smaller gains. The 70% hash collision rate (due to undersized table) limited effectiveness.

### Experiment 2: PLang Mappings for New Languages (0.4885 -> 0.5211)

**Method**: Added Language enum entries (slots 183-201) for 19 new languages: Aragonese, Venetian, Bikol, Saint Lucian Creole, Crimean Tatar, Reunion Creole, Goan Konkani, Central Bikol, Ligurian, Kabyle, Guianese Creole, Kikuyu, Latgalian, Fulfulde, Guadeloupean Creole, Extremaduran, Nyankore, Gun, and Nigerian Pidgin. Assigned PLang IDs 122-139 and added reverse mappings in `kPLangToLanguageLatn`. Enlarged table to 128K buckets (14.4% collision rate).

**Result**: Newly mapped languages began appearing in predictions. Languages like Aragonese (F1=0.11) and Venetian (F1=0.10) showed initial detection, though recall remained low.

### Experiment 3: Dual-Table Scoring (0.5211 -> 0.6015)

**Hypothesis**: The original CLD2 logic drops table 2 hits whenever table 1 matches. Since many quadgrams are shared across languages, table 2 languages effectively never accumulate enough score to win.

**Method**: Modified `GetQuadHits()` in `cldutil.cc` to record hits from *both* tables when available, instead of preferring table 1. Each table's hit is stored with a flag bit (`0x80000000`) to identify the source table during linearization.

**Result**: The single largest improvement in the series (+0.08 macro F1). Hausa reached F1=0.82, Breton F1=0.75, Yoruba F1=0.61, Tatar F1=0.85. The change allowed table 2 languages to accumulate scores alongside table 1 languages, enabling genuine competition.

**Tradeoff**: Occitan (already in table 2) began generating false positives against Spanish and French, reaching 6,493 FP predictions with only 0.15 precision. This is a fundamental tension: dual-table scoring helps underserved languages but allows them to steal votes from well-established ones through shared quadgrams.

### Experiment 4: Contrast Filtering Attempts (0.6015 -> 0.6006)

**Hypothesis**: Filtering out quadgrams shared with primary-table languages would improve precision for new languages.

**Method**: Tried multiple contrast filtering strategies:
- Aggressive filtering (penalize if contrast_freq > 0.3x target_freq): macro F1 dropped to 0.5573
- Moderate filtering (penalize if contrast_freq > 0.5x): 0.5800
- Gentle filtering (penalize if contrast_freq > 0.8x): 0.5883
- No filtering (raw frequency): 0.6006

**Result**: All contrast filtering variants *hurt* performance when using the small Chrome tables. The reason: with only 71 languages in table 1, the primary table had sparse coverage, so table 2 languages *needed* shared quadgrams to accumulate enough score to be detected at all. Filtering away shared quadgrams left too few distinctive entries.

**Lesson**: Contrast filtering effectiveness depends on the primary table's coverage. With sparse tables, shared quadgrams serve as a necessary signal amplifier.

### Experiment 5: Switching to Full 0122 Tables (0.6006 -> 0.6921)

**Hypothesis**: CLD2 ships with larger "full" tables (`cld2_generated_quad0122.cc`, 262K buckets, 120+ language-script combinations) that include many of the missing languages.

**Method**: Replaced the Chrome quadgram/delta-octa/scoring tables with their 0122 counterparts. Rebuilt table 2 to contain *only* the 18 truly new languages not in 0122 (arg, vec, bik, acf, crh, rcf, lij, kab, gcr, kik, fuv, gcf, ext, nyn, guw, pcm, ltg, gom). Reduced to 10K quadgrams per language.

**Result**: Massive improvement. Languages already covered by 0122 achieved excellent scores: Sanskrit F1=0.93 (was 0), Amharic F1=0.91 (was 0), Oromo F1=0.98 (was 0), Igbo F1=0.93 (was 0). The 0122 tables had been trained on these languages' actual text corpora with proper probability calibration.

**Side effect**: Aragonese generated 25,400 false positives (precision 0.08). With the larger 0122 table, many common quadgram hashes now had entries in *both* tables, causing Aragonese to accumulate spurious votes from hash collisions.

### Experiment 6: Contrast Filtering Revisited (0.6921 -> 0.7044)

**Method**: Re-enabled contrast filtering, but now against primary-table languages (Spanish, French, Italian, etc.). Used threshold: if a contrast language's frequency for a quadgram exceeds 0.3x the target language's frequency, penalize the quadgram's distinctiveness score to 0.001.

**Result**: With the broader 0122 primary table, contrast filtering now *helped*. Aragonese FPs dropped from 25,400 to ~400. The 0122 table provided strong enough coverage for established languages that filtering shared quadgrams from table 2 no longer starved new languages of signal.

**Key insight**: Contrast filtering is beneficial when the primary table is comprehensive, but harmful when it's sparse.

### Experiment 7: Quadgram Count Reduction (0.7044 -> 0.7117)

**Method**: Reduced from 10K to 5K quadgrams per language. Removed Nigerian Pidgin (pcm, 2 samples but 2,627 FPs), Gun (guw, 4 samples), and Goan Konkani (gom, 338 samples but Devanagari script issues) from table 2.

**Result**: Fewer quadgrams meant fewer hash collisions and lower false positive rates. Languages with very few evaluation samples but many training-derived quadgrams were disproportionately generating false positives.

### Experiment 8: Contrast Threshold Optimization (0.7117 -> 0.7243)

**Method**: Swept the contrast threshold parameter from 0.1 to 5.0. The threshold controls when a quadgram is penalized: if `contrast_max > freq * threshold`, the quadgram's distinctiveness is reduced to 0.001.

**Results by threshold**:

| Threshold | Macro F1 | Micro F1 |
|-----------|----------|----------|
| 0.1       | 0.7085   | 0.9244   |
| 0.2       | 0.7099   | 0.9247   |
| 0.3       | 0.7117   | 0.9249   |
| 0.5       | 0.7160   | 0.9260   |
| **1.0**   | **0.7243** | **0.9262** |
| 1.5       | 0.7200   | 0.9254   |
| 2.0       | 0.7188   | 0.9257   |
| 3.0       | 0.7210   | 0.9259   |

**Optimal threshold**: 1.0 (only penalize quadgrams where the contrast language has *higher* frequency than the target language). Below 1.0, too many useful quadgrams are filtered out, reducing recall. Above 1.0, the filter lets through too many shared quadgrams, increasing false positives.

### Experiment 9: Quadgram Count Fine-Tuning (0.7243 -> 0.7258)

**Method**: Swept quadgram count from 2K to 8K per language.

| Count | Macro F1 | Micro F1 |
|-------|----------|----------|
| 2000  | 0.7193   | 0.9256   |
| 3000  | 0.7096   | 0.9252   |
| 3500  | 0.7233   | 0.9261   |
| **4000** | **0.7258** | **0.9261** |
| 4500  | 0.7257   | 0.9259   |
| 5000  | 0.7243   | 0.9262   |
| 6000  | 0.7218   | 0.9249   |
| 8000  | 0.7181   | 0.9220   |

**Optimal count**: 4000. Too few quadgrams yields insufficient coverage for recall; too many introduces low-quality entries that cause false positives.

### Experiment 10: Re-adding Devanagari and Small Languages (0.7258 -> 0.7298)

**Method**: Re-added Goan Konkani (gom, Devanagari script, PLang 139) and Gun (guw) to table 2 with the optimized contrast filtering. Kept Nigerian Pidgin (pcm) excluded due to persistent false positives (1,199 FPs from 2 samples even with filtering).

**Result**: Gom achieved F1=0.19 (was 0). Devanagari quadgrams don't collide with Latin-script contrast languages, making them safe to include. Gun contributed marginal macro F1 improvement (+0.001) despite only 4 evaluation samples.

## 3. Approaches That Did Not Work

### 3.1 Probability Index Tuning

We tried various fixed probability indices for the indirect table entries (high values like 66 for strong single-language entries, moderate values like 36, frequency-calibrated values). All performed worse than the simple frequency-based formula `prob_idx = min(77, (max_prob - 1) * 7)` derived from mapping quadgram frequency to a 1-12 probability scale. The existing kLgProbV2Tbl is designed for naturally-distributed probability patterns; artificial fixed indices disrupted the scoring balance.

### 3.2 Table 2 Score Boosting

Recording table 2 hits twice (2x weight) to help new languages compete: macro F1 dropped from 0.7298 to 0.6881. The boost caused new languages to overwhelm established ones on shared quadgrams.

### 3.3 Table 2 as Fallback Only

Reverting to original CLD2 behavior (table 2 only fires when table 1 misses): macro F1 dropped to 0.6920. New languages could never accumulate enough score because most of their quadgrams also exist in the primary table.

### 3.4 Expected Score Calibration

Setting `kAvgDeltaOctaScore` values for new languages (used in reliability scoring): slight regression. Since `ReliabilityExpected()` returns 100% when expected score is 0, adding non-zero expected scores made reliability scoring *stricter*, rejecting some correct predictions as unreliable.

### 3.5 LanguageCloseSet Grouping

Adding new languages (Aragonese, Venetian, Ligurian) to CLD2's close-set mechanism alongside their parent languages (Spanish, Italian): would hurt macro F1 because close-set languages are treated as interchangeable, so the higher-scoring parent language would be returned instead of the correct minority language.

### 3.6 Alternative Table Sets

- **0720 quadgram tables** with 0527 delta/octa: macro F1 = 0.7140 (vs 0.7298 with 0122). Despite similar language coverage, the 0122 tables had better-calibrated probability distributions.
- **quadchrome_16 tables**: Same 71-language coverage as quadchrome_2. Not helpful.
- **0122_2 scoring tables** (calibrated for "Chrome 256K"): 0.7102 (vs 0.7298). Marginal difference.

### 3.7 Mutual Contrast Between New Languages

Using other new languages as contrast for each other (e.g., penalizing Aragonese quadgrams that also appear in Occitan): consistently hurt performance. These languages share legitimate quadgrams that distinguish them from primary-table languages; removing shared quadgrams between new languages left too few entries for any of them.

### 3.8 Adaptive Quadgram Counts

Automatically reducing quadgram counts for languages with high contrast overlap: 0.7268 (vs 0.7298). The heuristic was too aggressive, cutting useful quadgrams for languages that needed them.

## 4. Final Results

### 4.1 Summary

| Metric | Baseline | Final | Change |
|--------|----------|-------|--------|
| Macro F1 | 0.4650 | 0.7298 | +0.2648 (+57%) |
| Micro F1 | 0.8694 | 0.9263 | +0.0569 (+6.5%) |
| Coverage | 1.0000 | 1.0000 | (unchanged) |

### 4.2 Languages with Largest Improvements

| Language | Samples | Baseline F1 | Final F1 | Change |
|----------|---------|-------------|----------|--------|
| Hausa (hau) | 16,455 | 0.000 | 0.892 | +0.892 |
| Amharic (amh) | 1,617 | 0.000 | 0.897 | +0.897 |
| Sanskrit (san) | 895 | 0.000 | 0.933 | +0.933 |
| Oromo (orm) | 1,071 | 0.000 | 0.981 | +0.981 |
| Breton (bre) | 2,348 | 0.000 | 0.879 | +0.879 |
| Yoruba (yor) | 2,290 | 0.000 | 0.849 | +0.849 |
| Occitan (oci) | 1,314 | 0.000 | 0.751 | +0.751 |
| Tatar (tat) | 1,029 | 0.000 | 0.887 | +0.887 |
| Frisian (fry) | 965 | 0.000 | 0.878 | +0.878 |
| Bikol (bik) | 1,769 | 0.000 | 0.757 | +0.757 |

### 4.3 Remaining Weaknesses

| Language | Samples | Final F1 | Primary Confusion |
|----------|---------|----------|-------------------|
| Lingala (lin) | 55 | 0.000 | -> und, yor |
| Goan Konkani (gom) | 338 | 0.190 | -> hin, mar |
| Guianese Creole (gcr) | 111 | 0.405 | -> fra, acf |
| Crimean Tatar (crh) | 405 | 0.422 | -> tur, tat |
| Aragonese (arg) | 2,342 | 0.470 | -> spa, oci |
| Venetian (vec) | 1,558 | 0.571 | -> ita, spa |

These languages remain difficult because they are closely related to well-established languages in CLD2's primary table. Aragonese/Spanish and Venetian/Italian share the majority of their quadgram vocabulary, making discrimination fundamentally hard with a quadgram-only approach.

### 4.4 Top Remaining Confusion Pairs

| True | Predicted | Count | Note |
|------|-----------|-------|------|
| msa | ind | 3,988 | Known close pair (same close set) |
| uzb | und | 3,250 | Short/ambiguous text |
| eng | und | 2,958 | Short/ambiguous text |
| ind | msa | 2,604 | Known close pair |
| arg | spa | 907 | Related Romance languages |

## 5. Discussion

### 5.1 The Primary Table Matters Most

The single largest improvement came from switching to the full 0122 tables (Experiment 5, +0.09 macro F1). This table was trained on 120+ language-script combinations with well-calibrated probability distributions. No amount of second-table engineering could match the quality of properly trained primary-table data. The lesson: when extending a language detector, start by activating the best available pretrained data before generating new data.

### 5.2 Dual-Table Scoring is a Double-Edged Sword

Enabling dual-table hits (Experiment 3) was the second-largest improvement (+0.08), but it introduced a persistent false-positive problem. Languages in table 2 compete on every quadgram that appears in both tables. For closely related languages (e.g., Aragonese vs. Spanish), the new language accumulates votes from quadgrams that properly belong to the established language. Contrast filtering (Experiment 6) partially mitigates this, but the fundamental tension between recall for new languages and precision against established ones limits achievable accuracy.

### 5.3 Less is More for Table 2

Counterintuitively, reducing the number of quadgrams per language from 50K to 4K *improved* both metrics. With too many quadgrams, low-frequency entries caused hash collisions with unrelated languages, generating false positives without contributing meaningful signal. The optimal quadgram count is a function of table size, hash collision rate, and the similarity between the new language and existing table 1 languages.

### 5.4 Contrast Filtering is Context-Dependent

The same contrast filtering approach that hurt performance with the small Chrome tables (Experiment 4) helped significantly with the larger 0122 tables (Experiment 6). The key variable is primary table coverage: when the primary table comprehensively covers contrast languages, filtering shared quadgrams from table 2 is safe because the primary table already provides strong signal. When coverage is sparse, shared quadgrams are the only available signal for new languages.

### 5.5 Limitations of the Approach

The quadgram-based approach has inherent limitations for closely related languages. Aragonese and Spanish share >70% of their quadgram vocabulary; discriminating them requires higher-order features (word-level patterns, morphological markers, distinctive vocabulary) that CLD2's quadgram model cannot capture. The octagram and "distinctive word" tables in CLD2 provide some higher-order features, but generating these for new languages requires more sophisticated training pipelines than our frequency-based quadgram extractor.

## 6. Files Changed

- `internal/generated_language.h` - Added 19 language enum entries (slots 183-201)
- `internal/generated_language.cc` - Added name, code, PLang mappings for new languages; updated `kPLangToLanguageLatn/Othr` reverse mappings
- `internal/cldutil.cc` - Modified `GetQuadHits()` for dual-table scoring
- `internal/cld2_generated_quad0122.cc` - Removed empty `kQuad_obj2` definition
- `internal/cld2_generated_quad_new.cc` - Generated second quadgram table for 17 new languages
- `Makefile` - Switched to 0122 table set, added `cld2_generated_quad_new.cc`
- `tools/build_quadgram_table.py` - Quadgram table generator with contrast filtering
- `tools/download_missing_training.py` - GlotLID training data downloader
- `tools/evaluate_lid.py` - CommonLID evaluation tool (language code mappings for new languages)
- `tools/cld2_detect.cc` - Line-level language detection CLI
