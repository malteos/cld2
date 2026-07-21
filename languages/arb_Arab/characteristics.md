# Modern Standard Arabic (arb_Arab) - Identification Characteristics

## Arabic Script Features

The Arabic script is a cursive abjad consisting of **28 base letters**. Each letter typically has **four contextual forms** depending on its position within a word: isolated, initial, medial, and final. Six letters (ا د ذ ر ز و) do not connect to the following letter, which causes breaks within words.

The script is written **right-to-left (RTL)**, with numbers written left-to-right within the text. Arabic uses Eastern Arabic-Indic numerals (٠١٢٣٤٥٦٧٨٩) in the Mashriq (eastern Arab world) and Western Arabic numerals (0123456789) in the Maghreb (western Arab world).

### Diacritics (Tashkeel / Harakat)

Arabic text is typically written **without short vowel markings**. Optional diacritical marks include:

- **Fatha (ـَ):** short /a/
- **Damma (ـُ):** short /u/
- **Kasra (ـِ):** short /i/
- **Sukun (ـْ):** absence of vowel
- **Shadda (ـّ):** consonant gemination (doubling)
- **Tanwin (ـً ـٌ ـٍ):** nunation (indefinite marker)

Full diacritization (tashkeel) is used primarily in the Quran, children's textbooks, dictionaries, and texts for Arabic learners. Most published Arabic text is unvocalized or partially vocalized, relying on the reader's knowledge of Arabic morphology and context for correct pronunciation.

## Unicode Range

The primary Unicode block for Arabic is **U+0600 to U+06FF** (Arabic block), which contains the 28 basic letters, diacritical marks, punctuation, and Eastern Arabic-Indic digits. Additional blocks include:

- **U+0750-U+077F:** Arabic Supplement (additional characters for African and Asian languages using Arabic script)
- **U+08A0-U+08FF:** Arabic Extended-A
- **U+FB50-U+FDFF:** Arabic Presentation Forms-A (contextual forms, ligatures)
- **U+FE70-U+FEFF:** Arabic Presentation Forms-B (contextual forms)

Key Arabic-specific Unicode characters include:
- **U+0621:** ء (hamza)
- **U+0627:** ا (alif)
- **U+0644:** ل (lam)
- **U+0629:** ة (ta marbuta) - distinctive to Arabic
- **U+0649:** ى (alif maqsura)
- **U+0640:** ـ (tatweel/kashida - elongation character)

## Character Frequency Patterns

In Arabic text, the most frequently occurring letters are:

1. **ا** (alif) - most frequent; serves as a vowel carrier and long /a/
2. **ل** (lam) - extremely frequent due to the definite article ال
3. **ي** (ya) - common in verb conjugations and as long /i/
4. **و** (waw) - conjunction "and" and long /u/
5. **ن** (nun) - frequent in verb endings and tanwin
6. **م** (mim) - common prefix and root letter
7. **ت** (ta) - feminine marker and verb prefix
8. **ر** (ra) - frequent root consonant
9. **ب** (ba) - preposition "in/with" and common root letter
10. **ه** (ha) - pronoun suffix and common root letter

The combination **ال** (alif-lam, the definite article) is the single most frequent bigram in Arabic text and serves as a strong identifier for the language.

## Top Function Words

The most common function words in Modern Standard Arabic include:

| Rank | Arabic | Transliteration | Meaning |
|------|--------|----------------|---------|
| 1 | في | fi | in |
| 2 | من | min | from |
| 3 | على | 'ala | on/upon |
| 4 | إلى | ila | to/toward |
| 5 | أن | anna/an | that/to |
| 6 | ما | ma | what/not |
| 7 | لا | la | no/not |
| 8 | هذا | hadha | this (m.) |
| 9 | هذه | hadhihi | this (f.) |
| 10 | التي | al-lati | which (f.) |
| 11 | الذي | al-ladhi | which (m.) |
| 12 | كان | kana | was/were |
| 13 | قد | qad | may/already |
| 14 | عن | 'an | about/from |
| 15 | مع | ma'a | with |
| 16 | بين | bayna | between |
| 17 | حتى | hatta | until/even |
| 18 | ثم | thumma | then |
| 19 | أو | aw | or |
| 20 | لم | lam | did not |
| 21 | لن | lan | will not |
| 22 | إذا | idha | if/when |
| 23 | هو | huwa | he/it |
| 24 | هي | hiya | she/it |
| 25 | نحن | nahnu | we |
| 26 | هم | hum | they (m.) |
| 27 | أنا | ana | I |
| 28 | كل | kull | every/all |
| 29 | بعد | ba'da | after |
| 30 | قبل | qabla | before |
| 31 | هنا | huna | here |
| 32 | هناك | hunaka | there |
| 33 | ذلك | dhalika | that (m.) |
| 34 | عند | 'inda | at/with |
| 35 | لكن | lakin | but |

## Common Letter Combinations and Patterns

### Definite Article (ال)

The prefix **ال** (al-) is the definite article and appears with extremely high frequency. It is the single strongest indicator of Arabic text. When followed by a sun letter, the lam assimilates phonetically but remains written: الشمس (al-shams, "the sun").

### Common Prefixes

Arabic extensively uses single-letter prefixes that attach to words:

- **بـ** (bi-): preposition "in/with/by" - بالعربية (bil-'arabiyya, "in Arabic")
- **لـ** (li-): preposition "for/to" - للمدرسة (lil-madrasa, "for the school")
- **فـ** (fa-): conjunction "and so/then" - فقال (fa-qala, "and he said")
- **وَ** (wa-): conjunction "and" - والكتاب (wal-kitab, "and the book")
- **كـ** (ka-): preposition "like/as" - كالماء (kal-ma', "like water")
- **سـ** (sa-): future marker - سيذهب (sa-yadhhabu, "he will go")

These prefixes can stack: وبالتالي (wa-bi-al-tali, "and consequently").

### Verb Pattern Prefixes

Imperfect verb forms use characteristic prefixes:
- **يـ** (ya-): 3rd person masculine
- **تـ** (ta-): 3rd person feminine / 2nd person
- **أ** (a-): 1st person singular
- **نـ** (na-): 1st person plural

### Common Suffixes

- **ـة** (ta marbuta): feminine singular marker, distinctive to Arabic
- **ـات** (-at): feminine/regular plural
- **ـون / ـين** (-un/-in): masculine sound plural
- **ـها / ـه** (-ha/-hu): possessive pronouns "her/his"
- **ـهم** (-hum): possessive pronoun "their"

## Morphological Patterns for Identification

Key patterns that distinguish Arabic text:

1. **High frequency of ال**: the definite article appearing in roughly 10-15% of tokens
2. **Ta marbuta (ة)**: unique to Arabic among widely-used Arabic-script languages
3. **Alif with hamza variants**: أ إ آ appearing frequently
4. **Absence of non-Arabic letters**: no پ چ ژ گ (Persian), no ٹ ڈ ڑ (Urdu)
5. **Shadda and tanwin usage**: when diacritics are present
6. **Root-and-pattern word structure**: predictable morphological patterns
7. **Waw conjunction**: standalone و as one of the most frequent tokens
