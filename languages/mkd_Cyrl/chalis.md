# Macedonian in Latin Letters (CHALIS `cyrillic_to_english`)

Practical guide for recognising **Macedonian (gold label `mkd`)** typed in ASCII / English-style Latin. Script cues (ѓ, ќ, ѕ, ј) disappear, but Macedonian romanization keeps several tell-tale letter sequences, above all **kj / gj** and frequent **j**.

Grounding files: `variants/romanized_en/` (real UD text romanized deterministically; `vocabulary.tsv`), `../chalis/discriminators.md` (sections *bul_Cyrl vs mkd_Cyrl (roman)* and *srp_Cyrl vs mkd_Cyrl (roman)*), `../scripts/translit.py`. These model, but are not, the CHALIS data.

## How Macedonian Looks When Romanized

Repo scheme (`translit.py`, language `mk`): **ѓ -> gj, ќ -> kj, ј -> j, љ -> lj, њ -> nj, ѕ -> dz, џ -> dz, ж -> zh, ш -> sh, ч -> ch, ц -> c, х -> h**. This resembles common Macedonian practice (official romanization also uses *gj, kj*, *zh, sh, ch*, *c*, *dz*).

Visible consequences:

- **kj / gj**: *kje* (ќе, future), *povekje, vekje, kukja, bidejkji* and *lugje, megju, tugj, pagjashe, nagjam*. These sequences are essentially unique to Macedonian among the CHALIS Cyrillic languages.
- **j** very frequent: *jas, ja, toj, koj, koja, moj, mojot, svojot, dojde, najmnogu*. Bulgarian (in this scheme) uses *y* instead.
- **c** for ц (*Sonceto, crvena, crkva*), **sh / zh / ch** for ш / ж / ч (*shto, mozhe, chovek*). Serbian ASCII uses bare *s / z / c* instead.
- No **ya / yu / -at** (Bulgarian), no **kh / shch** (Russian).

**Repo artifact:** accented **ѝ, ѐ** are not mapped by `translit.py`, so files like `variants/romanized_en/ud_01.txt` keep Cyrillic *ѝ* / *Sѐ* inside Latin text. Real CHALIS texts probably write *i* / *se* (uncertain); if a stray *ѝ/ѐ* appears it is a near-certain Macedonian signal.

## Spelling Variation (likely in real data)

Informal Macedonian Latin varies a lot (not verified against CHALIS): ќ as **kj, k', k, ke** (*kje / ke / k'e*), ѓ as **gj, g', dj**, ш as **sh / s**, ж as **zh / z**, ч as **ch / c**. So the future particle may appear as *kje*, *ke* or *k'e*; *shto* as *sto* or *shto*; *mozhe* as *moze*. When *ke* / *sto* appear instead of *kje* / *shto*, the text can look Serbian-ASCII; use grammar (articles, *vo/so/deka*, no cases) to decide.

## Characteristic Romanized Words

Top forms in `variants/romanized_en/vocabulary.tsv`: *na, i, vo, da, se, od, za, e, so, ne, go, kje, shto, deka, gi, kako, ja, toa, a, koj, koi, si, po, mi, do, ti, mnogu, no, ili, samo, ima, koga, beshe, site, toj, ako, taka, mozhe, koja, ova, jas, godina, eden, nema, sum, bide*.

Markers (`../chalis/discriminators.md`):

- vs. Bulgarian: **od, kje, deka, kako, ja, toa, koj, mnogu, site, toj, koja, ova, jas, eden, nema, sum, bide, treba, povekje, ushte, tie, lugje, ovoj, ovaa**.
- vs. Serbian: **vo, kje, shto, deka, gi, toa, koi, mnogu, beshe, site, taka, mozhe, jas, eden, sum, bide, povekje, ushte, tie, edna, sega, kade, lugje, ovaa**.

Key glosses: *vo* "in", *so* "with", *od* "from", *deka* "that", *e* "is", *se* "are / reflexive", *sum* "I am", *ne e* "is not", *kje* future, *nema da* negative future.

## Endings

