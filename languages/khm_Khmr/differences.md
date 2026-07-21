# Distinguishing Khmer from Confusable Scripts

This document describes how to distinguish Khmer (Cambodian) script from three
visually or geographically confusable writing systems: Thai, Lao, and
Myanmar/Burmese. Although all four descend from Brahmic script traditions, each
occupies a distinct Unicode block, uses distinct character shapes, and encodes
distinct linguistic features. The differences fall into five areas: Unicode
ranges, visual script shapes, diagnostic characters, vocabulary sources, and
grammatical typology.

---

## 1. Unicode Range Differences

Each script lives in its own Unicode block, so codepoint inspection is the most
reliable automated discriminator.

| Script  | Primary Block          | Range             |
|---------|------------------------|-------------------|
| Khmer   | Khmer                  | U+1780 -- U+17FF  |
| Khmer   | Khmer Symbols          | U+19E0 -- U+19FF  |
| Thai    | Thai                   | U+0E00 -- U+0E7F  |
| Lao     | Lao                    | U+0E80 -- U+0EFF  |
| Myanmar | Myanmar                | U+1000 -- U+109F  |
| Myanmar | Myanmar Extended-A     | U+AA60 -- U+AA7F  |
| Myanmar | Myanmar Extended-B     | U+A9E0 -- U+A9FF  |

Any codepoint in the range U+1780--U+17FF is definitively Khmer. A single
codepoint check is usually sufficient to disambiguate entire documents, because
mixed-script text within a single word is extremely rare across these four
languages.

---

## 2. Visual Script Shape Differences

### Khmer vs. Thai

Khmer consonants tend to have more angular tops and more complex ligatures than
Thai consonants. Khmer subscript consonants (called "coeng" forms, written below
the base consonant) are a distinctive feature with no direct Thai parallel. Thai
consonants are more uniform in height and have rounded loops at the tops of many
letters (e.g., ก ถ ภ). Khmer letters such as ក (ka), ខ (kha), and គ (ko) have
flat or notched tops rather than the rounded loop tops common in Thai.

Thai places vowel signs above, below, before, and after the consonant, but the
vowel glyphs themselves are visually distinct from their Khmer counterparts.
Khmer vowels such as ា (aa), ិ (i), and ុ (u) differ in shape from the Thai
equivalents า, ิ, and ุ, even though both systems position some vowels
similarly relative to the consonant.

### Khmer vs. Lao

