# Galician (glg_Latn): Distinguishing from Confusable Languages

Galician sits between Spanish (shared spelling conventions, heavy lexical contact) and Portuguese (shared grammar and core vocabulary). Its main confusions are therefore **Portuguese** (CHALIS pair `por`/`glg`) and **Spanish** (`spa`/`glg`), plus Asturian and the Galician-Asturian transition varieties. Marker words are from `../chalis/discriminators.md` and the TSVs in `../chalis/discriminators/`.

## Galician vs Portuguese (por)

| | Galician (RAG) | Portuguese |
|---|---|---|
| fem. indefinite | **unha** | **uma** |
| negation | **non** | **não** |
| "with / without / in" | **con / sen / en** | **com / sem / em** |
| "already / very / more" | **xa / moi / máis** | **já / muito / mais** |
| "when / there is" | **cando / hai** | **quando / há** |
| "also / still" | **tamén / aínda** | **também / ainda** |
| "that (n.)" | **iso** | **isso** |
| "to him / to you" | **lle / che** | **lhe / te, lhe** |
| "my (f.) / his (f.)" | **miña / súa** | **minha / sua** |
| "people / way" | **xente / xeito** | **gente / jeito** |
| "you (polite)" | **vostede** | **você, o senhor** |
| "by the / with the" | **polo, pola / co, coa** | **pelo, pela / com o** |
| suffix | **-ción, -cións** | **-ção, -ções** |
| suffix | **-ble, -axe** | **-vel, -agem** |
| nasal letters | none (no ã, õ, ç) | **ã, õ, ç** |
| palatals | **ñ, ll, x** | **nh, lh, ch/x/j** |
| clitics | solid (*chámase*) | hyphenated (*chama-se*) |
| 3pl present | **teñen, falan** | **têm, falam** |

Ranked marker words (por-glg.tsv) — Galician: *unha, máis, pero, aquí, xa, hai, cando, súa, miña, así, moi, ten, facer, teño, quen, lle, xente, señor, tamén, sen, podo, estaba, día, aínda, che*. Portuguese: *em, não, uma, com, mas, você, tem, são, ele, muito, isso, já, também, quando, pela, bem, pessoas, tudo, fazer, minha, quem, sem, assim, depois, estão*.

Note: some Galician markers (*aquí, así, día, señor*) differ from Portuguese only by spelling (*aqui, assim, dia, senhor*), and *pero* is a normative Galician word absent from Portuguese. Shared items (*de, a, o, que, e, do, da, é, para, no, se, na, por, os, eu, como, as, mais, foi, ao, ser, seu, ou, está, ela, vai, só, sobre, agora, ter, anos*) are useless for this pair.

### Reintegrationist (lusist) Galician

Reintegrationists write Galician with Portuguese conventions. Typical forms:
- **Older AGAL / "minimal" norm:** *nom* (not), *umha* (a), *-çom/-som* (*naçom, decisom*), *mui*, *ainda*, *também*, *nh/lh* (*minha, trabalho*), *ç*, *j/g* (*gente, já*).
- **Current AGAL norm** (aligned with the Portuguese Orthographic Agreement): mostly Portuguese spelling (*não, uma, nação*) with Galician morphology and lexicon.

Galician tells inside lusist text: **Galiza**, **polo/pola** (Port. *pelo/pela*), **-che** dative (*dou-che*), **ti** as subject, 2pl **-des** verbs (*fazedes, sodes*), preterite 2sg **-aste(s)**, lexicon *cousa, rapaz, ren, ogalhá, ollar/olhar*, *nom*, *umha*. A lusist text without any of these may be indistinguishable from European Portuguese; mark low confidence (uncertain how such text is labelled in CHALIS).

## Galician vs Spanish (spa)

| | Galician | Spanish |
|---|---|---|
| definite articles | **o, a, os, as** | **el, la, los, las** |
| negation | **non** | **no** |
| "a/an" | **un, unha** | **un, una** |
| "already, very" | **xa, moi** | **ya, muy** |
| "there is" | **hai** | **hay** |
| "when, where" | **cando, onde** | **cuando, donde** |
| "I, I have" | **eu, teño** | **yo, tengo** |
| "has, can" | **ten, pode** | **tiene, puede** |
| "to do, until, since" | **facer, ata, dende** | **hacer, hasta, desde** |
| "or" | **ou** | **o** |
| "only" | **só** | **solo / sólo** |
| contractions | **ao, do, no, na, polo, coa, nun, dunha** | **al, del** only |
| plural *-ción* | **-cións** | **-ciones** |
| plural *-l* | **-is** (*animais*, *papeis*) | **-es** (*animales*) |
| diphthongs | *tempo, pode, novo, porta* | *tiempo, puede, nuevo, puerta* |
| /ʃ/ vs /x/ | **x** (*xente, dixo*) | **j/g** (*gente, dijo*) |
| *-mento* | *coñecemento* | *conocimiento* |

Spanish markers vs Galician (spa-glg.tsv): *sus, ya, yo, hay, fue, muy, también, tiene, puede, hasta, hacer, hace, ni, donde, mejor, mucho, mismo, siempre, tengo, después, estoy*.

**Castilianisms in Galician** (*castrapo*) are common in speech, subtitles and informal writing: *entonces* (norm *entón*), *bueno*, *gracias* (*grazas*), *sin embargo / sen embargo* (norm *porén, non obstante*), *estudiante* (*estudante*), *dijo*. The UD sample itself contains *sen embargo* and *estudiantes*. Such tokens do **not** make a text Spanish when Galician grammar words (`o/os/as`, `non`, `unha`, `xa`, `lle`, contractions) dominate. Conversely, a Spanish text quoting Galician place names (*Xunta*, *Ourense*, *A Coruña*) is still Spanish.

## Galician vs Asturian-Leonese (ast) and Eonavian

- **Asturian**: articles *el, la, lo, los, les*; masc. *-u* (*llobu*), fem. pl. *-es* (*les cases*), *ye* "is", *nun* "not", *pa*, initial **ll-** for Latin l- (*llingua*). Galician has *o/a*, *é*, *non*, *lingua*.
- **Eonavian / Galician-Asturian** (western Asturias, "fala"): Galician-like (*o, a, non, unha*) but with Asturian traits and its own spelling (*ḷḷ*, often *el* article in some areas). Treat as uncertain; likely not part of CHALIS.

## Galician vs Catalan / Occitan (rarely confused)

Catalan: *els, les, amb, és, més, molt, l·l, ç, ny, à/è/ò*, apostrophes. Occitan: *lh/nh, amb/dab, es, pas, ò/è*. Galician has none of these.

## Quick Priority List

1. `unha`, `non`, `xa`, `moi`, `hai`, `cando`, `lle`, `iso`, initial `x` → **glg** (vs both neighbours).
2. `ñ`, `ll`, no `ã/õ/ç` → rules out Portuguese.
3. `o/os/as` articles, `ao/polo/coa`, `-cións`, `ou` (or), solid enclitics → rules out Spanish.
4. `nom`, `umha`, `-çom`, `Galiza`, `polo/pola` in Portuguese-looking spelling → reintegrationist **glg**.
