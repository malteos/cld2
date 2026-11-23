# Portuguese (por_Latn): Identification Characteristics

## Letter Inventory

Latin a-z (k, w, y since the 1990 Agreement, mostly in loans) plus:

| Character | Use | LID value |
|---|---|---|
| **ã, õ** | nasal vowels/diphthongs: *não, mão, irmã, informações, põe* | Strongest single signal; not used by Spanish, Catalan or standard (RAG) Galician |
| **ç** | /s/ before a, o, u: *ação, começar, praça, cabeça* | Shared with Catalan and French; excludes Spanish and RAG Galician |
| **â, ê, ô** | closed vowels: *você, três, português, avô, câmara* | Circumflex excludes Spanish, Catalan, Galician |
| **á, é, í, ó, ú** | open/stressed vowels: *é, já, só, família* | shared with others |
| **à** | crasis only (*à, às, àquele*) | Catalan also has à, but in other words (*això, català*) |
| **ü** | pre-2009 PB only (*lingüística, freqüente*) | archaic marker of older PB text |

In the UD news sample (`examples/ud_*.txt`), non-ASCII letters by frequency were: ã, ç, í, é, á, ú, ê, ó, à, õ, â, ô. That **ã** outranks every acute vowel is itself a fingerprint (Spanish and Galician samples are led by ó/í).

### Digraphs

- **nh** (*minha, tenho, senhor, ninguém*) vs Spanish *ñ*, Catalan *ny*. Galician RAG uses *nh* only in *unha/algunha/ningunha*.
- **lh** (*filho, trabalho, melhor, mulher*) vs Spanish/Galician *ll* (*hijo/fillo*), Catalan *ll*.
- **ss** between vowels (*pessoas, isso, nosso, posso*): Spanish and Galician have no *ss*; Catalan does (*passat*).
- **-m** word-finally for nasal: *um, em, com, sem, tem, bem, também, homem*. Spanish/Galician/Catalan never end common function words in *-m* (Catalan *amb* ends in *-mb*).

## Top Function Words

From `vocabulary.json` (wordfreq, mixed PE/PB web text; content words skipped):

de, a, o, que, e, do, em, da, é, para, não, um, uma, com, no, se, na, por, os, eu, como, as, mais, dos, mas, foi, ao, me, você, ser, seu, sua, tem, são, das, ou, à, ele, muito, isso, já, nos, também, quando, está, meu, pelo, ela, vai, só, pela, sobre, bem, até, mesmo, pode, ter, tudo, ainda, aqui, sem

Portuguese-only items versus Galician (`../chalis/discriminators/por-glg.tsv`): **em, não, uma, com, mas, você, tem, são, ele, muito, isso, já, também, quando, pela, bem, tudo, fazer, minha, quem, sem, assim, depois, estão**. Versus Spanish (`spa-por.tsv`): **não, um, uma, mais, foi, ao, você, seu, sua, tem, ou, ele, muito, isso, já, também, quando, meu, ela, vai, só, pela, bem, até**.

## Frequent Character N-grams

Trigrams most frequent in the small UD sample (about 1.7k words, indicative): ` de`, `os `, `de `, `do `, ` co`, `as `, **`ão `**, `que`, ` se`, ` o `, `o d`, `ent`, ` a `, ` e `, `da `, `em `, ` um`, `com`.

Characteristic sequences:
- **`ão`, `ões`, `ção`, `ções`, `ães`**.
- **` o `, ` a `, ` os `, ` e `** as standalone words (articles/conjunction), shared with Galician but not Spanish/Catalan.
- **`lh`, `nh`, `ss`, `ç`**.
- **`ei`, `ou`** diphthongs: *primeiro, dinheiro, falou, outro, pouco* (Spanish *primero, dinero, habló, otro, poco*). Galician shares these.
- Final **`-mente`**, **`-dade`**, **`-agem`** (*viagem*), **`-vel`** (*possível, incrível*).

## Suffixes and Endings

Frequent endings in the UD sample: *-dade, -ente, -ação, -ados, -ento, -ante, -ador, -ando, -eiro*.

- **-ção / -ções** (Spanish *-ción/-ciones*, Galician *-ción/-cións*, Catalan *-ció/-cions*).
- **-dade, -idade** (Galician same; Spanish *-dad*; Catalan *-tat*).
- **-vel / -veis** (*possível, responsáveis*) — Spanish/Galician *-ble*.
- **-agem** (*mensagem, viagem*) — Spanish *-aje*, Galician *-axe*.
- **-eiro/-eira** (shared with Galician; Spanish *-ero*).
- Verb endings **-ou** (3sg pret.), **-aram/-eram** (3pl pret.), **-am/-em** (3pl pres.), **-ava** (impf.), **-ando/-endo** (gerund, common in PB).

## Orthographic Conventions

- **Hyphenated clitics** (*disse-lhe, chama-se, fazê-lo, dir-lhe-ei*) — a near-unique Portuguese convention among these languages; Galician and Spanish write enclitics solid.
- Crasis **à/às**; circumflex on *você, três, mês, pôr, pôde*.
- **1990 Orthographic Agreement** (in force in Brazil since 2009, Portugal since about 2009-2015): dropped silent *c/p* in PE (*acção → ação*, *óptimo → ótimo*), the PB trema (*freqüente → frequente*) and some PB accents (*idéia → ideia*, *vôo → voo*). Older texts show the pre-reform spellings; both are `por`.
- PE vs PB accent differences persist: PE *económico, género, António, facto*; PB *econômico, gênero, Antônio, fato*.
- **pra** (rank 134) is a frequent informal contraction of *para* (mainly PB); *tá, tô, cê, né, vc, pq, tb* appear in informal web/chat text.

## Short-Text Notes

A single **ã/õ**, **não**, **você**, **uma**, **com** or hyphenated clitic is usually enough to separate Portuguese from Spanish and Galician. Texts of only *de, o, a, que, e, do, da, é, para, no, se, na, por, os* are Portuguese-or-Galician ambiguous; see `differences.md` and `chalis.md`.
