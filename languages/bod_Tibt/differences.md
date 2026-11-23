# Tibetan vs. Confusable Languages (bod_Tibt)

## Overview of Confusable Languages

Several languages use the Tibetan script (or closely related scripts), making script-based identification insufficient for distinguishing Tibetan from these related languages. The primary confusable languages are:

1. **Dzongkha (dzo)** — National language of Bhutan
2. **Ladakhi (lbj)** — Spoken in Ladakh, India
3. **Balti (bft)** — Spoken in Baltistan (Pakistan/India)
4. **Sherpa (xsr)** — Spoken in Nepal
5. **Sikkimese/Bhutia (sip)** — Spoken in Sikkim, India
6. **Classical Tibetan (xct)** — Historical literary language

All of these languages belong to the Tibetic branch of Sino-Tibetan and use the Tibetan script, though with varying orthographic conventions and vocabulary.

## Tibetan vs. Dzongkha (dzo)

Dzongkha is the most important confusable language because it is a national language with substantial digital presence and uses the same Tibetan script.

### Vocabulary Differences

Dzongkha has borrowed extensively from different sources than Standard Tibetan:

- **Dzongkha-specific vocabulary:** Dzongkha uses many words not found in Standard Tibetan or uses common Tibetan words with different meanings. Examples:
  - "country": Dzongkha རྒྱལ་ཁབ (rgyal khab) vs. Tibetan ཡུལ (yul) or རྒྱལ་ཁབ
  - "government": Dzongkha ཞུང (gzhung) vs. Tibetan གཞུང (gzhung) — same word but different conventional spelling
  - "thank you": Dzongkha ཀ་དིན་ཆེ (ka din che) vs. Tibetan ཐུགས་རྗེ་ཆེ (thugs rje che)

- **Loanword sources:** Dzongkha borrows more from Hindi/Nepali and English for modern concepts, while Tibetan borrows more from Chinese (Mandarin) and creates neologisms from Classical Tibetan roots.
  - "telephone": Dzongkha ཁ་པར (kha par) vs. Tibetan ཁ་པར (kha par) — same in this case
  - "computer": Dzongkha ཀམ་པིའུ་ཊར (kampiutar, from English) vs. Tibetan གློག་ཀླད (glog klad, native coinage)

### Spelling Conventions

Dzongkha orthography differs from Tibetan in several systematic ways:

- **Simplified clusters:** Dzongkha writing sometimes simplifies consonant clusters differently than Tibetan.
- **Roman transliteration conventions:** Dzongkha uses a different official romanization system (based on pronunciation) compared to Wylie transliteration used for Tibetan.
- **Prefix conventions:** Some Dzongkha words use different prefixes than their Tibetan cognates.

### Particle Differences

While many grammatical particles are shared, there are differences in usage frequency and form:

- **Quotative particles:** Dzongkha uses ཟེར (zer) more frequently in certain constructions where Tibetan might use ཅེས (ces) or ཞེས (zhes).
- **Aspectual markers:** Dzongkha has developed some distinct aspectual constructions not found in Standard Tibetan.
- **Sentence-final particles:** Some Dzongkha sentence-final particles differ from their Tibetan counterparts. Dzongkha more frequently uses མས (mas) as a question particle, while Tibetan uses པས (pas).

### Diagnostic Features for Tibetan vs. Dzongkha

High-confidence indicators of **Tibetan** (not Dzongkha):
- Presence of Chinese loanwords (transliterated into Tibetan script)
- Use of distinctly Tibetan honorific forms (གསུངས, མཛད, ཕེབས in typical Tibetan patterns)
- Reference to Tibet-specific place names (ལྷ་ས, ཨ་མདོ, ཁམས, དབུས་གཙང)
- Tibetan-specific modern vocabulary coined from Classical Tibetan roots (e.g., གློག་ཀླད for "computer," འཕྲིན་སྐྱེལ for "message/communication")
- Sentence patterns using བྱུང (byung) and སོང (song) in characteristically Tibetan evidential constructions

