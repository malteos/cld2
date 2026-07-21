# French Characteristics for Language Identification

## Unique Characters and Diacritics

French uses the standard Latin alphabet supplemented by several diacritical marks and special characters:

- **Acute accent (accent aigu):** e -- used almost exclusively on the letter e to indicate /e/ (ecole, ete, cafe)
- **Grave accent (accent grave):** a, e, u -- indicates /ɛ/ on e (mere, pere), distinguishes homographs for a/a, ou/ou, la/la
- **Circumflex (accent circonflexe):** a, e, i, o, u -- historically indicates a lost letter (usually s): foret (cf. English "forest"), hopital (cf. "hospital"), ile (cf. "isle")
- **Diaeresis (trema):** e, i, u -- indicates that two adjacent vowels are pronounced separately: noel, naive, aigues
- **Cedilla (cedille):** c -- indicates /s/ before a, o, u: francais, garcon, recu
- **Ligatures:** oe (coeur, soeur, oeuvre), ae (rare, mostly in Latin-derived words)

The combination of these diacritics, particularly the frequent use of e, e, and c, is a strong identifier for French text. The cedilla on c is shared with Portuguese, Turkish, and Catalan, but the specific combination of all these diacritical marks together is highly diagnostic of French.

## Character Frequency Patterns

French text exhibits distinctive character frequency distributions:

- The letter **e** is by far the most frequent letter, occurring roughly 15-17% of the time, significantly higher than in most other languages.
- The letter **s** appears frequently (about 8%), often as a silent plural marker.
- The apostrophe **'** appears with very high frequency due to elision (l', d', n', j', c', s', qu').
- Hyphens are common in compound expressions and inverted verb-subject constructions (est-ce, peut-etre, c'est-a-dire).

## Top 50 Function Words

The following are the most frequent function words in French, listed approximately by frequency. These form the backbone of language identification:

1. de, 2. la, 3. le, 4. les, 5. des, 6. un, 7. une, 8. et, 9. en, 10. est,
11. que, 12. qui, 13. dans, 14. pour, 15. au, 16. sur, 17. pas, 18. plus, 19. par, 20. avec,
21. ce, 22. se, 23. son, 24. sa, 25. ses, 26. mais, 27. ou, 28. ou, 29. ne, 30. tout,
31. si, 32. leur, 33. meme, 34. aussi, 35. bien, 36. entre, 37. autre, 38. comme, 39. alors, 40. apres,
41. fait, 42. tres, 43. peu, 44. encore, 45. ces, 46. deux, 47. sans, 48. sous, 49. donc, 50. moins

Several of these are strong French identifiers. The words "dans," "avec," "pour," "mais," "donc," "aussi," "tres," "entre," "meme," and "encore" are particularly diagnostic. The combination of "de," "la," "le," "les," "des" as the top five words is also a strong signal for French.

## Common N-grams

### Bigrams
es, en, le, de, ou, qu, re, nt, on, an, er, ti, te, el, ai, se, it, ne, me, et

### Trigrams
ent, les, des, que, ion, ous, ait, est, tio, eme, ons, ant, men, our, par, com, eur, con, dan, oir

### Quadgrams
tion, ment, pour, dans, avec, ques, eurs, ement, ique, ette, elle, oire, ance, ence, iste, ement, omme, tout, mais, plus

The quadgram "tion" is extremely frequent in French. The sequence "ment" is also highly diagnostic, as it appears in the vast majority of French adverbs. The bigram "qu" followed by an apostrophe or a vowel (qu', que, qui) is one of the strongest single identifiers of French text.

## Morphological Patterns for Language Identification

### Verb Endings

French verb infinitives end in one of three patterns, all highly frequent in text:
- **-er** (first conjugation, the largest group): parler, manger, travailler, donner
- **-ir** (second/third conjugation): finir, partir, venir, dormir
- **-re** (third conjugation): prendre, vendre, mettre, connaitre

Common conjugated endings include: -e, -es, -ons, -ez, -ent (present); -ais, -ait, -aient (imperfect); -ai, -as, -a (future/simple past); -e (past participle of -er verbs).

### Nominal and Adjectival Suffixes

- **-tion / -sion:** nation, education, television, decision -- extremely common in formal and academic French
- **-ment:** gouvernement, mouvement, evenement, changement -- noun-forming suffix and adverb suffix
- **-eux / -euse:** heureux/heureuse, dangereux/dangereuse -- adjective pairs showing masculine/feminine
- **-ique:** politique, historique, scientifique, economique -- adjectives from Greek roots
- **-eur / -euse or -rice:** acteur/actrice, chanteur/chanteuse -- agent nouns
- **-ance / -ence:** importance, difference, presence, assurance
- **-iste:** artiste, journaliste, specialiste

### Adverb Formation

French adverbs are overwhelmingly formed by adding **-ment** to the feminine form of the adjective: lente > lentement, heureuse > heureusement, vraie > vraiment. This -ment suffix is one of the most reliable morphological markers for French identification.

## Script-Specific Features

- **Apostrophe frequency:** French uses apostrophes far more frequently than most other Romance languages due to systematic elision. Common patterns include: l'homme, l'eau, d'accord, j'ai, c'est, n'est, qu'il, s'il, aujourd'hui.
- **Hyphenation in verb forms:** Inverted questions and imperative constructions use hyphens: est-ce que, dit-il, donne-moi, allez-vous-en.
- **Quotation marks:** French traditionally uses guillemets (chevrons) for quotation marks rather than the English-style quotation marks.
- **Spacing before punctuation:** In formal French typography, a non-breaking space precedes semicolons, colons, exclamation marks, and question marks. This spacing convention, when present in text, is a strong indicator of French.
