# Persian LID characteristics

## Script signals

- Four Perso-Arabic extensions absent from standard Arabic: **پ چ ژ گ**. Any of these in Arabic-script text immediately rules out Arabic.
- Iranian code-points **ک** U+06A9 (not Arabic ك U+0643) and **ی** U+06CC (not Arabic ي U+064A with dots). CLD2 normalisation should treat these as diagnostic rather than map them to the Arabic forms.
- *Ezāfe* written overtly as kasra **ـِ** on the final letter of a head word, or as hamza-over-ye **ۀ** after silent final ه.
- Absence of Urdu retroflex letters **ٹ ڈ ڑ** and of Uzbek vowels **ۉ ې** — their presence indicates urd or uzs respectively, not fas.
- Eastern Arabic-Indic digits ۰۱۲۳۴۵۶۷۸۹ are common in Iranian text.

## Top function words

و، در، به، از، که، این، آن، با، را، بر، برای، تا، هم، نیز، یک، اما، ولی، اگر، چون، یا، هر، همه، هیچ، من، تو، او، ما، شما، ایشان، است، هست، بود، شد، می‌شود، می‌کند، کرد، کرده، نیست، خواهد، باید، شاید.

## N-gram and spelling patterns

- Very high frequency of **می‌** prefix (imperfective) and **ـها** suffix (plural) — both extremely productive and rare in Arabic.
- Common bigrams: **است**، **که**، **این**، **آن**، **برای**، **کرد**.
- Suffix **ـترین** (superlative) and **ـتر** (comparative) on adjectives.
- `که` (*ke*) is the single most recognisable Persian function word after و.

## Morphology hooks

- Plural **ـها** / **ـان**, imperfective prefix **می‌**, subjunctive prefix **بـ**, negation **نـ / نمی‌**.
- Object marker **را** following definite direct objects.
- Enclitic copula endings **ـم، ـی، ـست، ـیم، ـید، ـند** that attach to the last word of a predicate.
- Infinitives in **ـتن / ـدن** (کردن، رفتن، بودن).

## Punctuation / orthography quirks

- Right-to-left. ZWNJ (U+200C) is very common to separate the prefix **می‌** / suffix **ـها** from the stem without full joining.
- Persian uses its own comma **،** and question mark **؟**; Persian does NOT use the Urdu full stop **۔** — that alone often disambiguates fas from urd.
