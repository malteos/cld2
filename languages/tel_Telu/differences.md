# Telugu vs confusable languages

Telugu's own Unicode block (U+0C00–U+0C7F) separates it at the byte level from all non-Telugu-script languages. The single hard case is **Telugu vs Kannada**, which share a common ancestral script and look quite similar to untrained eyes.

## vs Kannada (kan) — the tricky pair

- **Disjoint Unicode blocks**: tel in U+0C00–U+0C7F, kan in U+0C80–U+0CFF. Any correctly-encoded text is trivially separable; the confusion is purely visual.
- **Headmark shape**: Telugu's talakattu is a rounded upward curl; Kannada's is a flatter, more horizontal top-bar that often resembles a small arch. In Kannada the head-arcs sit more level.
- **Word endings**: Telugu overwhelmingly ends words in **`ు`** (`-u`); Kannada ends words in **`ು`** (its own `-u` sign) but just as frequently in consonants marked with **`್`** (virama), producing more word-final "bare consonant" glyphs than Telugu.
- **Plural marker**: Telugu **`-లు`** vs Kannada **`-ಗಳು`** — a strong word-tail cue.
- **Dative**: Telugu **`-కి/-కు`** vs Kannada **`-ಗೆ/-ಕ್ಕೆ`**.
- **Function words**: Telugu *మరియు*, *యొక్క*, *అని* vs Kannada *ಮತ್ತು*, *ಅದು*, *ಇದು*.

## vs Tamil (tam) and Malayalam (mal)

- Entirely different Unicode blocks (tam: U+0B80–U+0BFF; mal: U+0D00–U+0D7F).
- Telugu keeps the four-way Sanskrit stop series (voiced/aspirated letters present); Tamil does not.
- Malayalam has chillu letters and dense top-heavy ligatures; Telugu does not.

## vs other Indic scripts

Devanagari, Bengali, Gujarati, Oriya, Sinhala all live in separate Unicode blocks and use clearly distinct glyph shapes. Telugu's combination of round curls + extremely frequent **`ు`** + **`యొక్క`** is a near-unique fingerprint.
