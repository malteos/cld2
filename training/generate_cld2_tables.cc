// Copyright 2026. Apache 2.0 licensed, like the rest of CLD2.
//
// generate_cld2_tables: reverse-engineered replacement for Google's
// unreleased "postproc-cld2" table generator.
//
// Reads training samples (one per line: <language-code> TAB <utf8 text>)
// and emits a generated C++ file containing drop-in replacements for the
// four non-CJK scoring tables that CLD2 links against:
//
//   kQuad_obj / kQuad_obj2   - primary quadgram lookup table
//   kDeltaOcta_obj           - word-based delta table   (emitted empty)
//   kDistinctOcta_obj        - distinctive-word table
//   kAvgDeltaOctaScore[]     - expected score per 1KB, for reliability
//
// The emitted file replaces these files in the build:
//   internal/cld2_generated_quadchrome_2.cc
//   internal/cld2_generated_deltaoctachrome.cc
//   internal/cld2_generated_distinctoctachrome.cc
//   internal/cld_generated_score_quad_octa_2.cc
//
// Compatibility with the runtime is achieved by reusing CLD2's own code
// for every step that must match bit-for-bit:
//   - text normalization:  ScriptScanner::GetOneScriptSpanLower
//                          (tag/entity stripping, single-script spans,
//                           non-letters -> single space, lowercasing)
//   - quadgram traversal:  the exact loop from GetQuadHits in cldutil.cc,
//                          including the vowel-skip sampling and the
//                          2-entry repeat filter
//   - word traversal:      the exact loop from GetOctaHits in cldutil.cc
//                          (words truncated to 8 chars)
//   - hashing:             QuadHashV2 / OctaHash40 (cldutil_shared.cc)
//   - bucket placement:    QuadFPJustHash / OctaFPJustHash
//   - probability packing: ProbPackV2 / FindBestProb3Match
//                          (cldutil_offline.cc) into kLgProbV2Tbl entries
//
// Only RTypeMany scripts (Latin, Cyrillic, Arabic, Hebrew, Devanagari,
// Bengali, Tibetan, Ethiopic, ...) are trainable: RTypeOne scripts are
// recognized structurally (script => language) and never consult these
// tables, and the CJK (Hani) path uses separate unigram/bigram tables
// that this tool does not regenerate.

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>

#include "cld2tablesummary.h"
#include "cldutil_shared.h"
#include "cldutil_offline.h"
#include "getonescriptspan.h"
#include "lang_script.h"
#include "langspan.h"
#include "utf8statetable.h"

using namespace CLD2;

// Local copy of GetLangScore (cldutil.cc defines it, but that file cannot
// be linked together with cldutil_offline.cc: both define ProcessProbV2Tote).
static int LangScoreOf(uint32 probs, uint8 pslang) {
  uint8 prob123 = (probs >> 0) & 0xff;
  const uint8* prob123_entry = LgProb2TblEntry(prob123);
  uint8 top1 = (probs >> 8) & 0xff;
  int retval = 0;
  if (top1 == pslang) {retval += LgProb3(prob123_entry, 0);}
  uint8 top2 = (probs >> 16) & 0xff;
  if (top2 == pslang) {retval += LgProb3(prob123_entry, 1);}
  uint8 top3 = (probs >> 24) & 0xff;
  if (top3 == pslang) {retval += LgProb3(prob123_entry, 2);}
  return retval;
}

// ---------------------------------------------------------------------------
// Options
// ---------------------------------------------------------------------------
struct Options {
  std::vector<std::string> inputs;
  std::string out_file = "cld2_generated_trained.cc";
  std::string table_name = "Trained";
  int min_count = 2;              // Drop ngrams seen fewer times than this
  int max_langs = 3;              // Max languages kept per table entry (<=6)
  int pref_log2 = -9;             // P(quad|lang)=2^pref_log2 maps to qprob 12
  uint32 quad_keymask = 0xffff0000u;
  uint32 octa_keymask = 0xfffff000u;
  int quad_buckets = 0;           // 0 = auto size
  int octa_buckets = 0;           // 0 = auto size
  int distinct_min_count = 4;     // Min word count to be a distinct word
  double distinct_min_share = 0.90;
  long max_bytes_per_lang = 0;    // 0 = unlimited
  bool verbose = false;
};

// lkey identifies a per-script language slot: (space<<8)|plang where
// space 0 = the Latn per-script number space, 1 = the Othr space.
static inline int MakeLkey(ULScript ulscript, uint8 plang) {
  return ((ulscript == ULScript_Latin) ? 0 : 0x100) | plang;
}

struct LangCount {
  uint16 lkey;
  uint32 count;
};

// One candidate table entry after collision-merging: all languages that
// produced this (bucket, hashkey) pair, with raw counts.
struct Candidate {
  uint32 subscr;         // bucket number
  uint32 hashkey;        // masked key bits
  uint64 weight;         // total raw count, for allocation priority
  std::vector<LangCount> langs;
};

typedef std::unordered_map<uint64, uint32> CountMap;   // (hash<<9|lkey) -> n

// ---------------------------------------------------------------------------
// Corpus reading and gram counting (mirrors GetQuadHits / GetOctaHits)
// ---------------------------------------------------------------------------

struct CorpusStats {
  CountMap quad_counts;                 // key: quadhash<<9 | lkey
  std::unordered_map<uint64, uint32> word_counts;  // wordhash40<<9 | lkey
  std::map<int, uint64> quad_totals;    // lkey -> total quads
  std::map<int, uint64> word_totals;    // lkey -> total words
  std::map<int, uint64> lang_bytes;     // lkey -> total span bytes
  std::set<std::pair<Language, ULScript> > langscripts_seen;
  std::map<Language, long> bytes_per_lang;
  long lines = 0, skipped_lines = 0;
  std::set<std::string> bad_codes;
  std::set<std::pair<Language, ULScript> > untrainable;
};

