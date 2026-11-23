# Slovak (slk_Latn) - Orthographic and LID Characteristics

## Alphabet

Officially 46 letters: *a á ä b c č d ď dz dž e é f g h ch i í j k l ĺ ľ m n ň o ó ô p q r ŕ s š t ť u ú v w x y ý z ž*. The letters *q, w, x* (and largely *f, g*) occur mainly in loanwords and names. Slovak does **not** use *ě, ř, ů* (Czech), *ł, ą, ę, ś, ź, ż, ć, ń* (Polish), or *ö, ü, ő, ű* (Hungarian).

## Diagnostic characters

| Char | Codepoint | Notes |
|---|---|---|
| **ľ** | U+013E | Soft l. Very frequent (*veľmi, ľudia, podľa, ďalej, vďaka*). Not used in Czech; among standard national languages essentially Slovak-only. Uppercase Ľ U+013D. |
| **ĺ** | U+013A | Long syllabic l (*dĺžka, dĺžne, vĺča*). Rare but practically unique to Slovak. Uppercase Ĺ U+0139. |
| **ŕ** | U+0155 | Long syllabic r (*vŕba, škŕtiť*). Rare; outside Slovak known from Lower Sorbian. Uppercase Ŕ U+0154. |
| **ô** | U+00F4 | Diphthong /uo/ (*môže, môj, pôsobiť, vôbec, skôr, kôň*). Also in French/Portuguese/Vietnamese, but not Czech. |
| **ä** | U+00E4 | *päť, mäso, pamäť, späť, väčší, opäť*. Also German/Finnish/Swedish, not Czech. |
| **ť** | U+0165 | In Slovak very common because every infinitive ends in *-ť* (*byť, mať, robiť*); in Czech rare (*ať*). |
| ď, ň | U+010F, U+0148 | Shared with Czech; more frequent in Slovak (*ďalej, deň, kôň*). |
| č š ž | U+010D, U+0161, U+017E | Shared with Czech, Slovenian, Croatian, etc. |
| á é í ó ú ý | U+00E1 ... U+00FD | Long vowels, shared with Czech. Non-initial **ú** (*sú, budú, majú, súčasť, ktorú*) is far more typical of Slovak; in standard Czech *ú* appears mainly word-initially (*úplně*). |

Letter frequencies measured on the repository's Slovak UD sample (`examples/ud_*.txt`, about 15,000 letters; a small sample, so treat as indicative only): á 1.9%, š 1.1%, č 1.0%, í 1.0%, ý 0.9%, é 0.8%, **ú 0.8%**, ž 0.8%, **ť 0.5%**, **ľ 0.3%**, **ô 0.2%**, ň 0.14%, ä 0.08%. On the Czech UD sample measured the same way, ú was only 0.04% and ť 0.06%, while ě (2.4%), ř (1.1%) and ů (0.4%) were frequent; in the Slovak sample ě and ř appeared only in isolated foreign names.

## Top ~50 function words (from vocabulary.json, in rank order)

*a, v, sa, na, je, to, z, že, s, ako, aj, o, si, do, som, ale, po, za, tak, od, čo, už, bol, by, pre, sú, ak, k, alebo, nie, sme, ich, len, vo, aby, keď, ktorý, ktoré, pri, má, jeho, bola, bude, ktorá, až, veľmi, bolo, byť, jej, so, ešte, zo, podľa, však, ani, ste, tu, viac, kde, boli, pred, medzi, môže, tiež, potom, iba, pretože*

Words in this list that are **absent from the top Czech vocabulary** (see `../chalis/discriminators/ces-slk.tsv`): *sa, ako, aj, som, čo, bol, pre, sú, ak, alebo, nie, ich, len, vo, keď, ktorý, ktoré, bola, ktorá, veľmi, bolo, ešte, zo, podľa, viac, boli, medzi, tiež*. Shared with Czech and therefore not diagnostic: *a, v, na, je, to, že, s, z, si, do, ale, o, i, tak, za, k, po, by, už, od, aby, ani, tam, kde*.

## Frequent character n-grams

From the same UD sample (word-internal, lowercase):

- Bigrams: *ov, st, na, po, ro, ko, en, pr, ne, ho, ch, sk, an, va, to, ie, al, om, ra, do, ia*
- Trigrams with word boundary: *␣po, ␣pr, ␣na, na␣, om␣, ch␣, ho␣, ␣sa, sa␣, ej␣, ie␣, ia␣, ova, pre, ost, nsk, ␣št*

Slovak-leaning n-grams compared with Czech: **ie, ia, iu** (*viac, miesto, riešenie*), **-ej** (fem. adjective/pronoun endings), **-om** (instr./loc.), **ô**, **ľ**, **dz** (*medzi*), word-final **-ť**, and *␣sa␣*. Czech-leaning n-grams: *ě, ř, ů*, *-ou* as a verb ending (*jsou, budou, mohou*; in Slovak *-ou* is mostly the fem. instrumental, *so ženou, slovenskou*), *-ové*, *␣jsem, ␣jsou, ␣se␣*. Note that *-ého* and *-ých* are frequent in **both** languages.

## Characteristic endings and affixes

- Word-final in the sample (top): *-ého, -ých, -val, -nie, -kom, -kej, -nej, -och, -vať, -sti, -ska, -sko*.
- Nouns: *-nie/-tie* (neuter verbal nouns: *riešenie, pôsobenie*), *-osť* (*spoločnosť, možnosť*), *-stvo* (*ministerstvo*), *-ia* in feminine loanwords (*história, kategória*; Czech *historie, kategorie*), masc. gen. pl. **-ov** (*rokov, Slovákov*), instr. sg. **-om**.
- Adjectives: *-ský/-ská/-ské*, fem. oblique **-skej/-ej**, plural *-ých/-ými*.
- Verbs: infinitive **-ť** (*-ovať, -iť, -ať*), past *-l/-la/-lo/-li*, 1sg present **-m**, 3pl **-ú/-ia**.
- Prefixes: *pre-* (Czech has both *pře-* and *pro-*, Slovak *pre-*: *prečo, prenos*), *roz-, vy-, za-, na-, po-, ne-, naj-* (superlative: *najlepší*).

## Orthographic conventions

- Softness of *d, t, n, l* before *e, i, í, ie* is normally unwritten (*deti, ten, niečo, lebo*); the caron/apostrophe-like mark appears elsewhere (*ďalej, ťažký, deň, ľud*). In print, *ď ť ľ* look like a letter followed by an apostrophe; in plain-text noise they are sometimes typed as *d' t' l'* (e.g. *l'udia*).
- *i/y* after hard and soft consonants follows Czech-like etymological rules (*byť* vs. *biť*).
- Prepositions *v, s, z, k* are separate one-letter words; vocalized as *vo, so, zo, ku*.
- Negated *byť* is written apart: *nie je, nie sú*; other verbs take *ne-* attached.
- Numbers: ordinal dot (*9. augusta*), decimal comma, space as thousands separator. Quotation marks „ ... “ in careful typography.
- Capitalization like Czech: only the first word of multiword proper names of institutions (*Slovenská národná rada*), month and day names lowercase (*apríl, pondelok*). Slovak month names are Latin-based (*január, február, marec, apríl, máj, jún, júl, august, september, október, november, december*), unlike Czech (*leden, únor, ...*).
