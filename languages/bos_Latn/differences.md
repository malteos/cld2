# Distinguishing Bosnian from Croatian, Serbian, and Montenegrin

## Overview

Bosnian, Croatian, Serbian, and Montenegrin are all standardized varieties based on the Neo-Stokavian dialect continuum. They are mutually intelligible to a very high degree, making language identification among them one of the most challenging tasks in computational linguistics. The differences are primarily in vocabulary (especially loanword layers), certain phonological preferences, and minor morphological/syntactic tendencies. This document catalogs the key differences relevant for language identification.

## Bosnian vs. Croatian

### Lexical Differences

This is the primary axis of distinction. Croatian underwent extensive purist campaigns to replace foreign (especially Turkish, Arabic, and Persian) loanwords with native Slavic neologisms or calques, while Bosnian retains many of these loanwords as part of its standard vocabulary.

| Bosnian | Croatian | English |
|---------|----------|---------|
| hljeb | kruh | bread |
| sedmica | tjedan | week |
| kahva | kava | coffee |
| historija | povijest | history |
| geografija | zemljopis | geography |
| hemija | kemija | chemistry |
| zrak | zrak | air (same) |
| tačka | točka | point/dot |
| općina | općina | municipality (same) |
| univerzitet | sveučilište | university |
| avion | zrakoplov | airplane |
| fudbal | nogomet | football |
| hiljada | tisuća | thousand |
| fabrika | tvornica | factory |
| muzika | glazba | music |
| pozorište | kazalište | theater |
| biblioteka | knjižnica | library |
| sahat / sat | sat | clock/hour |
| čaršija | (no equivalent) | bazaar |
| džamija | džamija | mosque (same, but rarer in Croatian text) |
| učiteljica | učiteljica | teacher (same, fem.) |
| sokak | ulica (preferred) | street |
| dućan | trgovina | shop |
| komšija | susjed | neighbor |
| avlija | dvorište | courtyard |
| rahatluk | udobnost | comfort |
| ćilim | tepih (preferred) | carpet |
| mahala | četvrt | neighborhood |
| bajram | (not nativized) | religious holiday |

### Phonological Differences

- **H-retention:** Bosnian more consistently retains /h/ in words where it has been historically present: *hljeb* (bread), *lahko* (easily), *mehko* (softly), *sahrana* (funeral). Croatian either has different lexical items (*kruh* for bread) or also retains /h/ but in different patterns.
- **Interrogative pronoun:** Bosnian strongly prefers *šta* (what) in questions, while Croatian uses *što*. Both use *što* as a relative pronoun/conjunction, but the interrogative use is a key discriminator.
- **Consonant cluster preferences:** Minor differences exist, e.g., Bosnian *tačka* vs. Croatian *točka* reflects different vowel outcomes.

### Loanword Patterns

The most diagnostic feature. Bosnian uses Turkish/Arabic loanwords in everyday contexts where Croatian uses Slavic words:

- **Turkish/Arabic layer in Bosnian:** džamija (mosque), avlija (courtyard), sokak (alley), čaršija (bazaar), dućan (shop), kahva (coffee), ćevap (kebab), sarma (stuffed rolls), burek (pastry), rahatluk (comfort), ćilim (rug), peškir (towel), jastuk (pillow), čarapa (sock), boja (color, from Turkish *boya*), komšija (neighbor), zanatlija (craftsman), zanat (craft), sevdah (longing/love), merak (pleasure), ćeif (mood/pleasure), behar (blossom), hajat (porch)

- **Croatian Slavic alternatives:** Croatian systematically replaces or avoids these with native formations. Where Bosnian says *univerzitet*, Croatian says *sveučilište*. Where Bosnian says *muzika*, Croatian says *glazba*. Where Bosnian says *hiljada*, Croatian says *tisuća*.

### Morphosyntactic Differences

- **Future tense formation:** Both use *ću/ćeš/će* + infinitive, but Croatian more frequently uses the *da* + present construction in some contexts. Bosnian freely uses both the infinitive and *da* + present.
- **Preposition *sa*:** Bosnian strongly prefers *sa* (with) before all nouns, while Croatian uses *s* before consonants and *sa* before vowels and certain consonant clusters.

## Bosnian vs. Serbian (Latin script)

### The Ekavian/Ijekavian Divide

This is the single most powerful discriminator between Bosnian and Serbian Latin text. Bosnian uses the **ijekavian** reflex of Common Slavic *yat*, while Serbian (as used in Serbia proper) predominantly uses the **ekavian** reflex:

| Bosnian (ijekavian) | Serbian (ekavian) | English |
|---------------------|-------------------|---------|
| mlijeko | mleko | milk |
| lijep | lep | beautiful |
| svijet | svet | world |
| vrijeme | vreme | time/weather |
| rijeka | reka | river |
| dijete | dete | child |
| cijena | cena | price |
| cvijet | cvet | flower |
| brijeg | breg | hill |
| bijel | beo | white |
| sijeno | seno | hay |
| liječnik | lekar | doctor |
| pjevati | pevati | to sing |
| bježati | bežati | to flee |
| snijeg | sneg | snow |
| zvijezda | zvezda | star |
| smijeh | smeh | laughter |
| prijelaz | prelaz | crossing |
| vijest | vest | news |
| tjeskoba | teskoba | anxiety |

