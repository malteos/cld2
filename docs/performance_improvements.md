# CLD2 Performance Improvement Opportunities

Analysis of the CLD2 C++ source code for optimization potential.
Baseline benchmark: **0.262ms mean / 0.148ms median per page** (1000 HTML pages, ~80MB total).

---

## Priority 1: High Impact, Low Effort

### 1.1 Build Flags (10-20% gain)

`internal/compile.sh` lines 17-28 warn that no optimization flags are set but does not default to any.
CLD2 does not use exceptions or RTTI.

```bash
CXXFLAGS="-O3 -march=native -flto -fno-exceptions -fno-rtti \
          -ffunction-sections -fdata-sections -Wl,--gc-sections"
```

### 1.2 Reuse Prediction Table via Thread-Local Storage (~50% faster squeeze path)

`compact_lang_det_impl.cc` lines 795-796, 879-880, 959-960 allocate and zero a 16KB array (`new int[kPredictionTableSize]`) on every call to `CheapSqueezeInplace()`, `CheapSqueezeInplaceOverwrite()`, and `CheapSqueezeTriggerTest()`, then immediately delete it.

**Fix:** Use a `thread_local static int predict_tbl[kPredictionTableSize]` with lazy clear.

### 1.3 Expand Quadgram Repetition Cache (5-15% fewer lookups on repetitive text)

`cldutil.cc` lines 334-335: only a 2-entry round-robin cache filters duplicate quadgram hashes.

```cpp
uint32 prior_quadhash[2] = {0, 0};  // Too small
```

HTML boilerplate and repeated patterns easily defeat this. Same issue for octagram cache at lines 439-440.

**Fix:** Expand to 8-16 entry cache or use a small Bloom filter for O(1) membership testing.

### 1.4 HTML Entity Lookup Without memcpy (up to 30% faster entity processing)

`getonescriptspan.cc` lines 290-301: `LookupEntity()` copies entity bytes to a temp buffer before binary search on every `&entity;` occurrence.

```cpp
char temp[16];
memcpy(temp, entity_name, entity_len);  // Unnecessary copy
temp[entity_len] = '\0';
int match = BinarySearch(temp, ...);
```

**Fix:** Use length-aware comparison in `BinarySearch` to avoid the copy.

---

## Priority 2: High Impact, Medium Effort

### 2.1 Eliminate ScoringHitBuffer Reallocation (~30% faster on large documents)

`scoreonescriptspan.cc` lines 1175-1176, 1236-1237: `new ScoringHitBuffer` is called inside the scoring loop. This structure contains vectors for quadgram, octagram, and bigram hits.

**Fix:** Allocate once per detection call and reuse via `.clear()` across script spans.

### 2.2 Keep Running Top-3 in Tote (~15% faster scoring)

`tote.cc` lines 65-99: `CurrentTopThreeKeys()` does a full linear scan over 64 groups with branch-heavy insertion sort after all scoring is complete.

**Fix:** Maintain a running top-3 heap during `Tote::Add()` calls, eliminating the final O(n) pass.

### 2.3 Separate CJK/Non-CJK Loop Paths (15-20% branch prediction improvement)

`cldutil.cc` lines 163-195 (`DoBigramScoreV3`): a single loop handles both CJK and non-CJK characters with an unpredictable branch on character length.

```cpp
if ((kMinCJKUTF8CharBytes * 2) <= len2) {  // Unpredictable
```

**Fix:** Split into two specialized loops: one for CJK-dominant spans, one for Latin/Cyrillic.

### 2.4 SIMD Tag Scanning (5-10% on HTML input)

`getonescriptspan.cc` lines 503-542: `ScanToPossibleLetter()` processes one byte at a time through a 800-entry state machine to skip HTML tags.

**Fix:** Use `memchr` or SSE/NEON vectorized scan to locate `<` and `>` in bulk, then fall back to the state machine only for edge cases.

### 2.5 Bulk UTF-8 Validation (5-8% gain)

`utf8statetable.cc` lines 179-228: per-character state machine lookup for UTF-8 property detection. `getonescriptspan.cc` line 887 calls `UTF8OneCharLen()` on every letter, and line 897 calls `GetUTF8LetterScriptNum()`.

**Fix:** Validate the entire input buffer once with a SIMD UTF-8 checker (e.g., `simdjson`-style), then skip per-character validation during scoring.

---

## Priority 3: Medium Impact, Medium-High Effort

### 3.1 Cache-Line Aware Hit Processing (~20% faster on large text)

