# Dutch (nld) in CHALIS - Practical Identification Guide

CHALIS (Tichý & Libovický 2026) includes Dutch alongside the cousin pairs. Which language Dutch is paired with in the benchmark is not documented in this repository; the only Dutch comparison in `chalis/discriminators.md` is **nld vs dan**, so this guide covers that contrast plus the West Germanic neighbours that can look like Dutch in non-standard text (Afrikaans, Frisian, German, Flemish spellings). Gold label: `nld` for all Dutch, Netherlandic or Belgian. Details: `nld_Latn/differences.md`, `nld_Latn/characteristics.md`.

## 1. Cues ranked by reliability

**Tier A - categorical for Dutch vs Danish/Norwegian**

- Dutch markers absent from the Danish 10k list (`chalis/discriminators/nld-dan.tsv`): **het, dat, voor, je, met, niet, zijn, maar, aan, hij, ook, ze, door, uit, bij, was, wat, heeft, nog, deze, hebben, meer, zo, geen, mijn**.
- Danish markers absent from the Dutch list: **og, det, til, på, jeg, har, ikke, med, så, fra, skal, ved, vil, også, være, hvor, hvis, sig, efter, mig, eller, hvad, ud, godt, meget**.
- The digraph **ij** (*zijn, bij, tijd, -lijk*): practically never in native Danish/Norwegian words.
- Letters æ/ø/å (genuine, not ASCII stand-ins) exclude Dutch.

**Tier B - strong**

- Doubled vowels **aa, ee, oo, uu** in closed syllables (*jaar, veel, voor, uur*) and **oe, ui, eu, ie** digraphs.
- **ge-** participles (*gemaakt, gezien*), **-heid, -lijk, -tje/-je, -tie**.
- Preposed articles *de/het/een* rather than suffixed *-en/-et*.
- Danish **hv-** words, **-hed, -tion, -igt** endings exclude Dutch.

**Tier C - weak**

- Words spelled identically in both (see section 3).
- Character n-grams *en_, er_, de_* (shared).

For Dutch vs Afrikaans/Frisian/German the strongest cues are: **ij** (Afrikaans/Frisian *y*), **het/niet/ik/zijn** (Afrikaans *die/nie/ek/is*; Frisian *it/net/ik/binne*), single negation, no noun capitalisation and no ä/ö/ü/ß (German).

## 2. Cues that survive diacritic replacement or stripping

Dutch is written almost entirely in ASCII, so stripping changes little: *één→een*, *ideeën→ideeen*, *België→Belgie*. All Tier A Dutch markers are ASCII.

The real hazard runs the other way: Danish/Norwegian text with **ø→oe** and **å→aa** acquires Dutch-looking digraphs (*goere* "gøre", *moede* "møde", *paa* "på", *gaa* "gå", *maa* "må"). Pre-1948 Danish also wrote *aa* genuinely. Rule: *oe/aa* count for Dutch only if Dutch function words are also present; *paa, maa, faa, gaa* as whole words are Scandinavian, not Dutch (Dutch has *ga, gaat, staat, maar*).

## 3. Short-text pitfalls

- Spellings shared with Danish (`chalis/discriminators.md`): *de, en, op, er, om, dit, over, kan, nu, hun, dag, alle, ja, man, af, hele*. Several are false friends: *en* (nl "and" / da "a"), *er* (nl "there" / da "is"), *hun* (nl "their" / da "she"), *dit* (nl "this" / da "your"), *om* (nl "around, in order to" / da "about, whether"). A fragment such as *"Hun dag er over"* or *"Ja, man kan"* is ambiguous.
- Colloquial and Flemish writing: *nie* for *niet*, *da* for *dat*, *ge/gij* for *je/jij*, *k* for *ik* (*'k heb*), *ken* for *kan*, chat abbreviations (*ff* = even, *idd* = inderdaad, *mss* = misschien, *wss* = waarschijnlijk). These remain `nld`; *nie* does not make a text Afrikaans unless it is double negation with Afrikaans pronouns (*ek, jy, hulle*) and *die* as article.
- Old or sloppy *y* for *ij* (*zyn, myn*) resembles Afrikaans; check articles and verb inflection.
- English loans (*online, website, team*) are frequent in Dutch and are neutral.

## 4. Decision checklist

1. Genuine æ/ø/å or *og, ikke, jeg, hvad*? → Scandinavian (see `dan_Latn/chalis.md`, `nob_Latn/chalis.md`).
2. *ij* plus *het/van/een/niet/zijn*? → `nld`.
3. *oe/aa* without Dutch function words? → suspect ASCII-transliterated Danish/Norwegian.
4. Capitalised nouns, *ä/ö/ü/ß*, *und, nicht, ist* → German; *die, nie...nie, ek, is* everywhere → Afrikaans; *it, net, yn, fan*, â/ê/û → Frisian.
5. Flemish forms (*gij, ge, goesting, amai, nie*) → still `nld`.
6. Only shared tokens → ambiguous; say so.

## 5. Illustrative snippets (constructed examples)

- *"Ik heb er geen zin in, maar we moeten toch even naar de winkel."* → **nld**: *ik, heb, geen, maar, moeten, toch, even, naar*; *er* here is the Dutch pronominal adverb.
- *"Hun er på arbejde hele dagen, men kan komme over i aften."* → **dan**, despite *hun, er, hele, kan, over* (all shared spellings) and *men* (also a Dutch word, "one/people"): *på, arbejde, dagen* (suffixed article), *komme, aften*; *er* is a verb after a pronoun subject. Dutch: *Zij is de hele dag aan het werk, maar kan vanavond langskomen.*
- *"Da's nie waar, ge moet da nie geloven."* → **nld** (Flemish colloquial): *ge moet, geloven, waar*; *nie/da* are colloquial Dutch, not Afrikaans (Afrikaans: *Dis nie waar nie, jy moet dit nie glo nie*).
