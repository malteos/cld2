# Dutch (Nederlands) - Language Identification Characteristics

## Characters

Dutch uses the plain 26-letter Latin alphabet. There are **no letters outside a-z** in ordinary words, which by itself separates Dutch from Danish/Norwegian (æ, ø, å), German (ä, ö, ü, ß), Frisian (â, ê, ô, û, ú) and most Romance languages.

Diacritics that do occur:

- **Diaeresis (trema)** to mark a vowel-hiatus: *ë, ï, ü, ö* - *ideeën, financiële, België, Israëlische, geïnteresseerd, reünie*. 27 of the top 5,000 entries in `vocabulary.json` contain *ë*. The trema is a good positive Dutch cue: German uses ö/ü as separate vowels, never *ë/ï*.
- **Acute accent** for emphasis (*één, dé, vóór, wél*) and in loans (*café, privé*). *één* "one" is in the top 200.
- **Apostrophe** in plurals and possessives after vowels (*foto's, auto's, collega's, Anna's*), in clitic spellings (*zo'n, m'n, z'n, 's ochtends, 't*), and in *d'r*. *zo'n* (rank 246), *m'n* (451), *z'n* (790) are in the 10k list.

## The ij Digraph

**ij** (/ɛi/) is the most recognisable Dutch spelling: *zijn, mijn, bij, wij, hij, tijd, krijgen, blijven, -lijk*. 329 of the top 5,000 words contain *ij*. It is treated as one letter (capitalised *IJ* together: *IJsselmeer*). The ligature **ĳ** (U+0133) exists in Unicode but does not occur in the vocabulary list; expect plain *ij*. In sloppy or old typing *y* may replace *ij* (*zyn, wy*), which can resemble Afrikaans (`afr_Latn/`).

Danish, Norwegian and German practically never have *ij* inside a native word, so even one *ij* word is strong evidence against them.

## Doubled Vowels and Other Vowel Spellings

Long vowels in closed syllables are doubled: **aa** (386 words in the top 5,000), **ee** (275), **oo** (232), **uu** (38): *jaar, maar, naar, staat, veel, een, meer, voor, door, ook, uur, duur*. Further typical vowel digraphs: **oe** (*goed, moet, boek*; 223), **ie** (*die, niet, iets*; 380), **ui** (*uit, huis, buiten*; 137), **eu** (*leuk, deur*), **ou** (*oud, zou, vrouw*). In Danish/Norwegian *aa* is only an old spelling of å, and *oe* occurs only as an ASCII stand-in for ø (see `nld_Latn/chalis.md`).

## Top 50 Words (vocabulary.json, rank order)

de, van, het, een, en, in, is, op, ik, dat, voor, je, te, met, niet, zijn, die, als, er, maar, om, aan, hij, ook, ze, door, naar, uit, bij, dan, dit, was, we, wat, heeft, of, over, nog, deze, hebben, kan, meer, zo, al, geen, mijn, wel, tot, u, wordt

Highly diagnostic among them (absent from the Danish 10k list according to `chalis/discriminators.md`): **het, dat, voor, je, met, niet, zijn, maar, aan, hij, ook, ze, door, uit, bij, was, wat, heeft, nog, deze, hebben, meer, zo, geen, mijn**. Shared with Danish/Norwegian spelling but with different meaning: *de, en, op, er, om, dit, over, kan, nu, hun, man, af*. Shared with German: *in, was, so (zo), kan*. Shared with English: *in, is, over, was*.

## Frequent N-grams

From the UD passages in `examples/ud_*.txt` (small sample; indicative):

- Bigrams: `en`, `de`, `er`, `te`, `an`, `ee`, `st`, `ge`, `in`, `aa`, `et`, `ie`, `el`, `he`, `ij`, `nd`.
- Trigrams: `en_`, `de_`, `_de`, `et_`, `an_`, `_he`, `_va`, `van`, `het`, `een`, `nde`, `ter`, `_ge`, `_ee`, `oor`, `aan`, `aar`.

*van, het, een, aan, oor, aar* and the bigram *ij* are the most Dutch-specific; *en_, de_, er_* are shared with Scandinavian and German.

## Morphology

- **-en** dominates word endings: infinitives, plurals, plural verbs (963 of the top 5,000 words end in *-en*).
- **ge-** participles: *gemaakt, gedaan, gezien, geweest* (270 top-5,000 words start with *ge-*).
- **-lijk / -lijke** adjectives and adverbs: *mogelijk, eigenlijk, duidelijk, belangrijk* (German *-lich*, Danish *-lig*).
- **-heid**: *vrijheid, waarheid, mogelijkheid* (German *-heit*, Danish *-hed*, Norwegian *-het*).
- **-ing**: *regering, opleiding*; **-tie** (Latinate): *informatie, situatie, politie* (German/Danish *-tion*, Norwegian *-sjon*).
- **-isch(e)**: *technisch, praktische, economische*; adjectives of place in **-se**: *Nederlandse, Amsterdamse, Amerikaanse*.
- Diminutives **-je/-tje/-pje**: *meisje, beetje, huisje*.
- **-baar**: *beschikbaar, zichtbaar*.
- **sch-** initial and **-cht** clusters: *school, schrijven, nacht, echt, recht*.

## Orthographic Conventions

- Nouns are **not capitalised** (unlike German).
- Compounds are written solid (*gemeenteraadsverkiezingen*), with a linking *-s-* or *-en-* (*pannenkoek*); hyphen when vowels clash (*zee-egel*, *auto-ongeluk*).
- *'s* at word start in time/place expressions: *'s avonds, 's-Hertogenbosch*.
- Newspaper text often has low-high quotes „..." typed as `,,` ... `''` (seen in `examples/ud_07.txt`).
- Official spelling is the *Groene Boekje* (2005/2015); *pannenkoek*-type rules apply in both the Netherlands and Flanders.
- Abbreviations: *bijv.*, *o.a.* (onder andere), *d.w.z.*, *enz.*, *m.b.t.*

## Key Identification Heuristics

1. Any **ij** word plus doubled vowels (*aa, ee, oo*) and no æ/ø/å/ä/ß.
2. Function words **het, van, een, niet, zijn, voor, dat, met, ook, wat, maar**.
3. **ge-...-t/-d/-en** participles and **-lijk/-heid/-tje** suffixes.
4. Trema (*ë, ï*) and apostrophe plurals (*foto's*).
5. Single negation with *niet/geen* (not Afrikaans *nie...nie*), article *de/het* (not Afrikaans *die*, Frisian *de/it*).
