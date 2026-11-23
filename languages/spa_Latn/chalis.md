# Spanish (spa_Latn) in CHALIS

Practical guide for labelling a CHALIS sample `spa` (ISO 639-3) when the competing labels are Catalan (`cat`), Galician (`glg`) and Portuguese (`por`). Marker words come from `../chalis/discriminators.md` and `../chalis/discriminators/spa-cat.tsv`, `spa-glg.tsv`, `spa-por.tsv` (frequent words of one language absent from the other's 10k list). Remember the caveat in that file: the Galician list comes from OpenSubtitles, so some "Spanish vs Galician" markers reflect genre rather than language.

## 1. Cousin-Pair Cues, Ranked by Reliability

### Spanish vs Catalan
1. **Orthography Catalan cannot have:** `¿ ¡`, `ñ`. Catalan-only: `l·l`, `ç`, grave `à è ò`, apostrophe elision (`l'`, `d'`, `s'`, `n'`).
2. **Articles/conjunction:** `y`, `los`, `las` (Spanish) vs `i`, `els`, `les` + noun (Catalan). `els`, `dels`, `als`, `pels` never occur in Spanish.
3. **Top markers** (spa-cat.tsv): Spanish *sus, todo, cuando, fue, muy, también, tiene, porque, así, años, bien, puede, hasta, hacer, ahora, esto, nada, donde, mucho, siempre, después*; Catalan *amb, és, més, hi, aquest, però, tot, fer, molt, també, ens, són, això, quan, ara, fins, què, perquè*.
4. **Endings:** `-ción/-ciones, -dad, -ado` vs `-ció/-cions, -tat, -at`.

### Spanish vs Galician
1. **Articles and negation:** `el/los/las` + `no` (Spanish) vs `o/os/as` + `non` (Galician). `non` is Galician rank 4 in `../glg_Latn/vocabulary.json` but appears in the Spanish list only at rank ~9500, so one `non` is strong evidence.
2. **Markers** (spa-glg.tsv): Spanish *sus, ya, yo, hay, fue, muy, también, tiene, puede, hasta, hacer, donde, mucho, siempre, tengo, después, estoy*; Galician *unha, máis, ao, iso, xa, hai, cando, ou, só, súa, miña, moi, onde, facer, teño, isto, quen, lle, xente, tamén*.
3. **x for /ʃ/** (*xa, xente, hoxe, dixo*) and **-cións** plural → Galician.
4. Shared and therefore useless: *de, que, en, a, se, por, es, con, para, como, pero, este, esta, todo, porque, así, vez, nada, día, vida*.

### Spanish vs Portuguese
1. **Nasal tilde and cedilla:** any `ã`, `õ`, `ç`, `-ção`, `-ões` → Portuguese. `ñ`, `¿` → Spanish.
2. **Function words:** Portuguese *não, um, uma, em, com, ao, você, muito, isso, já, também, quando*; Spanish *pero, cuando, hay, fue, muy, también, eso, tiene, qué, así, años, hasta, hacer, ahora*.
3. **Digraphs:** `nh/lh` vs `ñ/ll`; word-final `-m` in function words (Portuguese).

## 2. When Diacritics Are Stripped

Removing accents damages Spanish less than Catalan or Portuguese, but several collisions appear:
- **ñ → n:** *años → anos*, *año → ano*, *señor → senor*, *España → Espana*. *anos/ano* are genuine Portuguese and Galician words, so in stripped text they are no longer Spanish evidence. *nino, senor, manana, pequeno* remain Spanish-looking (Portuguese has *menino, senhor, amanhã, pequeno* — careful: **pequeno** is valid Portuguese/Galician).
- **más → mas:** Spanish *mas* (rank 100 in the Spanish list, often an accent-less *más*) collides with Portuguese *mas* "but" (rank 25). Not diagnostic either way once stripped.
- **también → tambien** stays Spanish (Port. *tambem*, Cat. *tambe*, Gal. *tamen*). **después → despues**, **está → esta** (shared), **qué → que**, **sí → si**, **él → el**.
- **-ción → -cion**: still differs from Portuguese *-cao* and Catalan *-cio*, but equals stripped Galician *-cion*; use the plural (*-ciones* vs Galician *-cions*).
- Spanish identification after stripping relies on **y**, **los/las**, **muy, hay, ya, yo, hasta, cuando, donde, puede, tiene**, which carry no diacritics.

Homoglyph and leetspeak variants (Cyrillic `о/а/е/с/р` for Latin letters, digits for letters such as `3`=e, `4`=a, `0`=o, `1`=i/l) should be normalised mentally before applying the cues; the underlying word list is the same. (General guidance; specific CHALIS substitution tables are not reproduced here.)

## 3. Short-Text Pitfalls and Code-Switching

- Strings like *"Es la vida"*, *"No sé"*, *"Para todos"* are valid Spanish but *es/la/vida/para/todos* also occur in Catalan, Galician or Portuguese. Prefer the label supported by any single distinctive token; if none exists, Spanish is the base-rate default only when nothing contradicts it.
- **Catalan with Castilianisms** (*pues, bueno, vale*, *o sea*) stays Catalan if it has `els`, `amb`, `és`, `l'`, `però`. Conversely, Spanish text from Catalonia may contain place names or a Catalan quote (*Generalitat*, *Diputació*): judge by the surrounding grammar.
- **Galician with Castilianisms** (*pero, gente, entonces, bueno*): if `non`, `unha`, `xa`, `o/os/as` articles or enclitic finite verbs (*chámase*) are present, label `glg`.
- **Portuñol / Brazilian-Spanish mixing**: weigh Portuguese nasals and `não` heavily; Spanish loans in Portuguese are less common than the reverse.
- Proper nouns (*Madrid*, *Galicia*, *Barcelona*) are not language evidence.

## 4. Decision Checklist

1. Normalise homoglyphs/leet; note whether accents seem stripped (no non-ASCII letters at all in a long text).
2. `¿` or `¡`? → **spa** (unless the rest is clearly Galician/Asturian).
3. `ã/õ/ç` or `não/um/uma/em/com/você`? → **por**.
4. `l·l`, `à/è/ò`, `els/amb/és/més/però`, `l'`/`d'` elision? → **cat**.
5. `non`, `unha`, `xa/moi/hai/cando/iso/lle`, `o/os/as` articles, `-cións`? → **glg**.
6. `y`, `los/las`, `muy/hay/ya/yo/hasta/donde/tiene/puede`, `ñ`, `-ciones`? → **spa**.
7. Only shared words: choose by the majority of weak cues (`el` + `la` favours spa/cat; `o` + `a` as articles favours por/glg), and state low confidence.

## 5. Illustrative Snippets

**A.** *"Ya no hay nada que hacer, los chicos se fueron."* → **spa**. `ya`, `hay`, `hacer`, `los`, `fueron` are all Spanish-side markers; no Galician `xa/hai/facer`, no Catalan `els/fer`.

**B.** *"Pero xa non hai nada que facer."* → **glg**. Despite Spanish-looking *pero* and *nada que*, `xa`, `non`, `hai`, `facer` are Galician markers (spa-glg.tsv).

**C.** *"Tambien fue muy dificil para los anos siguientes"* (stripped) → **spa**. *anos* is ambiguous after ñ-stripping, but `fue`, `muy`, `los` and `tambien` (not Portuguese *tambem*) decide it.
