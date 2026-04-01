#!/usr/bin/env python3
"""
Build a CLD2 quadgram table from training text files.

Generates a C++ source file containing a CLD2-compatible quadgram hash table
(kQuad_obj2) for new languages not in the primary table.

The format matches CLD2's IndirectProbBucket4 / CLD2TableSummary structures:
- 4-way associative hash table of quadgram fingerprints
- Indirect probability table with packed lang/prob entries
- Each indirect entry: prob_subscript(8) | lang1(8) | lang2(8) | lang3(8)

Usage:
    python3 tools/build_quadgram_table.py \
        --langs arg:123,vec:124,hau:125 \
        --training-dir data/training \
        --output internal/cld2_generated_quad_new.cc
"""

import argparse
import ctypes
import os
import struct
import sys
from collections import Counter, defaultdict


# Replicate CLD2's QuadHashV2 logic in Python
# Pre/post space indicators
PRE_SPACE = 0x00004444
POST_SPACE = 0x44440000

# Word masks for 0..3 trailing bytes
WORD_MASK = [0xFFFFFFFF, 0x000000FF, 0x0000FFFF, 0x00FFFFFF]


def to_uint32(val):
    return val & 0xFFFFFFFF


def quad_hash_v2_mix(data_bytes, prepost):
    """Replicate CLD2's QuadHashV2Mix."""
    # Pad to at least 12 bytes for safe 4-byte reads
    padded = data_bytes + b'\x00' * 16
    bytecount = len(data_bytes)

    if bytecount <= 4:
        word0 = struct.unpack_from('<I', padded, 0)[0] & WORD_MASK[bytecount & 3]
        word0 = to_uint32(word0 ^ (word0 >> 3))
        return to_uint32(word0 ^ prepost)
    elif bytecount <= 8:
        word0 = struct.unpack_from('<I', padded, 0)[0]
        word0 = to_uint32(word0 ^ (word0 >> 3))
        word1 = struct.unpack_from('<I', padded, 4)[0] & WORD_MASK[bytecount & 3]
        word1 = to_uint32(word1 ^ (word1 << 4))
        return to_uint32(to_uint32(word0 ^ prepost) + word1)
    else:
        word0 = struct.unpack_from('<I', padded, 0)[0]
        word0 = to_uint32(word0 ^ (word0 >> 3))
        word1 = struct.unpack_from('<I', padded, 4)[0]
        word1 = to_uint32(word1 ^ (word1 << 4))
        word2 = struct.unpack_from('<I', padded, 8)[0] & WORD_MASK[bytecount & 3]
        word2 = to_uint32(word2 ^ (word2 << 2))
        return to_uint32(to_uint32(word0 ^ prepost) + word1 + word2)


def quad_hash_v2_underscore(quadgram_str):
    """Hash a quadgram string that uses underscores for word boundaries.
    This matches CLD2's QuadHashV2Underscore used in offline table building."""
    data = quadgram_str.encode('utf-8')
    if len(data) == 0:
        return 0

    prepost = 0
    start = 0
    end = len(data)

    if data[0:1] == b'_':
        prepost |= PRE_SPACE
        start += 1
    if data[-1:] == b'_':
        prepost |= POST_SPACE
        end -= 1

    return quad_hash_v2_mix(data[start:end], prepost)


def extract_quadgrams(text):
    """Extract quadgrams from text, mimicking CLD2's approach.

    CLD2 processes text as sequences of non-space characters, extracting
    4-character windows. Word boundaries (spaces) are encoded as underscore
    markers in the hash.
    """
    quadgrams = []
    # Split into words, add word boundary markers
    words = text.split()
    for i, word in enumerate(words):
        if not word:
            continue
        # Add word-boundary quadgrams: _abc, abc_, _ab_, abcd, bcde, etc.
        chars = list(word)
        # For CLD2, quadgrams are 4 "characters" where _ represents word boundary
        # Prefix with _ for word start, suffix with _ for word end
        extended = ['_'] + chars + ['_']
        for j in range(len(extended) - 3):
            qchars = extended[j:j+4]
            qstr = ''.join(qchars)
            # Skip if all underscores or too short actual content
            actual = qstr.replace('_', '')
            if len(actual) < 2:
                continue
            quadgrams.append(qstr)
    return quadgrams


