# Tamil vs confusable languages

Tamil has its own Unicode block (`U+0B80–U+0BFF`), so **script detection alone disambiguates Tamil from all non-Tamil-script languages**. The real work is distinguishing it typologically from the other three Dravidian languages in CommonLID (Telugu, Malayalam, Kannada) and, for OCR/mojibake cases, identifying it despite visual confusion.

## vs Malayalam (mal)

- Malayalam uses script block U+0D00–U+0D7F; visually far more ligature-dense and rounded.
- Malayalam has the **chillu letters ൻ ൾ ർ ൽ ൺ** (pure consonants without visible virama); Tamil never has these.
- Malayalam preserves the full Sanskrit voiced/aspirated stop series (ഗ ഘ ദ ധ etc.); Tamil does not.
- Both share conceptual cognates ழ / ഴ, ள / ള, ண / ണ, but the host scripts look nothing alike.

## vs Telugu (tel) and Kannada (kan)

- Different Unicode block entirely (tel: U+0C00–U+0C7F, kan: U+0C80–U+0CFF).
- Telugu/Kannada letters have rounded top-arcs and cursive curls (*talakattu*/headmark); Tamil letters are more angular and open, without headmarks.
- Both tel and kan keep the full voiced/aspirated stop contrast (four-way series per place); Tamil has only one stop per place.

## vs Sinhala, Devanagari, Gujarati, etc.

All live in different Unicode blocks. The **presence of ழ (U+0BB4) is a near-unique giveaway for Tamil** — no other widely-used language uses this character.

## Diglossia and register cues

Formal/literary Tamil (books, news headlines) uses longer suffix chains and third-person neuter `-ஆது` negation; colloquial blog/social-media Tamil collapses forms (`இருக்கிறது → இருக்கு`) and borrows heavily from English. Both are still Tamil — the script block is the decisive signal.
