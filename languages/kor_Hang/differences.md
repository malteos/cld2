# Korean vs. confusable languages

## kor ↔ jpn — Korean vs Japanese

- **Script** is the decisive signal: Hangul syllable blocks (U+AC00–U+D7A3) vs Hiragana (U+3040–U+309F) / Katakana (U+30A0–U+30FF) / Kanji. The two script regions are entirely disjoint.
- Modern Korean is **space-separated**; Japanese has no inter-word spaces.
- Both languages are SOV/agglutinative with typologically similar grammar, but the orthographic contrast is absolute at the codepoint level.

## kor ↔ Chinese (cmn / zho / yue / wuu)

- Any Hangul syllable → not Chinese. Chinese varieties use only Han characters and lack Hangul entirely.
- If a text mixes Hangul with occasional parenthesised Han (漢字), it is still Korean.

## kor ↔ other scripts

- Hangul is unique to Korean. No confusion with Latin, Cyrillic, Arabic, Devanagari, Thai, etc. because their Unicode blocks are fully disjoint.

## North ↔ South Korean orthographic variation

- Both varieties share the Hangul code range and are treated as the same CommonLID row. Differences are:
  - Spacing: North tends to concatenate more noun compounds.
  - Loanword orthography: South transliterates English-origin loans more liberally; North prefers native or Russian-origin forms.
  - Initial-sound rule (두음법칙): South writes 노동 (labour); North writes 로동. Same language, different orthographic policy — both fall under `kor_Hang`.