def compute_quadgram_freqs(filepath, max_lines=10000):
    """Read a training file and compute quadgram frequencies."""
    freqs = Counter()
    lines_read = 0
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if len(line) < 10:
                continue
            quads = extract_quadgrams(line)
            freqs.update(quads)
            lines_read += 1
            if lines_read >= max_lines:
                break
    return freqs


def build_table(lang_configs, training_dir, contrast_langs=None,
                table_size_bits=14, max_quadgrams_per_lang=50000):
    """Build the quadgram hash table.

    Args:
        lang_configs: dict of {iso3_code: plang_id}
        training_dir: directory containing training files
        contrast_langs: optional dict of {iso3_code: plang_id} for contrast
        table_size_bits: log2 of bucket count (14 = 16384 buckets)
        max_quadgrams_per_lang: max quadgrams to keep per language

    Returns:
        (buckets, indirect_table, size_one, key_mask, recognized_scripts)
    """
    bucket_count = 1 << table_size_bits
    key_mask = 0xFFFF0000  # Upper 16 bits for hash key

    # Step 1: Compute quadgram frequencies for each language
    print(f"Computing quadgram frequencies for {len(lang_configs)} languages...",
          file=sys.stderr)
    lang_freqs = {}  # {lang_code: Counter of quadgram -> count}

    for lang_code in lang_configs:
        train_file = os.path.join(training_dir, f"{lang_code}_train.txt")
        if not os.path.exists(train_file):
            print(f"  WARNING: No training data for {lang_code}, skipping",
                  file=sys.stderr)
            continue
        freqs = compute_quadgram_freqs(train_file)
        if len(freqs) > 0:
            lang_freqs[lang_code] = freqs
            print(f"  {lang_code}: {len(freqs)} unique quadgrams from "
                  f"{sum(freqs.values())} total", file=sys.stderr)

    # Also load contrast language frequencies for filtering
    contrast_freqs = {}
    if contrast_langs:
        for lang_code in contrast_langs:
            contrast_file = os.path.join(training_dir, f"{lang_code}_contrast.txt")
            if not os.path.exists(contrast_file):
                continue
            freqs = compute_quadgram_freqs(contrast_file, max_lines=5000)
            if len(freqs) > 0:
                contrast_freqs[lang_code] = freqs

    # Pre-compute normalized frequencies for contrast and mutual filtering
    print("Pre-computing normalized frequencies...", file=sys.stderr)
    contrast_norm = {}  # {lang: {quad: freq}}
    for c_code, c_freqs in contrast_freqs.items():
        c_total = sum(c_freqs.values())
        if c_total > 0:
            contrast_norm[c_code] = {q: c / c_total for q, c in c_freqs.items()}

    lang_norm = {}  # {lang: {quad: freq}}
    for lang_code, freqs in lang_freqs.items():
        total = sum(freqs.values())
        if total > 0:
            lang_norm[lang_code] = {q: c / total for q, c in freqs.items()}

    # Build per-quadgram max contrast frequency for speed
    all_contrast_quads = defaultdict(float)  # quad -> max normalized freq across contrast
    for c_norms in contrast_norm.values():
        for q, f in c_norms.items():
            if f > all_contrast_quads[q]:
                all_contrast_quads[q] = f

    # Step 2: For each language, select most distinctive quadgrams
    print("Selecting distinctive quadgrams...", file=sys.stderr)
    hash_to_langs = defaultdict(list)  # hash -> [(plang, score)]

    for lang_code, freqs in lang_freqs.items():
        plang = lang_configs[lang_code]
        norms = lang_norm.get(lang_code, {})
        if not norms:
            continue

        # Pre-compute max mutual freq for this language's quadgrams
        mutual_max_map = defaultdict(float)
        for other_code, other_norms in lang_norm.items():
            if other_code == lang_code:
                continue
            for q in norms:
                if q in other_norms and other_norms[q] > mutual_max_map[q]:
                    mutual_max_map[q] = other_norms[q]

        scored = []
        for quad, count in freqs.items():
            freq = norms[quad]
            contrast_max = all_contrast_quads.get(quad, 0)
            mutual_max = mutual_max_map.get(quad, 0)

            # Simple distinctiveness: just use raw frequency
            # Contrast filtering is handled implicitly by the dual-table
            # scoring: table 1 languages already have strong quadgram coverage,
            # so table 2 entries only win when they have more distinctive data
            distinctiveness = freq
            scored.append((quad, distinctiveness, count))

        # Keep top quadgrams by distinctiveness
        scored.sort(key=lambda x: -x[1])
        kept = scored[:max_quadgrams_per_lang]

        for quad, score, count in kept:
            qhash = quad_hash_v2_underscore(quad)
            # Score -> probability index (1-12 range, higher = more probable)
            prob = min(12, max(1, int(score * 1000) + 4))
            hash_to_langs[qhash].append((plang, prob))

    print(f"Total unique quadgram hashes: {len(hash_to_langs)}", file=sys.stderr)

    # Step 3: Build indirect table entries
    # Each entry packs up to 3 languages: prob_idx(8) | lang1(8) | lang2(8) | lang3(8)
    # For entries with more languages, we use 6-lang format (two uint32s)
    indirect = []
    indirect_map = {}  # indirect_entry_value -> index

    # Reserve index 0 as empty
    indirect.append(0)

    # Step 4: Build hash table buckets
    buckets = [[0, 0, 0, 0] for _ in range(bucket_count)]
    collisions = 0
    inserted = 0

    for qhash, lang_probs in hash_to_langs.items():
        # Sort by probability descending, take top 3
        lang_probs.sort(key=lambda x: -x[1])
        top3 = lang_probs[:3]

        # Build the probability entry for the indirect table
        # Use prob index that best matches the distribution
        max_prob = top3[0][1] if top3 else 1
        # Map to kLgProbV2Tbl index (0-77 for 3-lang entries)
        prob_idx = min(77, max(0, (max_prob - 1) * 7))

        # Pack: prob_idx | lang1 << 8 | lang2 << 16 | lang3 << 24
        packed = prob_idx & 0xFF
        if len(top3) > 0:
            packed |= (top3[0][0] & 0xFF) << 8
        if len(top3) > 1:
            packed |= (top3[1][0] & 0xFF) << 16
        if len(top3) > 2:
            packed |= (top3[2][0] & 0xFF) << 24

        # Add to indirect table (dedup)
        if packed not in indirect_map:
            indirect_map[packed] = len(indirect)
            indirect.append(packed)
        ind_idx = indirect_map[packed]

        # Compute bucket subscript and hash key
        subscr = (qhash + (qhash >> 12)) & (bucket_count - 1)
        hashkey = qhash & key_mask

        # Pack: hashkey | indirect_subscript
        entry = hashkey | (ind_idx & ~key_mask)

        # Insert into bucket (4-way associative)
        bucket = buckets[subscr]
        placed = False
        for slot in range(4):
            if bucket[slot] == 0:
                bucket[slot] = entry
                placed = True
                inserted += 1
                break
        if not placed:
            collisions += 1

    print(f"Inserted {inserted} entries, {collisions} collisions (dropped)",
          file=sys.stderr)
    print(f"Indirect table size: {len(indirect)}", file=sys.stderr)

    # Build recognized lang-scripts string
    recognized = []
    for lang_code in sorted(lang_freqs.keys()):
        recognized.append(f"{lang_code}-Latn")
    recognized_str = " ".join(recognized) + " "

    return buckets, indirect, len(indirect), key_mask, recognized_str, bucket_count