// Walk one lowercased script span and count quadgrams, replicating the
// traversal in GetQuadHits (cldutil.cc) exactly.
static void CountQuads(const LangSpan& span, int lkey, CorpusStats* stats) {
  const char* src = span.text;
  const char* srclimit = src + span.text_bytes;
  int next_prior = 0;
  uint32 prior_quadhash[2] = {0, 0};

  if (src[0] == ' ') {++src;}
  while (src < srclimit) {
    const char* src_end = src;
    src_end += kAdvanceOneCharButSpace[(uint8)src_end[0]];
    src_end += kAdvanceOneCharButSpace[(uint8)src_end[0]];
    const char* src_mid = src_end;
    src_end += kAdvanceOneCharButSpace[(uint8)src_end[0]];
    src_end += kAdvanceOneCharButSpace[(uint8)src_end[0]];
    int len = src_end - src;
    uint32 quadhash = QuadHashV2(src, len);

    if ((quadhash != prior_quadhash[0]) && (quadhash != prior_quadhash[1])) {
      prior_quadhash[next_prior] = quadhash;
      next_prior = (next_prior + 1) & 1;
      uint64 key = (static_cast<uint64>(quadhash) << 9) | lkey;
      ++stats->quad_counts[key];
      ++stats->quad_totals[lkey];
    }

    if (src_end[0] == ' ') {
      src = src_end;
    } else {
      src = src_mid;
    }
    if (src < srclimit) {
      src += kAdvanceOneCharSpaceVowel[(uint8)src[0]];
    } else {
      src = srclimit;
    }
  }
}

// Walk one lowercased script span and count words truncated to 8 chars,
// replicating the traversal in GetOctaHits (cldutil.cc) exactly.
static void CountWords(const LangSpan& span, int lkey, CorpusStats* stats) {
  const char* src = span.text;
  // GetOctaHits scans to letter_limit+1 to see the trailing space
  const char* srclimit = src + span.text_bytes + 1;

  int next_prior = 0;
  uint64 prior_octahash[2] = {0, 0};
  int charcount = 0;
  if (src[0] == ' ') {++src;}

  const char* word_start = src;
  const char* word_end = word_start;
  while (src < srclimit) {
    if (src[0] == ' ') {
      int len = word_end - word_start;
      if (len > 0) {
        uint64 wordhash40 = OctaHash40(word_start, len);
        // Same repeat filter as the runtime: update even without a hit
        if ((wordhash40 != prior_octahash[0]) &&
            (wordhash40 != prior_octahash[1])) {
          prior_octahash[next_prior] = wordhash40;
          next_prior = 1 - next_prior;
          uint64 key = (wordhash40 << 9) | lkey;
          ++stats->word_counts[key];
          ++stats->word_totals[lkey];
        }
      }
      charcount = 0;
      word_start = src + 1;   // Over the space
      word_end = word_start;
    } else {
      ++charcount;
    }
    src += UTF8OneCharLen(src);
    if (charcount <= 8) {word_end = src;}
  }
}

static void ReadCorpus(const Options& opt, CorpusStats* stats) {
  std::string line;
  for (size_t f = 0; f < opt.inputs.size(); ++f) {
    FILE* fp = fopen(opt.inputs[f].c_str(), "rb");
    if (fp == NULL) {
      fprintf(stderr, "error: cannot open %s\n", opt.inputs[f].c_str());
      exit(1);
    }
    char* buf = NULL;
    size_t bufcap = 0;
    ssize_t n;
    while ((n = getline(&buf, &bufcap, fp)) >= 0) {
      if (n > 0 && buf[n - 1] == '\n') {buf[--n] = '\0';}
      if (n == 0) {continue;}
      char* tab = strchr(buf, '\t');
      if (tab == NULL) {++stats->skipped_lines; continue;}
      *tab = '\0';
      const char* code = buf;
      const char* text = tab + 1;
      int text_len = n - (tab + 1 - buf);
      if (text_len <= 0) {++stats->skipped_lines; continue;}

      Language lang = GetLanguageFromName(code);
      if (lang == UNKNOWN_LANGUAGE) {
        if (stats->bad_codes.insert(code).second) {
          fprintf(stderr, "warning: unknown language code '%s'"
                  " (register it first); skipping its lines\n", code);
        }
        ++stats->skipped_lines;
        continue;
      }
      if (opt.max_bytes_per_lang > 0 &&
          stats->bytes_per_lang[lang] >= opt.max_bytes_per_lang) {
        continue;
      }
      stats->bytes_per_lang[lang] += text_len;
      ++stats->lines;

      ScriptScanner ss(text, text_len, /*is_plain_text=*/true);
      LangSpan span;
      while (ss.GetOneScriptSpanLower(&span)) {
        ULScriptRType rtype = ULScriptRecognitionType(span.ulscript);
        if (rtype != RTypeMany) {
          if (rtype != RTypeNone) {
            stats->untrainable.insert(std::make_pair(lang, span.ulscript));
          }
          continue;
        }
        uint8 plang = PerScriptNumber(span.ulscript, lang);
        if (plang == 0) {
          stats->untrainable.insert(std::make_pair(lang, span.ulscript));
          continue;
        }
        int lkey = MakeLkey(span.ulscript, plang);
        stats->langscripts_seen.insert(std::make_pair(lang, span.ulscript));
        stats->lang_bytes[lkey] += span.text_bytes;
        CountQuads(span, lkey, stats);
        CountWords(span, lkey, stats);
      }
    }
    free(buf);
    fclose(fp);
  }
}

// ---------------------------------------------------------------------------
// Quantization
// ---------------------------------------------------------------------------

// Convert a per-language relative frequency into CLD2's quantized log2
// probability 1..12 (0 = drop). 2^pref_log2 (default 1/512) maps to 12.
static int QuantizeProb(double p, int pref_log2) {
  if (p <= 0.0) {return 0;}
  int q = static_cast<int>(lround(12.0 + (log2(p) - pref_log2)));
  if (q > 12) {q = 12;}
  return (q < 1) ? 0 : q;
}

