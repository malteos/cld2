# Distinguishing Kazakh from Confusable Languages

Kazakh can be confused with languages in two scripts. In Cyrillic the candidates are other Turkic languages and Russian, whose loanwords fill Kazakh text. In Arabic script the candidates are Uyghur and the major Perso-Arabic languages. The Arabic-script case is covered in detail in `chalis.md`. This file gives the short version.

## Cyrillic Script

### Kazakh vs. Kyrgyz (closest, highly confusable)

- **Letters:** Kyrgyz adds only **ң, ө, ү** to the Russian alphabet. Any **ә, ғ, қ, ұ, һ, і** means the text is not standard Kyrgyz. Kyrgyz spells /q/ and /ʁ/ with plain **к** and **г**.
- **Long vowels:** Kyrgyz writes long vowels double (**аа, ээ, оо, уу, өө, үү**: *баары*, *окуу*, *бөлүү*, *суроо*). Kazakh does not.
- **Initial э:** Kyrgyz writes *эмес, эле, эки*. Kazakh writes *емес, еді, екі*.
- **Rounding harmony:** Kyrgyz suffixes harmonise for rounding, giving forms like *-дун/-дүн, -го/-гө, -бу/-бү* (*үчүн*, *болуп*, *үйгө*, *колдун*). Kazakh suffixes do not round in writing.
- **ч vs ш:** Kyrgyz *үчүн, чык-, кичине* correspond to Kazakh *үшін, шық-, кішкене*.
- **Function words:** Kyrgyz *жана* "and", *менен* "with", *бул*, *жок*, *эмес*, *дагы*, *абдан* versus Kazakh *және*, *мен*, *бұл*, *жоқ*, *емес*, *тағы*, *өте*.

### Kazakh vs. Uzbek (Cyrillic)

- Uzbek Cyrillic has **ў, қ, ғ, ҳ**. It shares қ/ғ with Kazakh but lacks ә, ң, ө, ұ, ү, і. **ў** (U+045E) never occurs in Kazakh.
- Uzbek has largely lost vowel harmony: plural is always **-лар**, genitive **-нинг**, dative **-га/-ка/-қа**. Kazakh alternates *-лар/-лер*, *-ның/-нің*.
- Uzbek has initial **й** where Kazakh has **ж**: *йўқ / жоқ*, *йил / жыл*, *яхши / жақсы*.
- Function words: Uzbek *ва* "and", *билан* "with", *учун*, *бу*, *ҳам*, *эмас*, *лекин*.
- Since 1993 Uzbekistan's official script has been Latin (oʻ, gʻ, sh, ch), but Cyrillic Uzbek is still common online.

### Kazakh vs. Tatar

- Tatar has **ә, ө, ү, җ, ң, һ**, so it shares **ә ө ү ң һ** with Kazakh. Tatar has no **қ, ғ, ұ, і**, and it has **җ**, which Kazakh lacks.
- In Tatar, **ә** and **һ** are far more frequent (*һәм* "and", *белән* "with", *өчен* "for", *әле*, *һәр*).
- Regular vowel correspondences: Kazakh **е ↔ Tatar и**, **о ↔ у** (*деп / дип*, *бол- / бул-*); negation also differs lexically (*емес* vs *түгел*).
- Tatar initial **й/җ/ю** corresponds to Kazakh **ж** (*жыл / ел* "year", *жол / юл* "road", *жоқ / юк*).

### Kazakh vs. Bashkir

- Bashkir letters: **ә ө ү ғ ҡ ң ҙ ҫ һ**. Watch for **ҡ** (U+04A1) versus Kazakh **қ** (U+049B); they are visually almost identical. **ҙ** and **ҫ** are unique to Bashkir.
- Bashkir has **һ** where Kazakh has **с**, both word-initially and elsewhere (*һин / сен* "you", *һүҙ / сөз* "word"). As a result, **һ** is very frequent in Bashkir and rare in Kazakh.
- Function words: Bashkir *һәм*, *менән*, *өсөн*, *был*, *юҡ*, *тип*, *түгел*.

### Kazakh vs. Russian

- Russian has none of the nine Kazakh letters. Kazakh text is full of Russian loans (*президент*, *миллиард*, *компания*), and Russian quotations or names often appear inside Kazakh text.
- Use **function words** to decide which language dominates. Russian: *и, в, не, на, что, я, с, он, это, как*. Kazakh: *және, мен, бұл, үшін, деп, емес*.
- Shared strings such as **не** (Kazakh "what", Russian "not"), **да** (Kazakh "also", Russian "yes") and **бар** are ambiguous.
- Russian is fusional with prepositions (*в Москве*). Kazakh is agglutinative with postpositions (*Мәскеуде*, *Астана туралы*).
- Russian word endings **-ого, -ения, -ться, -ый/-ий** are absent from native Kazakh words.

### Also note

- **Karakalpak** (not in this benchmark) shares most Kazakh letters. It is written mainly in Latin today.
- **Mongolian** Cyrillic has **ө, ү** but none of **ә, қ, ғ, ұ, і**.
- **Ukrainian/Belarusian** share **і** but not the Turkic letters.

## Arabic Script

Kazakh in China (and historically elsewhere) is written in the Arabic-based **tote jazuw**, which writes **all vowels**. Quick discriminators:

- **vs. Uyghur** (the hardest case; both are fully vocalised Turkic orthographies):
  - Uyghur puts **ئ** before every word-initial vowel (*ئۇ, ئۈچۈن, ئەمەس*). Kazakh starts words with a bare vowel letter (*ول, ەمەس*), or puts the detached **high hamza ٴ** (U+0674) before front-vowel words that have no ە/ك/گ (*ٴۇشىن, ٴبىز*).
  - Uyghur has **ې, ۆ (=ö), ۈ (=ü)**. Kazakh uses **ۇ** for both ұ and ү and **و** for both о and ө, and its **ۆ** stands for **v** in loans.
  - Kazakh **ج** (ж) corresponds to Uyghur **ي** (*جوق / يوق*, *جىل / يىل*).
  - Kazakh *جانە* "and" vs Uyghur *ۋە*. Kazakh *بۇل* "this" vs Uyghur *بۇ*.
- **vs. Persian, Arabic, Urdu, Pashto:** these languages mostly leave short vowels unwritten. Kazakh text is therefore dense with **ا ە و ۇ ى** and uses **ە (U+06D5), ڭ, ۋ, ۇ, ى** and **ٴ**.
  - Persian uses **ی/ک** (U+06CC/U+06A9), **ه** and **ژ**.
  - Urdu uses **ے, ہ, ھ, ٹ, ڈ, ڑ**.
  - Pashto uses **ټ ډ ړ ږ ښ ځ څ ۍ**.
  - Arabic has the article **ال‍** before nouns, **ة**, and **ث ذ ص ض ط ظ**. None of these occur in native Kazakh words.

See `chalis.md` for word lists, a checklist and examples.
