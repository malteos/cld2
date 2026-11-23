# Russian in CHALIS: Romanized Russian Identification Guide

CHALIS (Tichý & Libovický 2026) contains Russian in two non-Cyrillic disguises:

- **`cyrillic_to_english`** — Russian, Bulgarian, Macedonian and Serbian typed in Latin letters with English-style digraphs (plus some Ukrainian that is not part of the labelled set; how it is scored is not documented here — if `ukr` is an allowed label, use it for Ukrainian). Gold label for Russian: **rus**.
- **`cyrillic_to_czech`** — Russian written with Czech orthography (ž, č, š, ch, c, šč, j, ja, ju). Gold label: **rus**, even though the text "looks Czech".

The repo's simulations of both are in `variants/romanized_en/` and `variants/romanized_cs/` (generated with `../scripts/translit.py`). Real CHALIS samples may deviate from these exact tables (e.g. *h* instead of *kh*, *ye* for word-initial е, *'* for ь, *iy/yi/ij* for й), so rely on several cues at once.

## 1. English-style: Russian vs. Ukrainian, Bulgarian, Serbian, Macedonian

### Letter-level cues (from `translit.py` tables)

| Cue | Russian | Ukrainian | Bulgarian | Serbian | Macedonian |
|---|---|---|---|---|---|
| х | **kh** only | kh | h | h | h |
| г | **g** | **h** | g | g | g |
| щ | **shch** | shch | **sht** | – | – |
| ч, ш, ж | ch, sh, zh | ch, sh, zh | ch, sh, zh | **c, s, z** (diacritics stripped) | ch, sh, zh |
| letter **j** | never | never | never | **je, ja, lj, nj** | **j, kj, gj** |
| ы | y | – (и → y) | – | – | – |
| ъ | dropped | – | **a** (*sam, kam, gradat*) | – | – |

Consequences:
- A bare **h** (not in kh/zh/sh/ch) is evidence *against* Russian: Ukrainian *yoho, toho, mozhna* has *h* from г; Bulgarian/Serbian/Macedonian have *h* from х (*hubav, hvala*). Exception: foreign names.
- Any **j** points to Serbian or Macedonian (in English-style data Russian uses *y*: *moy, ya, yu*).
- After k/g/kh Russian writes **i** (*russkiy, velikiy, knigi, drugikh, khorosho*), Ukrainian writes **y** (*ukrayinskyy, velykyy, knyhy, druhykh*). So **-kiy/-skiy/-gi/-ki** = Russian; **-kyy/-skyy/-hy/-ky** = Ukrainian.

### Word-level cues

- **Russian:** *chto, eto, kak, ego, ot, dlya, tolko, byl, esli, kogda, mne, menya, uzhe, eshche, oni, budet, chtoby, ochen, mozhet, zdes, sebya* (`chalis/discriminators.md`, `_roman` sections).
- **Russian endings:** *-ogo/-ego* (*etogo, svoego, sovetskogo*), *-omu*, *-yy/-iy* (*novyy, kotoryy, russkiy*), *-aya* (*novaya*), *-oy/-ey* (*odnoy, etoy*), *-ykh/-ikh*, *-ov* gen. pl., *-l* past (*skazal*), *-t/-at/-it* infinitive (*delat, govorit* — ь is dropped), *-etsya* (Russian -ется; Ukrainian -ється gives *-yetsya*).
- **Ukrainian:** *shcho, tse, yak, ta, vid, ale, vin, yoho, ye, vzhe, koly, yakshcho, abo, bulo, buv, meni, chy, duzhe*; endings *-nnya*, *-oyi*, *-iv*, *-ty*, *-v* past (*skazav*), *yi* (*yiyi, Ukrayina*). See `../ukr_Cyrl/chalis.md`.
- **Bulgarian:** *e, na, da, shte, sa, tova, kato, nyama, kakvo, tryabva, sht*-clusters (*oshte, kashta*), ъ as *a* (*sam, sas, kam*); postposed articles *-ta, -to, -ot, -at, -te* (*zhenata, deteto, gradat, horata*).
- **Serbian (ASCII):** *je, da, se, na, u, su, nije, sta, sto, ce, jos, zasto, nesto, koji, ovo, smo* — no zh/sh/ch digraphs, many *j*.
- **Macedonian:** *e, na, vo, so, od, da, se, kje, shto, deka, toa, ova, jas, sum, mnogu, site*, *gj/kj* (*lugje, kje, povekje*).

### Shared, non-diagnostic tokens
*v, i, na, ne, s, po, a, za, to, u, do, da, bez, nas, vas, tam, mnogo, li* occur in several of these languages. *ya* is also Bulgarian ("her"); *kak* and *eto* (*ето* "here is") also occur in Bulgarian; *mozhe* is Ukrainian/Bulgarian/Macedonian (Russian *mozhet*).

