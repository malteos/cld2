# Bulgarian Identification Characteristics (bul_Cyrl)

## Bulgarian Cyrillic Alphabet

The Bulgarian Cyrillic alphabet consists of **30 letters**. It differs from the Russian Cyrillic alphabet in important ways that are diagnostically useful for language identification.

### Letters present in Bulgarian but key for identification

| Letter | Name | IPA | Notes |
|--------|------|-----|-------|
| Щ щ | щъ | /ʃt/ | Represents /ʃt/ cluster; present in both Bulgarian and Russian but with different phonetic values (Russian /ɕː/) |
| Ъ ъ | ер голям | /ɤ/ | **Highly diagnostic.** Full vowel in Bulgarian, no longer used as a vowel in Russian (only as a hard sign) |
| Ь ь | ер малък | /ʲ/ | Palatalization marker, much less frequent in Bulgarian than Russian |
| Ю ю | ю | /ju/ | Iotated vowel |
| Я я | я | /ja/ | Iotated vowel |

### Letters ABSENT from Bulgarian (present in Russian)

These absences are critical for distinguishing Bulgarian from Russian:

- **Ы ы** -- Does NOT exist in Bulgarian. Its presence reliably indicates Russian (or another non-Bulgarian Cyrillic language).
- **Э э** -- Does NOT exist in Bulgarian. Strong indicator of Russian.
- **Ё ё** -- Does NOT exist in Bulgarian. Indicator of Russian.

The Bulgarian alphabet also lacks the Russian letters in the sense that Bulgarian Ъ functions as a full vowel (close-mid back unrounded /ɤ/) rather than merely a hard sign separator as in modern Russian.

## Character Frequency Patterns

In typical Bulgarian text, the most frequent letters are:

1. **а** -- the most common letter overall (~11-12%)
2. **е** -- (~9-10%)
3. **о** -- (~8-9%)
4. **и** -- (~8-9%)
5. **н** -- (~6-7%)
6. **т** -- (~6-7%)
7. **р** -- (~5%)
8. **с** -- (~4-5%)
9. **в** -- (~4%)
10. **л** -- (~3-4%)

The letter **ъ** appears at approximately 1.5-2.5% frequency, which is notably high for a single vowel character and serves as a strong signal for Bulgarian since it functions as a mere hard sign (virtually silent) in Russian and does not appear at all in Serbian or Macedonian Cyrillic.

## Top 50 Function Words

The following are the most frequent function words in Bulgarian, ranked by approximate corpus frequency. These are essential features for language identification:

| Rank | Word | Translation | POS |
|------|------|-------------|-----|
| 1 | и | and | conjunction |
| 2 | на | of, on, to | preposition |
| 3 | е | is | verb (copula) |
| 4 | в | in | preposition |
| 5 | за | for, about | preposition |
| 6 | да | yes; to (subjunctive particle) | particle |
| 7 | от | from | preposition |
| 8 | с | with | preposition |
| 9 | не | not | particle |
| 10 | се | (reflexive particle) | pronoun/particle |
| 11 | са | are | verb (copula) |
| 12 | че | that (conjunction) | conjunction |
| 13 | по | along, by, on | preposition |
| 14 | но | but | conjunction |
| 15 | а | and, but | conjunction |
| 16 | до | to, until | preposition |
| 17 | или | or | conjunction |
| 18 | при | at, by, near | preposition |
| 19 | като | as, like, when | conjunction |
| 20 | още | still, yet, more | adverb |
| 21 | това | this | pronoun |
| 22 | те | they; the (plural article) | pronoun |
| 23 | си | (reflexive/possessive clitic) | pronoun |
| 24 | му | him (dative clitic) | pronoun |
| 25 | ще | will (future particle) | particle |
| 26 | го | him/it (accusative clitic) | pronoun |
| 27 | може | can, may | verb |
| 28 | има | has, there is | verb |
| 29 | беше | was | verb |
| 30 | ги | them (accusative clitic) | pronoun |
| 31 | без | without | preposition |
| 32 | между | between, among | preposition |
| 33 | след | after | preposition |
| 34 | към | toward | preposition |
| 35 | също | also | adverb |
| 36 | който | who, which (masc. relative) | pronoun |
| 37 | която | who, which (fem. relative) | pronoun |
| 38 | което | which (neut. relative) | pronoun |
| 39 | този | this (masc.) | pronoun |
| 40 | тази | this (fem.) | pronoun |
| 41 | тя | she | pronoun |
| 42 | той | he | pronoun |
| 43 | ние | we | pronoun |
| 44 | ми | me (dative clitic) | pronoun |
| 45 | вече | already | adverb |
| 46 | само | only | adverb |
| 47 | няма | does not have, there is not | verb |
| 48 | над | above, over | preposition |
| 49 | под | under | preposition |
| 50 | пред | before, in front of | preposition |