The ijekavian reflex manifests in several patterns:
- Long yat becomes *ije*: *mlijeko, vrijeme, snijeg*
- Short yat becomes *je*: *mjera, mjesta, pjesma*
- Before certain consonants, *je* can become *lje* or *nje*: *ljeto* (summer), *nježan* (tender)

### Lexical Differences

Beyond the ekavian/ijekavian split, there are also vocabulary differences:

| Bosnian | Serbian | English |
|---------|---------|---------|
| hljeb | hleb | bread |
| sedmica | nedelja | week |
| kahva | kafa | coffee |
| historija | istorija | history |
| lahko | lako | easily |
| tačka | tačka | point (same) |
| pozorište | pozorište | theater (same) |
| ured | kancelarija | office |
| zvanično | zvanično | officially (same) |
| kolodvor / stanica | stanica | station |
| sahrana | sahrana | funeral (same) |

### Script Considerations

Serbian is predominantly written in Cyrillic in Serbia, though Latin script is also widely used. When Serbian appears in Latin script, the ekavian forms make it clearly distinguishable from Bosnian. However, Serbian from Montenegro, parts of Bosnia (Republika Srpska), and some diaspora contexts may use ijekavian, which complicates the distinction.

### Loanword Differences

Serbian, like Bosnian, retains some Turkish loanwords but generally fewer than Bosnian, and with different phonological adaptations:

- Bosnian *kahva* vs. Serbian *kafa* (coffee) — the /h/ > zero in Serbian
- Bosnian *lahko* vs. Serbian *lako* — h-retention in Bosnian
- Bosnian uses more Arabic/Turkish administrative and cultural vocabulary

## Bosnian vs. Montenegrin

### Shared Features

Bosnian and Montenegrin are the most similar pair among the four standards. Both use:
- Ijekavian reflex
- Many of the same Turkish loanwords
- Similar syntactic patterns

### Key Differences

The primary distinguishing feature is that Montenegrin has introduced two additional letters into its alphabet since its 2009 orthographic reform:

- **ś** (s with acute) — a soft /ɕ/ sound, as in *śutra* (tomorrow)
- **ź** (z with acute) — a soft /ʑ/ sound, as in *iźelica* (glutton)

These letters do not exist in the Bosnian alphabet. The presence of ś or ź in Latin-script text is a strong indicator of Montenegrin.

### Vocabulary Differences

| Bosnian | Montenegrin | English |
|---------|------------|---------|
| sutra | śutra | tomorrow |
| sjekira | śekira | axe |
| hljeb | hljeb | bread (same) |
| kahva | kafa | coffee |

Montenegrin also has some unique lexical items from its regional dialects, particularly from the coastal (maritime) vocabulary influenced by Venetian Italian:

- Montenegrin may use some Italian-origin words more commonly (e.g., from the Bay of Kotor traditions)

In practice, Montenegrin and Bosnian texts without the ś/ź letters and without distinctly regional vocabulary are extremely difficult to distinguish computationally.

## Diagnostic Feature Summary for LID

### Strong Bosnian Indicators (high confidence)

1. **Ijekavian reflex** (*ije/je* patterns) — eliminates Serbian ekavian
2. **Turkish/Arabic loanwords in natural context** (*džamija, avlija, sokak, čaršija, kahva, komšija, rahatluk, dućan, mahala*) — distinguishes from Croatian
3. **H-retention** (*hljeb, lahko, mehko*) — distinguishes from Serbian
4. **Absence of ś and ź** — eliminates Montenegrin
5. **Use of *šta* as interrogative** — distinguishes from Croatian (*što*)

### Moderate Bosnian Indicators (supporting evidence)

6. **International terminology over Slavic neologisms** (*univerzitet* not *sveučilište*, *historija* not *povijest*, *hemija* not *kemija*, *muzika* not *glazba*) — leans Bosnian over Croatian
7. **Preference for *sa* with instrumental** — more consistent in Bosnian
8. **Specific vocabulary items:** *hiljada* (thousand, vs. Croatian *tisuća*), *sedmica* (week, vs. Croatian *tjedan*), *tačka* (point, vs. Croatian *točka*)

### Weak Indicators (context-dependent)

9. **Topic and domain:** Texts about Bosnian geography, institutions (e.g., *Federacija Bosne i Hercegovine*, *kanton*, *Visoko predstavnik*), culture, or religion may signal Bosnian by content rather than purely linguistic features.
10. **Proper nouns and place names:** References to Bosnian cities (*Sarajevo, Mostar, Tuzla, Zenica, Banja Luka*) and institutions suggest Bosnian context.

### Combined Feature Scoring

For computational LID, a weighted combination yields the best results:

- **Ijekavian + Turkish loanwords** = very high Bosnian probability
- **Ijekavian + Slavic neologisms (e.g., *sveučilište*)** = Croatian
- **Ekavian + any features** = Serbian
- **Ijekavian + ś/ź** = Montenegrin
- **Ijekavian + Turkish loanwords + h-retention + *šta*** = near-certain Bosnian

### Challenges

1. Short texts provide insufficient evidence for reliable discrimination.
2. Code-switching and borrowing between the four varieties is common in informal text.
3. Many words are identical across all four standards.
4. Domain-specific texts (science, technology) tend to converge across standards.
5. Social media and informal writing often uses a mixed or supraregional style.
6. Diaspora speakers may use hybrid forms.
7. Historical texts (pre-1990s) were labeled Serbo-Croatian and may not align with any single modern standard.
