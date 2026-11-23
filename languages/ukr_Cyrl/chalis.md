# Ukrainian in CHALIS: Romanized Ukrainian Identification Guide

CHALIS (Tichý & Libovický 2026) has a `cyrillic_to_english` section in which Russian (rus), Bulgarian (bul), Macedonian (mkd) and Serbian (srp) are typed in Latin letters with English-style digraphs. It also contains **Ukrainian** samples that are not among the labelled languages of that section. How these are scored is not documented in this repo: if **ukr** is an allowed label, use it; the main practical value of this file is to keep romanized Ukrainian from being mislabelled as **rus** (and to recognise it as a distractor). There is no Czech-style Ukrainian section; CHALIS `cyrillic_to_czech` is Russian only (see `../rus_Cyrl/chalis.md`).

The repo's simulation is in `variants/romanized_en/` (generated with `../scripts/translit.py`, Ukrainian table: г→h, и→y, і→i, ї→yi, є→ye, й→y, х→kh, щ→shch, ь dropped, apostrophe kept).

## 1. Recognising English-style Romanized Ukrainian

### Letter-level cues

- **h from г** — very frequent: *yoho, toho, tsoho, druhyy, hroshi, hostro, Hryhoriy*. Russian English-style has **no bare h** (only kh/zh/ch/sh/shch): Russian *ego, togo, drugoy, mnogo*.
- **y everywhere for и** — *my, vy, ty, robyty, knyhy, dity*; and after velars: **-ky, -hy, -khy, -kyy, -skyy** (*ukrayinskyy, velykyy, druhykh*). Russian writes *i* after k/g/kh: *russkiy, velikiy, knigi, drugikh*.
- **yi** from ї — *yiyi* (її), *yikh* (їх), *Ukrayina, ukrayinskyy*, *-oyi* (fem. gen./dat. *novoyi, tsiyeyi*). Russian English-style never yields *yi* in native words (Russian *-yy* has two y's: *novyy*).
- **ye** from є — *ye* ("is"), *svoye, rozvivayetsya, Yevropa*. In the repo's Russian table е → *e*, so *ye* is a Ukrainian signal (real Russian translit sometimes writes initial *ye*, e.g. *Yeltsin* — weak evidence only).
- **apostrophe** inside words: *p'yat, im'ya, zv'yazku, zdorov'ya* (`variants/romanized_en/vocabulary.tsv`). Russian translit drops ъ/ь, so *C'yV* is a Ukrainian hint.
- Real-world variation: the official Ukrainian national system (2010) writes *ia, iu, ie, i* inside words and *-yi* for -ий (*Zelenskyi, Ukraina*); expect *-skyi/-skyy* and *ia/ya* side by side.

### Word-level cues

From `chalis/discriminators.md` (rus-ukr_roman) and `variants/romanized_en/vocabulary.tsv`:

- **Ukrainian markers:** *shcho, tse, yak, ukrayiny, ale, vin, yoho, ye, shche, yaki, pid, vzhe, koly, yakshcho, abo, roku, bulo, vony, mene, shchob, meni, chy, yakyy, buv, bude*; also *ta, i, y* ("and"), *vid, tilky, duzhe, zaraz, dyakuyu, tomu, tsey/tsya/tsi, mizh, bo*.
- **Endings:** *-nnya/-ttya* (*pytannya, rishennya, zhyttya*), *-iv* gen. pl. (*rokiv*), *-oyi*, *-ty/-tysya* infinitive, *-v* masc. past (*skazav, buv*), *-mo* 1pl (*mayemo, robymo*), *-yetsya* (-ється), *-ist* (*kilkist*).
- **Russian counterparts:** *chto, eto, kak, ego, ot, no, on, oni, est, esli, kogda, ili, goda, byl, bylo, mne, menya, uzhe, eshche, tolko, ochen, sejchas/seychas, spasibo*; endings *-ogo* (Ukrainian *-oho*), *-aya* (Ukrainian *-a*), *-oy* (Ukrainian *-oyi*), *-ov* (Ukrainian *-iv*), *-l* past, *-niye/-nie* nouns.

### Against Bulgarian, Serbian, Macedonian, Belarusian

- **Bulgarian** also has bare *h* (from х) and *y* for й, but: *sht* for щ (*oshte, shte*), ъ → *a* (*sam, sas, kam*), postposed articles (*-ta, -to, -at, -ot, -te*), and words *e, sa, tova, kato, nyama, kakvo, tryabva*. Bulgarian *shte* (future) vs. Ukrainian *shche* ("still").
- **Serbian** (ASCII): *j* in many words (*je, ja, nije, koji*), *lj/nj/dj*, and *c/s/z* for č/š/ž (*sta, zasto, jos*); no zh/sh/ch digraphs. Ukrainian English-style never uses *j*.
- **Macedonian:** *j, kj, gj* (*kje, lugje*), words *vo, so, od, deka, shto, toa, sum*. Macedonian *shto* vs. Ukrainian *shcho* vs. Russian *chto*.
- **Belarusian** (not a CHALIS label here; may appear in the wild): also *h* for г and *i* for і, but *shto, heta, yon, yany, kali, velmi, tsy/ci*, *dz* (*dzen, dzetsi*), akanye spellings (*malako*), and ў as *w/u/ŭ*. Ukrainian: *shcho, tse, vin, vony, koly, duzhe, chy, den, dity*.

## 2. Czech-style Text

If a Czech-letter text (ž, č, š, ch, j) shows *ščo, ce, jak, vin, jogo/joho, je, buv, ščob, -nnja*, it is romanized **Ukrainian**, not Russian (*čto, eto, kak, on, ego, est, byl, čtoby*), and not Czech (*co, to, jak, on, jeho, je, byl, aby*). Note *jak* and *je* are also Czech; Ukrainian lacks ř/ě/ů/long vowels and has *-nnja, vid, ale, ščo*.

## 3. Decision Checklist

1. **j present in many words?** → Serbian/Macedonian (English-style) or Czech-style text; go to step 5 for the latter.
2. **sht/shte, sa, tova, kato, articles, ъ→a** → Bulgarian.
3. **Bare h + y-heavy spelling + yi/ye + shcho/tse/vin/yoho** → Ukrainian (**ukr**, if allowed).
4. **No bare h, -ogo, -kiy/-skiy, -aya, chto/eto/kak/byl** → Russian (**rus**).
5. Czech-style: *ščo/ce/vin/buv* → Ukrainian; *čto/eto/kak/byl/-ogo* → Russian; ř/ě/ů/á/í + *co/že/jsem* → Czech.
6. Do not count shared tokens (*v, na, ne, i, za, do, ya, tak, vse, dlya, tam*); *mozhe* is Ukrainian, Bulgarian and Macedonian.

## 4. Illustrative Snippets

1. *Ya ne znayu, shcho tse bulo, ale meni duzhe spodobalosya.* — **ukr**. *shcho, tse, bulo, ale, meni, duzhe*. Russian equivalent: *Ya ne znayu, chto eto bylo, no mne ochen ponravilos.* (**rus**).
2. *Yakyy velykyy ukrayinskyy narod! Vin skazav, shcho pryyde. Yiyi batko chytaye.* — **ukr**. *-kyy* after k, *yi*, past *skazav*, 3sg *chytaye*.
3. *Zrechennya kulturnoyi identychnosti – tse vtrata svobody y samovladnosti.* (`variants/romanized_en/ud_01.txt`) — **ukr**. *-nnya*, *-oyi*, *tse*, *y* = "and".
4. *Zhenata shte doyde utre, gradat e hubav.* — **bul**, not Ukrainian: *shte*, articles *-ta/-at*, *e* "is", *h* from х.
