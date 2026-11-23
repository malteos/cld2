# Spanish (spa_Latn): Identification Characteristics

## Letter Inventory

Basic Latin a-z plus **ñ** (and *ü* in *güe/güi*: *pingüino*, *vergüenza*). Vowels take only the **acute accent**: **á é í ó ú**. Spanish never uses grave accents (à è ò), circumflex, tilde on vowels (ã õ), cedilla (ç) or the Catalan middle dot (l·l). *k* and *w* are confined to loans; *x* is mostly /ks/ (*examen*) or the Mexican /x/ in *México*, *Oaxaca*.

### Diagnostic characters and their value

| Feature | Value for LID |
|---|---|
| **¿ ¡** inverted question/exclamation marks | Practically unique to Spanish (Asturian and Galician writers sometimes use them too; mark as weaker for those) |
| **ñ** | Excludes Portuguese (nh) and Catalan (ny); shared with **Galician** and Asturian |
| **ll** | Shared with Catalan, Galician, Asturian; excludes Portuguese (lh) |
| **j** /x/ (*hijo, mujer, trabajo*) | Galician uses *x/ll* in cognates (*fillo, muller, traballo*); Portuguese uses *lh* (*filho, mulher, trabalho*) |
| acute-only accents, esp. **-ción, -ía, -ó** final | *-ó* on verbs (*habló*) has no Portuguese equivalent (-ou); Catalan uses *-ó* but with grave elsewhere |
| absence of ã õ ç à è ò l·l | A long text with accents but none of these strongly favours Spanish (or Galician) |

Unicode sample from the UD news examples (`examples/ud_*.txt`): non-ASCII letters were only ó, í, á, é, ñ, ú, in that order.

## Top Function Words

From `vocabulary.json` (wordfreq ranks; content words skipped):

de, la, que, el, en, y, a, los, no, un, se, por, es, del, las, con, una, para, lo, su, al, como, me, más, si, pero, te, o, mi, le, este, sus, esta, todo, ya, ha, cuando, yo, ser, son, sin, hay, está, fue, tu, muy, sobre, también, todos, eso, nos, porque, qué, así, entre, desde, hasta, ahora, esto, nada, ni, donde, mucho, después

The highest-yield Spanish-only items among these (see `../chalis/discriminators.md`):
- **y** (and) — Catalan *i*, Portuguese/Galician *e*. Spanish *e* only before /i/ (*e hijos*).
- **los, las, el** — Catalan *els/les*, Portuguese/Galician *os/as/o*.
- **con, una, para** (Cat. *amb, una, per*; Port. *com, uma, para*; Gal. *con, unha, para*).
- **muy, mucho** (Cat. *molt*, Port. *muito*, Gal. *moi, moito*).
- **hay, ya, yo, fue, hasta, cuando, también, después, siempre, puede, tiene**.
- **su/sus** (Port./Gal. *seu/sua/súa*, Cat. *seu/seva*).

## Frequent Character N-grams

Trigrams most frequent in the UD Spanish sample (small sample, about 2.5k words; indicative only): ` de`, `os `, `de `, ` la`, `es `, `as `, `el `, `la `, `que`, `ue `, `en `, ` y `, ` un`, `ent`, `los`, `nte`, `do `, `or `, `con`.

Characteristic sequences:
- **` y `** as a standalone word — very strong; it does not occur as a conjunction in Catalan, Portuguese or Galician.
- **`ie`, `ue`** diphthongs in stems: *tiempo, tiene, quiero, puede, nuevo, fuerza, pueblo*.
- **`ción`/`ciones`, `sión`/`siones`** (Port. *-ção/-ções*, Cat. *-ció/-cions*, Gal. *-ción/-cións*).
- **`ñ`** in `ño`, `ña`, `ñe`: *año, niño, España, señor, pequeño*.
- **`ll`** word-initially: *llegar, llamar, lleno* (Catalan also has initial *ll*; Portuguese/Galician use *ch* in cognates: *chegar/chamar*).
- **`j`** before a/o/u: *trabajo, hijo, mejor, junto, ejemplo*.
- Initial **h-** from Latin f-: *hacer, hijo, hasta, hablar* (Port./Gal. *fazer/facer, filho/fillo, até/ata, falar*; Cat. *fer, fill, fins, parlar*).

## Suffixes and Endings

Frequent 4-letter word endings in the UD sample: *-ente, -ción, -ncia, -ones, -ista, -ados, -ante, -ales, -idad, -sión, -ores, -able*. LID-relevant ones:

- **-idad / -idades** (Port./Gal. *-idade*, Cat. *-itat*).
- **-ción / -ciones** (only the plural *-ciones* separates it from Galician *-cións*).
- **-mente** adverbs (shared with Portuguese/Galician; Catalan *-ment*).
- **-ado/-ada/-ido/-ida** participles; Catalan *-at/-ada/-it/-ida*.
- **-aba/-ía** imperfect, **-ó/-aron** preterite (Port./Gal. *-ou/-aram/-aron*).
- **-ble** (*posible*); Catalan *-ble*, Portuguese *-vel* (*possível*).
- **-eza, -dad, -aje** (Port. *-eza, -dade, -agem*).

## Orthographic Conventions

- No apostrophe elision (Catalan *l'any, d'una*; Spanish *el año, de una*).
- Clitics written attached to infinitives/gerunds/imperatives without hyphen (*decirle*, *dámelo*); with finite verbs they precede and stand apart (*se lo dije*). Portuguese uses hyphens (*disse-lhe*); Galician attaches enclitics even to finite verbs (*díxolle*).
- Accented interrogatives *qué, cómo, dónde, cuándo, quién*; diacritic pairs *él/el, tú/tu, mí/mi, sí/si, más/mas, sé/se, té/te*.
- Doubled consonants are rare except *cc* (*acción*), *ll*, *rr*; no *ss*, *mm* (Portuguese has *ss*; Catalan *ss*, *l·l*).
- Numbers and dates use *de*: *10 de noviembre de 1989*.

## Short-Text Notes

Short Spanish strings consisting only of shared words (*de, la, que, en, no, se, es, como, para, todo, vida*) cannot be separated from Catalan, Galician or Portuguese with confidence. The first `y`, `los/las`, `ñ`, `¿`, or an `ie/ue` stem usually settles it.
