# Arabic LID characteristics (macrolanguage)

## Script signals

Arabic script block U+0600–U+06FF is the primary signal: ا ب ت ث ج ح خ د ذ ر ز
س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي. Variety-neutral MSA-style text avoids
Persian/Urdu-only letters (پ ،چ ،ژ ،گ ،ک ،ی ،ے) — their presence usually
rules out Arabic. Hamza forms ء أ إ ؤ ئ and *tāʾ marbūṭa* ة, *alif maqṣūra*
ى are strongly Arabic.

## Top function words

و (and), في (in), من (from/of), على (on), إلى (to), عن (about), أن / إن (that),
التي / الذي / الذين (relative), هذا / هذه / ذلك / تلك (dem.), ما (what/not),
لا (no/not), لم / لن (neg past/fut), قد (particle), هو / هي / هم (he/she/they),
أنا / أنت / نحن (I/you/we), كل (every), بعض (some), عند (at), بين (between),
بعد (after), قبل (before), حتى (until), أو (or), لكن (but), هناك (there),
كان / كانت (was), يكون (be-impf).

## N-gram / spelling patterns

- Word-initial **ال** (definite article) is extremely frequent; bigram **ال+
  Sun-letter** (الش الص الت الن الر الل الد) is a hallmark.
- Word-final **ـون / ـين** (masc. plural), **ـات** (fem. plural), **ـة** (fem.
  sing.), **ـها / ـهم / ـه / ـك / ـي** (possessive clitics).
- Prefixed prepositions: **ب ، ل ، ك ، و ، ف** attach directly to the next word
  with no space (وفي، بالبيت، للمدرسة).
- Trigrams الذي، التي، الذين، والذي are near-unique to Arabic (vs Persian/Urdu).

## Morphology hooks

Root-and-pattern templates leave visible CVCVC shapes (فاعل، مفعول، استفعال،
تفاعل). Verb prefixes يـ / تـ / نـ / أـ mark imperfective person. Nominal
prefix مـ (مكتب، مدرسة، منزل) and infinitive patterns (استقبال، تعليم).

## Punctuation / orthography quirks

Arabic comma **،**, semicolon **؛**, question mark **؟**. Decimal separator
**٫** and numeric comma **٬**. Eastern Arabic digits ٠١٢٣٤٥٦٧٨٩ often coexist
with Western 0–9. Right-to-left directionality; BiDi markers may appear.
