#!/usr/bin/env python3
"""
Inject new language quadgrams into an existing CLD2 quadgram table.

Instead of using a separate table 2, this injects entries directly into
the primary table's empty bucket slots. This allows new languages to
compete fairly with existing languages.

Usage:
    python3 tools/inject_into_table.py \
        --source internal/cld2_generated_quad0122.cc \
        --langs arg:122,vec:123 \
        --training-dir data/training \
        --max-quadgrams 2000
"""

import argparse
import os
import re
import struct
import sys
from collections import Counter, defaultdict

# Import hash functions from build_quadgram_table
sys.path.insert(0, os.path.dirname(__file__))
from build_quadgram_table import (
    extract_quadgrams, quad_hash_v2_underscore, compute_quadgram_freqs
)


def parse_table(source_path):
    """Parse the C++ source to extract table parameters."""
    with open(source_path) as f:
        content = f.read()

    # Extract key parameters
    size_match = re.search(r'kQuad\w+Size = (\d+);.*Bucket count', content)
    keymask_match = re.search(r'kQuad\w+KeyMask = (0x[0-9a-f]+);', content)
    sizeone_match = re.search(r'kQuad\w+SizeOne = (\d+);', content)

    if not all([size_match, keymask_match, sizeone_match]):
        print("ERROR: Could not parse table parameters", file=sys.stderr)
        sys.exit(1)

    bucket_count = int(size_match.group(1))
    key_mask = int(keymask_match.group(1), 16)
    size_one = int(sizeone_match.group(1))

    print(f"Table: {bucket_count} buckets, keymask=0x{key_mask:08x}, sizeone={size_one}",
          file=sys.stderr)

    # Extract bucket data
    table_match = re.search(r'(kQuad\w+)\[' + str(bucket_count) + r'\]', content)
    table_name = table_match.group(1) if table_match else None

    # Extract indirect table
    ind_match = re.search(r'(kQuad\w+Ind)\[(\d+)\]', content)
    ind_name = ind_match.group(1) if ind_match else None
    ind_size = int(ind_match.group(2)) if ind_match else 0

    return {
        'bucket_count': bucket_count,
        'key_mask': key_mask,
        'size_one': size_one,
        'table_name': table_name,
        'ind_name': ind_name,
        'ind_size': ind_size,
    }


def count_empty_slots(source_path, bucket_count):
    """Count empty bucket slots in the table."""
    with open(source_path) as f:
        content = f.read()

    # Find all bucket entries (groups of 4 hex values)
    bucket_pattern = re.compile(r'\{(0x[0-9a-f]+),(0x[0-9a-f]+),(0x[0-9a-f]+),(0x[0-9a-f]+)\}')
    matches = bucket_pattern.findall(content)

    empty_slots = 0
    for m in matches[:bucket_count]:
        for v in m:
            if int(v, 16) == 0:
                empty_slots += 1

    total_slots = bucket_count * 4
    print(f"Empty slots: {empty_slots}/{total_slots} ({100*empty_slots/total_slots:.1f}%)",
          file=sys.stderr)
    return empty_slots


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--langs", required=True)
    parser.add_argument("--training-dir", default="data/training")
    parser.add_argument("--max-quadgrams", type=int, default=2000)
    args = parser.parse_args()

    params = parse_table(args.source)
    empty = count_empty_slots(args.source, params['bucket_count'])

    lang_configs = {}
    for pair in args.langs.split(','):
        parts = pair.strip().split(':')
        if len(parts) == 2:
            lang_configs[parts[0]] = int(parts[1])

    print(f"\nLanguages to inject: {list(lang_configs.keys())}", file=sys.stderr)
    print(f"Max quadgrams per language: {args.max_quadgrams}", file=sys.stderr)
    print(f"Available empty slots: {empty}", file=sys.stderr)


if __name__ == "__main__":
    main()
