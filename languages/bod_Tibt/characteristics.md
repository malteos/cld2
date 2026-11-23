# Tibetan LID Characteristics (bod_Tibt)

## Script and Unicode

### Unicode Range

The Tibetan script is encoded in the Unicode block **U+0F00 to U+0FFF** (Tibetan). This block contains 211 assigned characters covering:

- U+0F00-U+0F47: Syllable OM, digits, marks, consonants (ཀ through ཇ)
- U+0F49-U+0F6C: Consonants (ཉ through ཬ)
- U+0F71-U+0F97: Vowel signs, subjoined consonants
- U+0F99-U+0FBC: Subjoined consonants (continued), various signs
- U+0FBE-U+0FCC: Symbols, astrological signs
- U+0FCE-U+0FD4: Marks and signs
- U+0FD5-U+0FDA: Religious symbols (right-facing svasti sign, etc.)

### Unique and Diagnostic Characters

The following characters are highly diagnostic of Tibetan script and rarely if ever appear in non-Tibetan contexts:

- **ༀ** (U+0F00) — Tibetan syllable OM
- **་** (U+0F0B) — Tsheg, the syllable delimiter (extremely frequent)
- **།** (U+0F0D) — Shad, the sentence/clause delimiter
- **༔** (U+0F14) — Gter tsheg, used in religious texts
- **༄༅** (U+0F04, U+0F05) — Initial decorative marks (head marks)
- **ྃ** (U+0F83) — Visarga/anusvara-like mark (sna ldan)
- **ཾ** (U+0F7E) — Rnam bcad (anusvara)
- **ཿ** (U+0F7F) — Rnam par bcad pa (visarga)

### Script Detection

The presence of characters in the U+0F00-U+0FFF range is a near-certain indicator of Tibetan-script text. For LID purposes, confirming the script is Tibetan is the first step; distinguishing Tibetan (bod) from other Tibetan-script languages (Dzongkha, Ladakhi, Balti, etc.) requires lexical and particle analysis.

## Character Frequency Patterns

### Most Frequent Characters

In typical Tibetan text, the following characters appear with the highest frequency:

