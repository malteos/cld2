# Ilocano Text Characteristics for Language Detection

## Character Set

Ilocano is written using the standard Latin alphabet with no special diacritical marks required. The alphabet consists of 28 letters:

**a b c d e f g h i j k l m n ng o p q r s t u v w x y z**

The digraph *ng* is considered a single letter in the Ilocano alphabet. The letters c, f, j, q, v, x, and z appear primarily in loanwords from Spanish and English.

Occasionally, accent marks (acute: a) are used in dictionaries and pedagogical materials to indicate stress, but these do not appear in standard text.

## Character Frequency Patterns

High-frequency characters in Ilocano text include:

- **a** -- the most frequent vowel, appearing in articles, affixes, and roots
- **i** -- very frequent, appearing in the article *ti*, oblique *iti*, and many affixes
- **n** -- extremely common, part of the digraph *ng*, articles, and many roots
- **t** -- high frequency due to articles *ti*, *iti*, *dagiti*
- **g** -- frequent as part of *ng* digraph, *ag-* prefix, *dagiti*
- **d** -- common in *dagiti*, *da*, demonstratives
- **k** -- frequent in *ken*, *ket*, *kadagiti*, *ko*
- **e** -- moderately frequent, found in *-en* suffix, *ken*, *ket*

The digraph **ng** is exceptionally frequent compared to most other Latin-script languages, serving as a key identifier for Philippine languages generally and Ilocano specifically.

## Top 50 Function Words

The following function words are highly frequent in Ilocano text and serve as strong diagnostic markers:

1. ti (the, singular article)
2. a (linker)
3. nga (linker, "that/which")
4. iti (in/at/on the, oblique singular)
5. ken (and)
6. dagiti (the, plural article)
7. ni (personal article)
8. da (they/their, plural personal article)
9. ket (and/but, topic-shift marker)
10. idi (when/at the time, past temporal)
11. kadagiti (in/at/on the, oblique plural)
12. manipud (from)
13. no (if/when)
14. ta (because/so that)
15. pay (also/too)
16. met (also/indeed)
17. ngem (but/however)
18. la (only/still)
19. koma (hopefully/should)
20. dayta (that)
21. daytoy (this)
22. awan (none/there is no)
23. adda (there is/exists)
24. saan (no/not)
25. kas (like/as)
26. uray (even/although)
27. amin (all)
28. maysa (one)
29. dua (two)
30. tallo (three)
31. adu (many)
32. bassit (few/small)
33. naimbag (good)
34. agpa- (verbal prefix)
35. mabalin (possible/can)
36. babaen (through/by means of)
37. para (for)
38. kasta (like that/thus)
39. ditoy (here)
40. idiay (there)
41. gapu (because/reason)
42. maipapan (about/concerning)
43. sakbay (before)
44. kalpasan (after)
45. kabayatan (while/during)
46. tunggal (each/every)
47. nupay (although)
48. wenno (or)
49. isuna (he/she/it)
50. na (his/her/its, enclitic)

## Common N-grams and Letter Combinations

### Bigrams (high frequency)
- **ng** -- digraph letter, extremely common
- **ti** -- article, ubiquitous
- **ag** -- verbal prefix marker
- **da** -- plural article/pronoun
- **an** -- suffix, common ending
- **en** -- patient focus suffix
- **it** -- part of *iti*, *dagiti*
- **na** -- enclitic pronoun, adjective prefix
- **ke** -- found in *ken*, *ket*
- **ma** -- stative/abilitative prefix

### Trigrams (high frequency)
- **dag** -- start of *dagiti*
- **iti** -- oblique article
- **agi** -- part of *dagiti*
- **git** -- part of *dagiti*
- **nga** -- linker
- **ken** -- conjunction
- **nag** -- completed actor focus prefix
- **man** -- part of *mang-*, *manipud*
- **ang** -- common sequence in affixed verbs
- **ket** -- topic marker

## Morphological Patterns as Detection Features

Ilocano verbs display distinctive morphological patterns that aid identification:

- **ag-** prefix: *agtrabaho*, *agbiag*, *agsurat*, *agluto* -- highly characteristic
- **nag-** prefix: *nagtrabaho*, *nagbiag* -- completed actor focus
- **mang-** prefix: *mangted*, *mangbasa*, *mangisuro* -- transitive actor focus
- **-um-** infix: *sumurat*, *tumulong*, *bumangon* -- actor focus
- **-in-** infix: *sinurat*, *tinulong* -- completed aspect
- **-en** suffix: *basaen*, *suraten*, *lutoen* -- patient focus
- **-an** suffix: *suratan*, *basaan* -- locative focus
- **ma-** prefix: *mabasa*, *mabalin*, *maamuan* -- stative/abilitative
- **na-** prefix (adjective): *napintas*, *naimbag*, *nalaing* -- characteristic Ilocano adjective formation

## Distinguishing Features from Other Languages

Key markers that separate Ilocano from other Latin-script languages:

1. **Article system:** *ti/dagiti* is unique to Ilocano (vs. Tagalog *ang/mga*)
2. **Conjunction:** *ken* for "and" (vs. Tagalog *at*, Cebuano *ug*)
3. **Topic marker:** *ket* appearing frequently between clauses
4. **Verbal prefixes:** *ag-/nag-* pattern is characteristic of Ilocano
5. **Linker:** *a/nga* pattern (shared with Tagalog but combined with other Ilocano markers)
6. **Oblique markers:** *iti/kadagiti* are distinctive
7. **High frequency of *ng* digraph** combined with the specific function word inventory
