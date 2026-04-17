# Ukrainian LID characteristics

## Script signals

Cyrillic with a Ukrainian-specific alphabet. Single best signals are the
letters **і**, **ї**, **є**, **ґ** — any of these in a Cyrillic text is a
strong positive signal for Ukrainian (also Rusyn/Belarusian partially, but
not Russian, Bulgarian, Serbian or Macedonian). The **absence** of **ы**,
**ъ**, **э** is corroborating. The apostrophe `’` before я/ю/є/ї (as in
`м'ясо`, `п'ять`) is a secondary signal.

## Top function words

і, й, в, у, на, не, що, я, він, вона, вони, ми, ви, це, то, та, але, як,
якщо, бо, тому, щоб, де, коли, чому, з, із, зі, до, від, по, про, за, для,
так, також, теж, вже, ще, тільки, дуже, свій, який, котрий, є, був, була,
було, були.

## N-gram / spelling patterns

- Adjective endings: `-ий/-ій` (m), `-а/-я` (f), `-е/-є` (n), `-і/-ї` (pl);
  genitive `-ого/-ої/-их`.
- Infinitive in `-ти` / `-тися` (vs Russian `-ть/-ться`).
- Past 3sg.m. ends in `-в` (vs Russian `-л`): `писав`, `читав`, `ходив`.
- Frequent digraphs `дж` /dʒ/, `дз` /dz/: `джміль`, `дзвін`.
- Common sequences `-ьк-`, `-цьк-`, `-ськ-` in adjectives/toponyms
  (`український`, `київський`).
- Endings `-ість`, `-ство`, `-ння`, `-ття` for abstract nouns.

## Morphology hooks

- Vocative case (productive): `-е`, `-о`, `-у`, `-ю`.
- Synthetic future `-му/-меш/-ме/-мемо/-мете/-муть` appended to infinitive
  (`робитиму`, `читатимеш`) — a unique Ukrainian feature among East Slavic.
- Reflexive `-ся` written attached: `здається`, `виявляється`.
- Alternations г→з→ж, к→ц→ч, х→с→ш in noun/verb inflection.

## Punctuation / orthography quirks

- Quotation marks: outer `«…»`, inner `„…"`.
- Dialogue with em-dash as in Russian/Polish.
- Apostrophe `’` is orthographic, separating a hard consonant from following
  `я/ю/є/ї` where palatalisation would otherwise be expected.
