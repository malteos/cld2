# Galician (glg_Latn) in CHALIS

Guide for labelling a CHALIS sample `glg` (ISO 639-3). Galician appears in two cousin pairs: **Portuguese vs Galician** and **Spanish vs Galician**. Markers come from `../chalis/discriminators.md`, `../chalis/discriminators/por-glg.tsv` and `spa-glg.tsv`. Important caveat: the Galician 10k list is from OpenSubtitles (dialogue), while Spanish and Portuguese lists are wordfreq; some Galician "markers" (*veña, merda, señor, papá*) and some missing words reflect subtitle genre rather than language.

## 1. Cousin-Pair Cues, Ranked by Reliability

### Galician vs Portuguese
1. **Absence of `ã/õ/ç` combined with presence of `ñ` or `ll`** in a text of reasonable length → Galician (official norm). Any `ã`, `õ`, `-ção` → Portuguese unless reintegrationist signs appear (see 3).
2. **Top function words:**
   - Galician: **non** (rank 4 in `vocabulary.json`), **unha** (10), **en**, **con**, **máis**, **xa**, **hai**, **cando**, **moi**, **iso**, **lle**, **tamén**, **sen**, **súa**, **miña**, **teño**, **aínda**, **che**, **vostede**, **polo/pola**, **coa**.
   - Portuguese: **em, não, uma, com, mas, você, tem, são, ele, muito, isso, já, também, quando, pela, sem, minha, depois**.
3. **Spelling of shared roots:** *-ción/-cións* vs *-ção/-ções*; *-ble* vs *-vel*; *-axe* vs *-agem*; *-za* vs *-ça* (*cabeza/cabeça*); *x* vs *j/g* (*xente/gente*, *xa/já*).
4. **Clitic writing:** solid *chámase, díxolle* (glg) vs hyphenated *chama-se, disse-lhe* (por).

### Galician vs Spanish
1. **Articles and negation:** `o, a, os, as` + `non` (glg) vs `el, la, los, las` + `no` (spa). One `non` or several article *o/os/as* before nouns is decisive.
2. **Markers** (spa-glg.tsv): Galician *unha, máis, ao, iso, meu, xa, hai, cando, ou, só, súa, miña, seu, agora, moi, onde, facer, foi, teño, isto, quen, vai, estou, lle, pode*; Spanish *sus, ya, yo, hay, fue, muy, también, tiene, puede, hasta, hacer, hace, ni, donde, mejor, mucho, mismo, siempre, tengo, después, estoy*.
3. **Contractions** `ao, aos, á, ás, do, da, no, na, polo, pola, co, coa, nun, dunha` (Spanish only *al, del*).
4. **Plural `-cións`**, no ie/ue diphthongs (*pode, tempo, novo*), letter **x** for /ʃ/.
5. Shared, not diagnostic: *de, que, en, a, se, por, es, con, para, como, me, pero, te, este, esta, todo, ser, son, está, así, porque, vez, nada, día, vida*.

## 2. When Diacritics Are Stripped

Galician is unusually robust: its best markers contain no diacritics — **non, unha, xa, moi, hai, cando, iso, isto, lle, che, sen, con, en, ou, polo, pola, coa, xente, facer, teño→teno**.

Collisions after stripping:
- **máis → mais**: merges with Galician *mais* "but" and Portuguese *mais* "more" — no longer diagnostic.
- **é → e** (merges with "and"), **á → a**, **só → so**, **súa → sua** (= Portuguese *sua*!), **aínda → ainda** (= Portuguese *ainda*!), **tamén → tamen** (still Galician; Port. *tambem*, Spa. *tambien*), **miña → mina**, **teño → teno**, **señor → senor**, **ningún → ningun**.
- **-ción → -cion**: equals stripped Spanish; the plural **-cions** vs Spanish **-ciones** still separates them (but equals Catalan *-cions* — Catalan has many other cues).
- **ñ → n** removes the anti-Portuguese signal; rely on *non/unha/xa/moi/cando* instead.

For Portuguese text, stripping produces *nao, tambem, -cao, -coes*, which never occur in Galician; for Spanish text, *y, los, muy, hay, ya, tambien* remain. Normalise homoglyphs (Cyrillic `о`, `а`, `е`, `с` in Latin words) and leetspeak digits before matching (general advice; exact CHALIS perturbations not reproduced here).

## 3. Short-Text Pitfalls and Code-Switching

- **Castilianisms** are normal in real Galician, especially subtitles and informal text: *pero* (normative, rank 25), *bueno, entonces, gracias, vale, sin embargo/sen embargo, estudiantes*. Do not switch to `spa` while `non`, `unha`, `xa`, `o/os/as`, `lle`, contractions or solid enclitics are present.
- **Older spelling** *ó, ós* (= *ao, aos*) appears in pre-2003 and some current texts, including the UD sample (`examples/ud_05.txt`: *permite ó ser humano*). It is Galician, not a typo.
- **Reintegrationist spelling** (*nom, umha, naçom, Galiza, também, trabalho*) is Galician (`glg`). Signs separating it from Portuguese: *nom, umha, -çom, polo/pola, -che, -des* 2pl, *Galiza*. Fully lusist text may be indistinguishable from PE (flag low confidence).
- **Shared Portuguese-Galician words** (*foi, agora, pode, vai, anos, até, só, ela*) are not Portuguese evidence.
- **Very short dialogue lines** (*"Si, vale."*, *"Que?"*, *"Ola!"*) are under-determined. *ola* (rank 133) is Galician/Portuguese spelling (Spanish *hola*, Portuguese *olá*); unaccented *si* "yes" fits Galician (Spanish *sí*), but stripped Spanish also yields *si*.
- Proper nouns (*Xunta, Ourense, Vigo, Santiago*) are weak evidence; Spanish text also uses *Xunta*.

## 4. Decision Checklist

1. Normalise homoglyphs/leet; note whether accents exist.
2. `ã/õ/ç`, `não/nao`, `-ção/-cao`, `uma`, `em`, `com`, hyphenated clitics? → **por**, unless `nom/umha/-çom/Galiza/polo` → **glg** (lusist).
3. `y`, `el/los/las` articles, `muy/hay/ya/yo/hasta/donde/tiene`, `¿`, `-ciones`? → **spa**.
4. `non`, `unha`, `xa`, `moi`, `hai`, `cando`, `iso/isto`, `lle/che`, `polo/pola/coa`, initial `x`, `-cións`, `ñ` with `o/os/as` articles → **glg**.
5. If only shared words remain: `o/a` articles + `en/con` → glg; `o/a` + `em/com` → por; `el/la` + `en/con` → spa.

## 5. Illustrative Snippets

**A.** *"Non sei se xa chegou, pero hai moita xente na rúa."* → **glg**. `non`, `xa`, `hai`, `xente` (+ *rúa*, *na*); *pero* is shared with Spanish and normative in Galician.

**B.** *"Eles tamen tenen unha casa preto do mar"* (stripped) → **glg**. `unha`, `tamen` (stripped *tamén*), `tenen` (stripped *teñen*); *preto do mar* would also fit Portuguese, but Portuguese would have *também têm uma*.

**C.** *"No sé si ya llegó, pero hay mucha gente en la calle."* → **spa** (the Spanish counterpart of A): `no`, `ya`, `hay`, `la`, `llegó`.
