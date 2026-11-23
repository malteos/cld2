# Hungarian - Language Identification Characteristics

## Script and Special Characters

Hungarian uses the Latin script with several unique characters and digraphs that serve as strong identification markers.

### Extended Characters

Hungarian adds the following characters to the basic Latin alphabet, each representing a distinct phoneme:

| Character | Phoneme | Description |
|-----------|---------|-------------|
| a | /aː/ | Long open front vowel |
| e | /eː/ | Long close-mid front vowel |
| i | /iː/ | Long close front vowel |
| o | /oː/ | Long close-mid back rounded vowel |
| o, o | /ø/, /øː/ | Front rounded vowels (short and long) |
| u | /uː/ | Long close back rounded vowel |
| u, u | /y/, /yː/ | Front rounded close vowels (short and long) |

The double acute accent (hungarumlaut) on **o** and **u** is particularly distinctive and almost exclusively associated with Hungarian among major world languages. Its presence in a text is an extremely strong indicator of Hungarian.

### Digraphs

Hungarian treats several two-letter (and one three-letter) combinations as single phonemic units. These are considered single letters of the Hungarian alphabet:

- **cs** /tʃ/ - voiceless postalveolar affricate
- **dz** /dz/ - voiced alveolar affricate
- **dzs** /dʒ/ - voiced postalveolar affricate (the only trigraph)
- **gy** /ɟ/ - voiced palatal stop
- **ly** /j/ - palatal approximant
- **ny** /ɲ/ - palatal nasal
- **sz** /s/ - voiceless alveolar fricative
- **ty** /c/ - voiceless palatal stop
- **zs** /ʒ/ - voiced postalveolar fricative

The digraphs **sz**, **cs**, **gy**, **ny**, and **zs** are among the most reliable orthographic indicators of Hungarian. Notably, the letter **s** alone represents /ʃ/ in Hungarian (not /s/ as in most Latin-script languages), while **sz** represents /s/.

## Character Frequency Patterns

Hungarian text shows distinctive character frequency distributions:

- High frequency of vowels **a**, **e**, **o** due to their role in both stems and suffixes
- Frequent occurrence of **t** (common in case suffixes like -t accusative, -nak/-nek dative)
- The digraph **sz** appears with high frequency
- Relatively high frequency of **k** (plural marker, various suffixes)
- The letter **q**, **w**, **x**, **y** (alone) are rare, appearing mainly in loanwords and proper names
- **ly** is relatively rare but distinctive

## Top 50 Function Words

The following function words are the most frequent in Hungarian text and serve as strong identification features:

1. **a** - the (definite article, before consonants)
2. **az** - the (definite article, before vowels); that
3. **es** - and
4. **hogy** - that (conjunction)
5. **nem** - not, no
6. **ez** - this
7. **is** - also, too
8. **egy** - a/an, one
9. **van** - is, exists
10. **meg** - verbal prefix (perfective); and, still
11. **de** - but
12. **volt** - was
13. **mar** - already
14. **meg** - still, yet
15. **mint** - as, like, than
16. **csak** - only, just
17. **vagy** - or; you are
18. **fel** - up (verbal prefix)
19. **ki** - out (verbal prefix); who
20. **le** - down (verbal prefix)
21. **be** - in (verbal prefix)
22. **el** - away (verbal prefix)
23. **en** - I
24. **te** - you (singular)
25. **o** - he/she
26. **mi** - we; what
27. **ti** - you (plural)
28. **ok** - they
29. **itt** - here
30. **ott** - there
31. **most** - now
32. **majd** - later, then
33. **nagyon** - very
34. **igen** - yes
35. **sem** - neither, nor
36. **ni** - look (interjection); infinitive marker in some dialects
37. **pedig** - however, whereas
38. **mert** - because
39. **ha** - if
40. **amikor** - when (conjunction)
41. **ahol** - where (conjunction)
42. **ami** - which, what (relative)
43. **aki** - who (relative)
44. **mely** - which (formal relative)
45. **minden** - every, all
46. **sok** - many, much
47. **mas** - other
48. **uj** - new
49. **nagy** - big, large
50. **jo** - good

The function word pair **a/az** (definite article) is particularly diagnostic: **a** before consonants, **az** before vowels is a pattern unique to Hungarian.

## Common N-grams

### Common Bigrams
- **sz**, **cs**, **gy**, **ny**, **zs** (digraph letters)
- **el**, **en**, **er**, **et**, **al**, **an**, **eg**, **es**, **te**, **ta**, **le**, **me**, **ke**, **ne**, **re**, **se**, **ok**, **ak**, **ek**

### Common Trigrams
- **sze**, **egy**, **ogy**, **nak**, **nek**, **ban**, **ben**, **hoz**, **hez**, **bol**, **bel**, **rol**, **rol**, **nak**, **val**, **vel**, **meg**, **nem**, **van**

### Common Word-Final Patterns (Case Suffixes)
- **-ban/-ben** (inessive)
- **-nak/-nek** (dative)
- **-val/-vel** (instrumental)
- **-bol/-bol** (elative)
- **-hoz/-hez** (allative)
- **-ra/-re** (sublative)
- **-rol/-rol** (delative)
- **-on/-en/-on** (superessive)
- **-t** (accusative)
- **-k** (plural)

## Agglutinative Suffix Patterns for LID Detection

Hungarian's agglutinative nature creates distinctive long words with recognizable suffix chains. These patterns are strong identifiers:

- Noun + possessive + case: **hazamban** (in my house)
- Verb + tense + person: **lattam** (I saw [definite])
- Noun + plural + case: **hazakban** (in houses)
- Verb + potential + person: **irhatnam** (I could write)
- Noun + derivational + case: **hazatlansagert** (for homelessness)

The average word length in Hungarian is notably longer than in most European languages due to agglutination, typically averaging 5-7 characters per word in running text, with many common words reaching 10-15 characters.

## Distinguishing Orthographic Features

Several features in combination make Hungarian text highly identifiable:

1. The double acute accent (**o**, **u**) - nearly unique to Hungarian
2. High frequency of **sz**, **cs**, **gy**, **ny** digraphs
3. The definite article pattern **a/az**
4. Long agglutinated words with recognizable suffix chains
5. Postpositional constructions (word after noun instead of before)
6. Absence of words beginning with certain consonant clusters common in Slavic languages
7. Frequent word-final **-k** (plural), **-t** (accusative/past tense), **-m** (first person)
