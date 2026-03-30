#!/usr/bin/env python3
"""
Download all datasets needed for CLD2 language extension.

- Evaluation: CommonLID from HuggingFace (gated, needs HF_TOKEN)
- Training: GlotLID corpus for new languages + contrast languages

Usage:
    python3 tools/download_data.py [--eval-only] [--train-only]
"""

import argparse
import gzip
import os
import shutil
import sys


def download_evaluation_data(output_dir="data/evaluation"):
    """Download CommonLID evaluation dataset."""
    from huggingface_hub import hf_hub_download

    os.makedirs(output_dir, exist_ok=True)
    dest = os.path.join(output_dir, "commonlid.tsv.gz")
    if os.path.exists(dest) and os.path.getsize(dest) > 1_000_000:
        print(f"  CommonLID already exists ({os.path.getsize(dest)//1024}KB), skipping")
        return

    print("Downloading CommonLID evaluation dataset...")
    path = hf_hub_download(
        repo_id="commoncrawl/CommonLID",
        repo_type="dataset",
        filename="commonlid_20251209.tsv.gz",
        token=os.environ.get("HF_TOKEN", ""),
    )
    shutil.copy2(path, dest)
    # Count lines
    with gzip.open(dest, "rt") as f:
        n = sum(1 for _ in f) - 1
    print(f"  Saved to {dest} ({n} samples)")


def download_training_data(output_dir="data/training"):
    """Download GlotLID training data for new + contrast languages."""
    from datasets import load_dataset

    os.makedirs(output_dir, exist_ok=True)

    # New languages that need quadgram tables (ISO 639-3 -> GlotLID config)
    new_languages = {
        "arg": "arg_Latn",     # Aragonese
        "vec": "vec_Latn",     # Venetian
        "acf": "acf_Latn",     # Saint Lucian Creole French
        "crh": "crh_Latn",     # Crimean Tatar
        "rcf": "rcf_Latn",     # Réunion Creole French
        "gom": "gom_Deva",     # Goan Konkani (Devanagari)
        "lin": "lin_Latn",     # Lingala
        "gcf": "gcf_Latn",     # Guadeloupean Creole French
        "bik": "bik_Latn",     # Bikol (also covers bcl)
        "lij": "lij_Latn",     # Ligurian
        "kab": "kab_Latn",     # Kabyle
        "gcr": "gcr_Latn",     # Guianese Creole French
        "kik": "kik_Latn",     # Kikuyu
        "ltg": "ltg_Latn",     # Latgalian
        "fuv": "fuv_Latn",     # Nigerian Fulfulde
        "ext": "ext_Latn",     # Extremaduran
        "nyn": "nyn_Latn",     # Nyankore
        "guw": "guw_Latn",     # Gun
        "pcm": "pcm_Latn",     # Nigerian Pidgin
    }

    # Contrast languages (already in CLD2, used for filtering distinctive quadgrams)
    contrast_languages = {
        "spa": "spa_Latn",     # Spanish (contrast for arg, ext)
        "eng": "eng_Latn",     # English (contrast for pcm, etc.)
        "ita": "ita_Latn",     # Italian (contrast for vec, lij)
        "fra": "fra_Latn",     # French (contrast for acf, rcf, gcf, gcr)
        "por": "por_Latn",     # Portuguese
        "tgl": "tgl_Latn",     # Tagalog (contrast for bik)
        "ind": "ind_Latn",     # Indonesian
        "tur": "tur_Latn",     # Turkish (contrast for crh)
        "hin": "hin_Deva",     # Hindi (contrast for gom)
        "mar": "mar_Deva",     # Marathi (contrast for gom)
        "yor": "yor_Latn",     # Yoruba (contrast for lin)
        "tat": "tat_Cyrl",     # Tatar (contrast for crh)
        "hat": "hat_Latn",     # Haitian Creole (contrast for acf, rcf, gcf, gcr)
        "lvs": "lvs_Latn",     # Latvian (contrast for ltg)
    }

    max_lines_new = 10_000
    max_lines_contrast = 5_000

    # Download new languages
    print(f"\nDownloading training data for {len(new_languages)} new languages...")
    for iso3, config in new_languages.items():
        outpath = os.path.join(output_dir, f"{iso3}_train.txt")
        if os.path.exists(outpath) and os.path.getsize(outpath) > 100:
            n = sum(1 for _ in open(outpath))
            print(f"  {iso3}: already {n} lines, skipping")
            continue
        try:
            ds = load_dataset("cis-lmu/glotlid-corpus", config, split="train",
                              streaming=True)
            count = 0
            with open(outpath, "w", encoding="utf-8") as f:
                for row in ds:
                    text = row.get("text", "").strip().replace("\n", " ")
                    if len(text) > 20:
                        f.write(text + "\n")
                        count += 1
                        if count >= max_lines_new:
                            break
            print(f"  {iso3}: {count} lines -> {outpath}")
        except Exception as e:
            print(f"  {iso3}: FAILED ({type(e).__name__}: {str(e)[:60]})")
            # Write empty file to mark as attempted
            open(outpath, "w").close()

    # Download contrast languages
    print(f"\nDownloading contrast data for {len(contrast_languages)} existing languages...")
    for iso3, config in contrast_languages.items():
        outpath = os.path.join(output_dir, f"{iso3}_contrast.txt")
        if os.path.exists(outpath) and os.path.getsize(outpath) > 100:
            n = sum(1 for _ in open(outpath))
            print(f"  {iso3}: already {n} lines, skipping")
            continue
        try:
            ds = load_dataset("cis-lmu/glotlid-corpus", config, split="train",
                              streaming=True)
            count = 0
            with open(outpath, "w", encoding="utf-8") as f:
                for row in ds:
                    text = row.get("text", "").strip().replace("\n", " ")
                    if len(text) > 20:
                        f.write(text + "\n")
                        count += 1
                        if count >= max_lines_contrast:
                            break
            print(f"  {iso3}: {count} lines -> {outpath}")
        except Exception as e:
            print(f"  {iso3}: FAILED ({type(e).__name__}: {str(e)[:60]})")
            open(outpath, "w").close()


def main():
    parser = argparse.ArgumentParser(description="Download datasets for CLD2 language extension")
    parser.add_argument("--eval-only", action="store_true", help="Only download evaluation data")
    parser.add_argument("--train-only", action="store_true", help="Only download training data")
    args = parser.parse_args()

    if not args.train_only:
        download_evaluation_data()

    if not args.eval_only:
        download_training_data()

    print("\nDone.")


if __name__ == "__main__":
    main()
