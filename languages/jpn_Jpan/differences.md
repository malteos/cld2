# Japanese vs. confusable languages

## jpn ↔ cmn / zho / yue / wuu — Japanese vs Chinese

- **Decisive signal**: presence of Hiragana (U+3040–U+309F) or Katakana (U+30A0–U+30FF). Chinese varieties use only Han characters plus full-width punctuation; they never contain kana.
- Sentence-final `です。` / `ます。` / `だ。` is Japanese-only.
- Kanji with trailing hiragana inflection (食べる, 行きます, 書いた) is Japanese-only.
- Katakana prolongation mark `ー` inside words does not occur in Chinese.
- In the rare edge case of a pure-Kanji short string (headline, name, compound), disambiguation is hard; look for Japanese-only kanji forms (例: 働, 峠, 辻, 畠) or the Japanese simplification set (学 vs 學, 国 vs 國 — overlaps with PRC Simplified, so non-decisive).

## jpn ↔ kor — Japanese vs Korean

- Korean uses Hangul syllable blocks (U+AC00–U+D7AF) almost exclusively. Any Hangul → not Japanese. Any Hiragana/Katakana → not Korean.
- Modern Korean text typically contains zero Han characters; Japanese text typically contains many.

## jpn ↔ other scripts

- Japanese is not confusable with any Latin, Cyrillic, Arabic, Devanagari, Thai, or other script language because Hiragana/Katakana/Kanji block membership is disjoint from those scripts.

## Edge cases

- Romaji-only Japanese (rare in natural text) can look like Latin-script languages; word endings in `-masu`, `-desu`, `-tta`, `-nai` and particles `wa`, `ga`, `no`, `wo` still identify it, but this is outside normal `jpn_Jpan` scope.
