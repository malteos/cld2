# Kazakh in Arabic Script (CHALIS section `arabic`)

In the CHALIS `arabic` section the gold label is **kaz**: Kazakh written in the Arabic-based alphabet (*tote jazuw* / *töte jazuw*, төте жазу). This script is used by Kazakhs in China (Xinjiang) and historically in Iran, Afghanistan and Mongolia. It goes back to Akhmet Baitursynuly's reform of the early 20th century. Unlike Persian or Arabic writing it is a **full alphabet**: every vowel is written. The main risks are confusing it with **Uyghur**, which is also a fully vocalised Turkic Arabic-script orthography, or with **Persian/Arabic/Urdu/Pashto/Sorani Kurdish** because the letters look the same.

**About the evidence in this repo.** The files in `variants/arabic_script/` were produced by a **simplified rule-based converter** (`languages/scripts/translit.py`, function `kk_cyr2arab`) applied to authentic Cyrillic Kazakh. They are not real tote jazuw texts. Statements below marked "(converter)" describe that output. Points where real usage may differ are flagged.

## Letter Correspondences (as in the converter)

| Cyrillic | Arabic | Note |
|---|---|---|
| а, ә | ا | ә is distinguished only by the word-level hamza ٴ |
| е, э | ە (U+06D5 AE) | not Persian ه (U+0647) |
| о, ө | و | |
| ұ, ү | ۇ (U+06C7) | |
| ы, і | ى (U+0649, dotless) | the most frequent letter in the converted sample |
| у | ۋ (U+06CB) | |
| в | ۆ (U+06C6) | loanwords only; in **Uyghur** ۆ means **ö** |
| и, й | ي | ий → يي (converter) |
| қ / к | ق / ك (U+0643) | |
| ғ / г | ع (U+0639, **no dot**) / گ | Uyghur writes /ʁ/ with غ (dotted) |
| ң | ڭ (U+06AD) | |
| ж / ш / ч | ج / ش / چ | |
| х / һ | ح / ھ | |
| ц, щ | تس, شش | loans (converter) |

**The hamza rule.** One detached **high hamza ٴ (U+0674)** goes at the **start** of a word that contains front vowels (ә, ө, ү, і) and **no** ە/ك/گ. Those three letters already mark the word as front-vocalic. Examples: *біз → ٴبىز*, *үшін → ٴۇشىن*, *қазір → ٴقازىر*, *бірақ → ٴبىراق*. Words that contain ە/ك/گ get no hamza, even when they are front-vocalic: *мемлекет → مەملەكەت*, *сізге → سىزگە*, *үлкен → ۇلكەن*. In the four converted passages, 68 of 899 tokens (about 7.6%) begin with ٴ (converter). Real texts may also use precomposed high-hamza letters (ٵ ٶ ٷ ٸ, U+0675–U+0678) or put the hamza elsewhere through input-method habits. **Uncertain.**

**Converter simplifications and likely differences from real tote jazuw:**
- Russian loans are transliterated letter by letter from Cyrillic (*стратегия → ستراتەگييا*, *компания → كومپانييا*, *Назарбаев → نازارباەۆ*). Real Chinese Kazakh texts usually adapt loans differently. They also contain **Chinese** loans and names (e.g. *جۇڭگو* "China", from Zhōngguó) rather than Russian ones. Expect content differences.
- Arabic has no capital letters. Embedded Latin is also lowercased in the converter (*xxi*).
- Only `,` → `،` and `?` → `؟` are converted. Digits stay Western (0–9). Real texts may use Arabic-Indic digits or `؛`. **Uncertain.**
- The hamza is decided per space-separated token, so tokens beginning with punctuation or digits never get it.

## Kazakh vs. Uyghur (the key confusion)

| Feature | Kazakh tote jazuw | Uyghur Ereb Yéziqi |
|---|---|---|
| Word-initial vowel | bare letter: *ول، ەندى، ەمەس، ادام* | always **ئ** + vowel: *ئۇ، ئەمەس، ئادەم* |
| Front-vowel marking | word-initial **ٴ** | separate letters: **ۆ ö, ۈ ü, ې é** |
| ö / ü | written as و / ۇ (+ ٴ) | ۆ / ۈ |
| ۆ | = v (rare) | = ö (very common) |
| /ʁ/ | **ع** (*ماعان*, *باعىت*) | **غ** (*تاغ*, *ياغاچ*) |
| x | ح (*حالىق*) | خ (*خەلق*) |
| Kazakh ж ~ Uyghur y | **ج**: *جوق، جاقسى، جىل* | **ي**: *يوق، ياخشى، يىل* |
| Kazakh ш ~ Uyghur ch | *ٴۇشىن، شىق-* | *ئۈچۈن، چىق-* |
| "and" | **جانە** | **ۋە** |
| "this" | **بۇل** | **بۇ** |
| "for" | **ٴۇشىن** | **ئۈچۈن** |
| "not (be)" | **ەمەس** | **ئەمەس** |
| "very" | **وتە** | **ناھايىتى** |

