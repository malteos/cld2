# Per-language markdown conventions

This file is the shared spec for the four markdown files that live in every
language folder. Keep content **concise but substantive**: each file is input
for future language-identification prompts, so every line should either
describe a typological fact or a useful LID signal.

## File: `overview.md`

Length: ~150–250 words. Format as GitHub-flavoured markdown.

- First-level heading: the language name plus ISO-639-3 code, e.g.
  `# English (eng)`.
- A **Summary** paragraph: family tree (Indo-European → Germanic → West), ISO
  codes (639-1 / 639-2 / 639-3), script, approximate speaker count, principal
  regions/countries.
- A **Writing system** paragraph: script details, casing, diacritics.
- Optional third paragraph on history/status if relevant.

## File: `grammar.md`

Length: ~200–350 words.

Use bullet sections for:
- **Word order** (SVO/SOV/VSO, analytic vs synthetic).
- **Morphology** (agglutinative, fusional, isolating; notable affixes).
- **Nouns** (gender, number, case).
- **Verbs** (tense/aspect/mood, agreement patterns).
- **Phonology** (notable sounds; vowel harmony, tone, stress if relevant).
- **Syntax notes** (pro-drop, copula presence, negation).

## File: `characteristics.md`

Length: ~200–350 words. **This is the most LID-relevant file.**

Sections:
- **Script signals** — unique Unicode characters or diacritics that strongly
  indicate this language (e.g. ł ę ą for Polish; ă î ș ț for Romanian).
- **Top function words** — give 20–30 of the most frequent high-precision
  markers (articles, prepositions, pronouns). Inline list is fine.
- **N-gram / spelling patterns** — character or character-class sequences that
  discriminate this language (e.g. `^sz-`, `-tsch`, double consonants).
- **Morphology hooks** — productive affixes or clitics that leave a recognisable
  surface signature.
- **Punctuation / orthography quirks** — e.g. Spanish inverted `¿` `¡`, Greek
  `;` as question mark, Armenian `։` full stop.

## File: `differences.md`

Length: ~100–250 words.

- List the **confusable languages** (usually 2–4). Use the CLD2 close-sets as a
  starting point: Indonesian/Malay, Bosnian/Croatian/Serbian, Hindi/Marathi,
  Czech/Slovak, Norwegian/Danish, Galician/Spanish/Portuguese, Zulu/Xhosa,
  Kinyarwanda/Rundi, Tibetan/Dzongkha.
- For each pair, give a **2–5 bullet diagnostic** — concrete, checkable surface
  features (unique characters, word endings, function word differences).
- If this language is *not* close to anything in the CommonLID set, say so and
  briefly describe what makes it distinctive.

## General rules

- No TODO markers. Remove the `<!-- TODO:`/placeholder banner if it still
  exists in the file.
- Spell out the endonym (self-name) once in `overview.md`.
- Keep claims factual. Where data varies (e.g. speaker counts), give a range.
- Use plain Unicode where possible; render script examples with actual
  characters, not transliterations-only.
- Aim for writing that a model can *consume* during prompting: short sentences,
  concrete features, no rhetorical filler.
