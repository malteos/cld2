# Bengali vs. Confusable Languages (ben_Beng)

## Bengali vs. Assamese (CRITICAL - Extremely Confusable)

Bengali and Assamese are the most confusable language pair in the Eastern Indo-Aryan family. Both languages use variants of the Eastern Nagari script, share substantial vocabulary, and have similar grammatical structures. Accurate discrimination is essential.

### Script Differences (Most Reliable Signals)

The single most reliable distinguishing feature is the letter for /r/:

- **Bengali র** (U+09B0) - The standard ra character
- **Assamese ৰ** (U+09F0) - A distinct character with a downward stroke (middle ra)

Any text containing **ৰ** is almost certainly Assamese, not Bengali. Conversely, text using **র** for /r/ throughout is Bengali.

Additionally, Assamese has the letter **ৱ** (U+09F1, Assamese wa), which does not exist in Bengali. The presence of ৱ is a definitive Assamese marker.

In summary:
| Feature | Bengali | Assamese |
|---|---|---|
| /r/ consonant | র (U+09B0) | ৰ (U+09F0) |
| /w/ consonant | (none; uses ওয়) | ৱ (U+09F1) |

### Phonological Differences

- Assamese has **velar fricatives** /x/ (written খ in certain positions) that Bengali lacks
- Assamese has a more extensive vowel inventory, including /ɯ/ (high back unrounded vowel, written as উ in some contexts)
- Bengali preserves the distinction between শ /ʃ/, ষ /ʃ/, and স /s/ in spelling (though pronunciation has merged); Assamese has merged these further
- The inherent vowel in Assamese is /ɔ/ as in Bengali, but some Assamese dialects realize it differently

### Vocabulary Differences

Many common words differ between the two languages:

| English | Bengali | Assamese |
|---|---|---|
| "beautiful" | সুন্দর (sundor) | ধুনীয়া (dhuniya) |
| "child" | শিশু/বাচ্চা (shishu/bachcha) | লৰা/ছোৱালী (lora/suwali) |
| "to eat" | খাওয়া (khaowa) | খোৱা (khuwa) |
| "to speak" | বলা (bola) | কোৱা (kuwa) |
| "house" | বাড়ি (bari) | ঘৰ (ghor) |
| "water" | জল/পানি (jol/pani) | পানী (pani) |
| "big" | বড় (boro) | ডাঙৰ (dangor) |
| "small" | ছোট (chhoto) | সৰু (xoru) |

### Grammatical Differences

- Assamese uses different verb conjugation patterns, particularly in the present tense
- Assamese classifier system differs: -টো (-to), -খন (-khon), -জন (-jon) vs. Bengali -টা (-ta), -টি (-ti), -জন (-jon)
- Assamese has distinct case markers and postpositions

### Detection Strategy

1. **First check**: Scan for ৰ (U+09F0) or ৱ (U+09F1) - if present, classify as Assamese
2. **Second check**: Look for র (U+09B0) usage - if consistently used for /r/, likely Bengali
3. **Third check**: Vocabulary analysis for Assamese-specific words
4. **Fourth check**: Verb endings and grammatical patterns

## Bengali vs. Hindi (Devanagari Script)

Bengali and Hindi, while both Indo-Aryan languages, are readily distinguishable by their scripts:

- **Bengali** uses the Bengali/Eastern Nagari script (U+0980-U+09FF)
- **Hindi** uses the Devanagari script (U+0900-U+097F)

These are entirely different Unicode blocks with no overlapping characters, making script-based discrimination trivial. However, there are linguistic similarities to note:

- Both are SOV languages with postpositions
- Shared Sanskrit-derived vocabulary (তৎসম/tatsama words)
- Hindi has grammatical gender (masculine/feminine); Bengali does not
- Hindi uses the inherent vowel /a/; Bengali uses /ɔ/
- Hindi has a richer case system with postpositional case markers (ne, ko, se, me, par)

## Bengali vs. Odia (Similar Script Ancestry)

Bengali and Odia scripts share a common ancestor (Eastern Nagari) and have some visual similarities, but the Odia script has a distinctive **rounded appearance** compared to Bengali's more angular forms:

- Odia script occupies Unicode block U+0B00-U+0B7F
- Odia characters have characteristic curved tops (due to palm-leaf manuscript tradition) while Bengali characters have a horizontal head-stroke (matra line)
- The scripts are distinct enough for reliable automated discrimination via Unicode ranges

Linguistically:
- Both are Eastern Indo-Aryan SOV languages
- Odia has a somewhat different vowel system and phonological inventory
- Shared literary and cultural heritage through the broader Eastern Indian tradition

## Bengali vs. Sylheti

Sylheti (সিলেটি/ꠍꠤꠟꠐꠤ) is sometimes classified as a dialect of Bengali, sometimes as a separate language. For language identification:

- Sylheti has its own script called **Sylheti Nagari** (ꠍꠤꠟꠐꠤ ꠘꠣꠉꠞꠤ), in Unicode block U+A800-U+A82F, though Sylheti is also frequently written in Bengali script or Latin script
- When written in Bengali script, Sylheti text may show phonological differences: absence of aspirated consonants, different vowel patterns
- Sylheti has lost the aspirated/unaspirated distinction that Bengali maintains
- Mutual intelligibility is limited, particularly in spoken form

## Bengali vs. Chakma

Chakma (𑄌𑄋𑄴𑄟𑄳𑄦𑄃𑄧) is a related language spoken in the Chittagong Hill Tracts:

- Uses the Chakma script (U+11100-U+1114F), completely distinct from Bengali script
- When written in Bengali script, distinguishable by vocabulary and grammatical differences
- Much smaller speaker population than Bengali

## Summary of Key Discriminators

| Comparison | Primary Signal | Reliability |
|---|---|---|
| Bengali vs. Assamese | র vs. ৰ, absence/presence of ৱ | Very High |
| Bengali vs. Hindi | Unicode block (Bengali vs. Devanagari) | Definitive |
| Bengali vs. Odia | Unicode block, character shapes | Definitive |
| Bengali vs. Sylheti | Script (if Sylheti Nagari), vocabulary/phonology | Moderate-High |
| Bengali vs. Chakma | Unicode block (if Chakma script) | Definitive |
