#!/usr/bin/env python3
"""
Inject new languages into CLD2's main quadgram scoring table (kQuad_obj).

Instead of relying on the secondary table (kQuad_obj2), this tool modifies
the MAIN table's indirect entries (kCLDTableInd) to add new languages as
scoring candidates alongside their confusable neighbors.

For example: if a langprob entry scores [hat, fra, 0] for a quadgram, and
we know acf (Saint Lucian Creole) shares that quadgram, we change it to
[hat, fra, acf] so CLD2 considers acf as a candidate.

The approach:
1. Parse the C++ source to extract kCLDTableInd[] entries
2. For each injection rule (e.g., "add acf where hat exists"):
   - Find langprob entries containing the source language
   - If an empty slot exists (lang=0), insert the target language
   - Adjust probability subscript to give the new language a fair score
3. Write the modified table back as valid C++

Usage:
    python3 tools/inject_languages.py \
        --input internal/cld2_generated_quad0122.cc \
        --inject hat:acf --inject hat:gcr --inject hat:gcf \
        --inject yor:lin \
        --output internal/cld2_generated_quad0122.cc
"""

import argparse
import re
import sys

# kLgProbV2Tbl backmap: desired probability value -> subscript
# From cldutil_shared.h
PROB_BACKMAP = [0, 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]


def find_best_prob3_match(prob1, prob2, prob3):
    """Find the probability subscript that best matches three target probabilities.
    Simplified version of CLD2's FindBestProb3Match."""
    # The kLgProbV2Tbl has 240 entries, each 8 bytes.
    # Bytes 5,6,7 are the 3-probability values.
    # We need to find the entry whose [5],[6],[7] best match our targets.
    #
    # For simplicity, use the backmap: if all three probs are equal,
    # use PROB_BACKMAP[prob1]. Otherwise, search the table pattern.
    #
    # The table is organized as: for each (hi, lo) pair where hi >= lo >= 1,
    # there are entries with hi, interpolated, lo probabilities.
    # Group 0: entries 0-77 (mid = (hi+lo)/2)
    # Group 1: entries 78-155 (mid = (3*hi+lo)/4)
    # Group 2: entries 156-233 (mid = (hi+3*lo)/4)

    if prob1 == prob2 == prob3:
        return PROB_BACKMAP[min(prob1, 12)]

    # For the common case of (hi, mid, lo) pattern:
    hi = max(prob1, prob2, prob3)
    lo = min(prob1, prob2, prob3)
    if hi == lo:
        return PROB_BACKMAP[hi]

    # Compute base index for this (hi, lo) pair
    # Each hi value starts at: sum of (hi-1) entries before it
    # hi=1: 1 entry (lo=1), hi=2: 2 entries, hi=3: 3 entries, ...
    base = 0
    for h in range(1, hi):
        base += h
    base += (hi - lo)  # offset within this hi group

    # Check if mid matches group 0 (1/2), group 1 (3/4), or group 2 (1/4)
    mid = prob2 if prob1 >= prob2 >= prob3 else sorted([prob1, prob2, prob3])[1]
    mid_half = (hi + lo + 1) // 2
    mid_3q = (3 * hi + lo + 2) // 4
    mid_1q = (hi + 3 * lo + 2) // 4

    if abs(mid - mid_3q) <= abs(mid - mid_half) and abs(mid - mid_3q) <= abs(mid - mid_1q):
        return base + 78  # Group 1
    elif abs(mid - mid_1q) < abs(mid - mid_half):
        return base + 156  # Group 2
    else:
        return base  # Group 0


def parse_indirect_table(cpp_source):
    """Parse kQuad0122Ind[] from C++ source. Returns list of uint32 values."""
    entries = []
    in_indirect = False
    for line in cpp_source.split('\n'):
        if 'kQuad0122Ind[' in line and '= {' in line:
            in_indirect = True
            continue
        if in_indirect:
            if line.strip().startswith('};'):
                break
            for m in re.finditer(r'0x([0-9a-fA-F]{8})', line):
                entries.append(int(m.group(1), 16))
    return entries


def decode_langprob(lp):
    """Decode a uint32 langprob into (prob_sub, lang1, lang2, lang3)."""
    return (lp & 0xFF, (lp >> 8) & 0xFF, (lp >> 16) & 0xFF, (lp >> 24) & 0xFF)


def encode_langprob(prob_sub, lang1, lang2, lang3):
    """Encode (prob_sub, lang1, lang2, lang3) into a uint32 langprob."""
    return (lang3 << 24) | (lang2 << 16) | (lang1 << 8) | (prob_sub & 0xFF)


