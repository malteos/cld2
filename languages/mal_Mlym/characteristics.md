# Malayalam characteristics (LID signals)

## Script signals

Malayalam lives in Unicode block **U+0D00–U+0D7F**, disjoint from all other scripts. Near-certain diagnostic signals:

- **Chillu letters** are unique to Malayalam: **ൻ** (U+0D7A), **ൾ** (U+0D7B), **ർ** (U+0D7C), **ൽ** (U+0D7D), **ൺ** (U+0D7E), **ൿ** (U+0D7F). Any of these characters is near-proof of Malayalam.
- **ഴ** (U+0D34) — cognate of Tamil ழ, unique within the Malayalam block.
- Dense **stacked conjuncts** are visually distinctive: **ന്ത**, **ണ്ട**, **ക്ക**, **ത്ത**, **സ്ത്ര**, **ന്ദ്ര**.
- Final-consonant mark **്** (chandrakkala, U+0D4D) is very frequent on word endings.
- Anusvara **ം** (U+0D02) is extremely common — many words end in *-ം*.

## Top function words

**ഞാൻ** (I), **നീ** (you sg.), **അവൻ / അവൾ / അത്** (he / she / it), **ഞങ്ങൾ / നമ്മൾ** (we excl. / incl.), **നിങ്ങൾ** (you pl.), **ഇത് / അത് / ഏത്** (this / that / which), **എന്ത് / എന്തുകൊണ്ട് / എങ്ങനെ** (what / why / how), **എവിടെ / എപ്പോൾ** (where / when), **ഉണ്ട്** (there is), **ഇല്ല / അല്ല** (not / is-not), **ആണ്** (is, copula), **ആയിരുന്നു** (was), **ഉം** (also/and, enclitic), **എന്ന്** (that, quotative), **പക്ഷേ** (but), **അല്ലെങ്കിൽ** (or), **കൂടാതെ** (besides), **വേണ്ടി** (for), **കൊണ്ട്** (with, because of), **നിന്ന്** (from), **വരെ** (until), **ശേഷം** (after), **മുമ്പ്** (before), **അതിനാൽ** (therefore).

## N-gram / spelling patterns

- Word-final **`ം`** (anusvara) is extraordinarily frequent — a top-ranked word-end byte sequence.
- Word-final chillu letters (`ൻ`, `ൾ`, `ർ`, `ൽ`) mark human plurals, agent nouns, and case forms.
- Sequences ending **`-ന്`** (half-n), **`-ത്`**, **`-ക്ക്`** are typical case/verb endings.
- **`-ുടെ`** (`-uṭe`, genitive) is a high-precision Malayalam tail.
- **`-ുന്നു`** (present tense `-unnu`) and **`-ും`** (future/and-coordinator) are very frequent.

## Morphology hooks

- Plural `-കൾ`/`-മാർ`; dative `-ന്/-ക്ക്`; genitive `-ുടെ/-ിന്റെ`; locative `-ിൽ`; ablative `-ിൽനിന്ന്`.
- Verb tails: `-ുന്നു` (present), `-ി/-ത്തു` (past), `-ും` (future), `-ുക` (infinitive), `-ാത്ത` (negative participle).
- Quotative complementiser **എന്ന്** ubiquitous before reporting verbs.

## Punctuation / orthography

Latin punctuation (. , ? !). Traditional Malayalam digits exist (൦–൯) but Western digits dominate. The reformed orthography (post-1971) splits many old conjuncts using visible chandrakkala, which can create stretches of explicit **്** dots between consonants.
