# Distinguishing Dhivehi from Similar Languages

## Dhivehi vs. Sinhalese (Sinhala)

Sinhalese is the closest genetic relative of Dhivehi, both belonging to the Insular Indo-Aryan branch. Despite their shared ancestry from Elu Prakrit, the two languages have diverged substantially and are not mutually intelligible.

### Script Differences
The most immediate distinguishing feature is the writing system. Sinhalese uses the Sinhala script, a left-to-right Brahmi-derived abugida with rounded letterforms. Dhivehi uses the Thaana script, a right-to-left system derived from Arabic numerals. The two scripts share no visual similarity whatsoever, making them instantly distinguishable in written form.

### Phonological Differences
While both languages share certain Indo-Aryan phonological features such as retroflex consonants, Dhivehi has developed prenasalized stops (/mb/, /nd/, /ɳɖ/, /ŋɡ/) that are more prominent than in Sinhalese. Dhivehi also lacks the breathy voiced (aspirated) stops that Sinhalese preserves from older Indo-Aryan. The Dhivehi vowel system is more reduced compared to Sinhalese.

### Vocabulary Differences
Dhivehi has extensive Arabic and Persian loanwords due to centuries of Islamic influence, whereas Sinhalese has more Pali and Sanskrit-derived vocabulary reflecting its Buddhist cultural heritage. Modern Dhivehi borrows heavily from English for technical terms, while Sinhalese often creates neologisms from Pali/Sanskrit roots. Common everyday vocabulary has diverged significantly, though cognates are recognizable to comparative linguists.

### Grammatical Differences
Both languages are SOV, but they differ in specific morphological patterns. Dhivehi has a productive focus-verb system that, while shared with Sinhalese in origin, has developed independently. The case suffix systems differ in specific forms, and the verb conjugation paradigms have diverged considerably.

## Dhivehi vs. Arabic

Arabic and Dhivehi are entirely unrelated genetically (Arabic is Semitic; Dhivehi is Indo-Aryan), but the Thaana script's right-to-left directionality and diacritical vowel marking can cause superficial confusion.

### Script Distinctions
- **Non-cursive vs. cursive:** Thaana letters stand independently and never connect, while Arabic is fundamentally a cursive script where letters join within words.
- **Thaana-specific characters:** Letters such as ށ, ޅ, ޏ, ޑ, ޓ, ޕ, ޖ, and ޗ have no counterparts in the Arabic alphabet. Their presence in text definitively identifies it as Thaana.
- **Mandatory diacritics:** Every consonant in Thaana carries a visible vowel diacritic or sukun. Arabic text in practice omits most diacritics.
- **Letter shapes:** Thaana letters are generally simpler and more geometric. Arabic calligraphic tradition produces more complex, flowing forms.
- **No ligatures:** Thaana has no ligatures, while Arabic has several mandatory ones (e.g., lam-alif).

### Linguistic Distinctions
- Arabic is a root-and-pattern (templatic) morphology language; Dhivehi is agglutinative with suffixing morphology.
- Arabic distinguishes grammatical gender throughout its system; Dhivehi has no grammatical gender.
- Arabic has pharyngeal and emphatic consonants that are phonemic in the language itself; Dhivehi only uses them (imperfectly) in Arabic loanwords.
- Word order differs: Arabic is primarily VSO; Dhivehi is SOV.

### Loanword Layer
Dhivehi contains many Arabic loanwords, particularly in religious, legal, and administrative domains. These words are adapted to Dhivehi phonology and morphology and take Thaana spelling. Their presence can confuse naive text classifiers, but the grammatical structure surrounding them remains entirely Dhivehi.

## Dhivehi vs. Urdu

Urdu, written in the Nastaliq variant of the Perso-Arabic script, can be confused with Thaana by systems that rely primarily on Unicode range detection or superficial visual analysis.

### Script Distinctions
- **Nastaliq vs. Thaana:** Urdu's Nastaliq style features a distinctive slanting, flowing calligraphic style entirely absent from Thaana's upright, disconnected letterforms.
- **Connected vs. disconnected:** Like Arabic, Urdu letters connect within words. Thaana letters never connect.
- **Character inventory:** Urdu has specific modified Arabic letters (e.g., ٹ, ڈ, ڑ, ں, ے, ھ) that do not appear in Thaana, and Thaana has letters (ށ, ޅ, ޏ, ޑ, ޓ) not found in Urdu.
- **Unicode ranges:** Urdu text primarily uses the Arabic Unicode block (U+0600-U+06FF) with some characters in the Arabic Supplement block. Thaana uses its own block (U+0780-U+07BF).

### Linguistic Distinctions
- Urdu has grammatical gender (masculine/feminine); Dhivehi does not.
- Urdu uses postpositions like Dhivehi, but its verb agreement system (agreeing with gender and number) differs markedly.
- Urdu vocabulary draws heavily from Persian and Arabic but also from Sanskrit/Prakrit and Turkish; Dhivehi vocabulary draws from Arabic, English, and its Indo-Aryan heritage.
- The phonological systems overlap significantly due to shared Indo-Aryan heritage and Arabic influence, but Dhivehi's prenasalized stops and retroflex lateral are absent from Urdu.

## Diagnostic Summary for Language Identification

The following features are most reliable for identifying Dhivehi text:

1. **Unicode range U+0780-U+07BF:** Presence of characters in the Thaana block is definitive.
2. **Non-cursive RTL text with mandatory diacritics:** This combination is unique to Thaana.
3. **Presence of Thaana-only letters:** ށ, ޅ, ޏ are found in no other script.
4. **Sentence-final patterns:** Dhivehi sentences characteristically end with verb forms containing sequences like -ެވެ, -ށެވެ, -ައެވެ.
5. **High frequency of postpositional case markers:** ގައި, އަށް, ގެ, އިން appearing frequently throughout text.
6. **Absence of cursive connections between letters** within words, distinguishing from Arabic and Urdu.
