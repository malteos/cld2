# Serbian vs. Confusable Languages

Two confusion sets:

1. **Cyrillic cousins** -- Macedonian, Bulgarian, Russian, Ukrainian: separable mainly by alphabet and function words.
2. **Serbo-Croatian sister standards** -- Croatian, Bosnian, Montenegrin: nearly identical grammar; separable only by lexical choices, yat reflex and some orthographic/syntactic habits. In Latin script this is the main difficulty.

## Machine-Checkable Cues

| Cue | Indicates |
|---|---|
| **ђ / ћ** in Cyrillic text | Serbian (or rare Bosnian/Montenegrin Cyrillic) |
| **ѓ, ќ, ѕ** | Macedonian |
| **щ, ъ, ю, я, й, ь** | Bulgarian or Russian/Ukrainian -- not Serbian |
| **ы, э, ё** | Russian; **є, і, ї, ґ** Ukrainian |
| future clitic **ће/ћу** (*će/ću*) | Serbian/HR/BS/ME (Bulgarian **ще**, Macedonian **ќе**) |
| copula **је**, **су**, negation **није** | Serbo-Croatian (Mk/Bg **е**, **се/са**, **не е**) |
| ekavian **време, где, пре, после, вероватно, лепо, дете** | Serbian (not HR/BS/ME standard) |
| **да ли** question | Serbian-leaning (Croatian prefers *je li*) |
| **хиљада** (*hiljada*) | Serbian/Bosnian/Montenegrin; Croatian **tisuća** |
| fused future **радићу, биће** | Serbian; Croatian *radit ću, bit će* |
| **ś, ź** (*śutra, iźesti*) | Montenegrin (optional letters, rare) |

## Serbian vs. Macedonian

Shared: ј, љ, њ, џ and a set of words (*да, не, се, ти, ми, за, си, ли, ја, само, од, како, добро, ако, има, нема, треба*). Different:

| | Serbian | Macedonian |
|---|---|---|
| is / are | **је / су** | **е / се** |
| is not | **није** | **не е** |
| in / with | **у / са** | **во / со** |
| what | **шта** (што) | **што** |
| will | **ће** | **ќе** |
| more / still | **више / још** | **повеќе / уште** |
| all (pl.) | **сви, све** | **сите** |
| people | **људи** | **луѓе** |

Serbian has cases (*-ом, -има*) and infinitives (*-ти, -ћи*); Macedonian has suffixed articles (*-от, -та*) and neither cases nor infinitives. False friend: *ја* = "I" (sr) vs. "her" (mk clitic).

## Serbian vs. Bulgarian

Bulgarian letters **ъ, щ, ю, я, й, ь** are absent from Serbian; Serbian **ђ, ћ, ј, љ, њ, џ** are absent from Bulgarian. Bulgarian *ще, това, като, са, съм, няма, който, че* vs. Serbian *ће, то/ово, као, су, сам, нема, који, да*. Bulgarian has articles (*-ът, -та*) and no cases.

## Serbian vs. Russian

Russian has **ы, э, ё, й, щ, ъ, ь, ю, я** and lacks **ј**. Russian *что, это, он был, для, его, только, если, когда* vs. Serbian *шта/што, ово/то, он је био, за, његов/га, само, ако, кад(а)*. Russian infinitive **-ть** vs. Serbian **-ти**.

## Serbian vs. Ukrainian

Ukrainian **і, ї, є, ґ, ь, щ, ю, я** vs. Serbian **ј, ђ, ћ, љ, њ, џ**. Ukrainian *що, це, як, від, він, його, але, вже, є* vs. Serbian *шта, то/ово, како, од, он, његов, али, већ, је*. Ukrainian **є** vs. Serbian **је** is a quick check.

## Serbian vs. Croatian

Croatian (`../hrv_Latn/differences.md`) is written only in Latin and is **ijekavian**. Serbian from Serbia is ekavian; Serbian ijekavian (Bosnia, Montenegro) overlaps Croatian phonologically, so lexis and syntax must decide.

| | Serbian | Croatian |
|---|---|---|
| yat | **vreme, reka, lepo, dete, pre** (ekav.) | **vrijeme, rijeka, lijepo, dijete, prije** |
| probably | **verovatno** | **vjerojatno** |
| thousand | **hiljada** | **tisuća** |
| who / what | **ko / šta** | **tko / što** |
| train / bread | **voz / hleb** | **vlak / kruh** |
| week | **nedelja** (also "Sunday") | **tjedan** |
| municipality | **opština** | **općina** |
| security | **bezbednost** | **sigurnost** |
| accurate | **tačno** | **točno** |
| months | **januar, februar, mart...** | **siječanj, veljača, ožujak...** |
| -ovati/-irati | **organizovati, komentarisati** | **organizirati, komentirati** |
| "I want to go" | **hoću da idem** (also *hoću ići*) | **hoću ići** |
| question | **da li je?** | **je li?** |
| future | **radiću** | **radit ću** |

Croatian also has distinctive vocabulary such as *glazba, kazalište, zrakoplov, sveučilište, povijest, zemljopis* (Serbian *muzika, pozorište, avion, univerzitet, istorija, geografija*).

## Serbian vs. Bosnian

Bosnian (`../bos_Latn/differences.md`) is ijekavian and Latin-dominant, shares many "eastern" words with Serbian (*hiljada, hemija, univerzitet, historija* vs. Serbian *istorija*), and keeps etymological **h** (*lahko, kahva, mehko, historija*) and many Turkish/Arabic loans (*sevdah, merhaba*). Serbian (ekavian) vs. Bosnian is easy via yat; Serbian **ijekavian** vs. Bosnian is very hard and may require such cues as *historija* (bs) vs. *istorija* (sr), *kahva* (bs) vs. *kafa* (sr), *sedmica* (bs, also used in sr).

## Serbian vs. Montenegrin

Montenegrin (ISO 639-3 *cnr*) is ijekavian and uses both scripts; optional letters **ś, ź** (Cyr. **с́, з́**) and jotated forms like *đe* ("where", Serbian *gde/gdje*), *śutra* ("tomorrow"), *đevojka* are characteristic but not obligatory. Without them, Montenegrin and ijekavian Serbian are effectively indistinguishable.

## Practical Rule of Thumb

- Ekavian + Serbian lexis -> **srp** with high confidence.
- Ijekavian + *tko/što/tisuća/tjedan/-irati/je li* -> Croatian.
- Ijekavian + *h*-forms / Oriental loans -> Bosnian; with *ś/ź/đe* -> Montenegrin.
- Cyrillic with **ђ/ћ** and *је/су* -> Serbian (Bosnian/Montenegrin Cyrillic are uncommon in data; label with care).
