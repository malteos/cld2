# Kannada vs confusable languages

Kannada's Unicode block (U+0C80–U+0CFF) is disjoint from every other script, so **byte-level classification is trivial**. The real LID interest is the visually similar Telugu.

## vs Telugu (tel) — the tricky pair

Telugu and Kannada descend from a common parent script and remain strongly look-alike in casual glance, but they diverge on several concrete signals:

- **Unicode blocks are disjoint**: kan U+0C80–U+0CFF vs tel U+0C00–U+0C7F. Any properly-encoded text distinguishes itself; the confusion is purely visual / OCR-driven.
- **Headmark / top-bar shape**: Kannada's top-arcs are flatter and more angular; Telugu's are rounded curls (the talakattu hook).
- **Virama frequency**: Kannada shows **`್`** (U+0CCD) much more often in running text than Telugu shows **`్`** (U+0C4D), because Kannada tolerates consonant-final word shapes more than Telugu, which almost always resolves to **`ు`**.
- **Plural marker**: Kannada **`-ಗಳು`** vs Telugu **`-లు`**.
- **Dative**: Kannada **`-ಗೆ/-ಕ್ಕೆ`** vs Telugu **`-కి/-కు`**.
- **"and"**: Kannada **ಮತ್ತು** vs Telugu **మరియు**.
- **Quotative**: Kannada **ಎಂದು** vs Telugu **అని**.

## vs Tamil (tam) and Malayalam (mal)

- Entirely different Unicode blocks (tam: U+0B80–U+0BFF; mal: U+0D00–U+0D7F).
- Kannada keeps the full Sanskrit voiced/aspirated stop series that Tamil lacks.
- Malayalam has chillu letters (ൻ ൾ ർ ൽ ൺ) and very dense stacked conjuncts; Kannada has neither.

## vs other Indic scripts

Devanagari, Bengali, Oriya, Gujarati, Sinhala occupy distinct Unicode blocks. **Kannada's combination of flat-top angular glyphs + extremely frequent `-ಗಳು` + `ಎಂದು` is a near-unique signature.**