Lao script is noticeably rounder and simpler than Khmer. Lao was historically
simplified from an earlier Tai script tradition and has fewer consonants (27
consonants versus Khmer's 33 base consonants). Lao characters such as ກ (ko),
ຂ (kho), and ງ (ngo) have a smoother, more circular appearance compared to
their Khmer equivalents. Lao lacks the elaborate subscript consonant system
found in Khmer.

### Khmer vs. Myanmar

Myanmar script is immediately recognizable by its highly circular letterforms.
Characters such as က (ka), ခ (kha), and င (nga) are built from circles and
partial circles. Khmer letterforms, by contrast, are more rectangular and
angular. Myanmar also uses a stacking system for conjunct consonants, but the
visual result is different from Khmer's coeng subscript system: Myanmar stacked
forms are smaller circles placed below or beside the base, while Khmer subscript
forms are reduced and modified versions of the full consonant placed directly
beneath the base character.

---

## 3. Diagnostic Characters Unique to Each Script

Certain characters or character classes appear in only one of these scripts and
serve as immediate identifiers.

**Khmer-only indicators:**
- Khmer sign coeng (U+17D2): the invisible stacking character that triggers
  subscript consonant rendering. No other script in this group uses this
  mechanism.
- Khmer currency symbol (U+17DB): the riel sign.
- Khmer lunar date symbols (U+19E0--U+19FF): unique to the Khmer calendar
  system.

**Thai-only indicators:**
- Tone marks: mai ek (U+0E48), mai tho (U+0E49), mai tri (U+0E4A), mai
  chattawa (U+0E4B). These small marks above consonants have no Khmer
  equivalent, because Khmer is not a tonal language.
- Mai yamok (U+0E46): the Thai reduplication sign, used to indicate that the
  preceding word is repeated. Khmer has no equivalent symbol.
- Thai currency symbol (U+0E3F): the baht sign.

**Lao-only indicators:**
- Lao tone marks: mai ek (U+0EC8), mai tho (U+0EC9), mai ti (U+0ECA), mai
  catawa (U+0ECB). Like Thai, Lao is tonal, and these marks are absent from
  Khmer text.
- Lao cancellation mark (U+0ECC) and Lao niggahita (U+0ECD) are specific to
  the Lao block.

**Myanmar-only indicators:**
- Myanmar sign virama (U+1039): triggers conjunct consonant stacking in
  Myanmar, functionally analogous to Khmer's coeng but in a different Unicode
  position.
- Myanmar digits (U+1040--U+1049): visually distinct rounded digit forms unlike
  Khmer digits (U+17E0--U+17E9).

---

## 4. Vocabulary Differences

Khmer has undergone heavy lexical borrowing from Sanskrit and Pali, reflecting
centuries of Hindu and Buddhist influence in the Angkorian period. Technical,
religious, royal, and literary vocabulary in Khmer is densely Indic. Words such
as "vihear" (temple, from Sanskrit vihara), "preah" (sacred, from Pali vara),
and "thevada" (deity, from Sanskrit devata) are characteristic. The base
vocabulary of Khmer is Austroasiatic, related to Mon and Vietnamese, giving it a
substrate of monosyllabic and sesquisyllabic words that are absent from the
Tai-Kadai and Sino-Tibetan families.

Thai shares some Sanskrit and Pali borrowings due to parallel Buddhist cultural
influence, but Thai has a substantially larger layer of Chinese loanwords,
particularly in commerce, food, and kinship terminology. Thai also borrows from
Khmer itself, especially in royal and formal registers, but the core vocabulary
is Tai-Kadai in origin.

Lao vocabulary is closely related to Thai (both are Tai-Kadai languages) but has
fewer Sanskrit/Pali borrowings and fewer Chinese loanwords than Thai. Lao
everyday vocabulary is largely Tai in origin.

Myanmar/Burmese belongs to the Sino-Tibetan language family, and its core
vocabulary is unrelated to Khmer, Thai, or Lao. Burmese has Pali borrowings
(from Theravada Buddhism) but its base morphology and word structure are
distinct, featuring verb-final sentence order and Sino-Tibetan roots.

---

## 5. Grammatical Differences

The most important structural discriminator is tonality. Khmer is **not a tonal
language**. It distinguishes meaning through vowel quality, vowel length, and
register (a phonation contrast between "clear" and "breathy" voice) rather than
through pitch contours. Thai has five tones, Lao has six tones, and Burmese has
four tones (sometimes analyzed as three tones plus a checked syllable). The
absence of tone marks in Khmer text is a direct visual consequence of this
linguistic fact and one of the most reliable script-level signals when
classifying text.

Khmer word order is subject-verb-object (SVO), which it shares with Thai and
Lao. Burmese, however, is subject-object-verb (SOV), a fundamental word-order
difference reflecting its Sino-Tibetan heritage.

Khmer morphology is largely isolating but retains productive prefixation and
infixation inherited from its Austroasiatic ancestry. For example, the causative
prefix "bong-" and various nominalizing infixes are common. Thai and Lao are
more strictly isolating, relying almost entirely on particles and word order
rather than affixation. Burmese uses agglutinative verb suffixes to mark tense,
mood, and politeness, a feature absent from Khmer, Thai, and Lao.

---

## Summary of Quick Discriminators

| Feature               | Khmer       | Thai        | Lao         | Myanmar     |
|-----------------------|-------------|-------------|-------------|-------------|
| Unicode block start   | U+1780      | U+0E00      | U+0E80      | U+1000      |
| Tonal                 | No          | Yes (5)     | Yes (6)     | Yes (4)     |
| Tone marks in script  | None        | 4 marks     | 4 marks     | Pitch/creak |
| Subscript consonants  | Coeng system| None        | None        | Stacking    |
| Script shape          | Angular     | Looped tops | Rounded     | Circular    |
| Language family       | Austroasiatic | Tai-Kadai | Tai-Kadai   | Sino-Tibetan|
| Dominant loanword source | Sanskrit/Pali | Chinese + Sanskrit | Tai core | Pali    |