1. **་** (tsheg, U+0F0B) — By far the most frequent character, appearing after nearly every syllable. Frequency: ~15-20% of all characters.
2. **ས** (sa, U+0F66) — Extremely common as a case particle suffix and in common words.
3. **ར** (ra, U+0F62) — Very frequent in particles, suffixes, and common words.
4. **ན** (na, U+0F53) — Common in particles (-ན, -ནས, -ནི) and words.
5. **པ** (pa, U+0F54) — Used as a nominalizer and in numerous words.
6. **བ** (ba, U+0F56) — Frequent as a prefix, suffix, and in words.
7. **ད** (da, U+0F51) — Common in particles (དང, དེ, དུ) and words.
8. **ག** (ga, U+0F42) — Frequent in particles (གི, གིས) and words.
9. **འ** (va/'a, U+0F60) — Common prefix and in words (འདི, འདུག).
10. **ལ** (la, U+0F63) — Very frequent as a dative/locative particle.
11. **ི** (gigu/i vowel, U+0F72) — The most common vowel sign.
12. **ཀ** (ka, U+0F40) — Common consonant.
13. **མ** (ma, U+0F58) — Frequent in words and as a negation prefix.
14. **ཡ** (ya, U+0F61) — Common in auxiliaries (ཡིན, ཡོད).
15. **།** (shad, U+0F0D) — Sentence/phrase delimiter.

### Tsheg Frequency as a Diagnostic

The tsheg (་) is the single most distinctive frequency feature of Tibetan script text. Its ratio to other characters (approximately 1 tsheg per 3-5 other characters) is a strong signal. Any text where U+0F0B constitutes 15-20% of all characters is almost certainly Tibetan-script text.

## Top 50 Function Words

The following function words (particles, postpositions, conjunctions, auxiliaries, pronouns) are the most frequent in Tibetan text and serve as key features for language identification:

| Rank | Word | Romanization | Function |
|------|------|-------------|----------|
| 1 | དང་ | dang | conjunction "and," comitative |
| 2 | གི་ | gi | genitive particle |
| 3 | ལ་ | la | dative/locative particle |
| 4 | ནི་ | ni | topic marker |
| 5 | ཡིན་ | yin | egophoric copula "is" |
| 6 | རེད་ | red | factual copula "is" |
| 7 | འདུག | vdug | sensory evidential "is/exists" |
| 8 | ཡོད་ | yod | egophoric existential "have/exist" |
| 9 | བྱེད་ | byed | "to do" (present stem) |
| 10 | དེ་ | de | demonstrative "that" |
| 11 | འདི་ | vdi | demonstrative "this" |
| 12 | གིས་ | gis | ergative/instrumental particle |
| 13 | ནས་ | nas | ablative "from"; sequential "after" |
| 14 | ས་ | sa | ergative particle (after vowels) |
| 15 | ཀྱི་ | kyi | genitive particle (allomorph) |
| 16 | གྱི་ | gyi | genitive particle (allomorph) |
| 17 | པ་ | pa | nominalizer |
| 18 | བ་ | ba | nominalizer (allomorph) |
| 19 | ཏུ་ | tu | dative/locative (allomorph) |
| 20 | དུ་ | du | dative/locative (allomorph) |
| 21 | ར་ | ra | dative/locative (after vowels) |
| 22 | མིན་ | min | negative egophoric copula |
| 23 | མེད་ | med | negative existential |
| 24 | མ་རེད་ | ma red | negative factual copula |
| 25 | ཚོ་ | tsho | plural marker |
| 26 | རྣམས་ | rnams | plural marker (formal) |
| 27 | ང་ | nga | first person pronoun "I" |
| 28 | ཁྱོད་ | khyod | second person pronoun "you" |
| 29 | ཁོ་ | kho | third person pronoun "he" |
| 30 | མོ་ | mo | third person pronoun "she" |
| 31 | ང་ཚོ་ | nga tsho | first person plural "we" |
| 32 | ཁོང་ | khong | third person pronoun (honorific) |
| 33 | ཀྱང་ | kyang | concessive "also, even, although" |
| 34 | ཡང་ | yang | concessive (allomorph) |
| 35 | ན་ | na | conditional "if, when" |
| 36 | ཏེ་ | te | conjunctive particle |
| 37 | སྟེ་ | ste | conjunctive particle (allomorph) |
| 38 | དེ་ | de | conjunctive particle (allomorph) |
| 39 | ཞིག | zhig | indefinite article |
| 40 | ཅིག | cig | indefinite article (allomorph) |
| 41 | གཅིག | gcig | numeral "one" |
| 42 | ཐམས་ཅད་ | thams cad | "all" |
| 43 | ཧ་ཅང་ | ha cang | "very, extremely" |
| 44 | ད་ | da | "now" |
| 45 | ད་ལྟ་ | da lta | "now, currently" |
| 46 | སོང་ | song | past sensory auxiliary |
| 47 | བྱུང་ | byung | past reportative auxiliary |
| 48 | ཡོང་ | yong | "come" / future auxiliary |
| 49 | ཆེན་པོ་ | chen po | "big, great" |
| 50 | བཟང་པོ་ | bzang po | "good" |

## Common Syllable Patterns

Tibetan syllables in the written language follow the structure:

```
(Prefix)(Superscript)Root(Subscript)(Vowel)(Suffix)(Post-suffix)
```

- **Prefixes:** ག, ད, བ, མ, འ (5 possible prefixes)
- **Superscripts:** ར, ལ, ས (3 possible superscripts)
- **Root consonants:** Any of the 30 basic consonants
- **Subscripts:** ྱ (ya-btags), ྲ (ra-btags), ླ (la-btags), ྭ (wa-zur)
- **Vowel signs:** ི (gigu/i), ུ (zhabs-kyu/u), ེ (vgreng-bu/e), ོ (na-ro/o); inherent /a/ is unmarked
- **Suffixes:** ག, ང, ད, ན, བ, མ, འ, ར, ལ, ས (10 possible suffixes)
- **Post-suffixes:** ས, ད (only 2, and only after certain suffixes)

The most common syllable shapes in running text are CV, CVC, and CCV patterns (in terms of pronunciation), though the orthography may encode more complex historical clusters.

## The Tsheg (་) Syllable Delimiter

The **tsheg** (་, U+0F0B) is one of the most important features of Tibetan script for both reading and computational processing. It serves as:

1. **Syllable boundary marker:** Placed after every syllable except before a shad (།) or at the end of a line.
2. **Word boundary indicator (partial):** Since Tibetan does not use spaces between words, the tsheg functions as the primary visual segmentation unit. However, note that many words are multi-syllabic, so tsheg marks syllable boundaries, not necessarily word boundaries.
3. **LID feature:** The regular rhythm of tsheg characters interspersed with consonant/vowel characters is a strong fingerprint of Tibetan-script text.

## Stacking Consonants (Subjoined Letters)

A distinctive visual feature of Tibetan script is the **vertical stacking** of consonant letters to represent consonant clusters. When a consonant occurs below the main (root) consonant, it is rendered in a special subjoined form. Unicode represents these subjoined consonants as separate characters (U+0F90-U+0FBC), which combine with the base consonant in rendering.

Common stacking patterns:
- རྒ (ra-superscript + ga) — the ར sits above the ག
- སྐ (sa-superscript + ka) — the ས sits above the ཀ
- གྲ (ga + ra-subscript) — the ྲ sits below the ག
- བྱ (ba + ya-subscript) — the ྱ sits below the བ
- རྒྱ (ra-superscript + ga + ya-subscript) — three-level stack

These stacking patterns and the specific combinations that occur are characteristic of Tibetan and can help distinguish it from other scripts.

## Morphological Patterns for LID

Key morphological patterns that aid in identifying Tibetan:

1. **Case particle allomorphy:** The systematic variation of case particles based on the preceding syllable's final consonant is a distinctive pattern. For instance, the genitive appears as -གི after ང and ད, -གྱི after བ and མ, -ཀྱི after ག, and -ཡི after vowels.

2. **Verb + auxiliary combinations:** The frequent co-occurrence of verb stems with auxiliaries like ཡིན, རེད, འདུག, ཡོད, སོང, བྱུང at clause/sentence boundaries.

3. **Nominalizer + genitive sequences:** The pattern [verb]-པའི / -བའི (nominalizer + genitive) is extremely common in attributive constructions.

4. **Sentence-final patterns:** Tibetan sentences characteristically end with auxiliary verbs/copulas followed by a shad (།). Common sentence endings include: པ་རེད།, པ་ཡིན།, གི་འདུག, གི་ཡོད།, etc.

5. **Honorific vocabulary:** The presence of specific honorific terms (གསུང, མཛད, ཕེབས, etc.) is characteristic of Tibetan discourse.