High-confidence indicators of **Dzongkha** (not Tibetan):
- Dzongkha-specific vocabulary and expressions (ཀུ་ཟུ་བཟང་པོ "hello/how are you")
- Reference to Bhutanese place names (ཐིམ་ཕུག/Thimphu, སྤ་རོ/Paro, སྤུ་ན་ཁ/Punakha)
- Hindi/Nepali loanwords transliterated into Tibetan script
- Specific Dzongkha grammatical constructions and sentence-final markers
- Reference to Bhutanese institutions (རྒྱལ་འཛིན "Gyaltsuen/Queen," འབྲུག་རྒྱལ "Druk Gyalpo/King of Bhutan")

## Tibetan vs. Ladakhi (lbj)

Ladakhi is spoken in the Ladakh region of India and uses the Tibetan script for writing. Key differences:

- **Phonological innovations:** Ladakhi has undergone different sound changes than Central Tibetan, and some of these are reflected in spelling.
- **Vocabulary:** Ladakhi has significant borrowings from Urdu, Hindi, and Persian that are absent in Standard Tibetan.
- **Archaic features:** Ladakhi preserves some archaic Tibetan features lost in Central Tibetan.
- **Diagnostic terms:** Ladakhi-specific words like ཇུ་ལེ (ju le, "hello/thank you/goodbye") are strong indicators.
- **Place names:** Reference to Ladakhi locations (ལེ/Leh, སྐར་རྡོ/Kargil) indicates Ladakhi.

## Tibetan vs. Balti (bft)

Balti is spoken in Baltistan (Gilgit-Baltistan, Pakistan, and parts of Ladakh, India). While traditionally written in Tibetan script, modern Balti increasingly uses a modified Urdu/Arabic script. When written in Tibetan script:

- **Archaic orthography:** Balti preserves very conservative spelling that reflects Old Tibetan pronunciation more closely than any other living Tibetic language.
- **No tonal distinctions:** Like Amdo Tibetan, Balti lacks tones.
- **Extensive Persian/Arabic/Urdu loanwords:** Especially for Islamic religious terminology and modern concepts, reflecting the predominantly Muslim population.
- **Diagnostic:** The combination of Tibetan script with Islamic vocabulary (Allah, mosque, etc. transliterated in Tibetan letters) strongly indicates Balti.

## Tibetan vs. Classical Tibetan (xct)

Classical Tibetan is the literary language of the Tibetan Buddhist canon and traditional scholarship:

- **Vocabulary:** Classical Tibetan uses many archaic terms and Buddhist technical vocabulary not common in modern Tibetan.
- **Grammar:** Classical Tibetan preserves the full four-stem verb system and uses more complex case particle patterns.
- **Content markers:** Texts in Classical Tibetan typically deal with Buddhist philosophy, ritual, medicine, or astrology and contain extensive Sanskrit-derived terminology.
- **Diagnostic:** Heavy use of Sanskrit transliterations, Buddhist technical terms, and archaic grammatical constructions indicates Classical Tibetan rather than modern Standard Tibetan.

## Summary of Diagnostic Strategy

For LID purposes, distinguishing Tibetan from other Tibetan-script languages requires a multi-layered approach:

1. **Script detection:** Confirm Tibetan script (U+0F00-U+0FFF) — this narrows to the Tibetic language family.
2. **Lexical analysis:** Check for language-specific vocabulary, loanword patterns, and place names.
3. **Particle analysis:** Examine grammatical particles and sentence-final markers for language-specific patterns.
4. **Content analysis:** Consider the domain and content for clues (Buddhist philosophy suggests Classical Tibetan; Bhutanese institutions suggest Dzongkha; modern news from Tibet suggests Standard Tibetan).
5. **Bigram/trigram analysis:** Character and syllable n-gram frequencies differ across Tibetic languages due to different vocabulary distributions.
