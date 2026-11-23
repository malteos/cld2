# Galician (glg_Latn): Identification Characteristics

Applies to the official norm of the Real Academia Galega (RAG, current norm 2003, revised 2012), which uses Spanish-style spelling. Reintegrationist (Portuguese-style) spelling is covered in `differences.md`.

## Letter Inventory

Latin a-z (k, w, y, j only in loans and foreign names) plus **ñ**, with acute accents **á é í ó ú** and diaeresis **ü** rarely (*pingüín*). No grave accent, no circumflex, no tilde vowels (ã õ), no cedilla (ç), no l·l.

### Diagnostic characters

| Feature | Examples | LID value |
|---|---|---|
| **x** for /ʃ/ | *xa, xente, xeito, hoxe, dixo, Xunta, xuño, baixo, deixar* | Very high. Spanish has *ya, gente, hoy, dijo*; Portuguese *já, gente, hoje, disse* (though Portuguese also writes *deixar, baixo*). Initial **x+vowel** in common words is Galician-specific. |
| **ñ** | *miña, teño, señor, coñecemento, ningún* | Excludes Portuguese (nh) and Catalan (ny); shared with Spanish |
| **nh** only in *unha, unhas, algunha, ningunha, nunha, dunha* | | The word **unha** is the best single Galician token |
| **ll** | *traballo, muller, mellor, ollos, fillo* | Shared with Spanish (which has *j* in these words: *trabajo, mujer*) |
| no **j**, no **ç**, no **ã/õ** | | A Galician-looking text with *j* in native words is likely Spanish; with *ç/ã* likely Portuguese or reintegrationist |
| diacritic accents | *é* "is" vs *e* "and"; *máis* "more" vs *mais* "but"; *á* = a + a; *só*, *nós*, *vós*, *dá* | *é* is shared with Portuguese |

In the UD sample (`examples/ud_*.txt`, mostly news/science/technical text from UD_Galician-CTG) non-ASCII letters ranked: ó (very frequent, driven by *-ción*), á, í, é, ú, ñ.

## Top Function Words

From `vocabulary.json` (FrequencyWords, OpenSubtitles 2018 — dialogue-heavy, so pronouns and interjections rank high):

que, a, o, non, de, e, é, un, os, unha, se, para, por, do, en, da, as, como, está, si, máis, no, ao, ben, pero, eu, na, con, aquí, son, me, todo, á, iso, meu, xa, hai, ti, cando, ou, só, dos, súa, miña, seu, agora, así, moi, onde, nada, era, ten, facer, ser, foi, el, teño, isto, quen, nos, todos, vai, estou, porque, lle, pode, te, mais, xente, tamén, sen, aínda, polo, che, pola, coa

Galician-only items versus Portuguese (`../chalis/discriminators/por-glg.tsv`): **unha, máis, pero, aquí, xa, hai, cando, súa, miña, así, moi, ten, facer, teño, quen, lle, xente, tamén, sen, aínda, che, vostede, pola, coa**. Versus Spanish (`spa-glg.tsv`): **unha, máis, ao, iso, meu, xa, hai, cando, ou, só, súa, miña, moi, onde, facer, foi, teño, isto, quen, vai, estou, lle**. **non** (rank 4) is not in either TSV for technical reasons but is absent from the Spanish list and near-absent from the Portuguese list; treat it as a top cue.

Notes: *si* "yes" is written without accent (Spanish *sí*); *pero* is normative in Galician and very frequent, alongside *mais* "but".

## Contractions (high-yield)

- Preposition + article: **do, da, dos, das, no, na, nos, nas, ao, á, aos, ás** (Portuguese shares most; Portuguese *à* has a grave accent, Galician *á* acute).
- **polo, pola, polos, polas** (*por* + article; Portuguese *pelo, pela*).
- **co, coa, cos, coas** (*con* + article) — standard written forms in Galician; Portuguese uses *com o* in writing.
- **nun, nunha, dun, dunha** (*en/de + un/unha*).
- Pronoun combinations: **cho, cha, llo, lla, mo, ma** (*che/lle/me + o/a*).
- Older texts (before the 2003 norm) and some current writers use **ó, ós** for *ao, aos* (seen in the UD sample: *permite ó ser humano*).

## Frequent Character N-grams

Trigrams most frequent in the UD sample (about 2.8k words; technical register, indicative only): `os `, ` de`, `de `, `as `, ` co`, `ent`, **`ión`**, **`ció`**, `ón `, `s d`, `do `, ` a `, `que`, `nte`, `da `, ` se`, `con`, `en `.

- **`-ción`, `-cións`, `-sión`, `-sións`**: Galician keeps the Spanish-looking singular but has a distinctive plural **-cións** (Spanish *-ciones*, Portuguese *-ções*). In the UD sample *-ción* was the single most frequent 4-letter ending and *-ións* ranked fifth.
- **`-ento`/`-mento`** (*mantemento, coñecemento, tratamento*): Spanish *-miento* (*mantenimiento, conocimiento*); Portuguese *-mento* too.
- **`-dade`** (*cidade, sociedade, universidade*) — Portuguese same, Spanish *-dad*.
- **`-axe`** (*viaxe, linguaxe*) vs Portuguese *-agem*, Spanish *-aje*.
- **`-eiro/-eira`** (*primeiro, carteira*) shared with Portuguese.
- **`ou`, `ei`** diphthongs (*cousa, pouco, falou, primeiro*) shared with Portuguese; Spanish *cosa, poco*.
- **`-zo/-za`** where Portuguese has *-ço/-ça* (*cabeza/cabeça, praza/praça, comezar/começar*).

## Verbal Endings

- 3sg preterite **-ou** (*falou*), 1sg **-ei** (*falei*), 2sg **-aches** (*falaches*), 3pl **-aron** (*falaron*; Portuguese *-aram*).
- 2pl **-ades/-edes/-ides** (*falades, tedes, ides*) — distinctive; Spanish *-áis/-éis*, Portuguese *-ais/-eis*.
- Infinitive **-ar/-er/-ir** + personal infinitive endings *-res, -rmos, -rdes, -ren*.
- **Enclitics written solid on finite verbs:** *chámase, pódese, díxolle, poderíase, fíxoo*. Spanish puts the clitic before finite verbs; Portuguese hyphenates. A finite verb with fused *-se/-lle/-che/-me* is a strong Galician cue.

## Orthographic Conventions Summary

- Spanish-like: *ñ, ll, ce/ci/z, gu/qu, -ción*, acute accents only, accent rules similar to Spanish.
- Portuguese-like: articles *o/a/os/as*, contractions, *ou/ei* diphthongs, no ie/ue diphthongization (*pode, tempo, porta, novo*).
- Galician-unique combination: **x** + **ñ** + **unha** + **-cións** + solid enclitics.
