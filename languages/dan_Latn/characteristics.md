# Danish (dansk) - Language Identification Characteristics

## Distinctive Characters

Danish uses the Latin alphabet with three additional vowel letters that appear at the end of the alphabet after Z:

- **æ** (Æ) - a front open-mid vowel, similar to the vowel in English "bed" but more open. Used frequently in Danish (være, fælles, mænd, læse).
- **ø** (Ø) - a front rounded vowel with no English equivalent; similar to German ö. Very common in Danish (før, større, købe, søster).
- **å** (Å) - an open back rounded vowel, similar to the vowel in English "law." Replaced the older digraph "aa" in 1948 (på, så, når, år, også).

These three characters are shared with Norwegian (both Bokmål and Nynorsk), which makes them useful for distinguishing Danish/Norwegian from other Latin-script languages but not helpful for distinguishing Danish from Norwegian. Swedish shares å but uses ä and ö where Danish and Norwegian use æ and ø; this æ/ø vs. ä/ö contrast is a key distinguishing feature.

## Character Frequency Patterns

Danish text shows distinctive character frequency distributions. Based on analysis of Danish corpora, the most frequent characters in Danish text (excluding spaces and punctuation) are approximately:

1. **e** - by far the most frequent letter (~15.8%)
2. **r** - (~8.3%)
3. **n** - (~7.3%)
4. **t** - (~6.8%)
5. **a** - (~6.3%)
6. **i** - (~6.0%)
7. **d** - (~5.9%)
8. **s** - (~5.5-6.5%)
9. **l** - (~5.2%)
10. **o** - (~4.5%)

The special characters æ, ø, and å together account for roughly 2.5-3.5% of all letters, with å usually the most frequent of the three (because of very common words such as på, så, når, år, også, få), followed by ø and æ. The relatively high frequency of 'd' compared to many other European languages is notable, as is the high frequency of 'e' due to its use in many common suffixes and function words.

## Top 50 Function Words

The following are the most frequent function words in Danish, which serve as strong indicators for language identification:

1. er (is/are)
2. i (in/you plural)
3. at (to/that)
4. det (it/the neuter)
5. en (a/one common)
6. og (and)
7. har (has/have)
8. de (they/the plural)
9. for (for)
10. den (the/it common)
11. med (with)
12. på (on/at)
13. af (of/by)
14. til (to/for)
15. kan (can)
16. et (a/one neuter)
17. var (was)
18. som (who/which/as)
19. han (he)
20. der (there/who/which)
21. ikke (not)
22. fra (from)
23. vi (we)
24. jeg (I)
25. sig (oneself)
26. vil (will/want)
27. blev (became/was)
28. men (but)
29. hun (she)
30. skal (shall/must)
31. efter (after)
32. sin (his/her/its own)
33. eller (or)
34. ved (by/at/know)
35. over (over/above)
36. da (then/when/since)
37. her (here)
38. kun (only)
39. hvor (where)
40. alle (all)
41. ham (him)
42. meget (much/very)
43. dette (this neuter)
44. denne (this common)
45. om (about/if)
46. andre (other/others)
47. også (also)
48. mod (against/toward)
49. mellem (between)
50. under (under/during)

Other very frequent words with the special letters: så (so/then), når (when), være (be), år (year), få/får (get), før (before), både (both), måske (maybe).

## Common Bigrams and Trigrams

### Most Frequent Bigrams

The most common two-character sequences in Danish text:

er, en, de, et, an, re, in, ed, nd, te, or, el, st, ar, ge, le, al, se, ne, li, ng, ti, me, ra, ke, fo, on, il, om, ha, be, ve, ig, da, la

### Most Frequent Trigrams

The most common three-character sequences in Danish text:

er_, en_, der, _de, for, den, _en, ing, ede, _fo, _og, _er, _at, _ha, _me, ter, _ti, ere, ige, _si, gen, _vi, nde, det, _af, lle, elt, _i_, _ko, and, _st, med, ger, ren, lig, _på

(Underscores represent spaces.)

## Morphological Patterns for Language Identification

### Suffixed Definite Articles

One of the most distinctive features of Danish (shared with Norwegian and Swedish but not with other Germanic languages) is the suffixed definite article. These patterns are highly diagnostic:

- **-en** (common gender singular definite): "bogen" (the book), "manden" (the man)
- **-et** (neuter gender singular definite): "huset" (the house), "barnet" (the child)
- **-ne** / **-ene** (plural definite): "bøgerne" (the books), "husene" (the houses)

### Genitive -s

The genitive is formed by adding -s to the end of the noun phrase: "Danmarks historie" (Denmark's history), "mandens bil" (the man's car).

### Verb Endings

- **-er** (present tense): "kommer" (comes), "taler" (speaks)
- **-ede** / **-te** (past tense, weak verbs): "arbejdede" (worked), "talte" (spoke)
- **-et** / **-t** (past participle): "arbejdet" (worked), "talt" (spoken)
- **-s** (passive): "skrives" (is written), "gøres" (is done)

### Adjective Endings

- **-t** (neuter agreement): "stort" (big, neuter), "godt" (good, neuter)
- **-e** (plural/definite agreement): "store" (big, plural), "gode" (good, plural)
- **-ere** (comparative): "større" (bigger), "nyere" (newer)
- **-est** (superlative): "størst" (biggest), "nyest" (newest)

### Common Derivational Suffixes

- **-hed** (abstract nouns, like English -ness): "frihed" (freedom), "skønhed" (beauty)
- **-else** (action nouns): "bevægelse" (movement), "følelse" (feeling)
- **-lig** (adjective, like English -ly/-like): "venlig" (friendly), "naturlig" (natural)
- **-ig** (adjective): "vigtig" (important), "rigtig" (correct)
- **-tion** (borrowed suffix): "information" (information), "station" (station)
- **-ning** (verbal noun): "bygning" (building), "løsning" (solution)

### Common Prefixes

- **be-**: "beskæftige" (to employ), "betyde" (to mean)
- **for-**: "forklare" (to explain), "forstå" (to understand)
- **und-**: "undgå" (to avoid)

## Key Identification Heuristics

For automated language identification, the following combined signals are most useful:

1. Presence of æ and ø (distinguishes from Swedish, which uses ä and ö instead).
2. High frequency of "er" as both a word and a word ending.
3. The function word set {er, og, det, en, at, har, ikke, med, på, af, til, for} appearing together.
4. Suffixed articles (-en, -et, -ne) on nouns.
5. The word "efter" (as opposed to Norwegian "etter").
6. The suffix "-tion" (as opposed to Norwegian "-sjon").
7. Words ending in "-ighed" (Danish) versus "-ighet" (Norwegian).
8. The conjunction "eller" is shared with Norwegian (and Swedish), and "enten...eller" (either...or) uses the same form in Danish and Norwegian, so it is not diagnostic.
9. Danish "af" (of) and "at" (infinitive marker) vs. Norwegian "av" and "å".

Note: in diacritic-free (ASCII) text, æ/ø/å may appear as "ae"/"oe"/"aa" or simply as "a"/"o" ("pa" for "på", "ogsa" for "også"); the letter cues are then lost and the word-level cues above become decisive.
