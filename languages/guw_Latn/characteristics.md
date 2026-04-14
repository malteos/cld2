# Gun / Gungbe LID characteristics

## Script signals

Gun text is identified by a mix of Africa-Alphabet IPA-style letters and tone marks:

- **ɛ** (U+025B) and **ɔ** (U+0254) — open-mid vowels, very frequent. Their presence together in Latin text points to a Gbe language (Fon/Gun/Ewe/Aja) rather than Yoruba (which uses under-dot **ẹ ọ**).
- **ɖ** (U+0256) implosive is common in careful orthography but often replaced with **d** in informal/online text.
- Digraph **gb** (labial-velar stop) appears at onset (*gbɔ, gba, gbè, gbɔn*) and **kp** is also attested but less frequent.
- Labialised digraphs **hw**, **xw**, **kw**, **gw**.
- Trailing **n** on a vowel marks nasalisation: *sun, tɔn, gbɔn, wehome, yiylon*.

## Top function words

**ɖò**, **tò**, **ná**, **lɛ́**, **lɛ**, **ɔ́**, **ɔ**, **ɖé**, **tɔ̀n**, **tɔn**, **kò**, **má**, **mɔ̀**, **nyí**, **wɛ̀**, **wɛ**, **dó**, **bo**, **ga**, **lé**, **lè**, **lo**, **é**, **un**, **a**, **mí**, **mìn**, **yé**, **nyɛ**, **hwenuɛnu**, **dìn**, **egbé**, **sɔ**, **jí**, **glɔ́**, **nù**, **ɖo…ji**, **to…mɛ**, **kple**, **kpo**.

## N-gram / spelling patterns

- Postnominal **lɛ́** or **lɛ** marking plural at clause end is highly diagnostic.
- Definite **ɔ́ / ɔ** as a single-character word after nouns.
- Word-initial **gb-, kp-, hw-, xw-, ny-, nw-** are common.
- Final **-n** (nasal) on many syllables (*sun, ton, mɛn, jɛn*).
- Vowel-only words **é, ɔ́, ɖé, ɔ̀, ì** with a tone diacritic are pervasive.
- Serialised verb strings often separated by short vowels *bo, dó, lè*.

## Morphology hooks

- Fixed preverbal particle order: subject pronoun + **tò / ɖò / ná / kò / má** + verb.
- Genitive chain X **tɔ̀n** Y.
- Absence of any person/number endings on verbs — verb stems appear bare.

## Punctuation / orthography quirks

Tone diacritics (acute, grave, circumflex) are common on vowels in careful writing but often dropped online. Writers may substitute **e** / **o** for **ɛ** / **ɔ** in ASCII environments, e.g. *tonon* for *tɔnɔ̀n* — worth allowing in LID training.
