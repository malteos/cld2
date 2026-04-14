# Bulgarian LID characteristics

## Script signals

Cyrillic, 30 letters. The clearest Bulgarian signals are:
- **ъ** used as an ordinary vowel letter, frequent and even word-initial
  (`ъгъл`, `ъглов`) — in Russian ъ is mute and never word-initial.
- Absence of **ё**, **ы**, **э**, **і**, **ї**, **є**, **ґ**, **ј**, **љ**,
  **њ**, **ќ**, **ѓ**, **ѕ**.
- High-frequency word-final sequences **-ът**, **-ят**, **-та**, **-то**,
  **-те** (the definite article enclitics).

## Top function words

и, в, на, да, се, не, че, е, са, но, или, за, от, по, с, със, като, също,
така, тук, там, кой, коя, кое, кои, какво, кога, къде, защо, аз, ти, той, тя,
то, ние, вие, те, ми, ти, му, ѝ, ни, ви, им, го, я, ги, ли, ще, бих, бе,
беше, бяха.

## N-gram / spelling patterns

- Definite article suffixes attached to nouns/adjectives: `-ът, -ят, -а, -я,
  -та, -то, -те, -та`.
- Verb endings 1sg `-м, -а, -я` (pres), aorist `-х/-хме/-ха`, imperfect
  `-ех/-еше/-ехме/-еха`.
- Negative future: `няма да` + finite verb.
- Future: clitic `ще` + finite verb (`ще бъда`, `ще работи`).
- Participles/adjectives in `-ен/-на/-но/-ни`, `-ащ/-ящ`, `-ал/-ял/-ел`.
- Neuter nouns in `-е, -о, -ие` (`момче, писмо, условие`).

## Morphology hooks

- Enclitic article is the highest-precision Bulgarian signal. A word ending
  in `-ът`, `-ят` or `-та` within a Cyrillic text is diagnostic.
- `да`-clauses replace infinitives: `да бъда, да направя, да видим`.
- Renarrative: perfect-like `-л` forms without auxiliary (`той бил`, `те
  казали`).

## Punctuation / orthography quirks

- Standard European quotation marks: outer `„…"` (low-high) or `«…»`.
- Question mark `?`; semicolon `;` used normally (not as `?` like in Greek).
- Month and weekday names lowercase, like other Slavic languages.
