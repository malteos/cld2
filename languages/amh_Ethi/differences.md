# Amharic (amh_Ethi) - Differences from Confusable Languages

## Overview of Confusable Languages

Because the Ethiopic (Ge'ez/Fidel) script is shared by multiple languages of Ethiopia and Eritrea, script-based detection alone cannot distinguish Amharic from several related languages. The primary confusable languages are:

1. **Tigrinya (tir)** - Very high confusability
2. **Ge'ez (gez)** - Moderate confusability
3. **Tigre (tig)** - Moderate confusability
4. **Harari (har)** - Lower confusability (rarely written in Ethiopic today)
5. **Other Ethiopian Semitic languages** using Ethiopic script (Gurage varieties, Argobba, etc.)

## Amharic vs. Tigrinya (Very Confusable)

Tigrinya is the most confusable language with Amharic. Both are South Ethiopic Semitic languages written in the same Ethiopic script, and they share substantial vocabulary due to common descent from Ge'ez. However, they are not mutually intelligible, and careful analysis reveals consistent differences.

### Function Word Differences

This is the most reliable method for distinguishing the two languages:

| Feature | Amharic | Tigrinya |
|---------|---------|----------|
| "and" | እና (ina) | ን (n) / ውን (wn) |
| "is" (copula masc.) | ነው (new) | እዩ (iyu) |
| "is" (copula fem.) | ናት (nat) | እያ (iya) |
| "they are" | ናቸው (nachew) | እዮም (iyom) |
| "but" | ግን (gin) | ግና (gina) / ግን (gin) |
| "or" | ወይም (weyim) | ወይ (wey) / ወይከ (weyke) |
| "this" (masc.) | ይህ (yih) | እዚ (izi) |
| "that" | ያ (ya) | እቲ (iti) |
| "not" | አይ...ም (ay...m) | አይ...ን (ay...n) |
| "I" | እኔ (ine) | ኣነ (ane) |
| "he" | እሱ (issu) | ንሱ (nisu) |
| "she" | እሷ (isswa) | ንሳ (nisa) |
| "we" | እኛ (igna) | ንሕና (nihna) |
| "you" (m.sg.) | አንተ (ante) | ንስኻ (niskha) |
| "now" | አሁን (ahun) | ሕጂ (hiji) |
| "today" | ዛሬ (zare) | ሎሚ (lomi) |
| "also" | ደግሞ (degmo) | ድማ (dima) / እውን (iwn) |

### Verb Morphology Differences

Amharic and Tigrinya verbs differ significantly in their conjugation patterns:

- **Imperfective prefix vowels:** Amharic uses yi- (ይ-) for 3sg.m; Tigrinya uses yi- but with different suffix patterns
- **Converb/gerundive forms:** Amharic converbs typically end in -o (masc.) or -a (fem.); Tigrinya converbs differ in form
- **Compound tenses:** Amharic uses gerund + ነው/ነበር; Tigrinya uses different auxiliary constructions with ኣሎ (alo) and ነበረ (nebere)
- **Negative marker:** Amharic al-...-m circumfix; Tigrinya ay-...-n circumfix (note the final -n vs. -m)
- **Causative prefix:** Both use a- but with different vowel patterns in derived stems
- **Jussive/imperative forms:** Distinct patterns in the two languages

### Phonological Differences Reflected in Spelling

- Tigrinya preserves the pharyngeal consonants ح (h) and ع (') more distinctly than Amharic
- Tigrinya uses certain Ethiopic characters (especially from the extended set) that are rare or absent in Amharic
- Tigrinya has a more productive gemination system, and certain gemination patterns differ from Amharic

### Structural Markers

- **Genitive prefix:** Both use የ- (ye-), but Tigrinya also uses ናይ (nay) as an independent genitive marker
- **Definite article:** Amharic uses -u/-w (masc.) and -wa/-itu (fem.); Tigrinya uses -ቲ (-ti) and related forms
- **Plural marking:** Amharic -oCH (ኦች); Tigrinya uses -tat (ታት) and -at (ኣት) as common plural suffixes
- **Relative clause formation:** Both use ye- prefixed verbs, but with different conjugation patterns

## Amharic vs. Ge'ez (Moderate Confusability)

Ge'ez is the classical ancestor of Amharic and is still used as a liturgical language of the Ethiopian Orthodox Tewahedo Church. While it uses the same script, Ge'ez is easily distinguished by several features:

- **Ge'ez has VSO word order** (as opposed to Amharic SOV)
- **Ge'ez vocabulary** is largely archaic, and many common Ge'ez words are only found in formal/religious registers of Amharic
- **Ge'ez lacks** many of the grammatical innovations of Amharic: no compound tenses, no converb chaining, simpler auxiliary system
- **Ge'ez texts** are overwhelmingly religious or historical in content
- **Ge'ez verb morphology** is closer to Classical Semitic patterns (prefix conjugation for imperfective, suffix conjugation for perfective) without the Amharic innovations
- **Function words** differ significantly: Ge'ez uses ወ- (we-) for "and," እምነ (imne) for "from," ውስተ (wiste) for "in"

## Amharic vs. Tigre (Moderate Confusability)

Tigre is a North Ethiopic Semitic language spoken primarily in Eritrea. It uses the Ethiopic script (though historically less consistently than Amharic or Tigrinya):

- **Different function words:** Tigre has distinct pronouns, conjunctions, and particles
- **Different copula:** Tigre uses ቱ (tu) for masculine and ታ (ta) for feminine
- **Lower text availability:** Tigre has considerably less written content available than Amharic
- **Arabic influence:** Tigre shows heavier Arabic lexical influence than Amharic due to the Islamic heritage of most Tigre speakers

## Amharic vs. Harari and Other Ethiopian Semitic Languages

Harari, Gurage varieties (Silt'e, Wolane, etc.), and Argobba occasionally appear in Ethiopic script but are very low-resource languages with minimal digital presence. They can be distinguished from Amharic by their unique function words, different verb conjugation patterns, and distinctive vocabulary items not found in Amharic.

## Summary of Best Discriminating Features

For automated language identification, the most reliable features for identifying Amharic among Ethiopic-script languages are:

1. **Copula forms:** ነው (new), ናት (nat), ናቸው (nachew) are strongly Amharic
2. **Conjunction:** እና (ina) for "and" is characteristic of Amharic
3. **Negation pattern:** አይ-...-ም (ay-...-m) is distinctly Amharic (-m vs. Tigrinya -n)
4. **Pronoun forms:** እኔ, እሱ, እሷ, እኛ are Amharic-specific
5. **Plural suffix:** -ኦች (-oCH) is characteristically Amharic
6. **Demonstratives:** ይህ (yih), ያ (ya) vs. Tigrinya እዚ (izi), እቲ (iti)
7. **High frequency of** ደግሞ (degmo, "also"), አሁን (ahun, "now"), ዛሬ (zare, "today")
