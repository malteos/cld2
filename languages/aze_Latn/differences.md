# Azerbaijani (macro) vs confusable languages

Closest confusables: Turkish (tur), North Azerbaijani (azj), Turkmen
(tuk), Crimean Tatar (crh).

## aze ↔ tur (Turkish)

- `ə` is the main diagnostic — Azerbaijani uses it pervasively; Turkish
  never does.
- `q` and `x` in native words (*qardaş, xoş*) are Azerbaijani;
  Turkish uses `k` / `h` in the cognates.
- Azerbaijani dative `-ə` vs Turkish `-e`; Azerbaijani locative `-də`
  vs Turkish `-de` (similar but driven by different harmony sets).

## aze (macro) ↔ azj (North Azerbaijani)

- In practice the macrocode `aze` often mixes modern `azj` Latin
  text with archaic 1992–1993 forms (occasional `ä`, apostrophes in
  Arabic loans, older hyphenation). Pure-`azj` corpora tend to be
  uniformly post-1993.
- Both share the schwa `ə`, `q`, `x`, and identical core morphology;
  treat as the same language for LID unless the downstream task
  demands dialect split.

## aze ↔ tuk (Turkmen)

- Turkmen has `ä ý ň ž`, not present in Azerbaijani.
- Azerbaijani has `ə q x`, not present in Turkmen.
- Turkmen writes long vowels doubled (*aalym*); Azerbaijani does
  not.

## aze ↔ crh (Crimean Tatar)

- Crimean Tatar has `ñ`; Azerbaijani does not.
- Crimean Tatar lacks `ə`; Azerbaijani has it in almost every
  sentence.
