# Dzongkha (dzo_Tibt) -- Language Identification Characteristics

## Script and Character Inventory

Dzongkha is written in the Tibetan script (Uchen / དབུ་ཅན་), the same script used for Standard Tibetan (bod_Tibt). Both languages share the same base alphabet, making script-level discrimination impossible; identification must rely on lexical, morphological, and distributional features.

### Consonants (30 base letters)

ཀ ཁ ག ང ཅ ཆ ཇ ཉ ཏ ཐ ད ན པ ཕ བ མ ཙ ཚ ཛ ཝ ཞ ཟ འ ཡ ར ལ ཤ ས ཧ ཨ

### Vowel Marks (4 diacritics)

- ི (gigu -- vowel /i/)
- ུ (zhabkyu -- vowel /u/)
- ེ (drengbu -- vowel /e/)
- ོ (naro -- vowel /o/)

The inherent vowel is /a/, unmarked in the script.

### Subjoined Letters

Tibetan script represents consonant clusters through vertical stacking (subjoined forms). Dzongkha uses a subset of the stacking combinations found in Classical Tibetan. Common subjoined consonants in Dzongkha include ྱ (ya-btags), ྲ (ra-btags), ླ (la-btags), and ྭ (wa-zur). Dzongkha text tends to use fewer complex multi-layer stacks than Classical Tibetan literary texts, because Dzongkha orthography has been partially modernized and standardized by the Dzongkha Development Commission. In particular, archaic consonant clusters preserved in Classical Tibetan literary spelling (such as five-layer stacks) are rare in contemporary Dzongkha writing.

## Character and Syllable Frequency: Dzongkha vs. Standard Tibetan

While both languages use identical Unicode codepoints, their frequency distributions differ measurably:

- **འ (achung):** Significantly more frequent in Dzongkha due to its role in the nominalizer འི and the pervasive Dzongkha particles འདི, འབད, འགྱོ. In Standard Tibetan, འ appears but at lower relative frequency.
- **སྦེ sequence:** The particle སྦེ ("like, as, having done") is a strong Dzongkha marker. This syllable is essentially absent from Standard Tibetan.
- **ལུ (lu):** The Dzongkha dative/locative particle ལུ is extremely common. Standard Tibetan uses ལ instead, making the presence of ལུ a reliable discriminator.
- **མས (me):** The Dzongkha evidential copula མས appears with high frequency as a sentence-final marker. It is not used in Standard Tibetan in the same grammatical role.
- **ཨིན (in):** The Dzongkha equative copula ཨིན is far more frequent than in Standard Tibetan, where yin (ཡིན) predominates.
- **ཚུ (tshu):** Dzongkha plural marker ཚུ is common; Standard Tibetan uses ཚོ instead.

Overall, Dzongkha text shows higher frequency of the consonant འ, the vowel mark ུ (due to particles like ལུ, ཚུ), and the letter ཨ (due to the copula ཨིན).

## Top 50 Function Words

The following are the most frequent function words in Dzongkha, ranked approximately by corpus frequency. Many of these serve as strong discriminators against Standard Tibetan because they are either unique to Dzongkha or used at vastly different frequencies.

1. འདི -- this (demonstrative, far more frequent in Dzongkha than in Tibetan where འདི also exists)
2. གི -- genitive particle
3. ལུ -- dative/locative particle (Tibetan uses ལ)
4. དང -- and, with (conjunction)
5. ཅིག -- one, a (indefinite article / numeral)
6. ནི -- topic marker
7. སྦེ -- having done, as (connective particle; unique to Dzongkha)
8. ཨིན -- equative copula "is" (Tibetan uses ཡིན)
9. མས -- evidential copula, "it is" (reportative/sensory evidence)
10. ཡོད -- existential verb "there is / have"
11. བཟུམ -- like, similar to (comparative particle)
12. ཚུ -- plural marker (Tibetan uses ཚོ)
13. ལས -- ablative particle, "from" / "than"
14. ནང -- in, inside (locative)
15. འབད -- to do, to make (auxiliary verb, extremely common)
16. རྐྱབས -- to do, to hit (auxiliary)
17. ཏེ -- connective particle, "and then"
18. བའི -- genitive form following verb stems
19. མི -- person, negative particle
20. པའི -- genitive nominalizer
21. ཁར -- to, toward (directional postposition)
22. ཤོམ -- probably, perhaps (epistemic particle)
23. མེད -- negative existential "there is not / do not have"
24. ཟེར -- to say (quotative verb, used for reported speech)
25. བཀོད -- to place, to arrange
26. ཡང -- also, even (additive particle)
27. དེ -- that (distal demonstrative)
28. ཆོས -- dharma, religion (high-frequency content word in both languages)
29. བཞིན -- while, as (simultaneous connective)
30. ཀྱི -- genitive particle (variant after certain finals)
31. མཛད -- to do (honorific)
32. ཐོག -- on top of, on the basis of
33. ཧེ་མ -- before, previously
34. ཚུགས -- to be able to (potential auxiliary)
35. བཅས -- together with, including
36. ཁ་ -- mouth, direction (component in many compounds)
37. ཞིབ -- detailed, fine (adjectival)
38. ཤེས -- to know
39. དགོ -- need to, must (modal auxiliary)
40. མཐོང -- to see
41. བྱིན -- to give
42. དཔེར -- for example
43. ཁོ -- he (third person pronoun)
44. མོ -- she (third person pronoun feminine)
45. ང -- I (first person pronoun)
46. ཁྱོད -- you (second person pronoun)
47. ག་ཅི -- what (interrogative)
48. ག་ཏེ -- where (interrogative)
49. ག་དེམ་ཅིག -- how, what kind (interrogative)
50. ག་དེ་སྦེ -- how, in what manner (interrogative; note the Dzongkha-specific སྦེ)

