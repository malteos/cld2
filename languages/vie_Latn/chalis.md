# Vietnamese (vie_Latn) under CHALIS conditions

In CHALIS (Tichý & Libovický 2026, arXiv 2606.06088) Vietnamese appears in the **diacritics-removed** condition: tone marks and vowel diacritics are stripped and *đ* becomes *d*, leaving plain ASCII. The gold label is the ISO 639-3 code **vie**. Vietnamese is not part of a CHALIS cousin pair and has no homoglyph condition, so the main task is recognizing Vietnamese when its most visible features are gone. Local references:

- `variants/no_diacritics/` (synthetic stripping of real UD text; models, but is not, the CHALIS data) and `variants/no_diacritics/vocabulary.tsv` (top 3,000 words, standard vs. stripped)
- `differences.md` (Pinyin, Yoruba/Igbo, Austronesian, other romanizations)
- `../chalis/discriminators.md` (no Vietnamese pair; useful only to see the method)

## 1. Confusable-language cues robust to noise

There is no close cousin in CHALIS. Realistic confusions for stripped Vietnamese are other short-token Latin strings: toneless Hanyu Pinyin, Cantonese/Korean/Thai/Hmong romanizations, and Austronesian languages (Indonesian, Malay, Tagalog). Cues that survive stripping:

- **One syllable per token**, almost always 1–7 letters; Pinyin, Indonesian, Tagalog and Thai romanization join syllables into longer words.
- **Stop codas** *-c, -ch, -t, -p* and nasal codas *-m, -n, -ng, -nh* (*mot, viet, hoc, dep, cach, lam, anh*). Pinyin has no stop codas; word-final *-nh* is rare in other common romanizations.
- **No *f, j, w, z*** in native words (Pinyin uses *j, w, z, zh* constantly).
- **Vietnamese-only onsets**: *ngh-* (*nghe, nghi, nghiep*), *gh-* (*ghe*), *nh-* (*nhu, nhung, nha*), *tr-*, *th-*, *ph-*, *kh-*, *gi-* (*gia, gio*), *qu-* (*quoc, qua*), *ng-* (*nguoi, ngay*). *ngh*, *nh-* and *gh-* as word onsets are especially telling.

## 2. Vietnamese without diacritics

Stripping merges many words: in `variants/no_diacritics/vocabulary.tsv` the 3,000 top words collapse to 1,358 distinct ASCII forms; *do* alone stands for *đó, độ, do, đồ, đô, đỏ, đổ, đỡ* and more. Identification must therefore rely on **syllable shape and frequent function words**, not on individual meanings.

Example (from `variants/no_diacritics/ud_03.txt`):

> *Nhung chat luong thuc te vo cung kem, mot dua tre cung co the de dang bop hai thanh mu cham nhau.*

Original: *Nhưng chất lượng thực tế vô cùng kém, một đứa trẻ cũng có thể dễ dàng bóp hai thành mũ chạm nhau.* Surviving cues: all tokens monosyllabic; *nh-, th-, tr-, ch-* onsets; codas *-ng, -nh, -t, -c, -p, -m*; the function words *nhung, mot, cung, co the*; the vowel cluster *uo* (*luong* < *lượng*).

Top stripped tokens (rank order from the vocabulary file): *la, va, co, cua, duoc, mot, cac, khong, trong, cho, nguoi, nay, voi, o, da, the, de, nhu, nhung, den, khi, lam, se, tu, ra, cong, ho, tai, ve, vao, do, cung, thanh, lai, dau, chi, nam, su, toi, bi, hoc, phai*.

Very strong stripped markers: *duoc* (được), *nguoi* (người), *khong* (không), *nhung* (những/nhưng), *truoc* (trước), *nuoc* (nước), *cua* (của), *trong*, *nhieu*, *chung toi*, *Viet Nam*. The *uo* sequence (from *ươ/uô*) before *c, i, n, ng, t* (*duoc, nguoi, muon, truong, thuoc*) is rare in other languages' short tokens.

**Ambiguity cases**: very short inputs of tokens that are also English or other words (*a, o, me, the, do, co, an, to, ban*) are not enough. *the* is a frequent Vietnamese token (*thể/thế/thẻ*) and also English; decide by its neighbours (*co the* → Vietnamese, *the house* → English).

## 3. Recognizing tone-mark-free Vietnamese (practical tests)

1. Split on spaces. If ≥ 80% of tokens are ≤ 7 letters and fit the template (onset)(vowels)(coda), Vietnamese is likely (threshold is a heuristic, not a measured value).
   - Onsets: *b c ch d g gh gi h k kh l m n ng ngh nh p ph qu r s t th tr v x* or none.
   - Codas: *c ch m n ng nh p t* or glide vowels *i y o u*.
2. Look for at least two of: *la, va, cua, duoc, mot, cac, khong, trong, nguoi, nhung, voi, cho, nay, nhu, den*.
3. Reject if there are many tokens with *f, j, w, z*, final *-k, -s, -r, -l, -d*, or initial clusters like *st, pr, kl, zh, sh*.
4. Proper names in Vietnamese order (*Nguyen Van ..., Tran Thi ..., Ha Noi, Sai Gon, Da Nang*) are supportive.

Homoglyphs are not applied to Vietnamese in CHALIS. If Cyrillic/Greek look-alikes nevertheless appear inside Latin tokens, normalize them to Latin first; a mostly-Latin token with one Cyrillic letter is noise, not a Cyrillic language.

Possible but undocumented noise: Telex or VNI residues from failed input methods (*Vieejt Nam*, *dduwowcj*, *Vie65t*). Doubled vowels (*aa, ee, oo*), *dd*, *uw/ow* and a trailing *s f r x j* on otherwise Vietnamese syllables point to Telex-typed Vietnamese.

## 4. Decision checklist

1. Any *ơ, ư, đ*, stacked marks (*ệ, ộ, ữ*) or characters in U+1EA0–U+1EF9 → **vie**.
2. Otherwise check token shape: short monosyllables, Vietnamese onsets/codas, no *f/j/w/z*.
3. Check function words (*la, va, co, cua, duoc, mot, cac, khong, trong, nguoi, nhung*).
4. Rule out Pinyin (*zh, j, w, z, -ou, -ei, -ian*, joined words), Indonesian/Tagalog (long words, *yang, dengan, ang, mga*), Korean romanization (*eo, eu, -seyo*).
5. If 2 and 3 hold and 4 finds nothing, label **vie**.

## 5. Illustrative noisy snippets

1. *Toi khong biet ong ay da den Ha Noi hay chua.* → **vie** (*toi, khong, biet, da, den, chua*; stop codas; place name).
2. *Nhung nguoi nay dang cho o ngoai cua.* → **vie** (*nhung, nguoi, nay, dang, ngoai*; *ng/nh* onsets).
3. *Wo shi zhongguo ren, wo xihuan chi mian.* → **not vie** (Mandarin Pinyin: *w, zh*, joined *zhongguo, xihuan*, final *-ian*).
