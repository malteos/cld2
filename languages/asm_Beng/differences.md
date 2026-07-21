# Assamese (asm_Beng) - Differentiation from Confusable Languages

## Bengali (ben_Beng) - EXTREMELY CONFUSABLE

Bengali and Assamese are the most confusable pair in the Eastern Nagari script family. They share the same script base, similar grammar, and significant lexical overlap. Accurate discrimination requires attention to specific characters, phonological patterns, and vocabulary differences.

### Script-Level Differences (PRIMARY DIAGNOSTIC)

| Feature | Assamese | Bengali | Notes |
|---------|----------|---------|-------|
| Ra letter | **ৰ** (U+09F0) | **র** (U+09B0) | **MOST CRITICAL** diagnostic |
| Wa/Va letter | **ৱ** (U+09F1) | Not used (ব is used) | **DEFINITIVE** Assamese marker |
| Ra frequency | ৰ is extremely frequent | র is extremely frequent | Check which codepoint is used |

**Detection Algorithm:**
1. Scan for ৰ (U+09F0) -- if present, classify as Assamese
2. Scan for ৱ (U+09F1) -- if present, classify as Assamese
3. If only র (U+09B0) is found for /r/ sounds, lean toward Bengali
4. Use vocabulary/morphological features as secondary signals

### Phonological Differences Reflected in Spelling

| Feature | Assamese | Bengali | Example |
|---------|----------|---------|---------|
| Velar fricative | /x/ for খ | /kʰ/ for খ | খোৱা (xowa) vs খাওয়া (khawa) "eating" |
| Sibilant merger | শ, ষ -> /x/; স -> /s/ | শ -> /ʃ/; স -> /s/ | Assamese: শ and ষ pronounced /x/ |
| Retroflex neutralization | Reduced retroflex distinction | Full retroflex series | Assamese neutralizes ড/ড় in some positions |

### Vocabulary Differences

| Meaning | Assamese | Bengali |
|---------|----------|---------|
| very | বৰ (bor) | খুব (khub) |
| what | কি (ki) | কী (ki) |
| how | কেনেকৈ (kenekoi) | কীভাবে (kibhabe) |
| to say | কোৱা (kowa) | বলা (bola) |
| to eat | খোৱা (xowa) | খাওয়া (khawa) |
| to come | অহা (oha) | আসা (asha) |
| to go | যোৱা (jowa) | যাওয়া (jaowa) |
| to see | দেখা (dekha) | দেখা (dekha) - same |
| child | ল'ৰা (lora) | ছেলে (chhele) |
| girl | ছোৱালী (sowali) | মেয়ে (meye) |
| beautiful | ধুনীয়া (dhuniya) | সুন্দর (sundor) |
| saying/that (quotative) | বুলি (buli) | বলে (bole) |
| question particle | নে / নেকি (ne/neki) | কি / না (ki/na) |
| now | এতিয়া (etiya) | এখন (ekhon) |
| today | আজি (aji) | আজ (aj) |
| house | ঘৰ (ghor) | বাড়ি (bari) / ঘর (ghor) |

### Morphological Differences

| Feature | Assamese | Bengali |
|---------|----------|---------|
| Genitive marker | -ৰ (-r, uses ৰ U+09F0) | -র (-r, uses র U+09B0) or -এর (-er) |
| Definite articles/classifiers | -জন, -গৰাকী, -খন, -টো | -টা, -টি, -খানা, -খানি |
| Present perfect | কৰিছে (korise) | করেছে (koreche) |
| Past tense | কৰিলে (korile) | করল (korlo) |
| Future tense | কৰিব (korib) | করবে (korbe) |
| Infinitive | কৰিবলৈ (koriboloi) | করতে (korte) |
| 1st person ending | -ওঁ (-oõ, nasalized) | -ই (-i) |
| Progressive | কৰি আছে (kori ase) | করছে (korchhe) |
| Conditional | কৰিলে (korile) | করলে (korle) |

### Syntactic Differences

- Assamese uses **বুলি** (buli) as a quotative complementizer; Bengali uses **বলে** (bole)
- Assamese **classifier system** is more extensive than Bengali's
- Assamese has **no grammatical gender**; Bengali retains vestiges of grammatical gender in some contexts
- Assamese question particle **নেকি** (neki) is not used in Bengali

## Odia (ori_Orya) - Moderately Confusable

Odia (Oriya) is a sister Eastern Indo-Aryan language but uses a completely different script (Odia script), making script-level confusion impossible. However, at the phonological and lexical level, there are some similarities.

### Key Differences

| Feature | Assamese | Odia |
|---------|----------|------|
| Script | Eastern Nagari (Bengali/Assamese) | Odia script (rounded letterforms) |
| Script confusion risk | **None** - scripts are visually distinct | Odia has curved/rounded letters |
| Vocabulary overlap | Moderate (shared Sanskrit base) | Different everyday vocabulary |
| Verb morphology | Distinct endings (-ছে, -িলে) | Distinct endings (-ଛି, -ିଲା) |
| Phonology | /x/ for খ | /kʰ/ for ଖ |

Since the scripts are entirely different, visual identification is straightforward. Confusion only arises in romanized text.

## Sylheti (syl_Beng) - Moderately Confusable

Sylheti is sometimes written in the Bengali/Assamese script (though it has its own Sylheti Nagari script). When written in Bengali script, it can be confused with both Assamese and Bengali.

### Key Differences

| Feature | Assamese | Sylheti |
|---------|----------|---------|
| Script variants | Uses ৰ (U+09F0) and ৱ (U+09F1) | Uses Bengali র (U+09B0) when in Bengali script |
| Geographic origin | Assam | Sylhet (Bangladesh/NE India) |
| Tone | Non-tonal | Has some tonal features |
| Vocabulary | Standard Assamese lexicon | Distinct vocabulary with Arabic/Persian loanwords |
| Verb forms | Standard Eastern Indo-Aryan | Simplified verb morphology |
| Native script | Not applicable | Sylheti Nagari (ꠍꠤꠟꠐꠤ) - distinct |

When Sylheti is written in Bengali script, it will lack the Assamese-specific characters ৰ and ৱ, making discrimination from Assamese straightforward. The challenge is distinguishing Sylheti from Bengali, not from Assamese.

## Bishnupriya Manipuri (bpy_Beng)

Bishnupriya Manipuri also uses the Bengali script and is spoken in parts of northeastern India. It lacks the Assamese characters ৰ and ৱ and has distinct vocabulary and grammar influenced by Tibeto-Burman languages.

## Summary Decision Tree

```
Text in Eastern Nagari script?
├── Contains ৰ (U+09F0) or ৱ (U+09F1)?
│   └── YES -> ASSAMESE (high confidence)
├── Contains only র (U+09B0) for /r/?
│   ├── Contains Assamese-specific vocabulary (বৰ, বুলি, নেকি, কেনেকৈ)?
│   │   └── YES -> Likely ASSAMESE (may be informal/non-standard encoding)
│   │   └── NO -> Continue checking
│   ├── Contains Bengali-specific vocabulary (খুব, বলে, ছেলে, মেয়ে)?
│   │   └── YES -> BENGALI
│   └── Check verb morphology and classifiers
│       ├── Assamese patterns (-ছে with Assamese vocabulary, -গৰাকী, বুলি)
│       │   └── ASSAMESE
│       └── Bengali patterns (-চ্ছে, করেছে, -টি)
│           └── BENGALI
```