## Common Character Sequences Unique to Dzongkha

The following n-grams and syllable sequences are highly characteristic of Dzongkha and rare or absent in Standard Tibetan text:

- **སྦེ** -- connective/manner particle, near-zero frequency in Standard Tibetan
- **ལུ་** -- dative particle (with tsheg), replaces Tibetan ལ་
- **ཨིན་** -- equative copula, much more frequent than in Standard Tibetan
- **མས་** -- evidential sentence-final marker
- **འབད་** -- auxiliary "to do," ubiquitous in Dzongkha verb constructions
- **ཚུ་** -- plural marker, replaces Tibetan ཚོ་
- **ཚུགས** -- potential auxiliary "to be able to"
- **ག་ཅི** -- interrogative "what" (Standard Tibetan uses ཅི་ཞིག or གང)
- **ག་ཏེ** -- interrogative "where" (Standard Tibetan uses གང་ན or ག་པར)
- **ག་དེམ་ཅིག** -- interrogative "how/what kind" (unique to Dzongkha)
- **བཟུམ་** -- comparative particle "like" (Standard Tibetan uses འདྲ or ལྟ་བུ)
- **རྐྱབས** -- auxiliary verb, distinctive Dzongkha usage
- **ཤོམ** -- epistemic "probably," not standard in Tibetan

## Particles That Differ from Standard Tibetan

This section directly enumerates grammatical particles where Dzongkha and Standard Tibetan diverge, providing the most actionable features for language identification.

| Function | Dzongkha | Standard Tibetan | Notes |
|---|---|---|---|
| Dative / locative | ལུ | ལ | Strongest single-particle discriminator |
| Plural | ཚུ | ཚོ | Vowel difference (u vs. o) |
| Equative copula | ཨིན | ཡིན | Initial consonant differs |
| Evidential copula | མས | རེད | Completely different morpheme |
| Connective "having done" | སྦེ | (no direct equivalent) | Unique to Dzongkha |
| Auxiliary "to do" | འབད | བྱས / བྱེད | Different verb root |
| Comparative "like" | བཟུམ | འདྲ / ལྟ་བུ | Different morpheme |
| Interrogative "what" | ག་ཅི | ཅི་ཞིག / གང | Different formation |
| Interrogative "where" | ག་ཏེ | ག་པར / གང་ན | Dzongkha uses ག་ prefix pattern |
| Potential "can" | ཚུགས | ཐུབ | Different verb |
| "Probably" | ཤོམ | སྲིད / ཡིན་སྲིད | Unique Dzongkha epistemic |
| "Before" (temporal) | ཧེ་མ | སྔོན / སྔ་མ | Different root |

## Morphological and Syntactic Signals

### Verb Auxiliaries

Dzongkha makes extensive use of light verb / auxiliary constructions with འབད (to do) and རྐྱབས (to do/hit). These auxiliaries combine with noun or adjective stems to form complex predicates. Standard Tibetan uses བྱེད and བྱས for similar purposes but with different frequency and distributional patterns. The bigram འབད་ appearing after a content word is a strong Dzongkha signal.

### Sentence-Final Particles

Dzongkha sentences typically end with copula or evidential markers that differ from Tibetan:
- ཨིན (speaker certainty, equative)
- མས (sensory/reportative evidence)
- ཡོད (existential, similar in both languages but combined differently)

Standard Tibetan sentence-final particles include རེད (factual), བྱུང (experiential), and འདུག (evidential based on direct observation), which are rare in Dzongkha.

### Honorific System

Both languages have honorific registers, but Dzongkha uses a distinct set of honorific vocabulary influenced by its independent development within Bhutan. Some honorific forms overlap with Classical Tibetan, but Dzongkha has innovated forms not found in Standard Tibetan.

## Orthographic Conventions

- Dzongkha uses the tsheg (་) syllable delimiter identically to Standard Tibetan.
- Dzongkha uses the shad (།) as a phrase/sentence delimiter, same as Standard Tibetan.
- Modern Dzongkha text often uses Arabic numerals alongside or instead of Tibetan numerals (༠-༩), whereas literary Tibetan texts more consistently use Tibetan numerals.
- Dzongkha text may contain loanwords from English and Hindi/Nepali transliterated into Tibetan script, while Standard Tibetan text more often contains loanwords from Chinese.

## Summary of Key Discriminators for LID

For automated language identification between Dzongkha and Standard Tibetan, the following features should be weighted most heavily:

1. **Presence of སྦེ** -- near-categorical Dzongkha marker
2. **ལུ vs. ལ** -- dative particle difference, extremely high frequency
3. **ཨིན vs. ཡིན** -- equative copula difference
4. **མས as sentence-final** -- Dzongkha evidential
5. **ཚུ vs. ཚོ** -- plural marker difference
6. **འབད as auxiliary** -- Dzongkha verb construction marker
7. **ག་ prefix interrogatives** (ག་ཅི, ག་ཏེ, ག་དེམ་ཅིག) -- Dzongkha question words
8. **བཟུམ** -- Dzongkha comparative particle
9. **Absence of རེད, འདུག, བྱུང** -- Standard Tibetan evidentials rare in Dzongkha
10. **Frequency of འབད + content word bigrams** -- structural pattern unique to Dzongkha
