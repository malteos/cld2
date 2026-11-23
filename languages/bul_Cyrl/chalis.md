# Bulgarian in Latin Letters (CHALIS `cyrillic_to_english`)

Practical guide for recognising **Bulgarian (gold label `bul`)** when it is typed in ASCII / English-style Latin letters instead of Cyrillic. In this condition all the usual script cues (ъ, щ, ю, я vs. ѓ, ќ, ђ, ћ) disappear, so identification rests on **romanized function words, spelling conventions and endings**.

Grounding files: `variants/romanized_en/` (deterministic romanization of real UD text, plus `vocabulary.tsv`), `../chalis/discriminators.md` (sections *rus_Cyrl vs bul_Cyrl (roman)* and *bul_Cyrl vs mkd_Cyrl (roman)*), `../scripts/translit.py`. These model CHALIS but are **not** the CHALIS data itself; real CHALIS texts may use other spellings (see "Spelling variation").

## How Bulgarian Looks When Romanized

The repo's scheme (`translit.py`, language `bg`) matches the Bulgarian official "streamlined" system: **ъ -> a, щ -> sht, ж -> zh, ч -> ch, ш -> sh, ц -> ts, х -> h, й -> y, ю -> yu, я -> ya**, ь dropped.

Consequences visible in text:

- **sht** everywhere: *shte* (ще, future), *oshte* (още), *zashtoto* (защото), *kashta* (къща), *ploshtad*, *noshtna*. Russian/Ukrainian щ is romanized *shch*. Caution: Macedonian *shto* (што) and *ushte* (уште) also contain the letters *sht*, so look for the Bulgarian word forms (*shte, oshte, zashtoto*), not just the letter sequence.
- **a** for ъ, giving clusters that look odd for Slavic: *kam* (към), *sas* (със), *vav* (във), *balgarski*, *parvi*, *varna se* (върна се), *dazhd* (дъжд).
- **y / ya / yu**: *toy, koy, nay, moy, koyto, koyato, nyama, tryabva, tya, golyam, lyubov*. The letter **j does not appear** in native Bulgarian words under this scheme. Frequent **j** therefore points to Macedonian or Serbian.
- **h** (not *kh*) for х: *hora, hubavo, haresva, hlyab*. Russian/Ukrainian romanizations in this repo use *kh*.
- **ts** (not *c*) for ц: *detsata, tsel, gradets, tsarkva*. Macedonian and Serbian romanizations use *c*.

## Characteristic Romanized Words

Top Bulgarian forms in `variants/romanized_en/vocabulary.tsv` begin: *na, i, v, da, e, ot, za, se, s, ne, si, che, po, shte, sa, tova, kato, a, mi, no, do, go, mnogo, nay, ima*.

