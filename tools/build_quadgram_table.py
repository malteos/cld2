#!/usr/bin/env python3
"""
Build CLD2 quadgram scoring tables for new languages.

Generates C++ source code for kQuad_obj2 (the secondary quadgram table)
from training text in multiple languages.

Usage:
    python3 tools/build_quadgram_table.py \
        --lang arg:data/training/arg.txt \
        --lang vec:data/training/vec.txt \
        --output internal/cld2_generated_quad_new.cc \
        --pslang-start 122
"""

import argparse
import struct
import sys
from collections import Counter, defaultdict


# CLD2 QuadHashV2 reimplementation
# From cldutil_shared.cc lines 167-202

WORD_MASK = [0xFFFFFFFF, 0x000000FF, 0x0000FFFF, 0x00FFFFFF]
PRE_SPACE  = 0x00004444
POST_SPACE = 0x44440000

def unaligned_load32_le(data, offset=0):
    """Load 4 bytes as little-endian uint32."""
    b = data[offset:offset+4]
    if len(b) < 4:
        b = b + b'\x00' * (4 - len(b))
    return struct.unpack('<I', b)[0]


def quad_hash_v2_mix(word_bytes, bytecount, prepost):
    """Reimplement QuadHashV2Mix from cldutil_shared.cc."""
    if bytecount <= 4:
        word0 = unaligned_load32_le(word_bytes, 0) & WORD_MASK[bytecount & 3]
        word0 = (word0 ^ (word0 >> 3)) & 0xFFFFFFFF
        return (word0 ^ prepost) & 0xFFFFFFFF
    elif bytecount <= 8:
        word0 = unaligned_load32_le(word_bytes, 0)
        word0 = (word0 ^ (word0 >> 3)) & 0xFFFFFFFF
        word1 = unaligned_load32_le(word_bytes, 4) & WORD_MASK[bytecount & 3]
        word1 = (word1 ^ (word1 << 4)) & 0xFFFFFFFF
        return ((word0 ^ prepost) + word1) & 0xFFFFFFFF
    else:
        word0 = unaligned_load32_le(word_bytes, 0)
        word0 = (word0 ^ (word0 >> 3)) & 0xFFFFFFFF
        word1 = unaligned_load32_le(word_bytes, 4)
        word1 = (word1 ^ (word1 << 4)) & 0xFFFFFFFF
        word2 = unaligned_load32_le(word_bytes, 8) & WORD_MASK[bytecount & 3]
        word2 = (word2 ^ (word2 << 2)) & 0xFFFFFFFF
        return ((word0 ^ prepost) + word1 + word2) & 0xFFFFFFFF


def quad_hash_v2(text_bytes, offset, length):
    """Hash a quadgram at given position in text bytes.
    Checks for space boundaries like CLD2 does."""
    prepost = 0
    if offset > 0 and text_bytes[offset - 1] == ord(' '):
        prepost |= PRE_SPACE
    if offset + length < len(text_bytes) and text_bytes[offset + length] == ord(' '):
        prepost |= POST_SPACE
    return quad_hash_v2_mix(text_bytes[offset:offset+length], length, prepost)


def extract_quadgrams(text, max_quadgrams=100000):
    """Extract quadgrams from text and return Counter of (quadhash -> count)."""
    # Lowercase and normalize
    text = text.lower()
    text_bytes = text.encode('utf-8')

    quadgrams = Counter()
    i = 0
    count = 0
    while i + 4 <= len(text_bytes) and count < max_quadgrams:
        # Find a 4-byte window
        qlen = 4
        # Extend for multi-byte UTF-8 chars
        while qlen < min(12, len(text_bytes) - i):
            # Count complete UTF-8 characters
            chars = 0
            j = 0
            while j < qlen and i + j < len(text_bytes):
                b = text_bytes[i + j]
                if b < 0x80:
                    j += 1
                elif b < 0xE0:
                    j += 2
                elif b < 0xF0:
                    j += 3
                else:
                    j += 4
                chars += 1
            if chars >= 4:
                qlen = j
                break
            qlen += 1

        h = quad_hash_v2(text_bytes, i, min(qlen, 12))
        if h != 0:
            quadgrams[h] += 1
            count += 1
        i += 1  # Advance by 1 byte

    return quadgrams


