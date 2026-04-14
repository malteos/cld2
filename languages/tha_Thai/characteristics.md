# Thai LID characteristics

## Script signals

- **Thai block** (U+0E00–U+0E7F) is disjoint from every other script — any character in this range is an immediate, high-precision Thai signal. (The related Lao block is U+0E80–U+0EFF, so they are adjacent but distinct.)
- **No inter-word spaces** within a sentence; spaces appear only at clause or sentence breaks.
- **Tone marks** (combining): ่ (U+0E48 mai ek), ้ (U+0E49 mai tho), ๊ (U+0E4A mai tri), ๋ (U+0E4B mai chattawa). Mai tho and mai ek are the most frequent.
- **Inherent vowel** means consonant runs often carry no explicit vowel.
- **Vowels written around consonant**: เ- แ- โ- ใ- ไ- (pre-consonant); -า -ำ -ิ -ี -ึ -ื -ุ -ู (post/above/below).
- **Digits**: ๐ ๑ ๒ ๓ ๔ ๕ ๖ ๗ ๘ ๙ coexist with Arabic 0–9.

## Top function words

ที่, และ, ใน, ของ, ได้, จะ, ไม่, เป็น, มี, กับ, ก็, แล้ว, ให้, มา, ไป, อยู่, กำลัง, ต้อง, หรือ, แต่, ถ้า, เพราะ, เมื่อ, นี้, นั้น, คน, เขา, เธอ, ฉัน, ผม, ดิฉัน, คุณ, เรา, พวก, อย่าง, มาก, น้อย, แค่, อีก, ซึ่ง.

## N-gram / spelling patterns

- Common short tokens delimited by clause-space: ` ที่ ` ` และ ` ` ใน ` ` ของ `.
- The iteration mark **ๆ** (U+0E46) after a word means "repeat"; a strong Thai-unique signal.
- The abbreviation sign **ฯ** (U+0E2F) and the "et cetera" glyph **ฯลฯ**.
- Frequent pre-vowels leading syllables: เ◌, แ◌, โ◌, ไ◌, ใ◌ — characters U+0E40–U+0E44 starting a cluster.
- Mai han-akat (ั) and the silencer mark (์ U+0E4C, karan) used in loanword spellings: โทรทัศน์ 'television', สยาม'.

## Morphology hooks

- Reduplication / iteration via ๆ, e.g. เด็กๆ 'children', เร็วๆ 'quickly-quickly / soon'.
- Compounding freely: นัก + verb → agent (นักเรียน 'student'), การ + verb → nominalised action (การเรียน 'studying'), ความ + adj → abstract noun (ความสุข 'happiness').
- Classifier insertion mandatory: `N + Num + CL`.

## Punctuation / orthography quirks

- Sentence boundaries are implicit; Western punctuation (. , ! ?) has been partially adopted but spaces still do much of the work.
- Karan mark ์ over a consonant silences it, normally in Sanskrit/Pali or English loans.
- Angkhan khu ๚ and khomut ๛ appear in literary/religious texts.
