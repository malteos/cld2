# English under Obfuscation (CHALIS `homoglyphs`, `antspeak`, `leetspeak`)

In three CHALIS sections the gold label is **eng**, but the surface form has been deliberately disguised. In each case the right move is to **undo the disguise first** and then identify the language from the recovered text. The common failure is to label the surface instead: "Russian/Greek" for homoglyphs, "unknown/garbage" for antspeak and leetspeak.

The examples in `variants/` (homoglyphs, antspeak, leetspeak) come from `languages/scripts/build_chalis_variants.py`, applied to authentic UD English passages. They imitate the CHALIS perturbations but are **not** the CHALIS data. Real samples may use more or different substitutions.

## 1. Homoglyphs

**What it looks like:** *I doubt the νеry fеw who асtually reаd my blog hаve not cоme acrоѕѕ this yеt…* The text renders as normal English, but some Latin letters have been replaced by Cyrillic or Greek letters that look the same.

**Substitution table used in the repo variant** (about 50% of eligible letters):

| Latin | Look-alike | Codepoint |
|---|---|---|
| a / A | а / А | Cyrillic U+0430 / U+0410 |
| c / C | с / С | U+0441 / U+0421 |
| e / E | е / Е | U+0435 / U+0415 |
| o / O | о / О | U+043E / U+041E |
| p / P | р / Р | U+0440 / U+0420 |
| x / X | х / Х | U+0445 / U+0425 |
| y | у | U+0443 |
| i | і | U+0456 (Ukrainian i) |
| j | ј | U+0458 (Serbian je) |
| s | ѕ | U+0455 (Macedonian dze) |
| v | ν | **Greek nu** U+03BD |
| B H K M T | В Н К М Т | Cyrillic capitals |

Real data may also use Greek **ο** (omicron), **α**, **ι**, **κ**, **τ**, Cyrillic **һ**, **ԁ**, **ԛ**, **ԝ**, or other confusables. Normalise anything that has a Latin twin.

**How to recognise it:**
- **Mixed-script tokens.** A single word mixes Latin and Cyrillic or Greek codepoints (*асtually*, *ѕсreеnѕhоtѕ*). Genuine Russian, Bulgarian or Greek text almost never mixes scripts inside a word. In the repo sample, 420 of 636 tokens (66%) were mixed-script.
- **Only "Latin-shaped" Cyrillic letters occur.** You see а е о р с у х і ј ѕ but never б, д, ж, з, и, л, п, ф, ц, ч, ш, щ, ы, ь, э, ю, я. Real Cyrillic text uses these constantly.
- **Normalise, then read.** Map each look-alike to its Latin twin. The result is plain English: *the very few who actually read my blog…* Function words (*the, and, of, to, a, in, is, that*) appear immediately.
- **Watch for ces/slk in the same section.** Homoglyph text that still contains č ř ě ů (Czech) or ľ ĺ ô ä (Slovak) after normalisation is Czech or Slovak, not English. In the repo variant, precomposed accented letters (č, é, ô) are never substituted, so they survive as Latin.

**Do not over-apply.** A Russian text with an embedded English brand name (*Microsoft*) has whole Latin words, not mixed letters. A Serbian/Macedonian text naturally contains ј and ѕ alongside љ, њ, џ, ќ, ѓ. A Greek text has ν next to λ, π, ς, ω, ή. If the letters are script-native and script switches happen only between whole words, treat the text as genuinely Cyrillic or Greek.

## 2. Antspeak

**What it looks like:** *I d o u b t t h e v e r y f e w w h o a c t u a l l y r e a d m y b l o g …*

In the repo variant every character is separated by a single space, and **word boundaries are lost**: the space between words is indistinguishable from the space between letters. CHALIS may preserve word gaps, for example as double spaces. **Uncertain.** If it does, use them.

**How to recognise it:**
- Almost every token has length 1. Punctuation is also a separate token (`y e t ,`).
- Remove the spaces and read the resulting string. English words segment out readily: *idoubttheveryfewwhoactuallyreadmyblog* → "I doubt the very few who actually read my blog". Frequent anchors are *the, and, ing, tion, that, with, you*.
- Capital letters inside the stream (*J o h n D o n o v a n*, *I*) often mark sentence starts or names and help segmentation.
- After rejoining, identify the language normally. Antspeak can apply to any language. Here the gold label is English, but rejoined text containing *jsem, který* would be Czech.

**Do not over-apply.** Lists of single-letter variables, initialisms (*U S A*), chess or math notation, and German or Czech letter-spaced emphasis (*g e s p e r r t*, applied to one or two words only) are not antspeak. Antspeak covers the whole text.

## 3. Leetspeak

**What it looks like:** *I dou87 7h3 very f3w wh0 4ctu41ly r34d my blog h4ve no7 c0m3 4cr0ss 7hi5 ye7…*

**De-leet map used in the repo variant** (about 70% of eligible letters are replaced):

| Digit | Letter(s) |
|---|---|
| 4 | a |
| 3 | e |
| 1 | **i or l** (ambiguous) |
| 0 | o |
| 5 | s |
| 7 | t |
| 8 | b |
| 9 | g |

Real leetspeak may also use `@`=a, `$`=s, `|`=l/i, `+`=t, `ph`=f, `|-|`=h, `\/`=v, `()`=o. This is **not confirmed** for CHALIS.

**How to recognise it:**
- Digits sit **inside** alphabetic words (*7h3*, *4ctu41ly*, *pr0of*). In the repo sample, 527 of 636 tokens mixed digits and letters. Ordinary numbers (*2010*, *55th*) stand alone or carry ordinal suffixes.
- Resolve **1** from context: try *i* and *l* and keep the reading that gives a word. *w1111n9* → "willing", *f14g* → "flag", *1n* → "in", *1* → "I". *8* and *9* can also be real digits.
- Unreplaced letters survive (the same word can show up as *the / 7h3 / 7he / th3*), so use the plain words as anchors: *the, of, and, my, very*.
- After de-leeting, check for English morphology (*-ing → 1n9*, *-tion → 710n*, *'s → '5*) and function words.

**Do not over-apply.** Product codes (*MP3, B2B, 4K*), chemical formulas (*H2O*), and texting abbreviations (*gr8, 2day, b4*) inside otherwise normal text do not make a text leetspeak. Leet-encoded text in another language is still that language. De-leet first, then decide.

## Checklist

1. Does a token mix Latin with Cyrillic or Greek letters, using only look-alike letters? → normalise homoglyphs, then identify. The candidates in CHALIS are eng, ces and slk.
2. Is the text almost entirely single-character tokens? → antspeak. Join and segment, then identify.
3. Do digits 0 1 3 4 5 7 8 9 appear inside words? → leetspeak. De-leet, try both i and l for 1, then identify.
4. After the repair, look for English function words (*the, and, of, to, is, that, you, it*) and endings (*-ing, -ed, -tion, -ly*). If they are present, the answer is **eng**.
5. Is the text genuinely Cyrillic or Greek, with native letters and no word-internal mixing? → it is not a disguised language. Identify the script-native language.
