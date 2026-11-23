# Breton Distinctive Characteristics for Language Identification

## Distinctive Characters and Orthographic Features

Breton uses the Latin alphabet with several distinctive orthographic conventions that serve as strong signals for language identification:

### The c'h Digraph
The most diagnostic feature of Breton orthography is the digraph **c'h**, representing a voiceless velar or uvular fricative [x] (similar to German "ch" in "Bach" or Scottish "loch"). This character combination is virtually unique to Breton among European languages and appears with high frequency. Its presence in a text is an extremely strong indicator of Breton. Examples: *c'hoari* (game), *marc'h* (horse), *c'hwec'h* (six), *ac'hano* (from there).

### Other Distinctive Characters
- **zh**: Represents a sound that is [z] in most dialects but [h] in the Vannetais dialect. Used in words like *Breizh* (Brittany), *kozh* (old).
- **ñ**: Indicates nasalization of the preceding vowel. Example: *Breizh* vs *brezhoneg* with the nasal variant *añ*.
- **ù**: Represents the vowel [y] (like French u). Example: *dùar* (earth, in some orthographies).
- **û**: Long version of ù.
- **ê**: Open e [ɛː]. Example: *bêr* (short).
- **ë**: Indicates a schwa or that vowels should be pronounced separately.
- **-añ**: The verbal noun (infinitive) ending, extremely common: *lenn**añ*** (to read), *skriv**añ*** (to write), *kan**añ*** (to sing).

## Character Frequency Patterns

Breton text shows distinctive character frequency distributions:
- High frequency of **a**, **e**, **n**, **r**, **o** among single letters
- Unusually high frequency of the apostrophe **'** due to the c'h digraph and elision
- Frequent occurrence of **z** compared to French or English
- The combination **c'h** appears far more frequently than in any other language
- **w** appears with moderate frequency (rare in French, common in Breton: *war*, *gwall*, *gwenn*)
- **k** is very common (Breton uses k where French uses c/qu: *ker* not *quer*, *kreñv* not *crenv*)

## Top 50 Function Words

The following function words are among the most frequent in Breton text and serve as strong identifiers:

1. **ar** / **an** / **al** - the (definite article variants)
2. **ur** / **un** / **ul** - a/an (indefinite article variants)
3. **da** - to, your (2sg possessive)
4. **e** - in, his (3sg.m possessive), verbal particle
5. **ha** / **hag** - and
6. **ne** - negative particle
7. **ket** - not (second part of negation)
8. **a** - of, from, preverbal particle
9. **eo** - is (3sg present of bezañ)
10. **zo** - is (existential/situational)
11. **en** - in the
12. **er** - in the
13. **war** - on
14. **gant** - with
15. **evit** - for
16. **eus** - of/from, have (auxiliary)
17. **bet** - been (past participle of bezañ)
18. **he** / **ho** - her, your (pl.)
19. **o** - their, progressive particle
20. **ra** - does (3sg present of ober)
21. **pe** - or
22. **met** - but
23. **pa** - when
24. **ma** - if, my, that
25. **d'** - to the (elided da + article)
26. **ez** - that (conjunction)
27. **holl** - all
28. **bras** - big/great
29. **mat** - good
30. **re** - too, those/ones
31. **ken** - so, as
32. **dre** - through
33. **diwar** - from/off
34. **etre** - between
35. **dreist** - above
36. **dindan** - under
37. **a-raok** - before
38. **goude** - after
39. **evel** - like/as
40. **pep** - each/every
41. **meur** - many
42. **gwelloc'h** - better
43. **hep** - without
44. **ouzh** - at/against
45. **deus** - of/from (variant)
46. **abaoe** - since
47. **betek** - until
48. **hervez** - according to
49. **peogwir** - because
50. **rak** - because/for

## Common Bigrams and Trigrams

### High-frequency bigrams:
- **an**, **ar**, **er**, **en**, **ou**, **ez**, **da**, **re**, **on**, **el**, **al**, **wa**, **eu**, **zh**, **eg**, **ed**, **añ**, **iñ**, **ek**, **c'** (part of c'h)

### High-frequency trigrams:
- **c'h**, **bre**, **eus**, **war**, **ket**, **gat**, **evr**, **enn**, **all**, **ezh**, **izh**, **eiz**, **oue**, **añ**, **neg**, **ont**, **ent**, **our**

### Highly diagnostic n-grams (nearly unique to Breton):
- **c'h** - the single strongest indicator
- **zh** in word-final position (e.g., *Breizh*, *kozh*)
- **-añ** as word ending (verbal noun suffix)
- **-erezh** (abstract noun suffix)
- **-adur** (noun suffix)
- **-añv** (noun suffix)

## Mutation Patterns Visible in Text

Initial consonant mutations create characteristic alternation patterns in Breton text that can assist identification:
- Words beginning with **v** that alternate with **b** or **m** base forms
- Words beginning with **z** alternating with **d** base forms
- **c'h** appearing as a mutation of **g** or **k**
- **f** appearing where **p** would be expected (spirantization)
- **w** appearing where **gw** would be expected (lenition)

These patterns mean that the same root word may appear with different initial consonants depending on syntactic context, creating a distinctive text signature.

## Morphological Patterns for LID

### Verb endings
- **-añ**: verbal noun / infinitive marker (*kanañ*, *lenn*, *skrivañ*)
- **-an**, **-in**, **-out**, **-omp**, **-it**, **-ont**: present tense synthetic endings
- **-en**, **-es**, **-e**, **-emp**, **-ec'h**, **-ent**: imperfect endings
- **-in**, **-is**, **-as**, **-jomp**, **-joc'h**, **-jont**: preterite endings

### Noun suffixes
- **-adur**: action/result nouns (*deskadurezh* = education)
- **-erezh**: abstract nouns (*skianterezh* = science)
- **-egezh**: quality nouns (*pinvidigezh* = wealth)
- **-enn**: singulative suffix (*gwezenn* = a tree, from *gwez* = trees)
- **-er**: agent nouns (*skriver* = writer)
- **-eg**: adjective/characteristic suffix

### Common word-final patterns
Words frequently end in: **-añ**, **-er**, **-el**, **-al**, **-eg**, **-ek**, **-ezh**, **-adur**, **-enn**, **-où** (plural), **-ioù** (plural)

## Summary of Top Diagnostic Features

For automated language identification, the following features ranked by discriminative power:

1. Presence of **c'h** digraph (near-certain Breton identifier)
2. Word-final **zh** (*Breizh*, *kozh*, *bazh*)
3. Function word set: *ar/an/al*, *ur/un/ul*, *ha/hag*, *ne...ket*, *eo*, *zo*
4. The **-añ** verbal noun ending at high frequency
5. Use of **k** where related languages use **c** or **qu**
6. High frequency of **w** in word-initial position
7. Presence of **ñ** for nasalization
8. Conjugated preposition forms (*ganin*, *dezhañ*, *evidon*)
9. Mutation alternation patterns in function word contexts
10. Characteristic plural suffixes **-où** and **-ioù**
