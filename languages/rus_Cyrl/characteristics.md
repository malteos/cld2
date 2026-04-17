# Russian LID characteristics

## Script signals

Cyrillic with Russian-specific distribution. Presence of **ы**, **ъ**, **э**
and especially **ё** is a strong Russian (or Russian-influenced) signal and
excludes Ukrainian and Belarusian for **ы** and **ъ**. Russian lacks
Ukrainian-only letters **і**, **ї**, **є**, **ґ** and Belarusian **ў**; it
also lacks Serbian/Macedonian **ј**, **љ**, **њ**, **ђ**, **ћ**, **ѓ**, **ќ**,
**ѕ**.

## Top function words

и, в, не, на, я, что, он, с, как, а, но, по, это, она, к, у, за, из, мы, вы,
они, же, бы, то, от, для, так, или, его, её, их, был, была, было, есть, нет,
все, ещё, уже, только, который, когда, где, тоже, очень.

## N-gram / spelling patterns

- Adjective endings: `-ый`, `-ий`, `-ой` (m.sg.nom), `-ая`, `-яя` (f.sg.nom),
  `-ое`, `-ее` (n.sg.nom), `-ые`, `-ие` (pl).
- Noun endings: genitive plural `-ов/-ев/-ей`, instrumental `-ом/-ем/-ой/-ей`.
- Verb endings: `-ть`/`-ться` infinitive, `-ла`/`-ло`/`-ли` past, `-ют`/`-ут`
  /`-ят`/`-ат` 3pl non-past, `-шь` 2sg.
- Digraph `-ого`/`-его` (pronounced /-ovo/-evo/) in gen.sg. of adjectives is
  Russian-characteristic.
- Initial sequences `че-`, `чт-`, `чу-`, `щ-` (letter щ is absent in Serbian
  and some other Cyrillic orthographies).
- Double-letter clusters `-сс-`, `-нн-`, `-тт-` in loanwords.

## Morphology hooks

- Reflexive/passive clitic `-ся`/`-сь` attached to finite verb forms.
- Diminutive suffixes `-очка`, `-ечка`, `-еньк-`, `-ушк-`.
- Nominalisations `-ение`, `-ание`, `-ость`, `-ство`.

## Punctuation / orthography quirks

- Dialogue introduced with an em-dash `— Привет, — сказал он.`
- Quotes: outer `«…»` with inner „…" guillemets.
- No capitalisation of months, weekdays, nationalities or common pronouns.
