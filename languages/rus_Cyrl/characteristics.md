# Russian (русский) — Cyrillic Script: Language Characteristics

## Alphabet and Diagnostic Letters

The Russian alphabet has 33 letters:

а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я

Letters that matter most for identification:

- **ы** — high central vowel. Very frequent (in the UD sample `examples/ud_*.txt` it is roughly as common as г or з). It occurs in plurals (*новые*, *были*), the past *был/была*, *мы*, *вы*, *ты*. **Absent from Ukrainian, Bulgarian, Serbian and Macedonian**; present in Belarusian and Carpathian Rusyn.
- **э** — mostly word-initial in a few high-frequency words (*это, этот, эта, эти, этом, этого, этой*) and in loanwords (*экономика*). Absent from Ukrainian, Bulgarian, Serbian, Macedonian; present in Belarusian (much more often, e.g. *гэта*).
- **ъ** — hard sign, rare, only after prefixes before е/ё/ю/я (*объект*, *съезд*, *подъём*). In Bulgarian ъ is a frequent vowel letter; in Ukrainian and Belarusian an apostrophe is used instead.
- **ё** — optional; most texts write е. Seeing ё at all (*её*, *ещё*, *всё*) is a Russian (or Belarusian) signal.
- **щ** — shared with Ukrainian and Bulgarian, absent from Belarusian, Serbian, Macedonian.
- **и** is the normal /i/ letter (Ukrainian uses і for /i/ and и for [ɪ]).

Letters that **never** appear in standard Russian: і, ї, є, ґ (Ukrainian), ў (Belarusian), ј, љ, њ, џ, ђ, ћ (Serbian), ѓ, ќ, ѕ (Macedonian), and the apostrophe inside words.

## Top 50 Function Words

From `vocabulary.json` (wordfreq ranks 1-110, nouns omitted), in order:

в, и, на, не, с, что, я, по, а, как, из, это, за, для, о, к, но, то, у, его, он, от, все, так, же, мы, до, ты, только, был, если, когда, было, мне, меня, уже, еще, бы, или, их, они, при, будет, кто, чтобы, есть, она, во, вы, может

Further high-frequency items: после, нет, очень, были, со, была, также, вот, ее, чем, быть, где, под, этом, вас, да, даже, можно, того, просто, этого, больше, сейчас, без, себя, этот, который, ли, тебя, теперь, всего, сегодня, надо, через, тоже, почему, здесь, между, однако, всегда.

According to `chalis/discriminators.md` the following are frequent Russian words that do **not** occur in the Ukrainian top-10k list: *была, году, себя, тебя, жизни, всегда, между, этой, здесь, однако, её, несколько, своей, сказал, тогда, хорошо, является, вместе, лишь*. Against Bulgarian: *что, это* (*это* as a word; Bulgarian has *това*), *для, его, он, же, мы, ты, только, был, если, когда, мне, меня, уже, еще, бы, они, будет, кто, чтобы*.

The single most compact Russian fingerprint is the co-occurrence of **что** + **это** + **ы**-containing words (*был*, *мы*, *вы*).

## Frequent Character N-grams

Computed informally from the 12 UD passages in `examples/` (about 2,700 words; treat as indicative only):

- Most frequent letters: о, е, и, а, н, с, т, р, в, л. Russian has a high share of **о** because unstressed о is written.
- Frequent bigrams: **ст, ен, ни, на, но, ра, ов, ан, ко, те, ро, го, ны**.
- Characteristic trigrams/sequences: **ого** (adjective/pronoun genitive), **ост** (*-ость* abstract nouns), **ени** (*-ение* nouns), **ств** (*-ство*, *-ственный*), **ые/ый/ий**, **ться/тся**, **ыв/ыл**.
- Combinations impossible or very rare in Ukrainian: **ы**, **э**, **ъ**, **ё**, word-final **-ть** on infinitives where Ukrainian has **-ти**, **-ов** genitive plural (Ukrainian **-ів**).

## Morphological Endings Useful for LID

### Verbs
- Infinitive **-ть** (*делать, говорить, быть*), **-ться** (*учиться*), **-ти**, **-чь**.
- 3sg **-ет/-ёт/-ит**, reflexive **-ется/-ится** (*является, кажется*). Ukrainian has *-є/-ить* and *-ється*.
- Past **-л, -ла, -ло, -ли** (*сказал, была*). Ukrainian masculine past ends in **-в**.
- Participles **-ющий, -ящий, -вший, -нный**; gerunds **-я, -в, -вшись**.

### Nouns
- Abstract **-ость** (*новость*), **-ние/-ение** (*решение, значение*: Russian single н + ие vs Ukrainian **-ння**: *рішення*), **-ство** (*государство*), **-тель**.
- Genitive plural **-ов/-ев**; locative plural **-ах/-ях**; instrumental plural **-ами/-ями**.

### Adjectives
- **-ый, -ий, -ой; -ая, -яя; -ое, -ее; -ые, -ие; -ого, -ому; -ой, -ей; -ых, -их; -ским, -ской**.
- Suffix **-ск-** with и: *российский, русский*; Ukrainian *російський*.

## Typography

Russian typography uses «ёлочки» quotation marks and the long dash for copula omission (*Москва — столица России*). The numero sign № and abbreviations г. (*год/город*), см., т.е. are common (*г* and *м* even appear as tokens in `vocabulary.json`). Ukrainian uses the same quotation conventions, so punctuation is not diagnostic between them.
