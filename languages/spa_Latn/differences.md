# Spanish (spa_Latn): Distinguishing from Confusable Languages

Spanish is mostly confused with Catalan, Galician and Portuguese (the CHALIS cousin pairs), and less often with Asturian-Leonese, Aragonese, Occitan and Italian. Marker lists below come from `../chalis/discriminators.md` and the TSVs in `../chalis/discriminators/` unless noted.

## Spanish vs Catalan (cat)

| Cue | Spanish | Catalan |
|---|---|---|
| "and" | **y** | **i** |
| plural articles | **los, las** | **els, les** (*les* also Spanish clitic "to them") |
| "with" | **con** | **amb** |
| "is" / "more" | **es / más** | **és / més** |
| "but" | **pero** | **però** |
| "very, much" | **muy, mucho** | **molt** |
| "also" | **también** | **també** |
| "when, now, until" | **cuando, ahora, hasta** | **quan, ara, fins** |
| "this" | **este, esta, esto** | **aquest, aquesta, això** |
| palatal nasal | **ñ** (*año*) | **ny** (*any*) |
| suffixes | **-ción/-ciones, -dad, -ado** | **-ció/-cions, -tat, -at** |

Machine-checkable Catalan-only signals: middle dot **l·l** (*col·legi*), grave accents **à è ò**, **ç**, apostrophe elision **l' d' s' n' m'** before vowels, clitics **hi, ho, en, ens**, periphrastic past **vaig/va/van + infinitive** (*va dir* "said"), word-final **-ix, -tx, -ig** (*baix*, *peix*, *cotxe*, *mig*). Spanish-only: **¿ ¡**, **ñ**, standalone **y**, **los/las**, diphthongs **ie/ue** in common stems (*tiene, puede, tiempo*), final **-o** on masculines where Catalan drops it (*nuevo/nou*, *todo/tot*).

## Spanish vs Galician (glg)

Galician shares **ñ**, **ll**, **-ción**, acute-only accents and many Castilian loans, so it is the hardest Romance neighbour after Catalan.

| Cue | Spanish | Galician |
|---|---|---|
| articles | **el, la, los, las** | **o, a, os, as** |
| negation | **no** | **non** |
| "a, an (fem.)" | **una** | **unha** |
| "already, very, more" | **ya, muy, más** | **xa, moi, máis** |
| "there is" | **hay** | **hai** |
| "when, where" | **cuando, donde** | **cando, onde** |
| "I, he/she has" | **yo, tiene** | **eu, ten** |
| "that (pron.)" | **eso, esto** | **iso, isto** |
| "to him/her" | **le** | **lle** |
| "people, way" | **gente, manera** | **xente, xeito** |
| contractions | only **al, del** | **ao, á, do, da, no, na, polo, pola, co, coa, nun, unha** |
| plural of *-ción* | **-ciones** | **-cións** |
| "f-" words | **hacer, hasta, hijo** | **facer, ata, fillo** |

Letter **x** for /ʃ/ (*xa, xente, hoxe, dixo, Xunta*) and diphthong-less stems (*pode, tempo, novo* vs *puede, tiempo, nuevo*) are strong Galician cues. Galician writes enclitics on finite verbs (*chámase*, *díxolle*); Spanish uses *se llama*, *le dijo*. Note that Galician *pero* and *gente*-type Castilianisms do occur (in `../glg_Latn/vocabulary.json`, *pero* is rank 25), so do not treat *pero* as Spanish evidence against Galician.

## Spanish vs Portuguese (por)

| Cue | Spanish | Portuguese |
|---|---|---|
| nasal vowels | none | **ã, õ, -ão, -ões, -ção** |
| palatals | **ñ, ll** | **nh, lh** |
| "and" / "in" | **y / en** | **e / em** |
| "not" | **no** | **não** |
| articles | **el, la, los, las** | **o, a, os, as** |
| "a/an" | **un, una** | **um, uma** |
| "with" | **con** | **com** |
| "very" | **muy** | **muito** |
| "there is" | **hay** | **há / tem** |
| "you" (polite) | **usted** | **você, o senhor** |
| suffixes | **-ción, -dad, -ble** | **-ção, -dade, -vel** |

Beware false friends that look Spanish: Portuguese *no/na* are "in the", *como*, *para*, *que*, *se*, *por*, *todo*, *nada*, *vida* are shared. Spanish never has **ç**, **ã**, **õ**, **ê/ô/â**, or word-final **-m** in function words (*um, em, com, sem, tem, bem*).

## Spanish vs Asturian (ast)

Asturian (Asturias, also Leonese varieties in León/Zamora) looks Spanish-like but has: masculine singular **-u** (*el llobu*, *bonu*), feminine plural **-es** (*les cases*, *les muyeres*) and articles **el, la, lo, los, les**; **ye** "is" (Spanish *es*), **nun** "not/in a", **pa** "for", **diz** "says", **-ín/-ina** diminutives, **h-** marking aspiration in eastern areas, and **ḷḷ** / **ḥ** with underdots in some spellings. Spanish feminine plural is always *-as*; a text with *les* + noun-*es* or *-u* masculines is not Spanish.

## Spanish vs Occitan (oci) and Aragonese (arg)

Occitan: **lh, nh** digraphs (*filha, senhor*), **ò** and **è** with grave accent, **amb/dab** "with", **es** "is", **pas** in negation, **aquò, çò**, infinitives in **-ar/-ir/-re**, plural **-s** but feminine singular often **-a** pronounced /ɔ/. Aragonese: **ye** "is", **bi** (locative "y"), **no'n**, **-ito/-eta** diminutives, past *cantó/cantoron*, **ny** in some spellings, **ch** for /tʃ/ where Spanish has *j/ll* (*muller*, *chent* vs *mujer*, *gente*).

## Spanish vs Italian (ita)

Italian lacks **ñ** (uses *gn*), uses **gli, chi, che, sc**, doubled consonants (*anno, tutto, della*), articles **il, lo, gli, i**, "and" **e**, "with" **con** (shared), final vowels on almost every word and grave-accented final vowels (*città, perché*).

## Quick Priority List

1. `¿`/`¡` → Spanish.
2. `l·l`, `à/è/ò`, `ç` + no `ã/õ`, apostrophe elision → Catalan.
3. `ã/õ/-ção`, `nh/lh`, `não`, `um/uma/em/com` → Portuguese.
4. `non`, `unha`, `xa/moi/hai/cando`, initial `x`, `-cións` → Galician.
5. `y` + `los/las` + `ie/ue` stems + `ñ` → Spanish.
