# Distinguishing Arabic (ara) from related labels

## Confusable labels

- **arb (Modern Standard Arabic)** — In practice `ara` and `arb` text are
  nearly indistinguishable: `ara` is a macrolanguage tag but, in CommonLID and
  most web corpora, it is dominated by formal MSA content. Prefer `arb` when
  the corpus curator explicitly separates MSA from dialects; otherwise treat
  `ara` as a superset that includes MSA plus uncategorised dialect/mixed text.
- **arz / ary / ars / aeb / apd (dialectal Arabic)** — `ara` should lack strong
  dialectal markers: no Egyptian negation *مش*, no Maghrebi pre-verbal *كـ/
  تـ* plus *ـش*, no Najdi *قلت لك* ↔ *قتلك* contractions, no Levantine *عم
  بـ*. Presence of these shifts the label toward the specific variety.
- **fas/urd/pes (Persian/Urdu)** — Same script, but those languages use پ چ ژ
  گ ک ی ے (Arabic does not) and have Indo-European function words (که، را،
  است، در، ہے، کا، کی). Arabic-only cues: ذلك، التي، الذي, definite ال,
  tāʾ marbūṭa ة.

## Diagnostics against non-Arabic Arabic-script languages

- Character **ة** (tāʾ marbūṭa) appears in Arabic/Dialects but is rare in
  Persian/Urdu/Kurdish/Pashto.
- Words ending **ـات** and **ـون** as productive plural endings are Arabic
  hallmarks.
- Sequence "ال" + sun letter (الش ،الص ،الد ،الن ،الر ،الت) followed by
  gemination shadda is near-unique to Arabic.
