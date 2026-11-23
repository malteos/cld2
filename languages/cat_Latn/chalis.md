# Catalan (cat_Latn) in CHALIS

Guide for labelling a CHALIS sample `cat` (ISO 639-3; covers Valencian). Catalan's cousin pair is **Spanish vs Catalan** (`spa`/`cat`). Markers come from `../chalis/discriminators.md` and `../chalis/discriminators/spa-cat.tsv` (both lists are wordfreq, so the pair is relatively corpus-balanced). Background: `characteristics.md`, `differences.md` in this folder.

## 1. Cousin-Pair Cues, Ranked by Reliability

1. **Characters Spanish never uses:** middle dot **l·l** (*col·legi, intel·ligent*), grave accents **à è ò** (*això, què, però*), **ç** (*plaça, començar*). One occurrence is close to conclusive (exclude Portuguese via absence of `ã/õ`).
2. **Apostrophe elision**: **l'**, **d'**, **s'**, **n'**, **m'**, **t'** before a vowel (*l'any, d'una, s'ha, n'hi ha*), and hyphenated enclitics (*fer-ho, dir-li, anar-hi*). Spanish has neither.
3. **Articles and conjunction:** **els, les** (+ noun), **dels, als, pels**, conjunction **i** (rank 4 in `vocabulary.json`) vs Spanish **los, las, y**.
4. **Top markers** (spa-cat.tsv), Catalan side: *els, amb, és, més, dels, hi, aquest, però, tot, fer, seu, aquesta, molt, als, seva, també, ens, són, anys, això, estat, quan, ara, fins, què, perquè, després, només, sense, encara*. Spanish side: *sus, todo, cuando, fue, muy, también, tiene, porque, así, años, bien, puede, hasta, hacer, ahora, esto, nada, donde, mucho, siempre, después*.
5. **Periphrastic past** *vaig/vas/va/vam/vau/van* + infinitive (*va dir* "said"). Caution: Spanish *va a decir* ("is going to say") has *a*; Catalan *va dir* has no *a*.
6. **Endings:** *-ció/-cions*, *-tat/-tats*, *-at/-ada*, consonant-final masculines (*nou, tot, bo*), *ny* (*any, Catalunya*), final *-ix/-tx/-ig* (*baix, cotxe, mig*) vs Spanish *-ción/-ciones, -dad, -ado, -o, ñ*.

Shared and not diagnostic (from discriminators.md): *de, la, que, el, en, a, no, un, se, es, del, una, lo, al, si, o, ha, ser, sobre, nos, dos, entre, era, ni, tan, vida, han, cada, va, les, gran, contra, país, casa, forma, aquí, sí*. Note **les** is shared (Catalan article vs Spanish dative clitic) and **va** is shared (Catalan past auxiliary vs Spanish "goes").

## 2. When Diacritics Are Stripped

Catalan suffers most among the four languages, because several top markers differ from Spanish only by an accent:
- **és → es** (= Spanish *es*), **més → mes** (= Catalan/Spanish *mes* "month"), **però → pero** (= Spanish *pero*), **què → que**, **sí → si**, **també → tambe** (still Catalan; Spanish *tambien*), **això → aixo** (still Catalan), **perquè → perque** (still Catalan; Spanish *porque*), **després → despres** (Spanish *despues*), **només → nomes**, **són → son** (= Spanish *son*).
- **ç → c**: *plaça → placa*, *començar → comencar* (comencar is still non-Spanish).
- **l·l**: how CHALIS-style stripping treats the middle dot is uncertain (it may survive, become `l.l`, `l-l`, `ll` or `l l`). A token like *col.lectiu*, *intel-ligent* or *col lectiu* is still Catalan evidence.
- Diacritic-free Catalan markers survive: **els, amb, dels, als, pels, hi, ho, aquest, aquesta, tot, fer, molt, seva, ens, anys, quan, ara, fins, encara, sense, gent, dir, veure, aixo, perque, tambe**, plus apostrophes (*l'any*) and **i** as conjunction. Weight these.
- Spanish after stripping keeps **y, los, las, muy, hay, ya, cuando, hasta, donde, tiene, puede**.

Normalise homoglyphs and leetspeak (e.g. `4mb`, Cyrillic `а` in *аmb*) before matching (general advice; exact CHALIS perturbations not reproduced here).

## 3. Short-Text Pitfalls and Code-Switching

- **Castilianisms in Catalan** (*bueno, pues, vale, o sea, entonces*; also non-normative *luego, hasta*) are frequent in colloquial text. Keep `cat` if `els`, `amb`, `i`, `l'`, `però`, `és`, `molt` are present.
- **Spanish text with Catalan names** (*Generalitat, Diputació, Sant Jordi, Barcelona*) stays `spa`.
- **Valencian forms** look more Spanish: demonstratives *este, esta, eixe* (instead of *aquest, aquesta, aqueix*), *meua, seua, xiquet, hui, vore, eixir*, 1sg *-e* (*parle*). Still Catalan: look for *els, amb, i, l'*, *-ció*.
- **Balearic article** *es, sa, ses* (*sa platja, es poble*) may be mistaken for Spanish *es* "is"; *sa/ses* + noun is Catalan.
- **Very short strings** made of shared words (*"No sé"*, *"la casa"*, *"Es la vida"*) cannot be decided; *sé* and *casa* exist in both. Prefer the label of any single distinctive token; otherwise flag low confidence.
- Catalan vs **Occitan** (if ever relevant): Occitan *lh/nh*, *lo/los* articles, *pas*; vs **Portuguese**: Portuguese has `ã/õ`, *o/os/as*, *com, não*.

## 4. Decision Checklist

1. Normalise homoglyphs/leet; check whether accents are present.
2. `l·l` (or `l.l`/`l-l`), `à/è/ò`, `ç` without `ã/õ` → **cat**.
3. Apostrophe elision `l'/d'/s'/n'` + vowel, or hyphenated `-ho/-hi/-li/-los` enclitics → **cat** (French also elides: check for French *le, est, pas, avec*).
4. `els/dels/als/pels`, `amb`, `i` (and), `hi/ho/ens`, `aquest/aquesta/això`, `molt`, `quan`, `ara`, `fins` → **cat**.
5. `y`, `los/las`, `muy/hay/ya/cuando/hasta/donde/tiene/puede`, `ñ`, `¿` → **spa**.
6. Only shared tokens left (`es`, `pero`, `mes`, `son` after stripping): undecidable; note low confidence and lean by any morphology (`-ció` vs `-ción`; consonant-final vs `-o` endings).

## 5. Illustrative Snippets

**A.** *"Els nens van anar a l'escola amb la seva mare."* → **cat**. `els`, `van anar` (periphrastic past), `l'` elision, `amb`, `seva`.

**B.** *"Pero es mes facil aixi, tambe per als nens"* (stripped) → **cat**. *pero, es, mes* are ambiguous after stripping, but `tambe`, `aixi` (*així*), `als`, `nens` are Catalan; Spanish would be *Pero es más fácil así, también para los niños*.

**C.** *"Pero es más fácil así, también para los niños."* → **spa**. `más`, `también`, `para los`, `niños` (ñ).