## 2. Czech-style romanized Russian vs. Czech, Slovak, Polish

Czech-style Russian (`variants/romanized_cs/`) uses Czech letters, so script cues mislead. Distinguish by **what is absent** and by **Russian words/endings**:

- **Absent in Czech-style Russian:** ř, ě, ů, and long vowels á é í ó ú ý; ň, ť, ď (ь is simply dropped in this repo's model: *očen, den, žizn*; real data may write *očeň*). Genuine Czech text with diacritics has many of these (*že, je, při, ještě, být, které*).
- **Russian words in Czech dress:** *čto, eto, kak, ego, dlja, esli, kogda, očen, tolko, uže, ešče, menja, mne, budet, možet, kotoryj, segodnja, gde, chorošo, skazal, javljaetsja*. Czech equivalents: *co, to, jak, jeho, pro, jestli/pokud, když, velmi/moc, jen, už, ještě, mě, bude, může, který, dnes, kde, dobře, řekl, je*.
- **Russian morphology:** *-ogo, -omu, -yj/-ij/-oj* (*novyj, russkij, drugoj*), *-aja/-jaja*, *-ych/-ich* without accents, gen. pl. *-ov*, infinitive *-t* (*delat*), reflexive attached **-sja/-s** (*učitsja, javljaetsja*) where Czech uses the separate word *se/si*.
- **ja/ju/jo after consonants:** *dlja, menja, vremja, ljudi, sebja, svoju, ejo, vsjo*; Czech uses *já* (with accent) only as the pronoun and has no *-lja/-mja*.
- **šč** (Russian щ: *ešče, ščuka, obščij*) vs. Czech *šť* (*ještě, štěstí*).
- **Caution with overlaps:** *byl/bylo/byla/byli, on, ona, oni, my, ty, vy, že, tam, tak, pod, nad, bez* are identical in Czech; *ja, kto, mne, ich* are also Slovak. Never decide on these alone.
- **Akanye is not visible:** Russian spelling keeps unstressed *o* (*chorošo*), so the giveaways are lexical and morphological, not phonetic.
- **vs. Slovak:** Slovak has ä, ô, ľ, ĺ, ŕ and words *ako, čo, som, sú, nie, pre, alebo, keď* (`chalis/discriminators.md`, ces-slk). Russian *čto* ≠ Slovak *čo*; Russian *kak* ≠ Slovak *ako*.
- **vs. Polish:** Polish uses sz, cz, rz, szcz, ł, ą, ę, ś, ć, ż, ź and *w* (not *v*); č/š/ž never occur in Polish. *Że, się, jest, nie, co* are Polish.

## 3. Decision Checklist

1. **Script/diacritics:** č/š/ž + no ř/ě/ů/long vowels → candidate Czech-style Russian; check Russian words (*čto, eto, kak, ego, -ogo*). With ř/ě/ů/á/í → Czech (or Slovak if ä/ô/ľ).
2. **Plain ASCII Latin:** any *j* in many words → Serbian or Macedonian; *kj/gj, vo, so, deka, shto* → Macedonian; *je, nije, sta, ce, su* with c/s/z for č/š/ž → Serbian.
3. **sht, shte, sa, tova, kato, -ta/-to/-at articles, ъ→a** → Bulgarian.
4. **h from г, yi, ye, -kyy, -nnya, -oyi, shcho, tse, vin** → Ukrainian.
5. **chto, eto, kak, ego, byl, -ogo, -kiy/-yy, -aya, kh only, no j** → Russian (**rus**).
6. Weigh several cues; shared tokens (*na, ne, i, po, za*) carry no information.

## 4. Illustrative Snippets

1. *Ya ne znayu, chto eto bylo, no mne ochen ponravilos.* — **rus**. *chto, eto, mne, ochen*; past neuter *bylo*; no *h*, no *j*.
2. *Ya ne znayu, shcho tse bulo, ale meni duzhe spodobalosya.* — **ukr** (same meaning). *shcho, tse, bulo, ale, meni, duzhe*.
3. *Ne znam kakvo beshe tova, no mnogo mi haresa. Zhenata shte doyde utre.* — **bul**. *tova, kakvo, shte*, article *zhena-ta*, *h* for х.
4. *Ne znam sta je to bilo, ali mi se jako dopalo.* — **srp**. *sta* (č/š stripped), *je*, *j*, *ali*; Macedonian would be *Ne znam shto beshe toa*.
5. *Včera on skazal mne, čto očen ustal i chočet domoj.* — **rus** (Czech-style). *skazal, čto, očen, chočet, domoj*; no ř/ě/á. Czech would be *Včera mi řekl, že je velmi unavený a chce domů.* (**ces**).