def build_table(lang_data, bucket_count=4096, pslang_start=122,
                contrast_data=None, min_count=3, min_ratio=0.7):
    """Build a CLD2-compatible quadgram hash table.

    Only includes quadgrams that are distinctive to the new languages
    compared to contrast languages.

    Args:
        lang_data: dict mapping lang_code -> list of training texts
        bucket_count: number of hash buckets (power of 2)
        pslang_start: first per-script language number to assign
        contrast_data: dict mapping lang_code -> list of texts for contrast languages
        min_count: minimum quadgram count to include
        min_ratio: minimum ratio of new-lang vs total to include

    Returns:
        (buckets, indirect, pslang_map, keymask, size_one)
    """
    # Assign per-script language numbers
    pslang_map = {}
    for i, lang in enumerate(sorted(lang_data.keys())):
        pslang_map[lang] = pslang_start + i

    # Extract quadgrams per language
    print(f"Extracting quadgrams for {len(lang_data)} new languages...", file=sys.stderr)
    lang_quadgrams = {}
    for lang, texts in lang_data.items():
        combined = Counter()
        for text in texts:
            combined.update(extract_quadgrams(text))
        lang_quadgrams[lang] = combined
        total = sum(combined.values())
        unique = len(combined)
        print(f"  {lang}: {unique} unique quadgrams, {total} total", file=sys.stderr)

    # Extract contrast language quadgrams
    contrast_quadgrams = Counter()
    if contrast_data:
        print(f"Extracting contrast quadgrams from {len(contrast_data)} languages...", file=sys.stderr)
        for lang, texts in contrast_data.items():
            combined = Counter()
            for text in texts:
                combined.update(extract_quadgrams(text))
            contrast_quadgrams.update(combined)
            print(f"  contrast {lang}: {len(combined)} unique quadgrams", file=sys.stderr)

    # All quadgram hashes from new languages
    all_hashes = set()
    for qg in lang_quadgrams.values():
        all_hashes.update(qg.keys())

    print(f"Total unique quadgram hashes: {len(all_hashes)}", file=sys.stderr)

    # Filter: only keep quadgrams that are distinctive to new languages
    quadgram_scores = {}
    for h in all_hashes:
        new_lang_counts = {}
        for lang, qg in lang_quadgrams.items():
            if h in qg:
                new_lang_counts[lang] = qg[h]

        new_total = sum(new_lang_counts.values())
        if new_total < min_count:
            continue

        contrast_count = contrast_quadgrams.get(h, 0)
        total = new_total + contrast_count

        # Only keep if the new language(s) dominate this quadgram
        ratio = new_total / total
        if ratio < min_ratio:
            continue

        # Sort by count, take top 3
        top = sorted(new_lang_counts.items(), key=lambda x: -x[1])[:3]

        # Quantize probabilities
        scores = []
        for lang, count in top:
            prob = count / total
            if prob > 0.9:
                score = 12
            elif prob > 0.8:
                score = 10
            elif prob > 0.7:
                score = 8
            elif prob > 0.5:
                score = 6
            elif prob > 0.3:
                score = 4
            elif prob > 0.15:
                score = 2
            else:
                score = 1
            scores.append((pslang_map[lang], score))

        quadgram_scores[h] = scores

    print(f"Distinctive quadgrams: {len(quadgram_scores)}", file=sys.stderr)

    # Build hash table
    keymask = ((bucket_count - 1) << 16) | 0xFFFF0000
    # Actually CLD2 uses bucket_count for size, keymask for key comparison
    # keymask = top N bits where N = log2(bucket_count)
    import math
    bits = int(math.log2(bucket_count))
    keymask = (0xFFFFFFFF << (32 - bits)) & 0xFFFFFFFF

    # Build indirect table
    indirect = []
    size_one = 0  # All entries are single-langprob (3 languages)

    # Build buckets
    buckets = [[0, 0, 0, 0] for _ in range(bucket_count)]

    # Assign quadgrams to buckets
    placed = 0
    collisions = 0
    for h, scores in quadgram_scores.items():
        subscr = ((h + (h >> 12)) & (bucket_count - 1))
        hashkey = h & keymask

        # Build langprob: top3_pslang[2:0] + prob_subscript
        # We use a simple probability subscript encoding
        langprob = 0
        if len(scores) >= 1:
            langprob |= (scores[0][0] & 0xFF) << 8
        if len(scores) >= 2:
            langprob |= (scores[1][0] & 0xFF) << 16
        if len(scores) >= 3:
            langprob |= (scores[2][0] & 0xFF) << 24

        # Prob subscript indexes into kLgProbV2Tbl (8 bytes per entry)
        # Last 3 bytes are probabilities for top1/top2/top3 language
        # kLgProbV2TblBackmap: prob -> subscript
        # prob 1->0, 2->1, 3->3, 4->6, 5->10, 6->15, 7->21, 8->28,
        # 9->36, 10->45, 11->55, 12->66
        backmap = [0, 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]
        if len(scores) >= 1:
            prob_sub = backmap[min(scores[0][1], 12)]
        else:
            prob_sub = 0
        langprob |= prob_sub & 0xFF

        # Add to indirect table
        ind_idx = len(indirect)
        indirect.append(langprob)

        # Build bucket entry: hashkey | indirect_subscript
        entry = hashkey | (ind_idx & ~keymask)

        # Find an empty slot in the bucket
        bucket = buckets[subscr]
        found = False
        for slot in range(4):
            if bucket[slot] == 0:
                bucket[slot] = entry
                placed += 1
                found = True
                break
        if not found:
            collisions += 1

    print(f"Placed {placed} entries, {collisions} collisions", file=sys.stderr)

    # size_one: all indirect entries are single (3-lang)
    size_one = len(indirect) + 2  # Set above total so all are single

    return buckets, indirect, pslang_map, keymask, size_one


