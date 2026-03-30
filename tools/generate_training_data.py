#!/usr/bin/env python3
"""
Generate linguistically-targeted training data for low-F1 CLD2 languages.

Produces JSONL files with {"text": "...", "lang": "...", "rationale": "..."}
where each sentence is dense in distinctive features that produce unique quadgrams.

Usage:
    python3 tools/generate_training_data.py --lang acf gcr lin gcf \
        --samples-per-lang 800 --output-dir data/training/
"""

import argparse
import json
import os
import random
import sys

random.seed(42)

# ============================================================================
# Language specifications: templates, vocabulary banks, and feature definitions
# ============================================================================

LANG_SPECS = {
    # ---- Saint Lucian Creole French (acf) ----
    "acf": {
        "name": "Saint Lucian Creole French",
        "features": ["sé plural", "sété copula", "épi conjunction", "possessive ʼy", "pronoun i"],
        "templates": [
            "Sé {noun_pl}-an ka {verb} {place} épi {noun2}.",
            "I sété {adj} {noun} épi i ka {verb} {place}.",
            "Mwen ka {verb} épi fwèʼy jounen-an.",
            "Sé ti-manmay la ka {verb} {place} épi manmanʼy.",
            "I kwiyé sé {noun_pl}-an épi diʼy {sentence_end}.",
            "Sé {noun_pl} la sété {adj} épi yo ka {verb}.",
            "Manmanʼy sété bon épi i ka bay sé ti-moun an {noun2}.",
            "Mwen ka palé Kwéyòl épi sé moun-an.",
            "Jounen-an sété {adj} épi sé {noun_pl}-an ka {verb}.",
            "I ka {verb} épi papaʼy dan sé {noun_pl}-an.",
            "Sé pyé bwa a sété {adj} épi sé zwazo a ka {verb}.",
            "Baʼy {noun2} épi diʼy sa sété bon.",
            "Sé moun-an ka fèté jounen Kwéyòl épi {noun2}.",
            "I sété an {adj} {noun} épi i ka kwiyé sé zanmiʼy.",
            "Mwen ka alé épi fwèʼy dan sé mòn-an.",
        ],
        "noun_pl": ["moun", "ti-manmay", "pyé bwa", "zwazo", "pwason", "kochon",
                     "kannot", "flè", "kay", "wòch", "bato", "fig", "zanmi"],
        "noun2": ["dlo", "manje", "lajan", "bannann", "pwason", "fig", "lapli"],
        "noun": ["moun", "papa", "manman", "fwè", "zanmi", "gason", "fi"],
        "verb": ["palé", "manjé", "dansé", "chanté", "maché", "jwé", "kwiyé",
                 "wè", "pwan", "bay", "alé", "vini", "woulé"],
        "adj": ["bon", "bèl", "gwo", "piti", "jòn", "vèt", "nwè", "vyé"],
        "place": ["anba pyé bwa a", "bò lanmè a", "dan mòn-an", "an lavil",
                  "bò rivyè a", "dan jaden-an", "anba soléy la"],
        "sentence_end": ["pou vini", "pou manjé", "pou jwé", "sa sété bon",
                         "pou palé Kwéyòl", "pou fèté jounen-an"],
    },

    # ---- Guianese Creole French (gcr) ----
    "gcr": {
        "name": "Guianese Creole French",
        "features": ["mo/to/so possessive", "ka progressive", "-yan plural", "preposed possessive"],
        "templates": [
            "Mo ka {verb} dan mo kaz épi so {noun}.",
            "To ka {verb} paské to ka bezwen {noun}.",
            "Sé moun-yan ka {verb} épi yé ka {verb2}.",
            "Mo ka {verb} épi to fanm dan so kaz.",
            "Yé ka {verb} paské sé moun-yan ka bezwen {noun}.",
            "So pitit ka {verb} dan mo kaz épi mo {noun}.",
            "To ka {verb} atò to ka alé dan to kaz.",
            "Mo kaz sété {adj} épi mo ka {verb} dèyè so kaz.",
            "Sé zanmi-yan ka {verb} paské yé ka bezwen {noun}.",
            "Mo ka {verb} épi so fanm dan sé kaz-yan.",
            "To ka bay mo pitit {noun} paské so {noun2} pa bon.",
            "Yé ka palé paské sé moun-yan ka travay.",
            "Mo ka alé dan mo kaz épi mo ka {verb} so {noun}.",
            "To ka {verb} dèyè mo kaz atò to ka {verb2}.",
            "So pitit sété {adj} épi yé ka {verb} dan sé kaz-yan.",
        ],
        "noun": ["kaz", "fanm", "pitit", "lajan", "manje", "rivyè", "pirog",
                 "jardin", "bwa", "dlo", "zanmi", "travay"],
        "noun2": ["manje", "dlo", "lajan", "travay", "bwa"],
        "verb": ["manjé", "travay", "palé", "chanté", "maché", "lavé", "pêché",
                 "gadé", "tandé", "rivé", "alé", "vini"],
        "verb2": ["manjé", "dòmi", "palé", "chanté", "travay", "alé"],
        "adj": ["bon", "bèl", "gran", "piti", "vyé", "nèf"],
    },

    # ---- Lingala (lin) ----
    "lin": {
        "name": "Lingala",
        "features": ["prenasalized mb/nd/ng/nk", "noun class prefixes", "oyo relative", "te negative"],
        "templates": [
            "Mbote na yo! {subject} azali na ndako na ngai.",
            "{subject} alingi koluka mbongo na nzela ya {place}.",
            "Bato nyonso bazali na mposa ya {noun} mpo na {purpose}.",
            "Mokolo oyo, {subject} akokende na {place} mpo na {verb_inf}.",
            "Mwana oyo azali na ndako na ngai te, alingi kokende na {place}.",
            "Mbote! Sango nini? {subject} azali na nzela ya ndako.",
            "Bana ba ngai bazali na mposa ya biloko ya kolya mpo na ntongo.",
            "Moto oyo alingi mbongo mpo na kosomba {noun} na {place}.",
            "{subject} azali na nkombo ya {name}, auti na mboka ya Kinshasa.",
            "Na ntango ya mbula, bato bazali na ndako na bango te.",
            "Ndeko na ngai alingi koluka nzela mpo na kokende na {place}.",
            "Mbote na ntongo! {subject} azali na ndako épi azali malamu.",
            "Bato oyo bazali na mposa ya ndako ya malamu mpo na bana na bango.",
            "Mwasi oyo azali na nzela ya ndako na ye mpo na kolamba.",
            "{subject} ayebi koloba Lingala épi azali na ndako na ngai.",
            "Sango malamu! Bato nyonso bazali na mposa ya nzete mpo na mbula.",
            "Mokolo oyo, moto te akokende na nzela mpo na mbongo.",
            "Ndeko na ngai alingi kosomba mésa épi kiti mpo na ndako na ye.",
            "Mbote! {subject} azali na nkombo ya {name} épi alingi {verb_inf}.",
            "Na ntango ya ntongo, bato bazali na nzela ya ndako na bango.",
        ],
        "subject": ["Moto oyo", "Mwana", "Ndeko na ngai", "Mobali oyo",
                    "Mwasi oyo", "Mokonzi", "Nkoko na ngai"],
        "noun": ["mbongo", "biloko", "nzete", "ndako", "nzela", "mbula",
                "mposa", "nkombo", "mángu", "búku", "sapátu", "mésa"],
        "place": ["mboka", "ndako ya nkoko", "engumba ya Kinshasa",
                 "nzela monene", "ndako ya Nzambe", "mai ya ebale"],
        "verb_inf": ["koluka mbongo", "kosomba biloko", "kolamba mpo na bato",
                    "koyekola", "kobina", "koloba na bato", "kotanga búku"],
        "purpose": ["kobika malamu", "koyekola", "kosomba biloko",
                   "kotonga ndako", "kolamba", "kobina"],
        "name": ["Bokelo", "Mpasi", "Nkumu", "Mbala", "Nzongo"],
    },

    # ---- Guadeloupean Creole French (gcf) ----
    "gcf": {
        "name": "Guadeloupean Creole French",
        "features": ["gy/ky orthography", "a-w/a-y possessive", "fò modal", "la article"],
        "templates": [
            "Sa ou fé? Fò-w alé adan kaz a-w.",
            "Sé moun la ka dansé gwoka épi {noun} a-y.",
            "Fò-nou {verb} kè sé zanmi a-nou ka vini.",
            "An ké rakonté a-w on bèl istwa: krik krak!",
            "Fò-w gadé {noun} la kè i ka {verb} a-y.",
            "Sé moun la ka manjé kassav épi {noun} a-y.",
            "Fò-y alé adan kaz a-y paské karnaval ka rivé.",
            "Krik krak! An ké di a-w sa ki rivé a-y.",
            "Fò-w {verb} épi sé zanmi a-w kè yo ka {verb2}.",
            "Sé timoun la ka jwé gwoka épi {noun} a-y.",
            "Fò-nou palé kè sé moun la ka vini adan kaz a-nou.",
            "An ké bay a-w on gyèl kè fò-w gadé.",
            "Sé fanm la ka {verb} épi {noun} a-y adan lavil la.",
            "Fò-w tandé kè sé moun la ka chanté gwoka.",
            "Kaz a-w sété bèl épi fò-y {verb} a-y.",
        ],
        "noun": ["dlo", "manje", "flè", "fwi", "pwason", "kann", "bannann",
                "kabrit", "matadò", "chivrèt"],
        "verb": ["gadé", "manjé", "dansé", "chanté", "palé", "maché",
                "tandé", "rivé", "alé"],
        "verb2": ["dansé", "chanté", "manjé", "jwé", "palé"],
    },
}


