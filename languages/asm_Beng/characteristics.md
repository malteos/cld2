# Assamese (asm_Beng) - Identification Characteristics

## Critical Script Diagnostic: Assamese vs Bengali

The single most important feature for identifying Assamese text versus Bengali text is the presence of **two script-level characters unique to Assamese**:

### ৰ (Assamese Ra) - Unicode U+09F0
- This is the standard letter for the /r/ sound in Assamese
- Bengali uses র (U+09B0) instead
- **Any text containing ৰ (U+09F0) is almost certainly Assamese, not Bengali**
- This character appears with extremely high frequency in Assamese text

### ৱ (Assamese Wa/Va) - Unicode U+09F1
- Used for the /w/ or /v/ sound in Assamese
- This character does **not exist** in Bengali at all
- **Presence of ৱ is a definitive marker of Assamese text**
- Less frequent than ৰ but still common

### Detection Rule
If a text in Eastern Nagari script contains ৰ (U+09F0) or ৱ (U+09F1), classify it as Assamese. If it uses র (U+09B0) for the /r/ sound exclusively and lacks ৱ, it is more likely Bengali.

## Character Frequency Profile

The following characters appear most frequently in Assamese text (ranked by approximate frequency):

1. **া** (aa matra) - most common vowel sign
2. **ৰ** (Assamese ra) - extremely frequent, key diagnostic
3. **ে** (e matra)
4. **ি** (i matra)
5. **ক** (ka)
6. **ত** (ta)
7. **ন** (na)
8. **স** (sa)
9. **ম** (ma)
10. **আ** (aa)
11. **ল** (la)
12. **প** (pa)
13. **হ** (ha)
14. **য** (ya)
15. **ো** (o matra)
16. **দ** (da)
17. **ব** (ba)
18. **গ** (ga)
19. **ৱ** (Assamese wa) - diagnostic character
20. **অ** (a)

## Top 50 Function Words

These are the most common function words and high-frequency content words in Assamese, essential for language identification:

| Rank | Word | Transliteration | Translation/Function |
|------|------|----------------|---------------------|
| 1 | আৰু | aru | and |
| 2 | এই | ei | this |
| 3 | তাৰ | tar | his/her/its |
| 4 | কৰি | kori | having done |
| 5 | হৈছে | hoise | has become |
| 6 | নাই | nai | not/no |
| 7 | এক | ek | one |
| 8 | বা | ba | or |
| 9 | যে | je | that (conjunction) |
| 10 | তেওঁ | teo | he/she (honorific) |
| 11 | মই | moi | I |
| 12 | আমাৰ | amar | our |
| 13 | এটা | eta | one (classifier) |
| 14 | হয় | hoy | is/yes |
| 15 | কৰা | kora | to do/doing |
| 16 | লৈ | loi | having taken/towards |
| 17 | সেই | xei | that |
| 18 | মোৰ | mor | my |
| 19 | তেওঁলোক | teolok | they |
| 20 | পৰা | pora | from/having fallen |
| 21 | বাবে | babe | because/for |
| 22 | আছে | ase | is/exists |
| 23 | নহয় | nohoy | is not |
| 24 | কিন্তু | kintu | but |
| 25 | ইয়াত | iyat | here |
| 26 | দৰে | dore | like |
| 27 | কাৰণে | karone | because |
| 28 | যদি | jodi | if |
| 29 | তাত | tat | there |
| 30 | সকলো | xokolo | all |
| 31 | ইয়াৰ | iyar | of this |
| 32 | প্ৰতি | proti | towards/each |
| 33 | বুলি | buli | saying/called |
| 34 | হৈ | hoi | having become |
| 35 | দুটা | duta | two (classifier) |
| 36 | আছিল | asil | was |
| 37 | তেখেত | tekhet | he/she (very respectful) |
| 38 | কোনো | kunu | some/any |
| 39 | যিটো | jito | which one |
| 40 | মাজত | majot | among/in the middle |
| 41 | বহুত | bohut | very/much |
| 42 | ওপৰত | oporot | on top/above |
| 43 | লগতে | logte | along with |
| 44 | যেতিয়া | jetia | when |
| 45 | তেতিয়া | tetia | then |
| 46 | ওচৰত | osorot | near |
| 47 | অতি | oti | very/extremely |
| 48 | নতুন | notun | new |
| 49 | আগত | agot | before/in front |
| 50 | পিছত | pisot | after/behind |

## Common N-grams

### Character Bigrams (most frequent)
- াৰ (ar) - extremely common, part of genitive -ৰ
- কৰ (kor) - from the verb কৰ- "to do"
- ৰে (re) - instrumental marker
- তে (te) - locative forms
- ীয (iya) - adjectival suffix
- ছে (se) - present perfect ending
- িত (it) - locative forms
- ান (an) - common syllable
- িক (ik) - suffix pattern

### Character Trigrams
- াৰে (are) - instrumental
- কৰি (kori) - conjunctive participle
- িলে (ile) - past tense/conditional
- ৰাজ (raj) - "king/rule"
- হৈছ (hois) - perfect tense marker
- মান (man) - common in words
- পৰা (pora) - "from"

### Word Bigrams
- আৰু তেওঁ (aru teo, "and he/she")
- কৰি আছে (kori ase, "is doing")
- হৈ আছে (hoi ase, "has become")
- তাৰ পিছত (tar pisot, "after that")
- লগতে আৰু (logte aru, "along with and")

## Morphological Patterns for Identification

### Verb Endings (distinctive patterns)
- **-ছে / -ছোঁ / -ছা** : present perfect markers
- **-িলে / -িলোঁ / -িলা** : simple past markers
- **-িব / -িম** : future tense markers
- **-ওঁ** (with chandrabindu) : first person endings

### Classifier Suffixes (diagnostic)
- **-জন / -জনী** : human classifiers
- **-গৰাকী** : respectful human classifier
- **-খন** : flat object classifier
- **-টো / -টা** : general classifiers

### Postpositional Markers
- **-ৰ** : genitive marker (very high frequency, uses Assamese ৰ)
- **-ত** : locative marker
- **-লৈ** : dative/directional marker
- **-ক** : accusative marker
- **-ৰে** : instrumental marker

### Common Suffixes
- **-মান / -মানে** : honorific plural
- **-বোৰ / -বিলাক** : plural markers
- **-সকল** : respectful plural
- **-ঈয়া / -ৱা** : adjectival/demonym suffix

## Additional Identification Signals

### Unique Vocabulary Items
Certain words are characteristic of Assamese and not commonly found in Bengali:
- **বৰ** (bor, "very/great") - extremely common intensifier
- **নেকি** (neki, question particle)
- **বুলি** (buli, "saying/that" - quotative)
- **যেনে** (jene, "so that")
- **কেনে** (kene, "how")
- **অলপ** (olop, "a little")

### Chandrabindu (ঁ) Usage
Assamese uses the chandrabindu (nasalization marker) distinctively in first-person verb forms: কৰোঁ, যাওঁ, খাওঁ. This pattern of nasalized first-person endings is characteristic.

### The Quotative বুলি (buli)
The word বুলি as a quotative marker ("saying/called") is a distinctive Assamese feature not found in Bengali, where বলে (bole) is used instead.
