# Malayalam vs confusable languages

Malayalam's own Unicode block (U+0D00–U+0D7F) makes script-level disambiguation trivial at the byte level. The informative comparisons are typological, for cases of mojibake or mixed-script material.

## vs Tamil (tam)

- Different script block (tam: U+0B80–U+0BFF).
- Malayalam preserves the full Sanskrit voiced/aspirated stop series (ഗ ഘ ദ ധ ബ ഭ etc.); Tamil does not write voicing.
- Malayalam has **chillu letters ൻ ൾ ർ ൽ ൺ**; Tamil has none — Tamil always uses a visible puḷḷi dot to mark a pure consonant.
- Malayalam verbs do **not** inflect for person/number/gender; Tamil verbs do.
- Tamil has **ழ**, Malayalam has **ഴ** (same phone, different block).

## vs Telugu (tel) and Kannada (kan)

- Different Unicode blocks (tel: U+0C00–U+0C7F, kan: U+0C80–U+0CFF).
- Telugu/Kannada glyphs have rounded top-arcs and are relatively "open"; Malayalam is densely stacked with more compact ligatures.
- Only Malayalam has chillu letters.
- Common word endings differ sharply: Malayalam `-ം / -ന് / -ുടെ / -ുന്നു`; Telugu `-ు / -లు / -కి`; Kannada `-ು / -ಗಳು / -ಕ್ಕೆ`.

## vs Sinhala, Devanagari, Bengali

All in distinct Unicode blocks. The **presence of any chillu letter (ൻ ൾ ർ ൽ ൺ ൿ) or the grapheme ഴ is near-proof of Malayalam**.

## Orthographic note

Both traditional and reformed orthographies are Malayalam. Traditional text will show more stacked conjuncts (e.g. ന്റ as a single ligature); reformed text will show more explicit **്** (chandrakkala) and split conjunct forms. A model should accept both as Malayalam.
