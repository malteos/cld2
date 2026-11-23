# Vietnamese (vie_Latn) - Differential Diagnostics

Vietnamese with diacritics is one of the easiest languages to identify: stacked diacritics (*ệ, ộ, ữ, ẩ*), the horned letters *ơ ư*, and the Latin Extended Additional block (U+1EA0–U+1EF9) are almost exclusive to it. Confusion arises mainly with (a) other tone-marked or dot-below orthographies, (b) **diacritic-free** text, where Vietnamese syllables look like generic short Latin tokens, and (c) romanizations of other Asian languages.

## Vietnamese vs. Hanyu Pinyin (Mandarin romanization)

Pinyin is the most likely confusion for both toned and toneless Vietnamese.

| Cue | Vietnamese | Pinyin |
|---|---|---|
| Tone marks | grave, acute, tilde, hook above, dot below | macron *ā*, acute *á*, caron *ǎ* (U+01CE etc.), grave *à*; never hook or dot below |
| Special letters | *đ ơ ư ă â ê ô* | *ü* (U+00FC), sometimes *v* for ü |
| Word division | one syllable per token (*Trung Quốc*) | polysyllabic words joined (*Zhōngguó*, *xuéshēng*) |
| Finals | *-p, -t, -c, -ch, -m, -n, -ng, -nh* | only *-n, -ng, -r*; no stop finals |
| Initials | *đ, nh, ngh, gh, tr, th, ph, kh, gi* | *zh, ch, sh, z, c, j, q, x, r, w* |
| Letters f/j/w/z | absent in native words | *j, w, z* very common |

Machine-checkable: tokens ending in *-t, -p, -c, -ch, -m, -nh* (*một, việt, học, đẹp, cách, làm, anh*) → Vietnamese. Initial *zh-, j-, w-, z-*, or finals *-ou, -ei, -ian, -er* (*zhou, mei, tian, er*), none of which form a Vietnamese syllable → Pinyin. (Pinyin *-ui, -iu, -ao, -uan* do occur in Vietnamese too: *vui, chịu, bao, quan*.) Caron tones (*ǎ ě ǐ ǒ ǔ*) → Pinyin.

## Vietnamese vs. Yoruba and Igbo

Both use dot-below letters that overlap with Vietnamese *nặng*: Yoruba *ẹ ọ ṣ* (+ acute/grave tones), Igbo *ị ọ ụ ṅ*.

- *ṣ* (U+1E63) and *ṅ* (U+1E45) never occur in Vietnamese.
- Stacked marks (*ộ, ệ, ặ, ợ, ự*), horned *ơ ư*, *đ*, hook above → Vietnamese only.
- Yoruba/Igbo words are polysyllabic and vowel-final (*ọmọ, àwọn, ndị, nke*); Vietnamese tokens are monosyllables often ending in *-ng/-nh/-t/-c*.
- Function words: Yoruba *ní, àti, tí, ṣe, wọ́n*; Igbo *na, nke, ndị, ya*; Vietnamese *và, của, là, có, không*.

## Vietnamese vs. Austronesian languages of SE Asia (Indonesian, Malay, Tagalog, Cebuano, Javanese)

These are mostly diacritic-free and polysyllabic: *yang, dengan, untuk, tidak, adalah* (Indonesian/Malay), *ang, ng, mga, sa, na, hindi* (Tagalog). Average word length is clearly greater than Vietnamese (~3.3 letters per token in the repository's Vietnamese UD sample). Distinctive: frequent *-an, -kan, -nya, ber-, meng-* affixes (Malay/Indonesian), *mag-, nag-, -in-* (Tagalog). Note Tagalog *ng* and *mga* are short and could match Vietnamese-like tokens; *mga* is impossible in Vietnamese (no *mg*).

## Vietnamese vs. other mainland SE Asian romanizations

- **Thai/Lao romanization** (RTGS etc.): polysyllabic joined words, finals like *-k, -p, -t* written with *k* (*Sukhumvit, krung thep*), *ph, th, kh* shared with Vietnamese. Final *-k* and initials *kr-, kl-, pr-, pl-* are impossible in Vietnamese.
- **Khmer romanization**: clusters such as *kh, chh, sr, pr, tr, kr* and finals *-k, -h, -s* (*Kampuchea, Preah, Sihanouk*).
- **Hmong RPA**: syllables end in tone letters *-b, -j, -v, -s, -g, -m, -d* and use doubled vowels for nasality (*kuv, hmoob, ntawv, peb*); onsets *hm, ntx, nq, pl* are impossible in Vietnamese.
- **Burmese romanization**: *-aung, -yi, ky-, hl-, hm-* (*Aung San, Kyaw*).
- **Muong** (closest relative) is written in Vietnamese-based orthography; distinguishing it requires lexical knowledge and is out of scope here (uncertain).

## Vietnamese vs. Romanian, French, Portuguese, Slovak

These share individual letters (*ă* Romanian; *â ê ô à é* French/Portuguese; *ô* Slovak) but never combine two diacritics on one vowel and never use *ơ ư đ*, hook above or dot below. Their words are polysyllabic with inflectional endings (*-ul, -ment, -ção, -ých*).

## Vietnamese vs. diacritic-free Vietnamese-like strings

When diacritics are stripped (see `variants/no_diacritics/`), the 3,000 most frequent Vietnamese words collapse to only 1,358 distinct ASCII forms (e.g. *do* stands for *đó, độ, do, đồ, đô, đỏ, đổ, đỡ* ...). Remaining positive evidence:

1. **Token length**: almost all tokens 1–7 letters, mean around 3–4.
2. **Onset/coda grammar**: every token fits (onset)(vowels)(coda) with onsets from *b c ch d g gh gi h k kh l m n ng ngh nh p ph qu r s t th tr v x* and codas from *c ch m n ng nh p t* or a vowel. A token like *strong, black, would* fails this test.
3. **High-frequency function words**: *la, va, co, cua, duoc, mot, cac, khong, trong, cho, nguoi, nay, voi, nhung, nhu, den, khi, se, tu, ve, vao, cung, thi, ma*.
4. **Vowel clusters typical of Vietnamese**: *uo* (from *ươ*: *duoc, nguoi, truoc, nuoc*), *ie* (*viet, tien, hien*), *oa, oai, uy, uye* (*hoa, ngoai, quyen, chuyen*).
5. **Absence** of *f, j, w, z* and of double consonant letters other than the digraphs above.

Strings that pass tests 1–2 but are not Vietnamese: toneless Pinyin (*wo shi zhongguo ren* – contains *w, zh*, joined *zhongguo*), Cantonese romanization (*nei5 hou2, m4 goi1* – tone digits; standalone *m*/*ng* syllables; Jyutping *eoi, oe* finals, uncertain as a sole cue), Korean romanization (*annyeong haseyo, eumsik* – *yeo, eu, ae* sequences, absent from Vietnamese; note Vietnamese does have *eo* as in *theo*), Hawaiian/Maori (no final consonants at all, *wh*, macrons). If tests 3–4 also succeed, the text is Vietnamese.
