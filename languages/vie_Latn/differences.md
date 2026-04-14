# Vietnamese vs. confusable languages

## vie ↔ any other Latin-script language in CommonLID

Vietnamese's diacritic inventory is **unique**. Key distinguishing features:

- **Letter đ / Đ** (U+0111 / U+0110) does not occur in any other CommonLID Latin-script language. It is sometimes confused visually with ð (Icelandic/Old English, not in this 8-language set), but the Unicode codepoints are different.
- **Horn diacritic** on ơ and ư does not appear in any other language worldwide.
- **Stacked double diacritics** (breve/circumflex + tone): ắ ằ ẵ ặ, ấ ầ ẫ ậ, ế ề ễ ệ, ố ồ ỗ ộ, ớ ờ ỡ ợ, ứ ừ ữ ự. No other Latin orthography routinely stacks two diacritics on a vowel.
- **Dot-below tone mark**: ạ ẹ ị ọ ụ ỵ and stacked variants. Absent elsewhere in this set.
- **Tone tilde over i, e, u** (ĩ ẽ ũ) and over already-modified vowels (ễ ỗ ữ) — Portuguese uses ã õ only; Vietnamese covers every vowel.
- Any sentence containing two or more of {ế, ớ, ễ, ộ, ợ, ử, ậ, đ} is Vietnamese with near certainty.

## vie ↔ tha — Vietnamese vs Thai

- Script entirely different: Vietnamese is Latin, Thai is the Thai script (U+0E00–U+0E7F). No confusion possible at the codepoint level.

## vie ↔ jpn / kor / cmn / zho / yue / wuu

- All the other languages in this 8-language set use CJK or Hangul scripts, entirely disjoint from Latin. A single Vietnamese letter disambiguates trivially from any of them.

## Edge cases

- Vietnamese proper nouns in ASCII-stripped form (no diacritics) look like generic Latin text. Such inputs lose most Vietnamese signals; rely on word-level lexical matches (là, của, không, được, những) if diacritics are missing.