struct PackedEntry {
  uint32 word0 = 0;
  uint32 word1 = 0;   // Only for 4..6-language entries
  bool is_double = false;
};

// Turn a candidate's language counts into 1 or 2 packed langprob words.
// Returns false if no language survives quantization.
static bool PackCandidate(const Candidate& cand,
                          const std::map<int, uint64>& totals,
                          const Options& opt,
                          PackedEntry* out) {
  // Merge per plang byte (two scripts' number spaces can map to the same
  // byte only via rare cross-script hash collisions; keep the best qprob).
  struct LQ { uint8 plang; int qprob; uint64 count; };
  std::map<uint8, LQ> merged;
  for (size_t i = 0; i < cand.langs.size(); ++i) {
    const LangCount& lc = cand.langs[i];
    uint64 total = totals.at(lc.lkey);
    double p = static_cast<double>(lc.count) / static_cast<double>(total);
    int q = QuantizeProb(p, opt.pref_log2);
    if (q == 0) {continue;}
    uint8 plang = lc.lkey & 0xff;
    LQ& slot = merged[plang];
    if (slot.count == 0 || q > slot.qprob) {
      slot.plang = plang;
      slot.qprob = q;
    }
    slot.count += lc.count;
  }
  if (merged.empty()) {return false;}

  std::vector<LQ> ordered;
  for (std::map<uint8, LQ>::iterator it = merged.begin(); it != merged.end();
       ++it) {
    ordered.push_back(it->second);
  }
  std::sort(ordered.begin(), ordered.end(), [](const LQ& a, const LQ& b) {
    if (a.qprob != b.qprob) {return a.qprob > b.qprob;}
    if (a.count != b.count) {return a.count > b.count;}
    return a.plang < b.plang;
  });
  int keep = std::min(static_cast<int>(ordered.size()), opt.max_langs);

  uint8 plang3[3] = {0, 0, 0};
  uint8 prob3[3] = {0, 0, 0};
  for (int i = 0; i < std::min(keep, 3); ++i) {
    plang3[i] = ordered[i].plang;
    prob3[i] = static_cast<uint8>(ordered[i].qprob);
  }
  out->word0 = ProbPackV2(plang3, prob3);
  out->is_double = (keep > 3);
  if (out->is_double) {
    uint8 plang3b[3] = {0, 0, 0};
    uint8 prob3b[3] = {0, 0, 0};
    for (int i = 3; i < keep; ++i) {
      plang3b[i - 3] = ordered[i].plang;
      prob3b[i - 3] = static_cast<uint8>(ordered[i].qprob);
    }
    out->word1 = ProbPackV2(plang3b, prob3b);
  }
  return true;
}

// ---------------------------------------------------------------------------
// Table assembly
// ---------------------------------------------------------------------------

struct BuiltTable {
  std::vector<IndirectProbBucket4> buckets;
  std::vector<uint32> ind;
  uint32 size_one = 0;
  uint32 keymask = 0;
  long offered = 0, filled = 0, merged = 0, dropped = 0, ind_full_drops = 0;
};

static int NextPow2(long x) {
  int p = 1;
  while (p < x && p < (1 << 30)) {p <<= 1;}
  return p;
}

