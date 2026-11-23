# Kazakh (Қазақ тілі) — Cyrillic Script: Language Characteristics

## Unique Characters

Kazakh Cyrillic has 42 letters: the 33 Russian letters plus nine extra letters. Seeing several of them together in one text is very strong evidence for Kazakh:

| Letter | Sound | Example | Also used in |
|---|---|---|---|
| **ә** | /æ/ | *әке* "father", *және* "and" | Tatar, Bashkir, Uyghur Cyrillic |
| **ғ** | /ʁ/ | *ғой*, *маған* "to me" | Uzbek, Bashkir, Tajik |
| **қ** | /q/ | *жоқ* "no", *қазақ* | Uzbek, Karakalpak, Tajik |
| **ң** | /ŋ/ | *менің* "my", *жаңа* "new" | Kyrgyz, Tatar, Bashkir |
| **ө** | /ø/ | *өте* "very", *өтті* | Kyrgyz, Tatar, Bashkir, Mongolian |
| **ұ** | /ʊ/ | *бұл* "this", *ұлт* "nation" | essentially Kazakh only |
| **ү** | /ʏ/ | *үшін* "for", *үй* "house" | Kyrgyz, Tatar, Bashkir, Mongolian |
| **һ** | /h/ | rare, mostly loans (*гауһар*) | Tatar, Bashkir |
| **і** | /ɪ/ | *бір* "one", *біз* "we" | Ukrainian, Belarusian (different role) |

**Diagnostic combinations.** **ұ** (straight-stroke u, U+04B1) is almost unique to Kazakh; do not confuse it with **ү** (U+04AF). **і** combined with **қ/ғ/ң/ә** rules out Ukrainian and Belarusian. **қ + ұ + і** together is about as close to a guarantee of Kazakh as a single character set can be. Bashkir writes **ҡ** (U+04A1), not Kazakh **қ** (U+049B). The two glyphs look nearly the same, so check the codepoint.

**Frequency (measured on a small sample).** In the 12 UD example passages (`examples/ud_*.txt`, about 2,600 words, mostly news) the share of all letters was roughly: і 5.9%, қ 3.9%, ң 1.6%, ғ 1.4%, ұ 1.1%, ө 0.85%, ү 0.7%, ә 0.66%, һ about 0.01%. Treat these numbers only as an order of magnitude. Any running Kazakh sentence of 5–10 words almost always contains at least one of і/қ.

Russian-only letters (**ё, щ, ъ, э**, and **ц, ч, ф, в** in native words) are rare. When they occur they mostly mark Russian loanwords (*президент*, *миллиард*, *компания*).

## Top Function and Frequent Words

`vocabulary.json` holds 3,402 entries from the **OpenSubtitles 2016 Kazakh** frequency list (FrequencyWords). The list is small and its raw counts are tiny (the top word, *мен*, has 279 occurrences). It is skewed towards film dialogue: character names (*николас*, *малдер*, *скалли*, *джо*), *доктор*, *президент*, *фбр*, plus many first- and second-person forms. The top items, with names removed, are:

мен, ол, жоқ, не, сен, керек, оны, жақсы, иә, менің, бұл, бар, ма, емес, маған, оның, деп, сіз, ба, біз, бе, мені, олар, үшін, де, енді, бір, жатыр, адам, саған, ал, неге, және, ғой, сенің, сені, осында, тек, оған, да, мүмкін, едім, бірақ, сол, осы, дұрыс, болды, басқа, сіздің, болады, бәрі, егер, болып, мына, еді, қайда, тағы, кім, қалай, туралы, сияқты, өте

In the UD news passages the most frequent words are: біз, бұл, мен, үшін, осы, біздің, да, болып, және, болды, бар, деп, ол, де, бойынша, керек, сондай-ақ.

Notes:
- **мен** means both "I" and "with / and" (comitative). That double use is why it ranks so high in every genre.
- **және** "and", **бірақ** "but", **үшін** "for", **емес** "not (to be)", **бұл** "this", **жоқ** "no / there isn't" and **ғой** (emphatic particle) are high-precision Kazakh markers.
- **не, да, де** also exist as Russian words (*не* "not", *да* "yes"). They are **not** diagnostic by themselves.
- The question particle **ма/ме/ба/бе/па/пе** is written as a separate word. That is why *ма, ба, бе, пе* appear as tokens in the list.

## Vowel Harmony and Suffix Patterns

Suffixes alternate between back (а, о, ұ, ы) and front (ә, ө, ү, і, е) forms, and the initial consonant of a suffix assimilates to the stem (л/д/т, н/д/т, ғ/г/қ/к). As a result, Kazakh text repeats a small set of suffix shapes:

- Plural: **-лар/-лер, -дар/-дер, -тар/-тер**
- Genitive: **-ның/-нің, -дың/-дің, -тың/-тің**. The word-final **-ң** is characteristic.
- Dative: **-ға/-ге, -қа/-ке**. Locative: **-да/-де, -та/-те**. Ablative: **-дан/-ден, -нан/-нен, -тан/-тен**
- Accusative: **-ны/-ні, -ды/-ді, -ты/-ті**. Instrumental: **-мен/-бен/-пен**
- Verbal forms: past **-ды/-ді** (*болды*), participle **-ған/-ген/-қан/-кен** (*болған*), converb **-ып/-іп/-п** (*болып*), present **-ады/-еді/-йды** (*келеді*, *қолдайды*), 1st person **-мын/-мін**, **-мыз/-міз**
- Derivation: **-лық/-лік, -дық/-дік, -тық/-тік** (*барлық*, *бірлік*), **-шы/-ші** (agent)

## Character N-grams

Frequent word-final trigrams in the UD sample were **-ның, -дің, -тан, -нда, -лық, -ады, -ған, -лды, -дың, -мен, -мыз, -тар, -нің, -міз, -лып, -мын**. Frequent internal trigrams included **ста, аза, қаз, ізд, біз, бол, асы, ған, ақс**. Some of these are inflated by the news topic (*Қазақстан*). Useful bigrams are **ың/ің** word-finally, **қа, ға, ұл, үш, ді, ні, ке**, and word-initial **жа/жо/жы/же** (Kazakh and Kyrgyz have initial **ж** where Uzbek, Tatar, Bashkir and Uyghur have **й/ي**: *жоқ* vs Uzbek *йўқ*, Tatar *юк*).

## Latin Alphabet Reform (brief)

A 2017 presidential decree started a move to the Latin script. The plan was announced with a target of 2025 and was later pushed back. Successive official drafts differed sharply:
- **2017**: apostrophe digraphs (e.g. *a'*, *s'*, *g'*). This version was widely criticised.
- **2018**: acute accents (e.g. *á, ǵ, ń, ó, ú, ý*) plus digraphs *sh, ch*.
- **2021**: Turkic-style diacritics (*ä, ğ, ñ, ö, ş, ü, ū, ı*).

The exact letter inventories of each draft are not reproduced here and should be checked against the official decrees. As of this writing Cyrillic remains dominant in Kazakhstan. Latin Kazakh shows up mainly in signage, some media and informal ASCII typing (e.g. *qazaq*, *men*, *jane* or *jäne*). The Kazakh community in China writes the Arabic-based script (see `chalis.md`), and Mongolia's Kazakhs use Cyrillic.