def generate_cpp(buckets, indirect, pslang_map, keymask, size_one,
                 lang_scripts, build_date="20260329"):
    """Generate C++ source code for the quadgram table."""
    lines = []
    lines.append("// Auto-generated quadgram table for new languages")
    lines.append("// Generated by tools/build_quadgram_table.py")
    lines.append("")
    lines.append('#include "cld2tablesummary.h"')
    lines.append("")
    lines.append("namespace CLD2 {")
    lines.append("")

    bucket_count = len(buckets)

    # Build date
    lines.append(f"static const uint32 kQuadNew_BuildDate = {build_date};")
    lines.append("")

    # Recognized lang scripts
    scripts_str = " ".join(lang_scripts)
    lines.append(f'static const char* const kQuadNewRecognizedLangScripts =')
    lines.append(f'  "{scripts_str} ";')
    lines.append("")

    # Main table
    lines.append(f"static const uint32 kQuadNew_Size = {bucket_count};")
    lines.append(f"static const uint32 kQuadNew_KeyMask = 0x{keymask:08x};")
    lines.append(f"static const IndirectProbBucket4 kQuadNew[{bucket_count}] = {{")
    for i, bucket in enumerate(buckets):
        vals = ", ".join(f"0x{v:08x}" for v in bucket)
        lines.append(f"  {{{vals}}},")
    lines.append("};")
    lines.append("")

    # Indirect table
    ind_size = max(len(indirect), 2)
    lines.append(f"static const uint32 kQuadNew_SizeOne = {size_one};")
    lines.append(f"extern const uint32 kQuadNewIndSize = {size_one};")
    lines.append(f"static const uint32 kQuadNew_Ind[{ind_size}] = {{")
    for i in range(0, len(indirect), 4):
        chunk = indirect[i:i+4]
        vals = ", ".join(f"0x{v:08x}" for v in chunk)
        lines.append(f"  {vals},")
    if len(indirect) == 0:
        lines.append("  0x00000000, 0x00000000,")
    lines.append("};")
    lines.append("")

    # Table summary
    lines.append("extern const CLD2TableSummary kQuad_obj2 = {")
    lines.append("  kQuadNew,")
    lines.append("  kQuadNew_Ind,")
    lines.append("  kQuadNew_SizeOne,")
    lines.append("  kQuadNew_Size,")
    lines.append("  kQuadNew_KeyMask,")
    lines.append("  kQuadNew_BuildDate,")
    lines.append("  kQuadNewRecognizedLangScripts,")
    lines.append("};")
    lines.append("")
    lines.append("}  // namespace CLD2")

    return "\n".join(lines)