**Shared and therefore NOT diagnostic between the two:** *مەن* "I", *دەپ* (quotative), plural *-لار/-لەر*, genitive *-نىڭ/-دىڭ*, *بار*, *بولۇپ / بولىپ* (similar), and the letters ڭ ۋ ۇ ە ى گ ق. Seeing **ئ** at the start of many words, or any **ې/ۈ**, points to Uyghur. Seeing **ٴ** and **ج**-initial words with no ئ points to Kazakh.

## Kazakh vs. Persian, Arabic, Urdu, Pashto, Sorani

- **Vowel density.** Kazakh writes every vowel, so almost every second letter is one of **ا ە و ۇ ى**. Persian, Arabic and Urdu leave short vowels unwritten and have long consonant clusters on the page.
- **Letters Kazakh uses that most of these lack:** ە (U+06D5), ى as a word-internal vowel, ۇ, ۋ, ڭ, ٴ.
- **Letters Kazakh does not use in native words:**
  - Arabic **ة, ث, ذ, ص, ض, ط, ظ**, the article **ال‍** prefixed to nouns (note that Kazakh *ال-* "take" and *الەم* "world" exist), and tanwin.
  - Persian **ی ک** (U+06CC, U+06A9), **ژ**, word-final **ه** as a vowel. Common Persian words: *و، در، به، از، که، این، است، را*.
  - Urdu **ے ہ ٹ ڈ ڑ ں** and aspirate **ھ** digraphs. Common Urdu words: *کے، کی، ہے، میں، اور، سے*.
  - Pashto **ټ ډ ړ ږ ښ ځ څ ۍ ې**. Common Pashto words: *د، او، په، چې، دی*.
  - Sorani Kurdish also writes vowels and uses **ە ۆ**, but it has **ێ ڵ ڕ**, Persian **ی/ک**, and initial **ئ**. Common Sorani words: *و، لە، بە، کە، ئەو*.
- **Kazakh word frequency.** These words are frequent in the converted sample and vocabulary: *بۇل، ٴبىز، وسى، مەن، ٴۇشىن، جانە، دەپ، ەمەس، بار، ول، كەرەك، بولادى، بولىپ، بولدى، ٴبىزدىڭ، سونداي-اق، بويىنشا، جوق، جاقسى*.
- **Suffixes at word end:** *-لار/-لەر، -دار/-دەر، -نىڭ/-دىڭ/-تىڭ، -عا/-گە/-قا/-كە، -دا/-دە/-تا، -دان/-دەن/-نان، -دى/-تى، -عان/-گەن، -ىپ، -مىز، -مىن، -لىق*.

## Checklist

1. Is the text in Arabic script, with written vowels (ا ە و ۇ ى) in nearly every syllable? → Turkic or Sorani candidate, not Persian, Arabic or Urdu.
2. Does a detached **ٴ** appear at the start of some words? → strong evidence for Kazakh.
3. Do many words start with **ئ**, or do **ې ۈ** or frequent **ۆ** appear? → Uyghur (or Sorani, if ێ ڵ ڕ ی ک are present).
4. Is /ʁ/ written with **ع** rather than **غ**, and **ج** used where Uyghur would have ي? → Kazakh.
5. Are the function words *جانە، بۇل، ٴۇشىن، ەمەس، وسى، دەپ* present? → Kazakh.
6. Are ة, ال‍ (Arabic), ی ک (Persian), ے ہ ٹ (Urdu) or ټ ډ ښ (Pashto) present? → not Kazakh.
7. Do not rely on Russian-looking loanwords. Real data may contain Chinese loans instead.

## Snippets

- **Kazakh (converter output, ud_01):** *قازاقستان وسى وڭىردەگى بەيبىتشىلىكتى قولدايدى. ٴبىزدىڭ ەلدە سىزگە ەرەكشە قۇرمەتپەن قارايدى.* ("Kazakhstan supports peace in this region. In our country you are treated with special respect.")
- **Kazakh (converter output, ud_03):** *بۇل ۇسىنىس ٴبىزدىڭ كورشىلەرىمىز تاراپىنان قولداۋ تاۋىپ وتىر.*
- **Contrast, "This book is very good":**
  - Kazakh (constructed by the converter rules): *بۇل كىتاپ وتە جاقسى.*
  - Uyghur: *بۇ كىتاب ناھايىتى ياخشى.*
  - Persian: *این کتاب خیلی خوب است.*
  - Urdu: *یہ کتاب بہت اچھی ہے۔*
  - Arabic: *هذا الكتاب جيد جدا.*

The Uyghur, Persian, Urdu and Arabic lines are illustrative, written from general knowledge, and not drawn from repository data.
