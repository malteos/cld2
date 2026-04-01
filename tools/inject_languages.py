#!/usr/bin/env python3
"""
Inject new languages into CLD2's main quadgram scoring table (kQuad_obj).

Two strategies for injection:
1. Empty-slot: if a langprob entry has an unused slot (lang=0), fill it
2. Replace: if all 3 slots are full, replace the LOWEST-probability language
   (only if it's not the source language and not in a protected list)

Usage:
    python3 tools/inject_languages.py \
        --input internal/cld2_generated_quad0122.cc \
        --inject 83:122 --inject 83:129 --inject 83:128 \
        --inject 74:135 \
        --prob 4 \
        --output internal/cld2_generated_quad0122.cc
"""

import argparse
import re
import sys

PROB_BACKMAP = [0, 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]

# kLgProbV2Tbl last 3 bytes (prob1, prob2, prob3) for first 78 entries
# These are the probabilities for 3-language lookup (Group 0: mid = average)
# Format: each entry is (hi, mid, lo) probabilities
LG_PROB_TABLE = []
for hi in range(1, 13):
    for lo in range(1, hi + 1):
        mid = (hi + lo + 1) // 2
        LG_PROB_TABLE.append((hi, mid, lo))


def get_probs_for_subscript(sub):
    """Get approximate (prob1, prob2, prob3) for a probability subscript."""
    if sub >= 234:
        return (1, 1, 1)
    group = sub // 78
    idx = sub % 78
    if idx >= len(LG_PROB_TABLE):
        return (1, 1, 1)
    hi, mid, lo = LG_PROB_TABLE[idx]
    if group == 0:
        return (hi, mid, lo)
    elif group == 1:
        return (hi, (3*hi + lo + 2) // 4, lo)
    else:
        return (hi, (hi + 3*lo + 2) // 4, lo)


def decode_langprob(lp):
    return (lp & 0xFF, (lp >> 8) & 0xFF, (lp >> 16) & 0xFF, (lp >> 24) & 0xFF)


def encode_langprob(prob_sub, lang1, lang2, lang3):
    return (lang3 << 24) | (lang2 << 16) | (lang1 << 8) | (prob_sub & 0xFF)


def find_best_prob_subscript(p1, p2, p3):
    """Find the probability subscript that best matches three target values."""
    p1, p2, p3 = max(1, p1), max(1, p2), max(1, p3)
    # Ensure sorted descending
    probs = sorted([p1, p2, p3], reverse=True)
    hi, mid, lo = probs

    if hi == lo:
        return PROB_BACKMAP[min(hi, 12)]

    # Find base index for this (hi, lo) pair
    base = 0
    for h in range(1, min(hi, 12)):
        base += h
    base += min(hi, 12) - max(lo, 1)
    if base >= 78:
        base = 77

    # Pick best group based on mid value
    mid_g0 = (hi + lo + 1) // 2
    mid_g1 = (3 * hi + lo + 2) // 4
    mid_g2 = (hi + 3 * lo + 2) // 4

    d0 = abs(mid - mid_g0)
    d1 = abs(mid - mid_g1)
    d2 = abs(mid - mid_g2)

    if d1 <= d0 and d1 <= d2:
        return base + 78
    elif d2 < d0:
        return base + 156
    return base


def parse_indirect_table(cpp_source):
    """Parse kQuad0122Ind[] from C++ source."""
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


def inject_languages(entries, injections, prob_value=4, protect=None):
    """Inject new languages into indirect table entries.

    Strategy:
    1. If source_pslang present and empty slot available: fill it (simple)
    2. If all slots full: replace the slot with the lowest probability
       (unless it's the source language or in the protected set)

    Args:
        entries: list of uint32 langprob values (modified in place)
        injections: list of (source_pslang, target_pslang) tuples
        prob_value: probability for injected language (1-12)
        protect: set of pslangs that must not be replaced

    Returns:
        stats dict
    """
    if protect is None:
        protect = set()

    stats = {"simple": 0, "replaced": 0, "skipped_present": 0, "skipped_protected": 0}

    for src_pslang, tgt_pslang in injections:
        for i in range(len(entries)):
            lp = entries[i]
            if lp == 0:
                continue

            prob_sub, l1, l2, l3 = decode_langprob(lp)
            langs = [l1, l2, l3]

            if src_pslang not in langs:
                continue
            if tgt_pslang in langs:
                stats["skipped_present"] += 1
                continue

            # Try empty slot first
            empty_slot = None
            for s in range(3):
                if langs[s] == 0:
                    empty_slot = s
                    break

            if empty_slot is not None:
                langs[empty_slot] = tgt_pslang
                # Recompute prob subscript with new language getting prob_value
                probs = list(get_probs_for_subscript(prob_sub))
                probs[empty_slot] = prob_value
                # Sort by probability descending, keeping lang-prob pairs together
                paired = sorted(zip(probs, langs), reverse=True)
                new_probs = [p for p, _ in paired]
                new_langs = [l for _, l in paired]
                new_sub = find_best_prob_subscript(*new_probs)
                entries[i] = encode_langprob(new_sub, new_langs[0], new_langs[1], new_langs[2])
                stats["simple"] += 1
                continue

            # All slots full — find the lowest-probability language to replace
            probs = list(get_probs_for_subscript(prob_sub))
            # Pair (prob, lang, slot_index) and sort ascending by prob
            paired = [(probs[s], langs[s], s) for s in range(3)]
            paired.sort()

            replaced = False
            for p, lang, slot in paired:
                if lang == src_pslang:
                    continue  # Never replace the source language
                if lang in protect:
                    continue  # Don't replace protected languages
                # Replace this language with the target
                langs[slot] = tgt_pslang
                probs[slot] = prob_value
                # Re-sort by probability
                repaired = sorted(zip(probs, langs), reverse=True)
                new_probs = [pr for pr, _ in repaired]
                new_langs = [la for _, la in repaired]
                new_sub = find_best_prob_subscript(*new_probs)
                entries[i] = encode_langprob(new_sub, new_langs[0], new_langs[1], new_langs[2])
                stats["replaced"] += 1
                replaced = True
                break

            if not replaced:
                stats["skipped_protected"] += 1

    return stats


def rebuild_cpp_indirect(original_source, new_entries):
    """Replace kQuad0122Ind[] in C++ source with modified entries."""
    lines = original_source.split('\n')
    result = []
    skip = False

    for line in lines:
        if 'kQuad0122Ind[' in line and '= {' in line:
            result.append(line)
            skip = True
            for i in range(0, len(new_entries), 4):
                chunk = new_entries[i:i+4]
                hex_vals = ', '.join(f'0x{v:08x}' for v in chunk)
                result.append(f'  {hex_vals},')
            continue

        if skip:
            if line.strip().startswith('};'):
                skip = False
                result.append(line)
            continue

        result.append(line)

    return '\n'.join(result)


def main():
    parser = argparse.ArgumentParser(description="Inject languages into CLD2 main quadgram table")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--inject", action="append", required=True,
                        help="source_pslang:target_pslang")
    parser.add_argument("--prob", type=int, default=4,
                        help="Probability value for injected languages (1-12)")
    parser.add_argument("--protect", type=int, nargs="*", default=[],
                        help="Pslangs that must not be replaced in full entries")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print(f"Reading {args.input}...", file=sys.stderr)
    with open(args.input, 'r') as f:
        source = f.read()

    entries = parse_indirect_table(source)
    print(f"Parsed {len(entries)} indirect entries", file=sys.stderr)

    injections = []
    for spec in args.inject:
        src, tgt = map(int, spec.split(':'))
        injections.append((src, tgt))

    protect = set(args.protect)
    # Always protect common major languages from replacement
    # (en=1, fr=5, es=11, de=6, pt=10, it=7, nl=3)
    protect.update({1, 3, 5, 6, 7, 10, 11})

    stats = inject_languages(entries, injections, prob_value=args.prob, protect=protect)

    print(f"Results:", file=sys.stderr)
    print(f"  Simple (empty slot): {stats['simple']}", file=sys.stderr)
    print(f"  Replaced (lowest prob): {stats['replaced']}", file=sys.stderr)
    print(f"  Skipped (already present): {stats['skipped_present']}", file=sys.stderr)
    print(f"  Skipped (all protected): {stats['skipped_protected']}", file=sys.stderr)
    print(f"  Total modified: {stats['simple'] + stats['replaced']}", file=sys.stderr)

    if args.dry_run:
        print("Dry run — no output written", file=sys.stderr)
        return

    print(f"Rebuilding C++ source...", file=sys.stderr)
    new_source = rebuild_cpp_indirect(source, entries)

    with open(args.output, 'w') as f:
        f.write(new_source)
    print(f"Written to {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
