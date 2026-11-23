# Distinguishing Kannada (kan_Knda) from Confusable Languages

Kannada belongs to the Dravidian language family and is written in its own script, which descends from the Kadamba and Chalukya scripts. Because of shared ancestry and regional contact, several South Indian languages can appear superficially similar. This document describes the distinguishing features that separate Kannada from the languages most likely to be confused with it.

---

## 1. Telugu (tel_Telu)

Kannada and Telugu scripts share a common ancestor in the old Telugu-Kannada script and consequently display similar rounded, curvilinear letterforms. This makes them the most frequently confused pair in automated language identification.

**Script differences.** Despite the visual resemblance, specific characters differ clearly. Kannada uses distinctive forms such as **ಕ**, **ಗ**, and **ದ**, whereas the Telugu equivalents **క**, **గ**, and **ద** have noticeably different stroke patterns, particularly in the placement and shape of the headstroke. Telugu letters tend to have a more prominent horizontal top bar, while Kannada letterforms are rounder and more self-contained. The Kannada vowel signs also attach differently to consonants compared to Telugu.

**Visarga usage.** Telugu text exhibits a higher frequency of the visarga character (ః), especially in formal and literary registers, whereas Kannada uses visarga (ಃ) more sparingly.

**Vocabulary.** Although both languages share Dravidian roots, Telugu has absorbed a larger proportion of Sanskrit loanwords in certain registers, including administrative and literary contexts. Common function words differ substantially: for instance, Kannada uses "ಮತ್ತು" (and) while Telugu uses "మరియు" or "మరి."

---

## 2. Tamil (tam_Taml)

Tamil script is visually quite different from Kannada, making script-level confusion less common, but at the language level the two share Dravidian heritage and some cognate vocabulary.

**Script differences.** Tamil script is noticeably more angular and compact than Kannada. Tamil has a smaller consonant inventory in its script -- it lacks dedicated symbols for aspirated consonants (kha, gha, cha, jha, etc.) that Kannada represents explicitly. Tamil uses only 18 consonant graphemes compared to Kannada's 34.

**Morphological markers.** The plural suffix in Tamil is **-கள்** (-kal), whereas Kannada uses **-ಗಳು** (-galu). Case marker suffixes also differ: Tamil locative is **-இல்** (-il) while Kannada uses **-ಅಲ್ಲಿ** (-alli). These endings provide strong diagnostic signals when identifying short text fragments.

**Shared roots, different forms.** Many basic vocabulary items descend from common Proto-Dravidian roots but have diverged significantly. For example, "water" is "நீர்" (niir) in Tamil and "ನೀರು" (niiru) in Kannada -- recognizably related but phonologically and orthographically distinct.

---

## 3. Malayalam (mal_Mlym)

Malayalam, spoken primarily in Kerala, is another Dravidian language whose script occasionally causes confusion with Kannada due to its rounded appearance.

**Script differences.** Malayalam script features highly rounded, flowing letterforms with frequent use of complex conjunct consonants (ligatures combining two or more consonants). The overall density of Malayalam text tends to be higher because of these conjuncts. Kannada script, while also rounded, uses conjunct forms less aggressively and has a more open, spacious look on the page.

**Character distinctions.** The Malayalam chi (ചി) and cha (ച) characters have distinctive shapes that differ clearly from Kannada equivalents like ಚಿ and ಚ. The Malayalam ra (ര) and la (ല) forms are also immediately distinguishable from Kannada ರ and ಲ.

**Vocabulary.** Despite both being Dravidian languages, Malayalam has been heavily influenced by Sanskrit in its formal registers and by Arabic and Portuguese in its colloquial vocabulary due to historical trade contacts. Kannada vocabulary, while also bearing Sanskrit influence, shows different patterns of borrowing and retains more native Dravidian forms in everyday speech.

---

## 4. Diagnostic Features for Identifying Kannada

When attempting to positively identify text as Kannada, the following features are most reliable.

**Unique script characters.** The presence of characters that are unmistakably Kannada script provides the strongest signal. Key characters include **ಕ**, **ಗ**, **ಜ**, **ಟ**, **ಡ**, **ಣ**, **ತ**, **ದ**, **ನ**, **ಪ**, **ಬ**, **ಮ**, **ಯ**, **ರ**, **ಲ**, **ವ**, **ಶ**, **ಷ**, **ಸ**, and **ಹ**. The Unicode block for Kannada (U+0C80 to U+0CFF) is distinct from Telugu (U+0C00 to U+0C7F), Tamil (U+0B80 to U+0BFF), and Malayalam (U+0D00 to U+0D7F), making codepoint-based detection straightforward for digital text.

**Common word endings.** Kannada text frequently exhibits characteristic suffixes:
- **-ಅಲ್ಲಿ** (-alli): locative case marker ("in" or "at")
- **-ಆಗಿ** (-aagi): adverbial suffix ("as" or "having become")
- **-ಎಂದು** (-endu): quotative marker ("that" in reported speech)

**Anusvara frequency.** Kannada makes heavy use of the anusvara (**ಂ**) to indicate nasalization. It appears with high frequency in ordinary prose, more so than in Telugu or Tamil. Words like "ಹಂಬಲ" (desire), "ಸಂಗೀತ" (music), and "ಮಂಗಳ" (auspicious) illustrate this pattern.

**Verb endings.** Kannada finite verbs carry tense-person-number suffixes that are distinctive to the language:
- **-ಆರು** (-aaru): third person plural marker in some dialects
- **-ಆಳು** (-aalu): feminine third person singular in colloquial usage
- **-ಇತು** (-itu): neuter past tense marker
- **-ಆಗಿದೆ** (-aagide): present perfect ("has become" or "is")

These verb endings rarely overlap with those of Telugu, Tamil, or Malayalam, making them reliable discriminators in language identification tasks.

---

## Summary

The most dependable method for distinguishing Kannada from its confusable neighbors combines script-level codepoint analysis with morphological pattern matching. Script detection alone separates Kannada from Tamil and Malayalam with high accuracy. Distinguishing Kannada from Telugu, however, benefits from examining characteristic suffixes, verb endings, and anusvara frequency alongside the script-level features.
