# Thai vs. confusable languages

## tha ↔ lao (not in this 8-language set, but worth noting)

- Thai script (U+0E00–U+0E7F) and Lao script (U+0E80–U+0EFF) occupy adjacent Unicode blocks and are visually related. Disambiguation is by block membership at the codepoint level — a single char decides. No Lao chars in Thai text, and vice versa.

## tha ↔ any other CommonLID language

- **Unique script**: Thai script does not appear in any other language in this set. A document with ≥1 character in U+0E00–U+0E7F is Thai with very high precision. No confusion with Mandarin, Cantonese, Wu, Japanese, Korean, or Vietnamese is possible at the script level.
- **No spaces** inside sentences distinguishes Thai from Vietnamese (which uses Latin with spaces) and from Korean (which uses Hangul with spaces). Chinese and Japanese also lack inter-word spaces, but their scripts are entirely distinct from Thai.

## tha ↔ vie — Thai vs Vietnamese

- Scripts are entirely different: Thai (Thai script) vs Vietnamese (Latin with diacritics). No overlap.
- Both are SVO, analytic, tonal Southeast Asian languages typologically, but orthographically they are instantly distinguishable.

## Near-ambiguity edge cases

- Very short strings consisting only of Arabic digits or Latin brand names embedded in a Thai document can be mis-classified. Even a single Thai codepoint in the surrounding context is sufficient to identify.
- Transliterated Thai in Latin (Royal Thai General System) is outside `tha_Thai` scope.
