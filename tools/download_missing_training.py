#!/usr/bin/env python3
"""Download GlotLID training data for languages missing from CLD2's quadgram table."""

import os
import sys


def download_lang(iso3, glotlid_config, output_dir, max_lines=10000):
    """Download training data for one language from GlotLID corpus."""
    from datasets import load_dataset

    outpath = os.path.join(output_dir, f"{iso3}_train.txt")
    if os.path.exists(outpath) and os.path.getsize(outpath) > 1000:
        n = sum(1 for _ in open(outpath))
        print(f"  {iso3}: already {n} lines, skipping")
        return

    try:
        ds = load_dataset("cis-lmu/glotlid-corpus", glotlid_config,
                          split="train", streaming=True)
        count = 0
        with open(outpath, "w", encoding="utf-8") as f:
            for row in ds:
                text = row.get("text", "").strip().replace("\n", " ")
                if len(text) > 20:
                    f.write(text + "\n")
                    count += 1
                    if count >= max_lines:
                        break
        print(f"  {iso3}: {count} lines -> {outpath}")
    except Exception as e:
        print(f"  {iso3}: FAILED ({type(e).__name__}: {str(e)[:80]})")
        open(outpath, "w").close()


def main():
    output_dir = "data/training"
    os.makedirs(output_dir, exist_ok=True)

    # Languages with existing CLD2 PLang but no quadgram data
    languages = {
        "hau": "hau_Latn",     # Hausa
        "yor": "yor_Latn",     # Yoruba
        "bre": "bre_Latn",     # Breton
        "oci": "oci_Latn",     # Occitan
        "sna": "sna_Latn",     # Shona
        "orm": "gaz_Latn",     # Oromo (West Central)
        "tat": "tat_Cyrl",     # Tatar (Cyrillic in GlotLID)
        "fry": "fry_Latn",     # Western Frisian
        "san": "san_Deva",     # Sanskrit (Devanagari)
        "xho": "xho_Latn",     # Xhosa
        "grn": "gug_Latn",     # Guarani (Paraguayan)
        "ibo": "ibo_Latn",     # Igbo
        "amh": "amh_Ethi",     # Amharic (Ethiopic)
        "asm": "asm_Beng",     # Assamese (Bengali script)
    }

    print(f"Downloading training data for {len(languages)} languages...")
    for iso3, config in languages.items():
        download_lang(iso3, config, output_dir)

    print("\nDone.")


if __name__ == "__main__":
    main()
