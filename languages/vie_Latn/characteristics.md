# Vietnamese (vie_Latn) - Orthographic and LID Characteristics

## Letter inventory

The alphabet has 29 letters: *a ă â b c d đ e ê g h i k l m n o ô ơ p q r s t u ư v x y*. Native words do **not** use *f, j, w, z* (they appear only in foreign names and loanwords). On top of the base letters, five tone marks may be added to any vowel letter, giving 12 vowel letters (*a ă â e ê i o ô ơ u ư y*) × 6 tones (one unmarked) = 72 lowercase vowel forms.

## Diagnostic characters

| Char | Codepoint | Notes |
|---|---|---|
| **ơ / Ơ** | U+01A1 / U+01A0 | o with horn. Essentially unique to Vietnamese among major languages. |
| **ư / Ư** | U+01B0 / U+01AF | u with horn. Essentially unique to Vietnamese. Digraph *ươ* (*người, được, trước, nước*) is extremely typical. |
| **đ / Đ** | U+0111 / U+0110 | d with stroke. Also Croatian/Bosnian/Serbian Latin, but there without tone marks. Vietnamese uppercase is U+0110 (not Icelandic Ð U+00D0). |
| **ă** | U+0103 | Also Romanian. With tones: *ắ ằ ẳ ẵ ặ* (U+1EAF–U+1EB7). |
| **Hook above** (hỏi) | combining U+0309 | Precomposed *ả ẩ ẳ ẻ ể ỉ ỏ ổ ở ủ ử ỷ* (U+1EA3, U+1EA9, U+1EB3, U+1EBB, U+1EC3, U+1EC9, U+1ECF, U+1ED5, U+1EDF, U+1EE7, U+1EED, U+1EF7). Practically Vietnamese-only. |
| **Dot below** (nặng) | combining U+0323 | *ạ ậ ặ ẹ ệ ị ọ ộ ợ ụ ự ỵ* (U+1EA1 ... U+1EF5). *ọ ẹ ị ụ* also occur in Yoruba/Igbo, but stacked forms like *ộ ệ ậ ợ ự* are Vietnamese. |
| **Stacked marks** | | Circumflex/breve/horn + tone on one vowel: *ế ề ể ễ ệ, ố ồ ổ ỗ ộ, ấ ầ ẩ ẫ ậ, ớ ờ ở ỡ ợ, ứ ừ ử ữ ự*. Two diacritics on one letter is the strongest single visual signal of Vietnamese. |
| à á â ã è é ê ì í ò ó ô õ ù ú ý | Latin-1 | Shared with French, Portuguese etc.; not diagnostic alone. |

Most precomposed toned letters live in the Unicode block **Latin Extended Additional, U+1EA0–U+1EF9**, which is used almost exclusively for Vietnamese. Decomposed (NFD) text uses base letters + U+0300 (grave), U+0301 (acute), U+0303 (tilde), U+0309 (hook), U+0323 (dot below).

Measured on the repository's UD sample (`examples/ud_*.txt`, about 9,000 letters, so indicative only), the most frequent non-ASCII letters were *đ* 2.6%, *à* 2.3%, *ư* 1.8%, *ô* 1.5%, *á* 1.4%, *ó* 1.1%, *ạ* 1.0%, *ế* 0.9%, *ờ* 0.9%. In that sample about 29% of all letters were non-ASCII (carried at least one diacritic or were *đ*).

## Token shape

- Every syllable is a separate space-delimited token. Average token length in the UD sample was about **3.3 letters**; native syllables have at most 7 letters (*nghiêng*); in the sample no token exceeded 7 letters.
- Onsets (spelled): *b, c, ch, d, đ, g, gh, gi, h, k, kh, l, m, n, ng, ngh, nh, p, ph, qu, r, s, t, th, tr, v, x*, or none.
- Codas (spelled): *c, ch, m, n, ng, nh, p, t* or vowel glides *i, y, o, u*. No other final consonants: tokens ending in *-b, -d, -g (except -ng), -k, -l, -r, -s, -v, -x* are not native Vietnamese.
- Spelling rules: *k* before *i, y, e, ê* (*kể, kỹ*), *c* elsewhere (*cá, có*); *gh/ngh* before *i, e, ê* (*nghĩ, ghế*), *g/ng* elsewhere; *q* always as *qu*.

## Top ~50 function words (from vocabulary.json, rank order, content words skipped)

*là, và, có, của, được, một, các, không, trong, cho, người, này, với, ở, đã, thể, để, như, những, đến, khi, làm, sẽ, từ, ra, họ, tại, về, vào, đó, cũng, lại, chỉ, tôi, bị, phải, mà, thì, trên, sau, còn, chúng, mình, nhưng, rất, theo, hơn, nhất, đây, nên, cả, vì, nó, nhiều, đang, do, lên, hay, nếu, trước, nào, cùng, qua, mới, bằng, rằng, hoặc, vẫn, gì*

Without diacritics (from `variants/no_diacritics/vocabulary.tsv`): *la, va, co, cua, duoc, mot, cac, khong, trong, cho, nguoi, nay, voi, o, da, the, de, nhu, nhung, den, khi, lam, se, tu, ra*.

## Frequent character n-grams (UD sample, lowercase)

- Bigrams: *ng, nh, th, ch, ôn, kh, an, tr, hi, ườ, ên, ại, qu, ph, iế, ời, iệ, gi, uy*
- Trigrams with boundaries: *ng␣, ␣th, ␣ch, ␣nh, nh␣, ông, ␣kh, ␣ng, ␣tr, ên␣, ại␣, ␣qu, ␣ph, ết␣, ời␣, ới␣, như, anh, ười, ngư, ngh, một*
- Most frequent syllable endings: *-ông, -ười, -ờng, -ưng, -ững, -anh, -oại, -ồng, -ơng, -yện, -ong, -ành, -ước*.

The token-final pattern *-ng/-nh* combined with token-initial *ng-, nh-, th-, tr-, kh-, ph-* is a strong signal even without diacritics.

## Orthographic conventions

- Proper names capitalize every syllable (*Hà Nội, Nguyễn Văn An, Thành phố Hồ Chí Minh*); common nouns are lowercase.
- Very frequent surnames: *Nguyễn, Trần, Lê, Phạm, Hoàng/Huỳnh, Phan, Vũ/Võ, Đặng, Bùi, Đỗ*.
- Compounds may be hyphenated in some older or foreign transcriptions (*Hà-nội*) and some corpora join syllables with underscores (*học_sinh*) for word segmentation; neither is standard in running text.
- Tone-mark placement varies between "old" and "new" styles (*hòa/hoà, thủy/thuỷ*); both are correct Vietnamese.
- Numbers use a dot as thousands separator and a comma as decimal mark (*1.000.000*, *3,5*).
- In typed text failures of input methods can leave Telex/VNI residues (*Vieejt Nam, tieengs*, *Vie6t*); this is a possible noise type, not one documented for CHALIS.
