# German (Deutsch) — Latin Script: Language Characteristics

## Unique Characters

German uses the standard Latin alphabet extended with four additional characters that are essential for correct orthography:

- **ä** (a with umlaut) — a fronted variant of /a/, appearing in words such as *Mädchen* (girl), *Ärger* (anger), and *Hände* (hands). It arises historically from an underlying /a/ that was fronted by a following /i/ or /e/ in older stages of the language.
- **ö** (o with umlaut) — a rounded front vowel, found in *schön* (beautiful), *Österreich* (Austria), and *Vögel* (birds). It has no direct equivalent in English and is one of the sounds that most reliably signals German text.
- **ü** (u with umlaut) — a rounded close front vowel, occurring in *über* (over), *Tür* (door), and *grün* (green). Like ö, it is typologically uncommon and a strong identifier of German.
- **ß** (eszett / sharp s) — represents a voiceless /s/ that historically derives from an older /ss/ or /sz/ combination. It appears after long vowels and diphthongs, as in *Straße* (street), *groß* (big), and *Fuß* (foot). Following the 1996 spelling reform, some former ß usages were replaced by *ss* after short vowels (e.g., *dass* instead of *daß*), but ß remains obligatory in many positions.

In digital contexts where these characters are unavailable, the conventional substitutions are ae, oe, ue, and ss respectively. CLD2 must account for both the proper Unicode forms and these ASCII fallbacks.

## Character Frequency

German text shows a character frequency distribution that differs from English in several notable ways. The letter **e** is by far the most frequent, accounting for roughly 16-17% of all letters. It is followed by **n** (approximately 10%), **i** (about 7.5%), **s** (about 7%), **r** (about 7%), **a** (about 6.5%), and **t** (about 6%). The umlauted vowels ä, ö, and ü each appear with a frequency below 1%, but their mere presence is a powerful discriminator between German and other Latin-script languages. The letter ß appears at an even lower frequency (around 0.3%), yet it is virtually unique to German. The letters **q**, **x**, and **y** are rare, mostly confined to loanwords.

Uppercase letters are more frequent in German than in most other Latin-script languages because all nouns are capitalized, not just proper nouns. This capitalization pattern is itself a useful signal for language identification.

## Top 50 Function Words

The most common function words in German, ordered roughly by corpus frequency, are:

der, die, das, und, in, den, von, zu, mit, ist, nicht, ein, eine, sich, auf, für, es, im, dem, dass, er, an, auch, noch, nach, wie, aus, bei, so, was, nur, aber, über, hat, mehr, wenn, dann, als, oder, man, da, vor, am, zum, um, schon, des, bis, war

These words make up a substantial proportion of any running German text. The definite articles alone (der, die, das, dem, den, des) and their frequency across genders and cases are a hallmark of German. The conjunction *und* (and) typically ranks as the single most frequent word in large corpora. Function words such as *nicht* (not), *sich* (reflexive pronoun), and *dass* (that, conjunction) are strong discriminators because they differ markedly from their counterparts in closely related languages like Dutch or Danish.

## Common Bigrams and Trigrams

German text is characterized by several high-frequency bigrams:

**en**, **er**, **ch**, **de**, **ei**, **te**, **in**, **ie**, **nd**, **ge**

The bigram **en** is especially dominant because it serves as the infinitive ending for almost all German verbs (e.g., *machen*, *gehen*, *sprechen*) and also marks many plural nouns. The bigram **ch** is distinctive because it maps to the palatal fricative /ç/ (after front vowels) or the velar fricative /x/ (after back vowels), sounds that are characteristic of German phonology. The bigram **ei** represents the diphthong /aɪ/ and appears with high frequency.

Common trigrams include:

**sch**, **ein**, **der**, **die**, **und**, **den**

The trigram **sch** is particularly important for language identification. It represents the single phoneme /ʃ/ and appears at the beginning of many common words (*Schule*, *schön*, *Schrift*), within words (*Mensch*, *Tisch*, *wünschen*), and is far more frequent in German than the same sequence in most other languages. The trigrams **der**, **die**, and **und** simply reflect the extreme frequency of these function words.

## Morphological Patterns

German morphology is richly inflectional and highly productive in derivation.

### Verb Endings

German verbs are conjugated for person and number. The most common endings are:

- **-en** — infinitive form and first/third person plural (*wir machen*, *sie gehen*)
- **-t** — third person singular present tense (*er macht*, *sie geht*) and past participle marker (*gemacht*, *gesagt*)
- **-st** — second person singular (*du machst*, *du gehst*)
- **-e** — first person singular (*ich mache*, *ich gehe*)

The infinitive ending **-en** is the single largest contributor to the high frequency of the *en* bigram.

### Noun Suffixes

German uses a set of productive derivational suffixes to form nouns from verbs, adjectives, and other nouns:

- **-ung** — forms feminine nouns from verbs, indicating a process or result (*Bildung* from *bilden*, *Bedeutung* from *bedeuten*, *Wohnung* from *wohnen*)
- **-keit** — forms feminine abstract nouns from adjectives, often those ending in -ig or -lich (*Möglichkeit*, *Schwierigkeit*, *Einsamkeit*)
- **-heit** — forms feminine abstract nouns from adjectives (*Freiheit*, *Schönheit*, *Gesundheit*)
- **-schaft** — forms feminine collective or abstract nouns (*Gesellschaft*, *Wissenschaft*, *Freundschaft*)

### Adjective Suffixes

- **-lich** — forms adjectives meaning "having the quality of" (*freundlich*, *herzlich*, *möglich*), comparable to English *-ly* in its adjectival sense
- **-isch** — forms adjectives often from proper nouns or foreign roots (*europäisch*, *politisch*, *historisch*), comparable to English *-ish* or *-ic*

These suffixes stack and combine with great regularity, producing long but fully transparent derived forms.

## Compound Word Formation

One of the most distinctive features of German is its ability to form compound words by concatenating nouns, adjectives, and other word classes without spaces. This process is essentially unlimited in productivity and can produce words of arbitrary length:

- *Handschuh* (hand + shoe = glove)
- *Krankenhaus* (sick + house = hospital)
- *Bundesrepublik* (federal + republic)
- *Lebensversicherungsgesellschaft* (life + insurance + company)
- *Rindfleischetikettierungsüberwachungsaufgabenübertragungsgesetz* (a famous example of an extremely long compound from legal language)

Compounds are typically written as a single word with no spaces or hyphens. The final component (the head) determines the gender and plural form of the entire compound. An optional linking element (Fugenelement) such as **-s-**, **-n-**, **-en-**, or **-er-** may appear between components (*Arbeit**s**platz*, *Sonne**n**schein*).

For language detection, the high average word length that results from compounding is a useful statistical feature. German text tends to have a noticeably higher mean word length than English, Dutch, or the Scandinavian languages. The presence of very long tokens (15+ characters) that are nonetheless common, correctly spelled words is a strong signal pointing to German.
