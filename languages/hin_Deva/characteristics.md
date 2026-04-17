# Hindi LID characteristics

## Script signals

- Devanagari block U+0900–U+097F; characteristic overhead bar **शिरोरेखा** ties letters within a word.
- Anusvāra **ं** and candrabindu **ँ** are frequent; visarga **ः** is rare and typically indicates Sanskrit-tatsama vocabulary.
- Nukta letters **क़ ख़ ग़ ज़ फ़** (Perso-Arabic loans) appear but are far less common than in Urdu-origin vocabulary; **ड़ ढ़** are routine.
- Hindi does *not* use **ळ** (that is Marathi / Konkani) and rarely uses **ऍ / ऑ** except for loanwords.

## Top function words

का, की, के, को, से, में, पर, और, या, लेकिन, पर, कि, जो, वह, यह, ये, वे, मैं, हम, तुम, आप, है, हैं, था, थी, थे, होगा, होगी, होंगे, नहीं, भी, ही, तो, तक, ने, अगर, तब, जब, क्या, क्यों, कैसे, कहाँ, कब, कौन.

## N-gram and spelling patterns

- Sequence **है** at the end of sentences (singular copula) and **हैं** (plural/honorific) are extremely common.
- Ergative marker **ने** between the subject and a perfective verb is a strong Hindi (and only-Hindi-vs-Marathi) cue.
- Postpositions **का / की / के** immediately after a noun.
- Habitual participle endings **-ता है, -ती है, -ते हैं** at sentence end.
- Progressive **रहा है / रही है / रहे हैं**.

## Morphology hooks

- Masculine-singular -ā / oblique -e / feminine -ī noun endings (लड़का / लड़के / लड़की).
- Verbal chain: stem + aspect participle + tense auxiliary (he/she **है**, they/honorific **हैं**).
- Future in **-गा / -गी / -गे** fused to the verb (जाऊँगा, जाएगी).
- Negator **नहीं** precedes the verbal complex.

## Punctuation / orthography quirks

- Sentence terminator **।** (U+0964, *daṇḍa*). Double daṇḍa **॥** is used in verse.
- Digits may be Devanagari (० १ २ ३ ४ ५ ६ ७ ८ ९) or Latin.
- ZWJ/ZWNJ are used to control conjunct-formation (e.g. half-letter + ZWNJ preserves the explicit halant form).
