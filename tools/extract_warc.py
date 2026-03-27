#!/usr/bin/env python3
"""Extract HTML pages from Common Crawl WARC files into a single JSONL file.

Each line is a JSON object: {"id": 0, "html": "<base64-encoded content>", "size": 12345}
Base64 encoding is used since HTML can contain arbitrary bytes.

Usage:
    python extract_warc.py --warc <path> [--num-pages N] [--output PATH]
"""

import argparse
import base64
import json
import os

from warcio.archiveiterator import ArchiveIterator


def extract_html_pages(warc_path: str, num_pages: int, output_path: str):
    if os.path.exists(output_path):
        # Check if existing file has enough pages
        with open(output_path) as f:
            existing = sum(1 for _ in f)
        if existing >= num_pages:
            print(f"Cache already has {existing} pages (>= {num_pages}), skipping extraction.")
            return

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    count = 0
    total_bytes = 0
    with open(output_path, "w") as out, open(warc_path, "rb") as f:
        for record in ArchiveIterator(f):
            if count >= num_pages:
                break
            if record.rec_type != "response":
                continue
            if not record.http_headers:
                continue
            if record.http_headers.get_statuscode() != "200":
                continue
            content_type = record.http_headers.get_header("Content-Type") or ""
            if "text/html" not in content_type:
                continue
            content = record.content_stream().read()
            line = json.dumps({
                "id": count,
                "html": base64.b64encode(content).decode("ascii"),
                "size": len(content),
            })
            out.write(line + "\n")
            total_bytes += len(content)
            count += 1
            if count % 1000 == 0:
                print(f"  extracted {count} pages...")

    print(f"Extracted {count} pages ({total_bytes:,} bytes) to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Extract HTML from WARC files")
    parser.add_argument("--warc", required=True, help="Path to .warc.gz file")
    parser.add_argument("--num-pages", type=int, default=10000, help="Number of pages to extract")
    parser.add_argument("--output", default="./data/benchmark/cache.jsonl", help="Output JSONL file")
    args = parser.parse_args()

    extract_html_pages(args.warc, args.num_pages, args.output)


if __name__ == "__main__":
    main()