// Common builder for quad and octa tables. hash40 says whether bucket/key
// placement uses OctaFPJustHash (40-bit fingerprints) or QuadFPJustHash.
static void BuildTable(std::vector<std::pair<uint64, std::vector<LangCount> > >&
                           grams,   // (fingerprint, langcounts), modified
                       const std::map<int, uint64>& totals,
                       const Options& opt, uint32 keymask, int bucket_override,
                       bool hash40, BuiltTable* out) {
  // Choose bucket count: ~60% fill of 4-way capacity, like the originals.
  int nbuckets = bucket_override;
  if (nbuckets == 0) {
    nbuckets = NextPow2(std::max(256L, static_cast<long>(grams.size() / 2.4)));
  }

  // Group colliding fingerprints: entries with identical (bucket, hashkey)
  // are indistinguishable at lookup time, so merge their counts.
  std::unordered_map<uint64, Candidate> cands;
  cands.reserve(grams.size());
  for (size_t i = 0; i < grams.size(); ++i) {
    uint32 subscr, hashkey;
    if (hash40) {
      OctaFPJustHash(grams[i].first, keymask, nbuckets, &subscr, &hashkey);
    } else {
      QuadFPJustHash(static_cast<uint32>(grams[i].first), keymask, nbuckets,
                     &subscr, &hashkey);
    }
    uint64 gkey = (static_cast<uint64>(subscr) << 32) | hashkey;
    Candidate& c = cands[gkey];
    if (c.langs.empty()) {
      c.subscr = subscr;
      c.hashkey = hashkey;
    } else {
      ++out->merged;
    }
    for (size_t j = 0; j < grams[i].second.size(); ++j) {
      const LangCount& lc = grams[i].second[j];
      c.weight += lc.count;
      bool found = false;
      for (size_t k = 0; k < c.langs.size(); ++k) {
        if (c.langs[k].lkey == lc.lkey) {
          c.langs[k].count += lc.count;
          found = true;
          break;
        }
      }
      if (!found) {c.langs.push_back(lc);}
    }
  }
  out->offered = cands.size();

  // Per bucket, keep the 4 highest-weight candidates (freq allocation).
  std::vector<std::vector<Candidate*> > per_bucket(nbuckets);
  for (std::unordered_map<uint64, Candidate>::iterator it = cands.begin();
       it != cands.end(); ++it) {
    per_bucket[it->second.subscr].push_back(&it->second);
  }

  // Pack all kept candidates, then build the indirect pool: singles first
  // (subscripts < size_one address one langprob word), then doubles
  // (stored subscript s >= size_one addresses ind[2s - size_one]).
  struct Kept {
    uint32 subscr;
    uint32 hashkey;
    uint64 weight;
    PackedEntry packed;
  };
  std::vector<Kept> kept;
  for (int b = 0; b < nbuckets; ++b) {
    std::vector<Candidate*>& v = per_bucket[b];
    std::sort(v.begin(), v.end(), [](const Candidate* a, const Candidate* b2) {
      return a->weight > b2->weight;
    });
    for (size_t i = 0; i < v.size(); ++i) {
      if (i >= 4) {++out->dropped; continue;}
      PackedEntry pe;
      if (!PackCandidate(*v[i], totals, opt, &pe)) {continue;}
      Kept k;
      k.subscr = v[i]->subscr;
      k.hashkey = v[i]->hashkey;
      k.weight = v[i]->weight;
      k.packed = pe;
      kept.push_back(k);
    }
  }

  // Deduplicate langprob words; highest-weight entries claim pool space
  // first so that overflow drops the rarest ngrams.
  std::sort(kept.begin(), kept.end(), [](const Kept& a, const Kept& b) {
    return a.weight > b.weight;
  });
  std::map<uint32, uint32> single_ix;                    // word -> subscript
  std::map<std::pair<uint32, uint32>, uint32> double_ix; // words -> subscript
  std::vector<uint32> singles;   // singles[0] is the reserved 0 entry
  singles.push_back(0);
  std::vector<std::pair<uint32, uint32> > doubles;
  const uint32 max_subscr = ~keymask;   // Largest storable subscript

  struct Placed { uint32 subscr; uint32 hashkey; bool is_double; uint32 pool; };
  std::vector<Placed> placed;
  for (size_t i = 0; i < kept.size(); ++i) {
    const Kept& k = kept[i];
    if (!k.packed.is_double) {
      std::map<uint32, uint32>::iterator it = single_ix.find(k.packed.word0);
      uint32 ix;
      if (it != single_ix.end()) {
        ix = it->second;
      } else {
        ix = singles.size();
        singles.push_back(k.packed.word0);
        single_ix[k.packed.word0] = ix;
      }
      placed.push_back({k.subscr, k.hashkey, false, ix});
    } else {
      std::pair<uint32, uint32> pr(k.packed.word0, k.packed.word1);
      std::map<std::pair<uint32, uint32>, uint32>::iterator it =
          double_ix.find(pr);
      uint32 ix;
      if (it != double_ix.end()) {
        ix = it->second;
      } else {
        ix = doubles.size();
        doubles.push_back(pr);
        double_ix[pr] = ix;
      }
      placed.push_back({k.subscr, k.hashkey, true, ix});
    }
  }

  // The pool must fit in the subscript bits: size_one + ndoubles <= max.
  uint32 size_one = singles.size();
  while (size_one + doubles.size() > max_subscr) {
    // Overflow: drop lowest-weight placed entries until it fits. Rebuild
    // is simple and rare; corpora that trip this need a wider ~keymask.
    ++out->ind_full_drops;
    placed.pop_back();
    // Recompute pools from scratch (cheap relative to corpus pass).
    single_ix.clear(); double_ix.clear();
    singles.clear(); singles.push_back(0);
    doubles.clear();
    for (size_t i = 0; i < placed.size(); ++i) {
      const Kept& k = kept[i];
      Placed& p = placed[i];
      if (!p.is_double) {
        std::map<uint32, uint32>::iterator it = single_ix.find(k.packed.word0);
        if (it != single_ix.end()) {p.pool = it->second;}
        else {
          p.pool = singles.size();
          singles.push_back(k.packed.word0);
          single_ix[k.packed.word0] = p.pool;
        }
      } else {
        std::pair<uint32, uint32> pr(k.packed.word0, k.packed.word1);
        std::map<std::pair<uint32, uint32>, uint32>::iterator it =
            double_ix.find(pr);
        if (it != double_ix.end()) {p.pool = it->second;}
        else {
          p.pool = doubles.size();
          doubles.push_back(pr);
          double_ix[pr] = p.pool;
        }
      }
    }
    size_one = singles.size();
  }

  // Materialize buckets and indirect pool.
  out->buckets.assign(nbuckets, IndirectProbBucket4());
  for (int b = 0; b < nbuckets; ++b) {
    for (int s = 0; s < 4; ++s) {out->buckets[b].keyvalue[s] = 0;}
  }
  std::vector<int> slots_used(nbuckets, 0);
  for (size_t i = 0; i < placed.size(); ++i) {
    const Placed& p = placed[i];
    uint32 stored = p.is_double ? (size_one + p.pool) : p.pool;
    int s = slots_used[p.subscr]++;
    out->buckets[p.subscr].keyvalue[s] = p.hashkey | stored;
    ++out->filled;
  }

  out->ind.assign(singles.begin(), singles.end());
  for (size_t d = 0; d < doubles.size(); ++d) {
    out->ind.push_back(doubles[d].first);
    out->ind.push_back(doubles[d].second);
  }
  out->size_one = size_one;
  out->keymask = keymask;
}

// ---------------------------------------------------------------------------
// Expected-score calibration
// ---------------------------------------------------------------------------

// Look up qprob credited to plang for one quadgram in the built table,
// mirroring the runtime lookup + GetLangScore.
static int TableLangScore(const BuiltTable& t, uint32 hash, bool hash40,
                          uint8 plang) {
  uint32 subscr, hashkey;
  if (hash40) {
    // Callers pass full 40-bit hash via SumScoreOcta below instead.
    return 0;
  }
  QuadFPJustHash(hash, t.keymask, t.buckets.size(), &subscr, &hashkey);
  const IndirectProbBucket4& b = t.buckets[subscr];
  uint32 probs = 0;
  for (int i = 0; i < 4; ++i) {
    if (((hashkey ^ b.keyvalue[i]) & t.keymask) == 0 && b.keyvalue[i] != 0) {
      probs = b.keyvalue[i];
      break;
    }
  }
  if (probs == 0) {return 0;}
  uint32 ix = probs & ~t.keymask;
  int score = 0;
  if (ix < t.size_one) {
    score = LangScoreOf(t.ind[ix], plang);
  } else {
    uint32 real = ix + (ix - t.size_one);
    score = LangScoreOf(t.ind[real], plang);
    score += LangScoreOf(t.ind[real + 1], plang);
  }
  return score;
}