def generate_template_samples(lang_code, n_samples):
    """Generate training samples using templates and vocabulary banks."""
    spec = LANG_SPECS[lang_code]
    templates = spec["templates"]
    samples = []

    for i in range(n_samples):
        template = random.choice(templates)
        # Fill all {slot} placeholders
        filled = template
        for key in spec:
            if key in ("name", "features", "templates"):
                continue
            if isinstance(spec[key], list):
                placeholder = "{" + key + "}"
                while placeholder in filled:
                    filled = filled.replace(placeholder, random.choice(spec[key]), 1)

        # Identify which features are present
        features_used = []
        for feat in spec["features"]:
            # Simple heuristic: check if any feature-related text is in the output
            feat_lower = feat.lower()
            if any(kw in filled.lower() for kw in feat_lower.split("/")):
                features_used.append(feat)

        # More specific feature detection
        if lang_code == "acf":
            if "sé " in filled:
                features_used.append("sé plural")
            if "sété" in filled:
                features_used.append("sété copula")
            if "épi" in filled:
                features_used.append("épi conjunction")
            if "ʼy" in filled:
                features_used.append("possessive ʼy")
        elif lang_code == "gcr":
            if any(f"{p} ka" in filled for p in ["mo", "to", "yé"]):
                features_used.append("progressive ka")
            if any(f"{p} kaz" in filled or f"{p} fanm" in filled for p in ["mo", "to", "so"]):
                features_used.append("preposed possessive")
            if "-yan" in filled:
                features_used.append("-yan plural")
        elif lang_code == "lin":
            if any(nc in filled.lower() for nc in ["mb", "nd", "ng", "nk", "nz", "mp", "nt"]):
                features_used.append("prenasalized consonants")
            if "oyo" in filled:
                features_used.append("oyo relative")
            if " te" in filled or filled.endswith(" te"):
                features_used.append("te negative")
        elif lang_code == "gcf":
            if "gy" in filled.lower() or "ky" in filled.lower():
                features_used.append("gy/ky orthography")
            if "a-w" in filled or "a-y" in filled or "a-nou" in filled:
                features_used.append("possessive a-w/a-y")
            if "fò" in filled.lower():
                features_used.append("fò modal")

        features_used = list(set(features_used))

        samples.append({
            "text": filled,
            "lang": lang_code,
            "rationale": f"Features: {', '.join(features_used) if features_used else 'general vocabulary'}",
        })

    return samples