def emit_cc(buckets, indirect, size_one, key_mask, recognized, bucket_count,
            output_path):
    """Write the C++ source file."""
    with open(output_path, 'w') as f:
        f.write('// Generated quadgram table for new languages\n')
        f.write('// Auto-generated by tools/build_quadgram_table.py\n\n')
        f.write('#include "cld2tablesummary.h"\n\n')
        f.write('namespace CLD2 {\n\n')

        # Build date
        f.write('static const uint32 kQuadNew_BuildDate = 20260401;\n\n')

        # Recognized scripts
        f.write(f'static const char* const kQuadNew_RecognizedLangScripts =\n')
        f.write(f'  "{recognized}";\n\n')

        # Hash table
        f.write(f'static const uint32 kQuadNew_Size = {bucket_count};'
                f'    // Bucket count\n')
        f.write(f'static const uint32 kQuadNew_KeyMask = 0x{key_mask:08x};'
                f'    // Mask hash key\n\n')

        f.write(f'static const IndirectProbBucket4 kQuadNew'
                f'[{bucket_count}] = {{\n')
        for i, bucket in enumerate(buckets):
            f.write(f'  {{0x{bucket[0]:08x},0x{bucket[1]:08x},'
                    f'0x{bucket[2]:08x},0x{bucket[3]:08x}}},\n')
        f.write('};\n\n')

        # Indirect table
        f.write(f'static const uint32 kQuadNew_SizeOne = {size_one};'
                f'    // Bucket count one-lang\n')
        f.write(f'static const uint32 kQuadNew_Ind[{len(indirect)}] = {{\n')
        for i in range(0, len(indirect), 8):
            chunk = indirect[i:i+8]
            vals = ', '.join(f'0x{v:08x}' for v in chunk)
            f.write(f'  {vals},\n')
        f.write('};\n\n')

        # Table summary object
        f.write('extern const CLD2TableSummary kQuad_obj2 = {\n')
        f.write('  kQuadNew,\n')
        f.write('  kQuadNew_Ind,\n')
        f.write('  kQuadNew_SizeOne,\n')
        f.write('  kQuadNew_Size,\n')
        f.write('  kQuadNew_KeyMask,\n')
        f.write('  kQuadNew_BuildDate,\n')
        f.write('  kQuadNew_RecognizedLangScripts,\n')
        f.write('};\n\n')
        f.write('}       // End namespace CLD2\n')

    print(f"Wrote {output_path}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Build CLD2 quadgram table for new languages")
    parser.add_argument("--langs", required=True,
                        help="Comma-separated lang:plang pairs, e.g. hau:122,yor:123")
    parser.add_argument("--contrast", default="",
                        help="Comma-separated contrast lang:plang pairs")
    parser.add_argument("--training-dir", default="data/training",
                        help="Directory with training text files")
    parser.add_argument("--output", default="internal/cld2_generated_quad_new.cc",
                        help="Output C++ file path")
    parser.add_argument("--table-size-bits", type=int, default=14,
                        help="Log2 of hash table bucket count (default: 14 = 16384)")
    parser.add_argument("--max-quadgrams", type=int, default=50000,
                        help="Max quadgrams per language (default: 50000)")
    args = parser.parse_args()

    # Parse language configs
    lang_configs = {}
    for pair in args.langs.split(','):
        parts = pair.strip().split(':')
        if len(parts) == 2:
            lang_configs[parts[0]] = int(parts[1])

    contrast_langs = {}
    if args.contrast:
        for pair in args.contrast.split(','):
            parts = pair.strip().split(':')
            if len(parts) == 2:
                contrast_langs[parts[0]] = int(parts[1])

    if not lang_configs:
        print("ERROR: No languages specified", file=sys.stderr)
        sys.exit(1)

    buckets, indirect, size_one, key_mask, recognized, bucket_count = build_table(
        lang_configs, args.training_dir,
        contrast_langs=contrast_langs if contrast_langs else None,
        table_size_bits=args.table_size_bits,
        max_quadgrams_per_lang=args.max_quadgrams,
    )

    emit_cc(buckets, indirect, size_one, key_mask, recognized, bucket_count,
            args.output)


if __name__ == "__main__":
    main()
