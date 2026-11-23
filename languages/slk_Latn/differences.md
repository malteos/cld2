# Slovak (slk_Latn) - Differential Diagnostics

## Slovak vs. Czech (critical pair)

Czech and Slovak share most grammar and a large part of the core vocabulary (*a, v, na, je, to, že, ale, tak, už, aby, kde* are common to both). Decide on **specific letters and specific word forms**, never on overall "Slavic look". Word lists below are grounded in `../chalis/discriminators/ces-slk.tsv` (with diacritics) and `../chalis/discriminators/ces-slk_nodiac.tsv` (diacritics stripped).

### 1. Letters (decisive when present)

| Points to Czech | Points to Slovak |
|---|---|
| **ě** U+011B (*mě, něco, není, ještě, město*) | **ä** U+00E4 (*päť, opäť, väčší*) |
| **ř** U+0159 (*při, před, řekl, tři, příklad*) | **ô** U+00F4 (*môže, vôbec, skôr, pôsobiť*) |
| **ů** U+016F (*může, domů, důvod, roků*) | **ľ** U+013E (*veľmi, podľa, ľudia*) |
| | **ĺ** U+013A, **ŕ** U+0155 (*dĺžka, vŕba*) |
| | **dz/dž** clusters in native words (*medzi, cudzí*) vs. Czech *mezi, cizí* |
| | frequent word-final **-ť** (infinitives) and non-initial **ú** |

One Czech letter rules out Slovak only if it recurs; a single *ř* or *ě* may be a Czech name inside Slovak text (the Slovak UD sample contains a few). Weigh repeated occurrences.

### 2. Function words (strongest cue overall)

| Czech | Slovak | Meaning |
|---|---|---|
| *jsem, jsi, jsme, jste, jsou* | *som, si, sme, ste, sú* | am/are |
| *není, nejsou* | *nie je, nie sú* | is not / are not |
| *se* (reflexive) | *sa* | oneself |
| *jako* | *ako* | as/like |
| *když* | *keď* | when |
| *protože* | *pretože, lebo* | because |
| *který, která, které* | *ktorý, ktorá, ktoré* | which |
| *byl, byla, bylo, byli* | *bol, bola, bolo, boli* | was/were |
| *pro* | *pre* | for |
| *ještě* | *ešte* | still |
| *také, taky* | *tiež* | also |
| *pouze, jen* | *iba, len* | only |
| *nebo* | *alebo* | or |
| *jejich* | *ich* | their |
| *mezi* | *medzi* | between |
| *více, víc* | *viac* | more |
| *pokud* | *ak, pokiaľ* | if |
| *kdo, co, proč* | *kto, čo, prečo* | who, what, why |
| *teď* | *teraz* | now |
| *ve, ze, ke* (vocalized prep.) | *vo, zo, ku* | in, from, to |
| *bych, bys, bychom* | *by som, by si, by sme* | would |
| *ne* | *nie* | no/not |
| *velmi* | *veľmi* | very |
| *podle* | *podľa* | according to |

### 3. Morphology

- Present 1sg: Czech *-u/-i* in many verbs (*chci, můžu, píšu, jdu*) vs. Slovak always *-m* (*chcem, môžem, píšem, idem*).
- 3pl: Czech *-ou/-í/-ají* (*budou, mohou, mají*) vs. Slovak *-ú/-ia/-ajú* (*budú, môžu, majú, robia*).
- Infinitive: Czech *-t* (*být, mít, dělat*) vs. Slovak *-ť* (*byť, mať, robiť*).
- Masc. gen. pl.: Czech *-ů* vs. Slovak *-ov* (*roků/rokov, studentů/študentov*).
- Masc./neut. instr. sg.: Czech *-em* vs. Slovak *-om* (*s přítelem / s priateľom*).
- Fem. adjective gen./dat./loc. sg.: Czech *-é* vs. Slovak *-ej* (*české republiky / slovenskej republiky*, *v této / v tejto*).
- Verbal nouns: Czech *-ní/-tí* vs. Slovak *-nie/-tie* (*řešení/riešenie*).
- Vowel correspondences: Czech *í* ↔ Slovak *ie* (*místo/miesto, bílý/biely*), Czech *ů* ↔ Slovak *ô* (*kůň/kôň*), Czech *ou* ↔ Slovak *ú* (*jsou/sú, mouka/múka*).
- Month names: Czech Slavic (*leden, únor, březen, ...*) vs. Slovak Latin-based (*január, február, marec, ...*).

### 4. Shared or ambiguous items (do not use)

*a, v, na, je, to, že, ale, tak, už, aby, ani, kde, tam, toho, ten, si, mi, ho, bude, má, jeho, až*. Also several forms that become identical when diacritics are stripped: *co* (Cz. *co* / Sk. *čo*), *pri* (Cz. *při* / Sk. *pri*), *pred* (Cz. *před* / Sk. *pred*), *byt* (Cz. *být* / Sk. *byť*), *velmi*, *ze* (Cz. *že/ze* / Sk. *že*), *nic* (Cz. *nic* / Sk. *nič*). See `../chalis/discriminators/ces-slk_nodiac.tsv`.

## Slovak vs. Polish

- Polish letters **ł ą ę ś ź ż ć ń ó** (ó exists in Slovak too, but is rare there) and digraphs **sz, cz, rz, dz, ch** written as clusters; Slovak uses carons (*š, č, ž*).
- Polish function words: *się, jest, nie, że, jak, który, oraz, dla, przez, czy, ale, w, z*. Slovak *sa, je, ako, ktorý, pre, cez*. Note *nie* and *że/ze* are shared, so do not rely on them.
- Polish long vowels are not written; Slovak has many *á, í, ú, ý*.

## Slovak vs. Slovenian / Croatian / Serbian Latin

- South Slavic Latin orthographies have *č š ž* but **no length marks** (*á í ý ú*) and no *ä ô ľ ť ď ň*; Croatian/Bosnian/Serbian Latin add *ć, đ*.
- Slovenian function words: *in, je, da, se, za, ki, so, pa, tudi, kot*; Croatian: *i, je, da, se, su, za, koji, što, kao, ali, od*. Slovak *sa* vs. their *se*; Slovak *sú* vs. Croatian *su* (identical when stripped!) and Slovenian *so*; Croatian *kao* vs. Slovak *ako*.

## Slovak vs. Hungarian

- Hungarian has **ö ü ő ű** and digraphs *sz, cs, gy, ny, ly, zs*; no carons. Slovak *á é í ó ú* overlap, so check consonants.
- Hungarian function words: *a, az, és, hogy, nem, is, egy, van, meg*. Only *a* overlaps.

## Quick rule of thumb

1. Any recurring *ä, ô, ľ, ĺ, ŕ* → Slovak; recurring *ě, ř, ů* → Czech.
2. Otherwise count marker words: *som/sú/sa/ako/keď/bol/pre/alebo/nie je/ktor-* (Slovak) vs. *jsem/jsou/se/jako/když/byl/pro/nebo/není/kter-* (Czech).
3. Otherwise endings: *-ť, -om, -ej, -ov, -nie, -ú* (Slovak) vs. *-t, -em, -é, -ů, -ní, -ou* (Czech).