`scoreonescriptspan.cc` lines 1256-1262: `GetQuadHits()` produces a hit vector with offsets scattered through the text. `ProcessHitBuffer()` iterates in offset order, causing cache misses on documents >40KB.

**Fix:** Sort hits by 64-byte cache-line chunks before processing.

### 3.2 Fuse Text Preprocessing with Scoring (15-25% gain, hardest change)

`compact_lang_det_impl.cc` line 1848: the current pipeline is strictly sequential:

```
GetOneScriptSpanLower() → store in buffer → ScoreOneScriptSpan()
```

Data flows through 3 passes: entity expansion, lowercasing, scoring — each touching the same memory.

**Fix:** Implement a streaming n-gram extractor that scores during text processing, eliminating intermediate `script_buffer_` copies and reducing memory bandwidth by 3x.

### 3.3 Reduce Double Buffer Overhead

`getonescriptspan.cc` lines 555-556: two heap buffers per `ScriptScanner` instance:

```cpp
script_buffer_       = new char[40960];   // 40 KB
script_buffer_lower_ = new char[61440];   // 60 KB
```

~100 KB per instance with data copied twice (original → buffer → lowered buffer).

**Fix:** Use single buffer with in-place lowercasing, or pre-allocate on thread-local storage.

### 3.4 Make OffsetMap Lazy

`offsetmap.cc`: `OffsetMap` tracks byte-level offset mapping using a `std::string diffs_` that grows with every Insert/Delete/Copy operation. Two maps are maintained per span (`map2original_`, `map2uplow_`).

**Fix:** Only build the offset map when the caller actually requests result chunk positions. Most callers only need the top language, not byte-level spans.

### 3.5 Dual-Table Single-Pass Lookup (~10% on weak matches)

`cldutil.cc` lines 356-362: on a primary table miss, a second table is consulted:

```cpp
probs = QuadHashV3Lookup4(quadgram_obj, quadhash);
if ((probs == 0) && (quadgram_obj2->kCLDTableSize != 0)) {
    probs = QuadHashV3Lookup4(quadgram_obj2, quadhash);  // 2nd cache miss
}
```

**Fix:** Merge tables or interleave buckets to check both in a single cache-line load.

---

## Priority 4: Low Impact / Incremental

### 4.1 Inline UTF8OneCharLen in Tight Loops

`cldutil.cc` line 515: function call overhead inside the `GetOctaHits` character loop. The lookup table `kAdvanceOneChar` already exists.

### 4.2 Reduce Probability Table Indirection

`cldutil.cc` line 130: `LgProb2TblEntry(prob123)` → `&kLgProbV2Tbl[i * 8]` is called for every gram hit. Cache the entry pointer across consecutive lookups with the same probability index.

### 4.3 Increase DistinctOcta Table Size

Currently 8K buckets at 93% fill — high collision rate. Doubling to 16K buckets (+0.12 MB) would reduce collision-related extra comparisons by 10-20%.

### 4.4 Pre-reserve ResultChunkVector

`compact_lang_det_impl.cc` lines 1141-1147: `resultchunkvector->resize(k)` may trigger reallocation. Reserve capacity upfront based on document size estimate.

---

## Summary

| # | Optimization | Est. Impact | Effort | Priority |
|---|---|---|---|---|
| 1.1 | Compiler flags (-O3, LTO, -march=native) | 10-20% | Trivial | **P1** |
| 1.2 | Thread-local prediction table | ~50% squeeze | Low | **P1** |
| 1.3 | Expand repetition cache (2 → 16 entries) | 5-15% | Low | **P1** |
| 1.4 | Entity lookup without memcpy | ~30% entity | Low | **P1** |
| 2.1 | Reuse ScoringHitBuffer | ~30% large docs | Medium | **P2** |
| 2.2 | Running top-3 in Tote | ~15% scoring | Medium | **P2** |
| 2.3 | Split CJK/non-CJK loops | 15-20% branch | Medium | **P2** |
| 2.4 | SIMD tag scanning | 5-10% HTML | Medium | **P2** |
| 2.5 | Bulk UTF-8 validation | 5-8% | Medium | **P2** |
| 3.1 | Cache-line aware hits | ~20% large text | Medium-High | **P3** |
| 3.2 | Fuse preprocessing + scoring | 15-25% | High | **P3** |
| 3.3 | Single-buffer lowercasing | Memory + 3-5% | Medium | **P3** |
| 3.4 | Lazy OffsetMap | 2-4% | Medium | **P3** |
| 3.5 | Merge dual lookup tables | ~10% weak match | Medium | **P3** |

**Combined estimated improvement: 2-4x faster on typical HTML documents** when applying P1+P2 optimizations.
