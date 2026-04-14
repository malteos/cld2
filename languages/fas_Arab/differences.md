# Persian vs confusable languages

Persian shares the Arabic script with Arabic, Urdu and Southern Uzbek; all surface differences in CommonLID must be script-level.

## fas vs Arabic (ara)

- Presence of **پ چ ژ گ** → fas (or urd / uzs), never ara.
- Persian uses **ک** U+06A9 and **ی** U+06CC; Arabic uses **ك** U+0643 and **ي** U+064A.
- Persian function words و، در، به، از، که، این، است have no Arabic cognates of the same form.
- Persian lacks the Arabic definite article **ال‍** fused onto nouns.

## fas vs Urdu (urd)

- Urdu adds retroflex letters **ٹ ڈ ڑ** and a distinct final **ہ** (U+06C1) versus Persian **ه** (U+0647). Their presence indicates urd.
- Urdu uses the sentence-final full stop **۔** (U+06D4); Persian uses `.`.
- Common Urdu function words **کی، کے، کا، ہے، ہیں، میں، نے** have no direct Persian equivalents.
- Persian *ezāfe* kasra **ـِ** does not exist in Urdu.

## fas vs Southern Uzbek (uzs)

- Uzs borrows Perso-Arabic پ چ ژ گ but additionally uses vowel letters **ۉ** (U+06C9) and **ې** (U+06D0) to mark Turkic back/front vowels not present in Persian. Their presence is a strong uzs signal.
- Uzs shows vowel-harmony orthography and Turkic suffixes **ـلر، ـده، ـدن، ـگه** that never occur in Persian.
- Persian *ezāfe* and object marker **را** are absent in uzs.

## fas vs Dari / Tajik

Dari is essentially the same written language as Iranian Persian and is *not* separately tagged in CommonLID — both fall under `fas_Arab`. Tajik is written in Cyrillic (tgk_Cyrl) and so is trivially distinguishable at the script level.
