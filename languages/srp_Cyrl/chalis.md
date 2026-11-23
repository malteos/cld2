# Serbian in Latin Letters (CHALIS `cyrillic_to_english`)

Practical guide for recognising **Serbian (gold label `srp`)** typed in Latin letters. Serbian is special among the CHALIS Cyrillic languages: it already has a native Latin alphabet (Gaj's *latinica*), so a "romanized" Serbian text may be:

1. **Native Gaj Latin** with diacritics: *Šta ćeš da radiš? Već sam rekao da neću.*
2. **ASCII-ized Gaj Latin** (diacritics dropped): *Sta ces da radis? Vec sam rekao da necu.*
3. **English-style transliteration** (frequency uncertain): *Shta chesh da radish?*

Grounding files: `variants/romanized_en/` (type 2: ASCII, c for č/ć, s for š, z for ž, dj for đ; see its `README.md`), `vocabulary.json` (has a `latin` field with Gaj spelling), `../chalis/discriminators.md` (sections *srp_Cyrl vs mkd_Cyrl (roman)*, *rus_Cyrl vs srp_Cyrl (roman)*), `../scripts/translit.py`. These model, but are not, the CHALIS data.

## How Serbian Looks in ASCII Latin

Repo scheme (`translit.py`, language `sr`): **ч, ћ, ц -> c; ш -> s; ж -> z; ђ -> dj; џ -> dz; љ -> lj; њ -> nj; ј -> j; х -> h**. Consequences:

- **c** is frequent (*ce, cu, vec, kuci, Stefanovic*); no *ts* (Bulgarian/Russian) or *ch* (Macedonian/Russian).
- **s / z** stand for š / ž, so *sta, sto, jos, vise, zasto, mozda, zivot, drzava*.
- **lj, nj, dj, j** survive: *ljudi, njegov, medjutim, rodjenih, je, koji, jos*.
- No **y**, no **kj / gj**, no **kh / shch / zh** (in this scheme).

## Characteristic Function Words (ASCII forms)

Top ASCII forms (`variants/romanized_en/vocabulary.tsv`) begin: *da, je, ne, se, i, u, to, sam, na, ti, mi, za, si, li, sta, sto, ja, ali, sa, su, nije*.

Markers (`../chalis/discriminators.md`):

- vs. Macedonian: **sta, nije, ovo, ga, smo, ce, tako, nisam, mogu, bio, zasto, jos, nesto, biti, koji, kad, cu, hvala, iz, mislim, znas, mozda, ih, vise**.
- vs. Russian: **je, sa, nije, ovo, od, kako, ako, sve, smo, kao, ce, tako, koji**.

The single best quick test is the trio **je / su / nije** together with **u** ("in"), **da** (complementizer) and **ce / cu** (future).

## Endings

- Cases: **-om / -em** (*Pristinom, vremenom*), **-ima / -ama** (*zivotima, rizicima, Drzavama*), **-og / -oga, -ih, -oj** (*Svetskog, kosovskih, tog*), locative **-u** (*u Briselu, u Beogradu*).
- Infinitive **-ti / -ci** (*biti, raditi, doneti, reci, ici*).
- l-participles **-ao / -io / -la / -li** (*rekao, bio, insistirao, upozorio, postigli*).
- Fused future **-cu / -ce** (*bice, radicu*), Serbian-specific spelling (Croatian *bit će*).
- **-ovati / -isati** verbs: *komentarisuci, sugerisu, eliminisanje* (Croatian *komentirajući, sugeriraju, eliminiranje*).
- No article endings *-ot / -at*.

## Native Latin vs. ASCII Serbian

- With diacritics (**č ć š ž đ**), the text is Serbo-Croatian of some standard; **ć / đ** exclude Slovene, Czech and Slovak. Decide srp vs. hrv / bos / cnr lexically (below). The gold label for Serbian in either script is `srp`.
- Without diacritics, *ce* = će, *sto* = što or sto ("hundred"), *kuca* = kuća; read at the word level.
- English-style digraphs (*sh, ch, zh*) for Serbian are possible in real data (uncertain frequency); then *shta, che, chu* would appear. Without *kj/gj/-ot*, these still point to Serbian rather than Macedonian.

## Telling Serbian From ...

**Macedonian**: Macedonian *e, se* (are), *ne e, vo, so, kje / ke, shto, deka, koj, ushte, povekje, -ot*. Serbian *je, su, nije, u, sa, ce, sta, da, koji, jos, vise*, cases, infinitives. ASCII Macedonian *ke* vs. Serbian *ce* is a clean split.

**Bulgarian**: Bulgarian *shte, tova, che, sa* (are), *az, nyama, koyto*, *y / ya / yu*, article *-at*. Shared spellings *sam, sa, mnogo, posle, vreme, dobro* are not diagnostic (`../bul_Cyrl/chalis.md`).

**Russian**: Russian *chto, eto, ego, byl, ty, tolko, kogda, uzhe, eshche, kto*, letters *y* (ы), *kh, zh, shch, ya, yu*, genitive *-ogo / -ego*. Serbian *lj / nj / j* vs. Russian *ly / ny / y* (*ljudi* vs. *lyudi*).

**Ukrainian**: *shcho, tse, ye, yak, vin, yoho, i* (and), *z* (with/from), *h* for г, *-ty* infinitives. Ukrainian appears unlabelled in this CHALIS section; a Ukrainian-looking text should not be labelled `srp`.

**Croatian / Bosnian / Montenegrin (genuine Latin)**: same alphabet and grammar. Serbian cues: ekavian **vreme, pre, posle, gde, ovde, lepo, dete, verovatno, uvek**; **hiljada, ko, sta, voz, hleb, kafa, opstina, bezbednost, tacno, istorija**; months *januar, februar*; *da li*; *hocu da idem*; fused *bice*. Croatian cues: ijekavian + **tko, što** (interrogative), **tisuća, tjedan, vlak, kruh, sigurnost, točno, povijest**, *siječanj*, *-irati*, *je li*, *bit će*. Bosnian: ijekavian + *h*-forms (*historija, lahko, kahva*). Montenegrin: *ś, ź, đe*. Caveat: OpenSubtitles-based `vocabulary.json` also contains ijekavian forms (*ovdje, gdje, vjerojatno*), and real Serbian is ijekavian in Bosnia/Montenegro; ijekavian alone does not exclude `srp`. Inference (not verified): since this CHALIS section is built from Cyrillic-script source text, a Serbo-Croatian text found there is most likely `srp`.

**Slovene / Czech / Slovak**: Slovene *in* ("and"), *so* ("are"), *bo, kot, tudi, ki, zelo, lahko*, dual; Czech *jsem, jsou, neni, byl, ktery, ze* (že), *aby*, *ř, ě, ů*; Slovak *som, sú, nie je, ktorý, ä, ô, ľ*. Serbian *je* collides with all three (and ASCII Slovak *su* = sú), but *nije, sta, ce, da li, koji* do not.

## Decision Checklist

1. **je + su + nije + u** present, no *-ot / -at* articles -> Serbo-Croatian.
2. Cyrillic origin / ASCII with *ce / cu / sta / jos / vise / koji* -> `srp` (vs. mk/bg/ru/uk).
3. Ekavian forms (*vreme, pre, gde, ovde, verovatno*) or *hiljada, ko, voz, -ovati / -isati, bice* -> `srp` over hrv/bos.
4. *kje / ke, vo, so, deka, -ot* -> Macedonian; *shte, tova, che, sa, -at* -> Bulgarian.
5. *chto, eto, kh, shch, y* -> Russian; *shcho, tse, ye* -> Ukrainian.
6. Ijekavian + *tko / tisuća / -irati / je li* -> Croatian (if that label is available).

## Illustrative Snippets

1. *"Dok vlasti u Beogradu pokusavaju da predstave prve dogovore sa Pristinom kao uspeh koji ce doneti poboljsanje..."* (`variants/romanized_en/ud_01.txt`) -> **srp**. *u, da, sa, koji, ce*, instrumental *-om*, ekavian *uspeh, doneti*.
2. *"Teroristicki napadi slicni onima u Sjedinjenim Drzavama pre jedne decenije danas su malo verovatni, rekao je..."* (`ud_03.txt`) -> **srp**. Ekavian *pre, verovatni*; *su*, *rekao je*.
3. Constructed native Latin: *"Šta ćeš da radiš sutra? Mislim da ću ostati kod kuće."* -> **srp**. *šta*, *ćeš da radiš*. Croatian would say *"Što ćeš raditi sutra?"*.
4. Constructed contrast: *"Sto ces raditi sutra? Ne znam tko ce doci, valjda tjedan dana..."* -> **Croatian**, not srp (*tko, tjedan*, infinitive *raditi* after *ces*). If only `srp` is available among Serbo-Croatian labels, prefer `srp`.