def _load_text_file(path):
    """Load text lines from a .txt or .jsonl file."""
    import json as _json
    texts = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if path.endswith(".jsonl"):
                try:
                    record = _json.loads(line)
                    text = record.get("text", "").strip()
                    if text:
                        texts.append(text)
                except _json.JSONDecodeError:
                    continue
            else:
                texts.append(line)
    return texts


def main():
    parser = argparse.ArgumentParser(description="Build CLD2 quadgram table")
    parser.add_argument("--lang", action="append", required=True,
                        help="lang_code:training_file (can repeat)")
    parser.add_argument("--contrast", action="append", default=[],
                        help="contrast_lang:file (existing languages for filtering)")
    parser.add_argument("--output", required=True,
                        help="Output C++ file path")
    parser.add_argument("--pslang-start", type=int, default=122,
                        help="Starting per-script language number")
    parser.add_argument("--bucket-count", type=int, default=4096,
                        help="Number of hash buckets (power of 2)")
    parser.add_argument("--min-count", type=int, default=3,
                        help="Minimum quadgram count to include")
    parser.add_argument("--min-ratio", type=float, default=0.7,
                        help="Minimum ratio of new-lang vs total to include")
    parser.add_argument("--script", default="Latn",
                        help="Script for new languages (default: Latn)")
    args = parser.parse_args()

    # Load training data (supports .txt and .jsonl)
    lang_data = {}
    for spec in args.lang:
        code, path = spec.split(":", 1)
        texts = _load_text_file(path)
        if code in lang_data:
            lang_data[code].extend(texts)
        else:
            lang_data[code] = texts
        print(f"Loaded {len(texts)} lines for {code} from {path}", file=sys.stderr)

    # Load contrast data
    contrast_data = {}
    for spec in args.contrast:
        code, path = spec.split(":", 1)
        texts = _load_text_file(path)
        contrast_data[code] = texts
        print(f"Loaded {len(texts)} contrast lines for {code} from {path}", file=sys.stderr)

    # Build table
    buckets, indirect, pslang_map, keymask, size_one = build_table(
        lang_data,
        bucket_count=args.bucket_count,
        pslang_start=args.pslang_start,
        contrast_data=contrast_data if contrast_data else None,
        min_count=args.min_count,
        min_ratio=args.min_ratio,
    )

    # Generate lang-script strings
    lang_scripts = [f"{code}-{args.script}" for code in sorted(lang_data.keys())]

    # Generate C++
    cpp = generate_cpp(buckets, indirect, pslang_map, keymask, size_one, lang_scripts)

    with open(args.output, "w") as f:
        f.write(cpp)
    print(f"Generated {args.output}", file=sys.stderr)

    # Print pslang mapping for updating generated_language.cc
    print("\nPer-script language number assignments:", file=sys.stderr)
    for lang, pslang in sorted(pslang_map.items()):
        print(f"  {lang}: pslang={pslang}", file=sys.stderr)


if __name__ == "__main__":
    main()