def inject_language(entries, source_pslang, target_pslang, prob_value=None):
    """Inject target_pslang into entries that contain source_pslang.

    For each entry containing source_pslang with an empty slot (lang=0),
    insert target_pslang into the empty slot.

    Args:
        entries: list of uint32 langprob values (modified in place)
        source_pslang: the confusable language to look for (e.g., hat=83)
        target_pslang: the new language to inject (e.g., acf=122)
        prob_value: probability to assign (1-12). If None, uses source's prob minus 2.

    Returns:
        number of entries modified
    """
    modified = 0
    for i in range(len(entries)):
        lp = entries[i]
        if lp == 0:
            continue

        prob_sub, lang1, lang2, lang3 = decode_langprob(lp)
        langs = [lang1, lang2, lang3]

        if source_pslang not in langs:
            continue

        # Find an empty slot
        empty_slot = None
        for slot in range(3):
            if langs[slot] == 0:
                empty_slot = slot
                break

        if empty_slot is None:
            continue  # All 3 slots full, skip

        # Determine probability for the new language
        # Use source language's probability minus a penalty (new lang is less likely)
        source_slot = langs.index(source_pslang)

        # Insert target into empty slot
        langs[empty_slot] = target_pslang

        # Recompute probability subscript
        # Get approximate probabilities from current subscript
        # The new language gets a slightly lower probability than the source
        if prob_value is not None:
            # Use specified probability for all slots
            new_probs = [0, 0, 0]
            for s in range(3):
                if langs[s] == target_pslang:
                    new_probs[s] = prob_value
                elif langs[s] == source_pslang:
                    new_probs[s] = prob_value + 2  # source gets higher score
                elif langs[s] != 0:
                    new_probs[s] = max(1, prob_value - 1)
            # Sort: highest prob first
            paired = sorted(zip(new_probs, langs), reverse=True)
            new_probs = [p for p, _ in paired]
            langs = [l for _, l in paired]
            new_sub = find_best_prob3_match(*new_probs)
        else:
            # Keep existing probability subscript (simplest approach)
            new_sub = prob_sub

        entries[i] = encode_langprob(new_sub, langs[0], langs[1], langs[2])
        modified += 1

    return modified


def rebuild_cpp_indirect(original_source, new_entries):
    """Replace kQuad0122Ind[] in the C++ source with modified entries."""
    lines = original_source.split('\n')
    result = []
    in_indirect = False
    skip_until_close = False

    for line in lines:
        if 'kQuad0122Ind[' in line and '= {' in line:
            result.append(line)
            in_indirect = True
            skip_until_close = True
            # Write new entries
            for i in range(0, len(new_entries), 4):
                chunk = new_entries[i:i+4]
                hex_vals = ', '.join(f'0x{v:08x}' for v in chunk)
                result.append(f'  {hex_vals},')
            continue

        if skip_until_close:
            if line.strip().startswith('};'):
                skip_until_close = False
                result.append(line)
            # Skip original data lines
            continue

        result.append(line)

    return '\n'.join(result)


def main():
    parser = argparse.ArgumentParser(description="Inject languages into CLD2 main quadgram table")
    parser.add_argument("--input", required=True, help="Input C++ source file")
    parser.add_argument("--output", required=True, help="Output C++ source file")
    parser.add_argument("--inject", action="append", required=True,
                        help="source_pslang:target_pslang (e.g., 83:122 to add acf where hat exists)")
    parser.add_argument("--prob", type=int, default=None,
                        help="Probability value for injected languages (1-12, default: auto)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Only report what would be changed")
    args = parser.parse_args()

    print(f"Reading {args.input}...", file=sys.stderr)
    with open(args.input, 'r') as f:
        source = f.read()

    entries = parse_indirect_table(source)
    print(f"Parsed {len(entries)} indirect entries", file=sys.stderr)

    total_modified = 0
    for spec in args.inject:
        src_pslang, tgt_pslang = map(int, spec.split(':'))
        n = inject_language(entries, src_pslang, tgt_pslang, prob_value=args.prob)
        print(f"  Inject pslang {tgt_pslang} where pslang {src_pslang} exists: {n} entries modified",
              file=sys.stderr)
        total_modified += n

    print(f"Total entries modified: {total_modified}", file=sys.stderr)

    if args.dry_run:
        print("Dry run - no output written", file=sys.stderr)
        return

    print(f"Rebuilding C++ source...", file=sys.stderr)
    new_source = rebuild_cpp_indirect(source, entries)

    print(f"Writing {args.output}...", file=sys.stderr)
    with open(args.output, 'w') as f:
        f.write(new_source)
    print("Done.", file=sys.stderr)


if __name__ == "__main__":
    main()