def main():
    parser = argparse.ArgumentParser(description="Generate training data for low-F1 languages")
    parser.add_argument("--lang", nargs="+", default=["acf", "gcr", "lin", "gcf"],
                        help="Language codes to generate")
    parser.add_argument("--samples-per-lang", type=int, default=800,
                        help="Number of samples per language")
    parser.add_argument("--output-dir", default="data/training",
                        help="Output directory for JSONL files")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    args = parser.parse_args()

    random.seed(args.seed)
    os.makedirs(args.output_dir, exist_ok=True)

    for lang in args.lang:
        if lang not in LANG_SPECS:
            print(f"WARNING: No spec for {lang}, skipping", file=sys.stderr)
            continue

        outpath = os.path.join(args.output_dir, f"{lang}_generated.jsonl")
        samples = generate_template_samples(lang, args.samples_per_lang)

        with open(outpath, "w", encoding="utf-8") as f:
            for s in samples:
                f.write(json.dumps(s, ensure_ascii=False) + "\n")

        # Stats
        feature_counts = {}
        for s in samples:
            for feat in s["rationale"].replace("Features: ", "").split(", "):
                feature_counts[feat] = feature_counts.get(feat, 0) + 1

        print(f"{lang}: {len(samples)} samples -> {outpath}")
        for feat, count in sorted(feature_counts.items(), key=lambda x: -x[1]):
            print(f"  {feat}: {count} ({count/len(samples)*100:.0f}%)")


if __name__ == "__main__":
    main()