static int OctaTableLangScore(const BuiltTable& t, uint64 hash, uint8 plang) {
  if (t.buckets.size() <= 1) {return 0;}
  uint32 subscr, hashkey;
  OctaFPJustHash(hash, t.keymask, t.buckets.size(), &subscr, &hashkey);
  const IndirectProbBucket4& b = t.buckets[subscr];
  uint32 probs = 0;
  for (int i = 0; i < 4; ++i) {
    if (((hashkey ^ b.keyvalue[i]) & t.keymask) == 0 && b.keyvalue[i] != 0) {
      probs = b.keyvalue[i];
      break;
    }
  }
  if (probs == 0) {return 0;}
  uint32 ix = probs & ~t.keymask;
  if (ix < t.size_one) {return LangScoreOf(t.ind[ix], plang);}
  uint32 real = ix + (ix - t.size_one);
  return LangScoreOf(t.ind[real], plang) +
         LangScoreOf(t.ind[real + 1], plang);
}

struct Calibration {
  // (Language, script4) -> {score_sum, byte_sum}
  std::map<std::pair<int, int>, std::pair<uint64, uint64> > acc;
};

static int LScript4Of(ULScript ulscript) {
  if (ulscript == ULScript_Latin) {return 0;}
  if (ulscript == ULScript_Cyrillic) {return 1;}
  if (ulscript == ULScript_Arabic) {return 2;}
  return 3;
}

// Second pass over the corpus: with the freshly built tables, accumulate
// the score the true language earns per span, to fill kAvgDeltaOctaScore.
static void CalibrateExpectedScore(const Options& opt, const BuiltTable& quad,
                                   const BuiltTable& distinct,
                                   Calibration* cal) {
  for (size_t f = 0; f < opt.inputs.size(); ++f) {
    FILE* fp = fopen(opt.inputs[f].c_str(), "rb");
    if (fp == NULL) {continue;}
    char* buf = NULL;
    size_t bufcap = 0;
    ssize_t n;
    std::map<Language, long> bytes_per_lang;
    while ((n = getline(&buf, &bufcap, fp)) >= 0) {
      if (n > 0 && buf[n - 1] == '\n') {buf[--n] = '\0';}
      char* tab = strchr(buf, '\t');
      if (tab == NULL) {continue;}
      *tab = '\0';
      const char* text = tab + 1;
      int text_len = n - (tab + 1 - buf);
      if (text_len <= 0) {continue;}
      Language lang = GetLanguageFromName(buf);
      if (lang == UNKNOWN_LANGUAGE) {continue;}
      if (opt.max_bytes_per_lang > 0 &&
          bytes_per_lang[lang] >= opt.max_bytes_per_lang) {continue;}
      bytes_per_lang[lang] += text_len;

      ScriptScanner ss(text, text_len, true);
      LangSpan span;
      while (ss.GetOneScriptSpanLower(&span)) {
        if (ULScriptRecognitionType(span.ulscript) != RTypeMany) {continue;}
        uint8 plang = PerScriptNumber(span.ulscript, lang);
        if (plang == 0) {continue;}
        uint64 score = 0;

        // Quads, same traversal as CountQuads
        {
          const char* src = span.text;
          const char* srclimit = src + span.text_bytes;
          int next_prior = 0;
          uint32 prior_quadhash[2] = {0, 0};
          if (src[0] == ' ') {++src;}
          while (src < srclimit) {
            const char* src_end = src;
            src_end += kAdvanceOneCharButSpace[(uint8)src_end[0]];
            src_end += kAdvanceOneCharButSpace[(uint8)src_end[0]];
            const char* src_mid = src_end;
            src_end += kAdvanceOneCharButSpace[(uint8)src_end[0]];
            src_end += kAdvanceOneCharButSpace[(uint8)src_end[0]];
            int len = src_end - src;
            uint32 quadhash = QuadHashV2(src, len);
            if ((quadhash != prior_quadhash[0]) &&
                (quadhash != prior_quadhash[1])) {
              prior_quadhash[next_prior] = quadhash;
              next_prior = (next_prior + 1) & 1;
              score += TableLangScore(quad, quadhash, false, plang);
            }
            if (src_end[0] == ' ') {src = src_end;} else {src = src_mid;}
            if (src < srclimit) {
              src += kAdvanceOneCharSpaceVowel[(uint8)src[0]];
            } else {
              src = srclimit;
            }
          }
        }

        // Distinct words
        {
          const char* src = span.text;
          const char* srclimit = src + span.text_bytes + 1;
          int charcount = 0;
          if (src[0] == ' ') {++src;}
          const char* word_start = src;
          const char* word_end = word_start;
          while (src < srclimit) {
            if (src[0] == ' ') {
              int len = word_end - word_start;
              if (len > 0) {
                uint64 h = OctaHash40(word_start, len);
                score += OctaTableLangScore(distinct, h, plang);
              }
              charcount = 0;
              word_start = src + 1;
              word_end = word_start;
            } else {
              ++charcount;
            }
            src += UTF8OneCharLen(src);
            if (charcount <= 8) {word_end = src;}
          }
        }

        std::pair<int, int> key(lang, LScript4Of(span.ulscript));
        cal->acc[key].first += score;
        cal->acc[key].second += span.text_bytes;
      }
    }
    free(buf);
    fclose(fp);
  }
}

// ---------------------------------------------------------------------------
// Emission
// ---------------------------------------------------------------------------