Strongest positive markers (absent from the other language's top list, per `../chalis/discriminators.md`):

- vs. Macedonian: **shte, tova, kato, nay, kam, nyama, sled, prez, az, koito, koyto, tryabva, vsichki, vav, koeto, edin, oshte, sas, kogato, tozi**.
- vs. Russian: **shte, sa, tova, kato, nay, ima, ako, kam, nyama, prez, az, koito, kakvo, tryabva, vsichki, koyto, vav, oshte, sas, kogato**.

Also very useful: **che** ("that"; Macedonian *deka*, Serbian *da*, Russian *chto*), **ot** ("from"; Macedonian/Serbian *od*), **e** ("is"; Serbian *je*, Russian usually nothing), **sa** ("are"), **sam** ("am", spelled like Serbian *sam*), **veche** ("already"), **sega** ("now", shared with Macedonian), **beshe**.

## Endings

- **Definite article**: masc. **-at / -yat** (from -ът/-ят: *gradat, narodat, kmetat, knyazat, nachalnikat, plodat*), short form **-a / -ya** (*grada, mazha si*), fem. **-ta** (*zhenata, proletta*), neut. **-to** (*seloto, darvoto, shoseto*), pl. **-te** (*horata* irregular, *sivite, debelite*). Adjectives: **-iyat / -iya** (*nashiyat, shirokiya, strashniya*). The ending **-at** on nouns (and **-iyat/-iya**) is distinctive against Macedonian **-ot / -iot**.
- **Verbs**: 1sg often **-a / -ya** (*pisha, mislya, zhiveya*), past **-h, -hme, -hte, -ha** (*imah, chetoh, izbrahte, nameriha, razbyagaha*) -- the past endings in **-h-** are a good Bulgarian signal (Macedonian *-v, -vme, -vte, -a*: *vidov, bevme*).
- Imperfect 3sg **-she** (*imashe, deleshe*) is shared with Macedonian.

## Telling Bulgarian From ...

**Macedonian (romanized)**: Bulgarian *shte / ot / v, vav / s, sas / che / tova / az / sam / nyama / koyto / mnogo* vs. Macedonian *kje, ke / od / vo / so / deka / toa, ova / jas / sum / nema / koj / mnogu*. Bulgarian has **y, ya, yu, a-for-ъ**; Macedonian has **j, gj, kj, c** and the article **-ot**. Shared words (*na, i, da, e, za, se, ne, si, po, ima, ako, samo, mozhe, godini, sega, beshe*) are not diagnostic.

**Serbian (ASCII)**: Serbian uses **j** (*je, koji, jos*), **c** for ц/ч/ћ, **s** for ш, and case endings (*-om, -ima*). Serbian copula **je / su** vs. Bulgarian **e / sa**; Serbian **ce** vs. Bulgarian **shte**. Beware look-alikes: **sam** (both "am"), **sa** (bg "are", sr "with"), **mnogo, posle, vreme, dobro** occur in both.

**Russian (romanized)**: Russian *chto, eto, ego, zhe, ty, tolko, byl, esli, kogda, mne, menya, uzhe, eshche, budet, kto* are absent in Bulgarian; Russian uses **kh** and **shch**, **-ogo/-ego** genitives, **-t'/-t** infinitives (*delat, byt*), **y** from ы (*byl, my, ty*). Bulgarian *kak*, *eto* ("here is"), *mnogo* also exist in Russian, so rely on *shte, tova, che, sa, -at*.

**Ukrainian (romanized)**: *shcho, tse, yak, vin, yoho, ye, shche, ale, vzhe, i* (and), **-ty** infinitives, **h** for г (*yoho, mohu*). Note Ukrainian *shche* vs. Bulgarian *oshte*. Ukrainian items occur unlabelled in this CHALIS section; do not force them into `bul`.

## Spelling Variation (uncertain for CHALIS)

Informal Bulgarian web Latin ("shlyokavitsa") also writes ъ as **u** or **y** (*sum/sym* for съм), щ as **sht** or **6t**, ч as **4**, ш as **6**, я as **q** or **ia**, ж as **j** or **zh**. If digits/`q` appear inside words (*6te, 4e, qko*) this is a strong Bulgarian signal; whether CHALIS contains such texts is not known.

## Decision Checklist

1. Words **shte / oshte / zashtoto / kashta** (sht) -> strong `bul`.
2. **tova, che, sa, az, nyama, koyto, kato, kam, sas, vav** -> `bul`.
3. Nouns in **-at / -yat**, adjectives in **-iyat / -iya**, past tense **-h / -ha / -hme** -> `bul`.
4. Frequent **j / gj / kj**, *vo, so, od, deka, -ot* -> Macedonian, not Bulgarian.
5. *je, su, nije, ce*, case endings -> Serbian.
6. *chto, eto, ego, byl, kh, shch* -> Russian; *shcho, tse, ye, yoho* -> Ukrainian.

## Illustrative Snippets

1. *"Shte vlyaza tiho, krotko shte prisedna."* (`variants/romanized_en/ud_01.txt`) -> **bul**. Double *shte*, *vlyaza* with *ya* and *a*-for-ъ.
2. *"Knyazat se varna ot lov i sega se kapeshe."* (`variants/romanized_en/ud_03.txt`) -> **bul**. Article *-at* (*knyazat*), *ot*, *varna* (върна). *sega*, *kapeshe* alone would fit Macedonian too.
3. *"Izbrahte me za voyvoda i dosega ne ste me popitali koy sam az."* (`ud_01.txt`) -> **bul**. Past *-hte*, *koy*, *az*; *sam* here = съм, not Serbian *sam*.
4. Constructed contrast: *"Toj kje dojde utre, no ne znam dali kje ostane."* -> **mkd**, not bul (*toj, kje, dojde* with *j*). Bulgarian would be *"Toy shte doyde utre, no ne znam dali shte ostane."*