## Common Bigrams

High-frequency character bigrams in Bulgarian text:

- **на** -- extremely common (preposition + frequent combination)
- **та** -- very frequent (definite article suffix -та, and within words)
- **то** -- frequent (definite article suffix -то, and within words)
- **не** -- negation particle and word-internal
- **ен** -- common in adjective/participle endings
- **ра** -- common in many native roots
- **ст** -- very frequent consonant cluster
- **но** -- conjunction and word-internal
- **те** -- plural definite article suffix and pronoun
- **пр** -- very common word-initial cluster (предложение, правителство, пред)
- **ни** -- common in pronouns and suffixes
- **ан** -- frequent in noun/adjective endings
- **ат** -- present tense verb ending (3rd person plural)
- **ов** -- common in adjective/noun suffixes
- **от** -- preposition and word-internal

## Common Trigrams

- **ата** -- very frequent: feminine definite article suffix (*жената*, *книгата*)
- **ото** -- neuter definite article suffix (*детето*, *селото*)
- **ите** -- plural definite article suffix (*хората*, *градовете*)
- **ъта** -- feminine definite article after ъ (*дъщерята*)
- **ият** -- masculine definite article after и (*учителят*)
- **ето** -- neuter definite suffix (*времето*, *детето*)
- **ние** -- pronoun "we" and noun suffix (*знание*)
- **ост** -- abstract noun suffix (*радост*, *младост*)
- **ств** -- noun suffix (*правителство*, *общество*)
- **пре** -- common prefix (*предложение*, *преди*)
- **про** -- common prefix (*продължава*, *против*)
- **ска** -- adjective suffix (*българска*, *градска*)

## Highly Diagnostic Features

### 1. Suffixed Definite Article

The **suffixed definite article** is the single most diagnostic feature for identifying Bulgarian text. It appears as endings attached directly to nouns and adjectives:

- **-ът / -ят** (masculine subject): *градът* "the city," *учителят* "the teacher"
- **-а / -я** (masculine non-subject): *града*, *учителя*
- **-та** (feminine): *жената* "the woman," *книгата* "the book"
- **-то** (neuter): *детето* "the child," *селото* "the village"
- **-те** (plural): *хората* "the people," *градовете* "the cities"

These suffixed articles are visible in text as word-final patterns and are a strong indicator of Bulgarian (or Macedonian, which has a similar but not identical system).

### 2. The Vowel Ъ as a Full Vowel

The letter **ъ** functioning as a regular vowel within words is highly diagnostic. Common words with ъ include: *бъдеще* "future," *дъжд* "rain," *дълг* "long/debt," *пълен* "full," *първи* "first," *ъгъл* "corner," *българин* "Bulgarian."

### 3. Preposition Use Instead of Cases

The heavy reliance on prepositions (*на*, *в*, *с*, *от*, *за*, *по*, *до*, *при*, *към*) where other Slavic languages would use case inflections leads to a distinct distributional pattern. The preposition *на* is especially frequent for expressing possession and indirect objects.

### 4. The Particle Да

The subjunctive particle *да* (used instead of an infinitive) is extremely frequent and characteristic: *Искам да ям* "I want to eat" (literally "I want that I eat"). This construction, combined with the absence of infinitive forms in common usage, produces a distinctive pattern.

### 5. Future Particle Ще

The future tense is formed analytically with the particle *ще*: *Ще дойда* "I will come." This particle is distinctive to Bulgarian and is not used in Russian, Serbian, or Macedonian (which uses *ке*).

### 6. Reflexive Particle Се

The reflexive particle *се* is extremely frequent in Bulgarian, appearing as a separate word (not attached to the verb as in some other Slavic languages in certain forms). Its high frequency as a standalone token is a useful signal.