static void EmitBuckets(FILE* out, const char* name,
                        const std::vector<IndirectProbBucket4>& buckets) {
  fprintf(out, "static const IndirectProbBucket4 %s[%zu] = {\n", name,
          buckets.size());
  for (size_t i = 0; i < buckets.size(); ++i) {
    fprintf(out, "  {{0x%08x,0x%08x,0x%08x,0x%08x}},\n",
            buckets[i].keyvalue[0], buckets[i].keyvalue[1],
            buckets[i].keyvalue[2], buckets[i].keyvalue[3]);
  }
  fprintf(out, "};\n\n");
}

static void EmitInd(FILE* out, const char* name,
                    const std::vector<uint32>& ind) {
  fprintf(out, "static const uint32 %s[%zu] = {\n", name, ind.size());
  for (size_t i = 0; i < ind.size(); ++i) {
    if ((i & 7) == 0) {fprintf(out, " ");}
    fprintf(out, " 0x%08x,", ind[i]);
    if ((i & 7) == 7) {fprintf(out, "\n");}
  }
  fprintf(out, "\n};\n\n");
}

static void EmitTable(FILE* out, const std::string& prefix,
                      const BuiltTable& t, uint32 build_date,
                      const std::string& recognized) {
  std::string b = prefix;
  fprintf(out, "static const uint32 %sSize = %zu;\n", b.c_str(),
          t.buckets.size());
  fprintf(out, "static const uint32 %sKeyMask = 0x%08x;\n", b.c_str(),
          t.keymask);
  fprintf(out, "static const uint32 %sBuildDate = %u;\n", b.c_str(),
          build_date);
  fprintf(out, "static const char* const %sRecognizedLangScripts =\n  \"%s\";\n\n",
          b.c_str(), recognized.c_str());
  EmitBuckets(out, (b + "Buckets").c_str(), t.buckets);
  fprintf(out, "static const uint32 %sSizeOne = %u;\n", b.c_str(), t.size_one);
  fprintf(out, "extern const uint32 %sIndSize = %zu;\n", b.c_str(),
          t.ind.size());
  EmitInd(out, (b + "Ind").c_str(), t.ind);
}

static void EmitSummaryObj(FILE* out, const char* obj_name,
                           const std::string& prefix) {
  fprintf(out,
          "extern const CLD2TableSummary %s = {\n"
          "  %sBuckets,\n  %sInd,\n  %sSizeOne,\n  %sSize,\n  %sKeyMask,\n"
          "  %sBuildDate,\n  %sRecognizedLangScripts,\n};\n\n",
          obj_name, prefix.c_str(), prefix.c_str(), prefix.c_str(),
          prefix.c_str(), prefix.c_str(), prefix.c_str(), prefix.c_str());
}

static void EmitEmptyTable(FILE* out, const std::string& prefix,
                           const char* obj_name, uint32 build_date) {
  fprintf(out,
          "static const uint32 %sSize = 1;\n"
          "static const uint32 %sKeyMask = 0xffffffff;\n"
          "static const uint32 %sBuildDate = %u;\n"
          "static const char* const %sRecognizedLangScripts = \"\";\n"
          "static const IndirectProbBucket4 %sBuckets[1] = {\n"
          "  {{0x00000000,0x00000000,0x00000000,0x00000000}},\n};\n"
          "static const uint32 %sSizeOne = 1;\n"
          "extern const uint32 %sIndSize = 1;\n"
          "static const uint32 %sInd[1] = {0x00000000,};\n\n",
          prefix.c_str(), prefix.c_str(), prefix.c_str(), build_date,
          prefix.c_str(), prefix.c_str(), prefix.c_str(), prefix.c_str(),
          prefix.c_str());
  EmitSummaryObj(out, obj_name, prefix);
}