- **Article -ot** (masc.): *krajot, prozorecot, televizorot, filmot, stadionot, gradot*; adjectival **-iot**: *negoviot, rasipaniot, stariot, minatiot*. Bulgarian has **-at / -iyat**; Serbian has no articles.
- **-ta / -to / -te** (shared with Bulgarian): *knigata, sobata, vremeto, oblacite*.
- Proximal/distal **-ov / -on, -va / -na** (*denov, ovoj, onoj*), less frequent.
- Verbs: 1sg **-am** (*mislam, sakam, imam, znam*), 3pl **-aat / -at** (*sakaat, znaat*), aorist **-v, -vme, -vte, -a / -ja** (*kupiv, vlegov, bevme, otidovme, zabelezhija*), imperfect **-she** (*beshe, studeshe, trebashe*), *-l / -la / -le* l-forms (*napishal*). The past 1sg in **-v** and 1pl in **-vme** contrast with Bulgarian **-h / -hme** and with Serbian perfect *sam + -o/-la*.

## Telling Macedonian From ...

**Bulgarian**: see `../bul_Cyrl/chalis.md`. Macedonian *kje, vo, so, od, deka, toa, jas, sum, nema, koj, mnogu, -ot* vs. Bulgarian *shte, v/vav, s/sas, ot, che, tova, az, sam, nyama, koy, mnogo, -at*. Letters: Macedonian **j, gj, kj, c** vs. Bulgarian **y, ya, yu, ts, a-for-ъ**. Collision: Macedonian *shto, ushte* contain *sht*, like Bulgarian *shte, oshte*.

**Serbian (ASCII)**: Serbian *je, su, nije, u, sa, iz, ce, cu, sta, koji, jos, vise, biti* vs. Macedonian *e, se, ne e, vo, so, od, kje, shto, koj, ushte, povekje, bide*. Serbian has case endings (*-om, -ima, -ama, -og*) and infinitives in *-ti / -ci*; Macedonian has *-ot* articles and none of those. False friends: **ja** (sr "I", mk "her"), **koja, kako, treba, nema, od** are shared. Macedonian *verojatno* vs. Serbian *verovatno*.

**Russian / Ukrainian (romanized)**: Russian *chto, eto, ego, byl, ty, kh, shch, -ogo*; Ukrainian *shcho, tse, ye, yak, vin, yoho, i*. Both use **y** (й, ы / и) where Macedonian uses **j**, and neither has *kj / gj*. Ukrainian items occur unlabelled in this CHALIS section; do not force them into `mkd`.

**Genuine Latin-script languages**: Croatian/Bosnian (ijekavian *je, nije, sto/što, ce/će*, cases, *tko*, *tisuća*), Slovene (*in* "and", *je, so* "are", *bo, kot, tudi, ki*, dual *-va / -ta*), Czech (*je, se, na, ze, že, jsem, jsou, ktery, -ou*). Note Slovene **so** = "are" and Macedonian **so** = "with": check the context (Macedonian *so* precedes a noun phrase, Slovene *so* follows a plural subject). None of these use *kj / gj*, *deka* or the article *-ot*.

## Decision Checklist

1. **kje / povekje / vekje / lugje / megju** (kj, gj) -> strong `mkd`.
2. **vo, so, od, deka, jas, sum, toa, mnogu, site, ushte** -> `mkd`.
3. Nouns in **-ot**, adjectives in **-iot**, past **-v / -vme / -vte** -> `mkd`.
4. *shte, tova, che, sa, az, -at, y / ya* -> Bulgarian.
5. *je, su, nije, u, sa, ce / cu*, case endings, *-ti* infinitives -> Serbian (or Croatian/Bosnian if genuine Latin with ijekavian forms).
6. *chto, eto, kh, shch* -> Russian; *shcho, tse, ye* -> Ukrainian.

## Illustrative Snippets

1. *"Mislam deka vrne."* (`variants/romanized_en/ud_01.txt`) -> **mkd**. *deka*, 1sg *mislam*; very short but both words are Macedonian markers (Bulgarian *Mislya, che vali*; Serbian *Mislim da pada kisa*).
2. *"Sonceto chas kje se pojaveshe chas kje se skrieshe zad oblacite."* (`ud_02.txt`) -> **mkd**. *kje*, *c* for ц, *j*, imperfect *-she*.
3. *"Vchera se vrativ od Rim, kade shto vremeto beshe prekrasno."* (`ud_03.txt`) -> **mkd**. Aorist *vrativ* (-v), *od*, *kade shto*; *vremeto*, *beshe* alone would also fit Bulgarian.
4. Constructed: *"Utre ke odam vo Skopje so drugarite."* -> **mkd** despite ASCII *ke*: *vo, so*, article *-te*, 1sg *odam*. Serbian would be *"Sutra cu ici u Skoplje sa drugovima."*
