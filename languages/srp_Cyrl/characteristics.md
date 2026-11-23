# Serbian Identification Characteristics (srp_Cyrl)

## Alphabet and Diagnostic Letters

Serbian Cyrillic (30 letters) and its Latin equivalent:

| Cyr | а б в г д **ђ** е ж з и **ј** к л **љ** м н **њ** о п р с т **ћ** у ф х ц ч **џ** ш |
|---|---|
| Lat | a b v g d **đ** e ž z i **j** k l **lj** m n **nj** o p r s t **ć** u f h c č **dž** š |

**Unique to Serbian among Cyrillic standards:** **ђ** (*међутим, рођен, Ђорђе*) and **ћ** (*ће, ћу, већ, кући, хоћу, помоћ, укључујући*). Montenegrin and Bosnian Cyrillic also have them, but they are much rarer in data.

**Shared only with Macedonian:** **ј, љ, њ, џ**. The letter **ј** is very frequent (*је, ја, још, који, моја*; about 3% of letters in `examples/ud_*.txt`).

**Absent from Serbian:** **й, щ, ъ, ь, ю, я, ы, э, ё** (Russian/Bulgarian/Ukrainian), **є, і, ї, ґ** (Ukrainian), **ѓ, ќ, ѕ** (Macedonian). Serbian writes /ja/, /ju/ as *ја, ју*, and palatal /ʎ, ɲ/ as *љ, њ* (never *ль, нь*).

In **Latin-script** Serbian the diacritic letters **č ć š ž đ** (and digraphs *lj nj dž*) are shared with Croatian, Bosnian and Montenegrin; **ć** and **đ** exclude Slovene, Czech and Slovak (Polish also has *ć*, but not *đ*, and is recognisable by *ł, ą, ę, rz, sz, cz*).

## Letter Frequency (rough)

In `examples/ud_*.txt` (about 2,600 words of news text), the most frequent letters were а, и, о, е, н, с, р, у, т, к; **у** (about 5%) is notably more frequent than in Macedonian (preposition *у* "in"; dative/locative *-у*). **ћ** was about 0.6%, **ђ** about 0.3%. Indicative only.

## Top 50 Frequent Words (from `vocabulary.json`, ranks 1-50; Latin in parentheses)

да (da), је (je), не (ne), се (se), и (i), у (u), то (to), сам (sam), на (na), ти (ti), ми (mi), за (za), си (si), ли (li), шта (šta), што (što), ја (ja), али (ali), са (sa), су (su), није (nije), ово (ovo), само (samo), ме (me), те (te), од (od), а (a), га (ga), би (bi), како (kako), о (o), добро (dobro), ако (ako), све (sve), смо (smo), као (kao), ће (će), тако (tako), знам (znam), нисам (nisam), могу (mogu), сте (ste), овде (ovde), па (pa), био (bio), зашто (zašto), с (s), он (on), још (još), нешто (nešto)

Note: this list comes from **OpenSubtitles** (conversational, film dialogue), so first/second person forms (*сам, ти, знам, нисам*) rank higher than in news or web text. It also contains Croatian/Bosnian-flavoured items from regional subtitles (e.g. ijekavian *овдје* rank 174, *гдје* 244; *вјеројатно* 1245; *точно* 1073), so do not treat every word in the list as specifically Serbian.

Markers vs. cousins (`../chalis/discriminators.md`): vs. Macedonian -- *шта, није, ово, га, смо, ће, тако, нисам, могу, био, још, бити, који, кад, ћу, хвала, из, мислим, знаш, можда, их, више, онда, сада*.

## Character N-grams and Endings

Frequent trigrams in the sample include *је#, #по, #пр, да#, #у#, #на, #ко, ост, пре, ом#, их#, #су, ије, ти#, ија*. Distinctive patterns:

- **#је#**, **#су#**, **#није#**: copula forms (Macedonian/Bulgarian *е, се/са, не е*).
- **ћ** in **ће/ћу/ћемо/ћеш**, **-ћи** infinitives (*рећи, ићи, моћи*) and fused futures (*биће, радићу*).
- **-ти#** infinitives (*бити, радити, рећи*) -- impossible in Macedonian/Bulgarian.
- Case endings **-ом#, -има#, -ама#, -ога#/-ог#, -ему#, -их#, -ој#**.
- l-participles **-ао#, -ио#, -ла#, -ли#** (*рекао, био, била, били*).
- **-ије** sequences: in ekavian text mostly from the noun suffix *-ија* (gen. *Србије*) and from *није*; in ijekavian text also from yat (*вријеме, прије*).
- Ekavian yat words: *време, где, пре, после, лепо, дете, вероватно, увек* -- support Serbian over Croatian/Bosnian.
- **-овати / -исати** international verbs (*организовати, коментарисати*).
- Word-initial **#кад, #ко#, #шта#** (Croatian *kad, tko, što*).

## No Definite Article

Unlike Macedonian (*-от*) and Bulgarian (*-ът*), Serbian nouns have no article suffix. Endings like *-та, -то* in Serbian are case/gender endings or part of the stem (*света, место*), not articles; a high density of *-от/-ът* word endings argues against Serbian.

## Highly Diagnostic Features (summary)

1. **ђ, ћ** (Cyrillic) -- unique; in Latin, **ć/đ** narrow to Serbo-Croatian standards.
2. Function words **је, су, није, шта, ће, ћу, који, из, још, више, у, са, код**.
3. Seven-case morphology (*-ом, -има, -ама, -ог*), infinitives in *-ти/-ћи*.
4. Ekavian reflexes and Serbian lexis (*хиљада, воз, хлеб, ко, да ли*) vs. Croatian/Bosnian (see `differences.md`).

## Caveats

- `examples/ud_*.txt` are SETimes news originally in Latin and transliterated to Cyrillic (see `examples/SOURCES.md`).
- Percentages above are from a small sample and are not corpus statistics.
