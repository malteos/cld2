# Portuguese (por_Latn): Distinguishing from Confusable Languages

The main confusions are Galician (closest relative, CHALIS pair `por`/`glg`), Spanish, and to a lesser degree Catalan, Mirandese and Asturian-Leonese. European (PE) and Brazilian (PB) Portuguese are both labelled `por`. Marker lists come from `../chalis/discriminators.md` and `../chalis/discriminators/por-glg.tsv`, `spa-por.tsv`.

## Portuguese vs Galician (glg), official RAG norm

Galician written in the Real Academia Galega (RAG) norm uses Spanish-style spelling, which gives very clean orthographic cues:

| Feature | Portuguese | Galician (RAG) |
|---|---|---|
| nasal tilde | **não, mão, ação, -ções** | none: **non, man, acción, -cións** |
| cedilla | **ç** (*começar, cabeça*) | **z/c** (*comezar, cabeza*) |
| /ʃ/, /ʒ/ | **x, ch, j, g** (*já, gente, deixar*) | **x** only (*xa, xente, deixar*) |
| palatal nasal | **nh** (*minha, tenho, senhor*) | **ñ** (*miña, teño, señor*); *nh* only in *unha* |
| palatal lateral | **lh** (*filho, trabalho, melhor*) | **ll** (*fillo, traballo, mellor*) |
| "a/an (fem.)" | **uma** | **unha** |
| "not" | **não** | **non** |
| "with", "without" | **com, sem** | **con, sen** |
| "very, much" | **muito** | **moi, moito** |
| "already" | **já** | **xa** |
| "more" | **mais** | **máis** (*mais* = "but" in Galician) |
| "when" | **quando** | **cando** |
| "there is" | **há / tem** | **hai** |
| "also, still" | **também, ainda** | **tamén, aínda** |
| "that (n.)" | **isso, isto** | **iso, isto** |
| "to him" | **lhe** | **lle** |
| "you" (polite) | **você, o senhor** | **vostede** |
| "by the" | **pelo, pela** | **polo, pola** |
| "with the" | **com o** (colloquial *co*) | **co, coa, cos, coas** |
| 3pl present | **falam, têm** | **falan, teñen** |
| 2pl present | **falais** (rare; *vocês falam*) | **falades** |
| clitics | **hyphen**: *chama-se, disse-lhe* | **solid**: *chámase, díxolle* |
| *-vel* | **possível** | **posible** |
| *-agem* | **viagem** | **viaxe** |

Word-level markers (por-glg.tsv): Portuguese *em, não, uma, com, mas, você, tem, são, ele, muito, isso, já, também, quando, pela, bem, pessoas, tudo, fazer, minha*; Galician *unha, máis, pero, aquí, xa, hai, cando, súa, miña, así, moi, ten, facer, teño, quen, lle, xente, tamén, sen, aínda, che*. Note that Galician **non** (rank 4 in `../glg_Latn/vocabulary.json`) is missing from the TSV only because it appears once in the Portuguese 10k list (rank ~6800, probably Latin/foreign phrases); in practice it is one of the best Galician cues.

Shared and not diagnostic: *de, a, o, que, e, do, da, é, para, no, se, na, por, os, eu, como, as, mais, dos, foi, ao, me, ser, seu, ou, nos, está, meu, ela, vai, só, sobre*.

## Portuguese vs Reintegrationist Galician

Reintegrationist (*lusista*) Galician uses Portuguese-like spelling: *ç, nh, lh, -ção, j/g*. Two main flavours:
- **Minimal/AGAL older norm:** *umha, nom, -çom* (*naçom*), *-zom*, *mui*, *ainda*, *também*.
- **Current AGAL / fully lusist:** nearly identical to Portuguese spelling (*uma, não, nação*).

Cues that such text is Galician rather than Portuguese: **umha, nom, -çom/-som**, place name **Galiza**, **polo/pola** (vs *pelo/pela*), clitic **che/-che** "to you" (*dou-che*), 2pl verbs **-des** (*fazedes, tendes*), **ti** as subject, lexicon *cousa, ogalhá, achegar, ren, eido*. Fully lusist text without these may be indistinguishable from PE; the CHALIS gold label would then depend on the source, not the spelling (uncertain; flag low confidence).

## European vs Brazilian Portuguese (both `por`)

Not needed for the label, but useful to recognise either variety as Portuguese:
- PB: *você* as default "you", **a gente** "we", proclisis (*me disse, se chama*), **estar + gerund** (*estou fazendo*), *ônibus, trem, celular, time, banheiro*, accents *econômico, gênero, Antônio*, informal *pra, tá, né, cê*.
- PE: *tu*, enclisis with hyphen (*disse-me*), **estar a + infinitive** (*estou a fazer*), *autocarro, comboio, telemóvel, equipa, casa de banho*, accents *económico, género, António*, pre-1990 *acção, facto, óptimo, actual*.

## Portuguese vs Spanish (spa)

| Cue | Portuguese | Spanish |
|---|---|---|
| nasals | ã, õ, -ão, word-final -m | none |
| palatals | nh, lh | ñ, ll |
| "and", "in" | e, em | y, en |
| "not" | não | no |
| articles | o, a, os, as | el, la, los, las |
| "a/an" | um, uma | un, una |
| diphthongs | *tempo, pode, novo* | *tiempo, puede, nuevo* |
| f-/h- | *fazer, falar, filho* | *hacer, hablar, hijo* |

Spanish markers vs Portuguese (spa-por.tsv): *pero, cuando, hay, fue, muy, también, eso, tiene, qué, así, años, bien, puede, hasta, hacer, ahora*. Beware: Portuguese *no/na* = "in the", *e* = "and", *mas* = "but", *como, para, que, todo, nada, vida* are shared.

## Portuguese vs Catalan (cat)

Both use **ç** and grave **à**. Catalan has no tilde vowels, uses **els/les, i, amb, és, més, l·l, ny, -ció**, apostrophe elision (*l'any*); Portuguese has **o/os/as, e, com, é, mais, nh/lh, -ção**.

## Portuguese vs Mirandese (mwl) and Asturian-Leonese

Mirandese (official locally in Miranda do Douro, Portugal) is Astur-Leonese with Portuguese-influenced spelling: **lh** word-initially for Latin l- (*lhéngua, lhobo*), diphthongs **ie/uo** (*tierra, puorta*), *ye* "is", *nun* "not" (details from general knowledge; verify against real Mirandese text). Initial *lh-* + *ie/uo* diphthongs rules out Portuguese.

## Quick Priority List

1. `ã/õ`, `-ção/-ções`, `não`, hyphenated clitics → **por** (unless `umha/nom/-çom/Galiza` → reintegrationist `glg`).
2. `non`, `unha`, `ñ`, `xa/moi/hai/cando`, `-cións`, solid enclitics on finite verbs → **glg**.
3. `y`, `el/los/las`, `ñ`, `ie/ue` stems → **spa**.
4. `els/amb/és/l·l` → **cat**.