int main(int argc, char** argv) {
  Options opt;
  for (int i = 1; i < argc; ++i) {
    std::string a = argv[i];
    auto next = [&](const char* what) -> const char* {
      if (i + 1 >= argc) {
        fprintf(stderr, "error: %s needs a value\n", what);
        exit(1);
      }
      return argv[++i];
    };
    if (a == "--in") {opt.inputs.push_back(next("--in"));}
    else if (a == "--out") {opt.out_file = next("--out");}
    else if (a == "--table_name") {opt.table_name = next("--table_name");}
    else if (a == "--min_count") {opt.min_count = atoi(next(a.c_str()));}
    else if (a == "--max_langs") {opt.max_langs = atoi(next(a.c_str()));}
    else if (a == "--pref_log2") {opt.pref_log2 = atoi(next(a.c_str()));}
    else if (a == "--quad_buckets") {opt.quad_buckets = atoi(next(a.c_str()));}
    else if (a == "--octa_buckets") {opt.octa_buckets = atoi(next(a.c_str()));}
    else if (a == "--distinct_min_count") {
      opt.distinct_min_count = atoi(next(a.c_str()));
    }
    else if (a == "--distinct_min_share") {
      opt.distinct_min_share = atof(next(a.c_str()));
    }
    else if (a == "--max_bytes_per_lang") {
      opt.max_bytes_per_lang = atol(next(a.c_str()));
    }
    else if (a == "--verbose") {opt.verbose = true;}
    else {
      fprintf(stderr, "usage: %s --in train.tsv [--in more.tsv]"
              " [--out file.cc] [--min_count N] [--max_langs 3|6]"
              " [--pref_log2 -9] [--quad_buckets N] [--octa_buckets N]"
              " [--distinct_min_count N] [--distinct_min_share 0.9]"
              " [--max_bytes_per_lang N] [--verbose]\n", argv[0]);
      exit(1);
    }
  }
  if (opt.inputs.empty()) {
    fprintf(stderr, "error: at least one --in file required\n");
    exit(1);
  }
  if (opt.max_langs < 1) {opt.max_langs = 1;}
  if (opt.max_langs > 6) {opt.max_langs = 6;}

  fprintf(stderr, "Pass 1: counting ngrams...\n");
  CorpusStats stats;
  ReadCorpus(opt, &stats);
  fprintf(stderr, "  %ld lines used, %ld skipped\n", stats.lines,
          stats.skipped_lines);
  for (std::set<std::pair<Language, ULScript> >::iterator it =
           stats.untrainable.begin(); it != stats.untrainable.end(); ++it) {
    fprintf(stderr, "warning: cannot train %s in script %s "
            "(script is not RTypeMany, or language has no per-script number "
            "for it)\n",
            LanguageCode(it->first), ULScriptCode(it->second));
  }
  for (std::map<Language, long>::iterator it = stats.bytes_per_lang.begin();
       it != stats.bytes_per_lang.end(); ++it) {
    fprintf(stderr, "  %-8s %8ld bytes\n", LanguageCode(it->first),
            it->second);
  }

  // Regroup quad counts by fingerprint, applying min_count.
  std::unordered_map<uint32, std::vector<LangCount> > by_quad;
  for (CountMap::iterator it = stats.quad_counts.begin();
       it != stats.quad_counts.end(); ++it) {
    uint32 hash = static_cast<uint32>(it->first >> 9);
    int lkey = static_cast<int>(it->first & 0x1ff);
    by_quad[hash].push_back(
        {static_cast<uint16>(lkey), it->second});
  }
  std::vector<std::pair<uint64, std::vector<LangCount> > > quad_grams;
  quad_grams.reserve(by_quad.size());
  for (auto& kv : by_quad) {
    uint64 total = 0;
    for (auto& lc : kv.second) {total += lc.count;}
    if (total < static_cast<uint64>(opt.min_count)) {continue;}
    quad_grams.push_back({kv.first, kv.second});
  }
  by_quad.clear();
  fprintf(stderr, "Pass 2: building quad table from %zu distinct quads...\n",
          quad_grams.size());
  BuiltTable quad;
  BuildTable(quad_grams, stats.quad_totals, opt, opt.quad_keymask,
             opt.quad_buckets, false, &quad);
  fprintf(stderr,
          "  quad: %ld offered, %ld filled into %zu buckets, %ld merged, "
          "%ld bucket-drops, %ld pool-drops\n",
          quad.offered, quad.filled, quad.buckets.size(), quad.merged,
          quad.dropped, quad.ind_full_drops);

  // Distinct words: strongly language-pure words, scored as single-language
  // entries with modest qprob (the originals use 2..4).
  std::vector<std::pair<uint64, std::vector<LangCount> > > distinct_words;
  {
    std::unordered_map<uint64, std::vector<LangCount> > by_word;
    for (auto& kv : stats.word_counts) {
      uint64 hash = kv.first >> 9;
      int lkey = static_cast<int>(kv.first & 0x1ff);
      by_word[hash].push_back({static_cast<uint16>(lkey), kv.second});
    }
    for (auto& kv : by_word) {
      uint64 total = 0;
      uint32 best = 0;
      uint16 best_lkey = 0;
      for (auto& lc : kv.second) {
        total += lc.count;
        if (lc.count > best) {best = lc.count; best_lkey = lc.lkey;}
      }
      if (total < static_cast<uint64>(opt.distinct_min_count)) {continue;}
      double share = static_cast<double>(best) / static_cast<double>(total);
      if (share < opt.distinct_min_share) {continue;}
      // Encode only the winner; qprob by purity like the original tables.
      int q = (share >= 0.97) ? 4 : (share >= 0.93 ? 3 : 2);
      LangCount lc;
      lc.lkey = best_lkey;
      lc.count = best;
      std::vector<LangCount> v(1, lc);
      distinct_words.push_back({kv.first, v});
      // Stash qprob via count trick? No: distinct table entries are packed
      // through the same PackCandidate path; override below via a
      // per-table pref that yields the intended qprob is fragile. Instead
      // we pack directly here by marking count so that PackCandidate is
      // bypassed for the distinct table (see BuildDistinct below).
      distinct_words.back().second[0].count = q;  // count now carries qprob
    }
  }
  fprintf(stderr, "Pass 3: building distinct-word table from %zu words...\n",
          distinct_words.size());

  // Distinct table build: same placement machinery, but entries are packed
  // directly from (plang, qprob).
  BuiltTable distinct;
  {
    int nbuckets = opt.octa_buckets;
    if (nbuckets == 0) {
      nbuckets = NextPow2(std::max(
          256L, static_cast<long>(distinct_words.size() / 2.4)));
    }
    std::unordered_map<uint64, std::pair<uint32, uint32> > slots;  // key->word0
    // Merge collisions: keep higher qprob.
    std::unordered_map<uint64, Candidate> cands;
    for (auto& dw : distinct_words) {
      uint32 subscr, hashkey;
      OctaFPJustHash(dw.first, opt.octa_keymask, nbuckets, &subscr, &hashkey);
      uint64 gkey = (static_cast<uint64>(subscr) << 32) | hashkey;
      Candidate& c = cands[gkey];
      if (c.langs.empty()) {
        c.subscr = subscr; c.hashkey = hashkey;
        c.langs.push_back(dw.second[0]);
        c.weight = dw.second[0].count;
      } else {
        ++distinct.merged;
        if (dw.second[0].count > c.langs[0].count) {c.langs[0] = dw.second[0];}
      }
    }
    distinct.offered = cands.size();
    std::vector<std::vector<Candidate*> > per_bucket(nbuckets);
    for (auto& kv : cands) {per_bucket[kv.second.subscr].push_back(&kv.second);}

    std::map<uint32, uint32> single_ix;
    std::vector<uint32> singles;
    singles.push_back(0);
    distinct.buckets.assign(nbuckets, IndirectProbBucket4());
    for (int b = 0; b < nbuckets; ++b) {
      for (int s = 0; s < 4; ++s) {distinct.buckets[b].keyvalue[s] = 0;}
    }
    const uint32 max_subscr = ~opt.octa_keymask;
    for (int b = 0; b < nbuckets; ++b) {
      std::vector<Candidate*>& v = per_bucket[b];
      std::sort(v.begin(), v.end(),
                [](const Candidate* a, const Candidate* b2) {
        return a->weight > b2->weight;
      });
      int slot = 0;
      for (size_t i = 0; i < v.size() && slot < 4; ++i) {
        uint8 plang3[3] = {static_cast<uint8>(v[i]->langs[0].lkey & 0xff),
                           0, 0};
        uint8 prob3[3] = {static_cast<uint8>(v[i]->langs[0].count), 0, 0};
        uint32 word0 = ProbPackV2(plang3, prob3);
        uint32 ix;
        std::map<uint32, uint32>::iterator it = single_ix.find(word0);
        if (it != single_ix.end()) {
          ix = it->second;
        } else if (singles.size() <= max_subscr) {
          ix = singles.size();
          singles.push_back(word0);
          single_ix[word0] = ix;
        } else {
          ++distinct.ind_full_drops;
          continue;
        }
        distinct.buckets[b].keyvalue[slot++] = v[i]->hashkey | ix;
        ++distinct.filled;
      }
      distinct.dropped += (v.size() > 4) ? (v.size() - 4) : 0;
    }
    distinct.ind = singles;
    distinct.size_one = singles.size();
    distinct.keymask = opt.octa_keymask;
  }
  fprintf(stderr,
          "  distinct: %ld offered, %ld filled into %zu buckets\n",
          distinct.offered, distinct.filled, distinct.buckets.size());

  fprintf(stderr, "Pass 4: calibrating expected scores...\n");
  Calibration cal;
  CalibrateExpectedScore(opt, quad, distinct, &cal);

  // RecognizedLangScripts string
  std::string recognized;
  for (auto& ls : stats.langscripts_seen) {
    if (!recognized.empty()) {recognized += " ";}
    recognized += LanguageCode(ls.first);
    recognized += "-";
    recognized += ULScriptCode(ls.second);
  }

  time_t now = time(NULL);
  struct tm* tmv = localtime(&now);
  uint32 build_date = (tmv->tm_year + 1900) * 10000 + (tmv->tm_mon + 1) * 100 +
                      tmv->tm_mday;

  FILE* out = fopen(opt.out_file.c_str(), "w");
  if (out == NULL) {
    fprintf(stderr, "error: cannot write %s\n", opt.out_file.c_str());
    exit(1);
  }
  fprintf(out,
          "// Generated by generate_cld2_tables (reverse-engineered CLD2 "
          "trainer).\n"
          "// Build date %u. Do not edit by hand.\n"
          "// Replaces: cld2_generated_quadchrome_2.cc,\n"
          "//   cld2_generated_deltaoctachrome.cc,\n"
          "//   cld2_generated_distinctoctachrome.cc,\n"
          "//   cld_generated_score_quad_octa_2.cc\n\n"
          "#include \"cld2tablesummary.h\"\n\n"
          "namespace CLD2 {\n\n",
          build_date);

  std::string qp = "k" + opt.table_name + "Quad";
  EmitTable(out, qp, quad, build_date, recognized);
  EmitSummaryObj(out, "kQuad_obj", qp);

  // Secondary quad table: empty, size 0 (guarded by kCLDTableSize != 0).
  fprintf(out,
          "static const uint32 %s2Size = 0;\n"
          "static const uint32 %s2KeyMask = 0xffffffff;\n"
          "static const IndirectProbBucket4 %s2Buckets[1] = {\n"
          "  {{0x00000000,0x00000000,0x00000000,0x00000000}},\n};\n"
          "static const uint32 %s2SizeOne = 2;\n"
          "extern const uint32 %s2IndSize = 2;\n"
          "static const uint32 %s2Ind[2] = {0x00000000, 0x00000000,};\n"
          "extern const CLD2TableSummary kQuad_obj2 = {\n"
          "  %s2Buckets,\n  %s2Ind,\n  %s2SizeOne,\n  %s2Size,\n"
          "  %s2KeyMask,\n  %u,\n  \"\",\n};\n\n",
          qp.c_str(), qp.c_str(), qp.c_str(), qp.c_str(), qp.c_str(),
          qp.c_str(), qp.c_str(), qp.c_str(), qp.c_str(), qp.c_str(),
          qp.c_str(), build_date);

  // Delta-octa: empty 1-bucket table (safe: lookups always miss).
  EmitEmptyTable(out, "k" + opt.table_name + "DeltaOcta", "kDeltaOcta_obj",
                 build_date);

  std::string dp = "k" + opt.table_name + "DistinctOcta";
  EmitTable(out, dp, distinct, build_date, recognized);
  EmitSummaryObj(out, "kDistinctOcta_obj", dp);

  // Expected score per 1KB, subscripted by lang*4 + script4.
  // 0 entries make ReliabilityExpected return 100 (always reliable), which
  // is the safe default for untrained languages.
  fprintf(out, "extern const int kAvgDeltaOctaScoreSize = 614 * 4;\n");
  fprintf(out, "extern const short kAvgDeltaOctaScore[kAvgDeltaOctaScoreSize]"
          " = {\n");
  for (int lang = 0; lang < 614; ++lang) {
    short row[4] = {0, 0, 0, 0};
    for (int s4 = 0; s4 < 4; ++s4) {
      std::map<std::pair<int, int>, std::pair<uint64, uint64> >::iterator it =
          cal.acc.find(std::make_pair(lang, s4));
      if (it != cal.acc.end() && it->second.second > 0) {
        uint64 v = it->second.first * 1024 / it->second.second;
        if (v > 32000) {v = 32000;}
        row[s4] = static_cast<short>(v);
      }
    }
    fprintf(out, "  %5d, %5d, %5d, %5d,  // %d %s\n", row[0], row[1], row[2],
            row[3], lang, LanguageCode(static_cast<Language>(lang)));
  }
  fprintf(out, "};\n\n}       // End namespace CLD2\n");
  fclose(out);

  fprintf(stderr, "Wrote %s\n", opt.out_file.c_str());
  fprintf(stderr, "RecognizedLangScripts: %s\n", recognized.c_str());
  return 0;
}
