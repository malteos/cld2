# Portuguese (por_Latn) in CHALIS

Guide for labelling a CHALIS sample `por` (ISO 639-3). The direct cousin pair is **Portuguese vs Galician** (`glg`); Spanish (`spa`) is the second main competitor. Markers are from `../chalis/discriminators.md`, `../chalis/discriminators/por-glg.tsv` and `spa-por.tsv`. Both European and Brazilian Portuguese are `por`. Caveat from the discriminators file: the Portuguese list is wordfreq (web/news/subtitles mix), the Galician list is OpenSubtitles only, so a few markers (e.g. *pessoas*, *site*, *twitter*, *brasileiro*) reflect corpus genre rather than grammar.

## 1. Cousin-Pair Cues, Ranked by Reliability

### Portuguese vs Galician
1. **Nasal tilde:** `ã`, `õ`, `-ão`, `-ção`, `-ções`, `não`, `são`, `estão`, `mãe`. Official Galician never uses them (reintegrationist Galician may — see section 3).
2. **Very frequent function words:**
   - Portuguese: **em** (rank 7), **não** (11), **uma** (13), **com** (14), **mas** (25), **você** (29), **tem**, **são**, **ele**, **muito**, **isso**, **já**, **também**, **quando**, **pela**, **sem**, **minha**, **depois**.
   - Galician: **non** (rank 4), **unha** (10), **en**, **con**, **máis**, **xa**, **hai**, **cando**, **moi**, **iso**, **lle**, **tamén**, **sen**, **miña**, **teño**, **aínda**, **che**, **vostede**.
   `em` vs `en` and `com` vs `con` alone separate most sentences of 10+ words.
3. **Digraphs:** `nh`, `lh`, `ç`, `ss` → Portuguese; `ñ`, `ll`, initial `x` (*xa, xente, xeito*) → Galician.
4. **Endings:** `-ção/-ções`, `-vel`, `-agem`, 3pl `-am/-em` (Portuguese) vs `-ción/-cións`, `-ble`, `-axe`, 3pl `-an/-en` (Galician).
5. **Clitic spelling:** hyphen (*chama-se*, *disse-lhe*) = Portuguese; solid (*chámase*, *díxolle*) = Galician.

Shared top words (useless): *de, a, o, que, e, do, da, é, para, no, se, na, por, os, eu, como, as, mais, dos, foi, ao, me, ser, seu, ou, está, meu, ela, vai, só, sobre, agora*.

### Portuguese vs Spanish
1. `ã/õ/ç`, `nh/lh` vs `ñ/ll/¿`.
2. Portuguese *não, um, uma, em, com, ao, você, muito, isso, já, também, quando, meu, ela, vai, só, até*; Spanish *pero, cuando, hay, fue, muy, también, eso, tiene, qué, así, años, hasta, hacer, ahora*.
3. Articles `o/os/as` + `e` (and) vs `el/los/las` + `y`.

## 2. When Diacritics Are Stripped

Portuguese loses its best signal (`ã/õ/ç`), but the residues remain distinctive:
- **não → nao**, **são → sao**, **estão → estao**, **então → entao**, **mãe → mae**: *nao* is attested in the Portuguese list (rank ~1160, informal writing) and absent from the Galician and Spanish lists. *nao/sao/estao* are therefore still Portuguese cues.
- **-ção → -cao**, **-ções → -coes**: unique to stripped Portuguese (Galician *-cion/-cions*, Spanish *-cion/-ciones*, Catalan *-cio/-cions*).
- **também → tambem** (Gal. *tamen*, Spa. *tambien*, Cat. *tambe*), **você → voce**, **já → ja** (also Catalan *ja*!), **está → esta** (shared with Spanish/Galician *esta*), **é → e** (merges with "and"), **até → ate**, **só → so**.
- **mas** is ambiguous: Portuguese "but" (rank 25) and accent-stripped Spanish *más* (Spanish *mas* rank 100). Galician *máis → mais* collides with Portuguese *mais* "more". Neither *mas* nor *mais* is usable after stripping.
- Diacritic-free Portuguese markers survive unchanged: **em, uma, um, com, sem, tem, bem, muito, isso, quando, pela, pelo, minha, depois, fazer, lhe, dele, nossa**. Weight these most.
- Galician competitors also survive unchanged: **non, unha, xa, moi, cando, hai, iso, lle, sen, con, en**. So stripped por-vs-glg remains easy; stripped por-vs-spa relies on *em/com/um/uma/muito* vs *en/con/un/una/muy*.

Homoglyphs (Cyrillic `а е о с р` in Latin words) and leetspeak digits should be normalised first; a Cyrillic *о* inside *nãо* is still *não*. (General advice; the exact CHALIS perturbation set is not reproduced here.)

## 3. Short-Text Pitfalls and Code-Switching

- **Reintegrationist Galician** looks Portuguese: *nom, umha, naçom, Galiza, polo/pola, dou-che, fazedes*. If any of these appear, prefer `glg`. Fully lusist text using *não/uma* with no Galician-specific lexicon is genuinely ambiguous; default to `por` but flag low confidence (uncertain how CHALIS sources such text).
- **Galician with Portuguese-like forms** (*foi, agora, pode, mais, até* are shared) — do not let them pull toward `por`; look for `non/unha/xa/moi`.
- **Short PB chat** (*vc, pq, tb, blz, kkkk, né, tá, pra*) is Portuguese; *kkkk* laughter and *vc/pq* abbreviations are typical Brazilian internet style (Spanish uses *jajaja*, *q*, *xq*).
- **Portuñol**: mixed Spanish-Portuguese from border areas; label by the majority of function words (*em/com/não* vs *en/con/no*).
- **Spanish-looking Portuguese**: *no* ("in the"), *como*, *para*, *todo*, *nada*, *esta*, *vida*, *casa* do not indicate Spanish.
- Proper nouns (*Brasil*, *São Paulo*, *Lisboa*) are weak evidence; *Galiza/Galicia* names can occur in either language.

## 4. Decision Checklist

1. Normalise homoglyphs/leet; check whether diacritics are present at all.
2. Any `ã/õ/-ção/-ções` or stripped `nao/-cao/-coes`? → lean **por**; check for reintegrationist Galician signs (`nom`, `umha`, `-çom`, `Galiza`, `-des` 2pl, *che*).
3. `non`, `unha`, `xa`, `moi`, `hai`, `cando`, `lle`, `ñ`, initial `x` → **glg**.
4. `em`, `com`, `uma`, `muito`, `você`, `isso`, `sem`, `minha`, `lh/nh` → **por**.
5. `y`, `el/los/las`, `muy`, `hay`, `pero`, `ñ`, `¿` → **spa**.
6. Only shared words (*de, o, a, que, é, para, foi*): por and glg both possible; a hyphenated clitic or `-m` final function word decides; otherwise label with low confidence.

## 5. Illustrative Snippets

**A.** *"Eu não sei se ele já foi embora."* → **por**. `não`, `ele`, `já` are por-glg markers; Galician would be *Eu non sei se el xa marchou*.

**B.** *"Nao tenho tempo pra isso agora"* (stripped) → **por**. `nao` (stripped *não*), `tenho` (Gal. *teño*), `pra`, `isso` (Gal. *iso*); *tempo* and *agora* are shared.

**C.** *"Eu nom sei se ele já marchou, mas umha cousa é certa."* → **glg** (reintegrationist spelling). Despite *já* and *ele*, `nom`, `umha`, and *marchou*/*cousa* point to Galician.
