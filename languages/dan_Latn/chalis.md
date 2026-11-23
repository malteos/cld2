# Danish (dan) in CHALIS - Practical Identification Guide

CHALIS (Tichý & Libovický 2026) pairs Danish mainly with **Norwegian Bokmål (nob)**; Dutch (nld) is the West Germanic contrast. Gold labels are ISO 639-3. Marker lists below come from `chalis/discriminators.md` and `chalis/discriminators/dan-nob.tsv` (top-1500 words of one language absent from the other's 10k list); ranks are from `dan_Latn/vocabulary.json` and `nob_Latn/vocabulary.json`. See also `dan_Latn/differences.md` (note: that file renders æ/ø/å as ae/oe/aa) and `nob_Latn/differences.md`.

## 1. Danish vs Bokmål cues, ranked by reliability

**Tier A - very frequent and practically categorical**

| Danish | Bokmål |
|---|---|
| *at* + infinitive (*at gøre, for at se*) | *å* + infinitive (*å gjøre, for å se*) |
| **sig, mig, dig** | **seg, meg, deg** |
| **noget, nogen, nogle** | **noe, noen** |
| **blev, bliver, blive, blevet** | **ble, blir, bli, blitt** |
| **havde** | **hadde** |
| **hvad** | **hva** |
| **efter** | **etter** |
| **af** (rank 4) | **av** (rank 10) |
| adjectives/adverbs in **-igt** (*vigtigt, muligt, hurtigt*; 117 in Danish 10k, 0 in Bokmål 10k) | *viktig, mulig, fort* |

Caution: Danish *av* exists as the interjection "ouch" (Danish rank 1871); Bokmål *af* is rare (9132).

**Tier B - reliable, slightly less frequent or with exceptions**

- *lidt / litt*, *igen / igjen*, *fik / fikk*, *ud, op, ind / ut, opp, inn*, *end / enn*, *mod / mot*, *meget / mye, veldig*, *vores / vår, våre*, *jer, I / dere*, *os / oss*, *måske / kanskje*, *sådan / slik, sånn*, *tak / takk*, *altid, aldrig / alltid, aldri*, *mellem, gennem, tilbage / mellom, gjennom, tilbake*.
- *nu / nå*: Danish also uses the interjection *nå* (rank 425), and conservative Norwegian occasionally writes *nu*; check other cues.
- Spelling rules: soft *b/d/g* after vowels (*mad, gade, bage, uge, købe, måde*) vs *mat, gate, bake, uke, kjøpe, måte*; **-hed** vs **-het**; **-tion** vs **-sjon**; **-skab** vs **-skap**; **ej/øj** (*vej, nej, øje, høj*) vs **ei/øy**; **nd** (*mand, finde, kvinde*) vs **nn**; *k/g/sk* (*kende, gøre, ske*) vs *kj/gj/skj*.
- Weak past **-ede** (*startede, arbejdede*) vs *-et/-a*.
- Vigesimal numerals *tyve, tredive, halvtreds, tres, firs, halvfems* vs *tjue, tretti, femti*.

**Tier C - tendencies, use only to break ties**

- Existential *der er / der var* (Danish *der* rank 16) vs Bokmål *det er*.
- No double definiteness: *den store bil* (Da) vs *den store bilen* (Nb).
- Comma before *at*-clauses (*Jeg tror, at ...*) is common in Danish and not used in Bokmål (tendency; Danish comma rules allow both).
- Definite plural *-erne* on non-agent nouns (*pigerne, bilerne*) vs *-ene*.
- More *æ* in Danish (*tænke, læse, kendt* vs *tenke, lese, kjent*).

## 2. Cues that survive æ/ø/å replacement or stripping

If *æ→ae, ø→oe, å→aa* or the letters are dropped (*paa/pa, gøre→goere/gore*), these still work: *sig, mig, dig, noget, nogen, nogle, blev, bliver, havde, hvad, efter, af, lidt, igen, fik, ud, ind, end, mod, meget, vores, altid, aldrig, mellem, gennem, tilbage, uden, siger*, every *-igt, -hed, -tion, -ede* word, *ej* spellings and soft consonants. On the Norwegian side *kj/gj/skj, ei, -sjon, -het* survive.

Lost or ambiguous after stripping: *måske→maske*, *gør→gor*, *nu/nå→na*, and the infinitive marker *å→a/aa* (Norwegian *a gjore* still signals nob). Note that *aa* was genuine Danish spelling before 1948 and survives in names (*Aarhus, Aalborg*).

## 3. Short-text pitfalls

- Shared top words carry **no signal**: *i, og, er, det, at, en, til, på, jeg, har, for, ikke, med, den, der, de, du, kan, som, så, et, var, vi, om, han, fra, men, skal, ved, vil, også, være, hvor, man, hvis, eller, her, alle, godt, da*. A sentence built only from these (*Det er ikke min skyld*) is undecidable; do not guess from *ikke* or *jeg*.
- *at* alone is ambiguous: it is "that" in both languages; it is Danish only when followed by an infinitive.
- Informal Danish writing uses apostrophe short forms (*ha', ta', gi', hva', ik'*) that resemble Norwegian *ha, ta, gi, hva*; look for the apostrophe and for Danish forms nearby (uncertain how frequent in CHALIS).
- Norwegian dialect spelling online (*æ* "I", *ikkje, ka, dæ, mæ*) is still Norwegian, not Danish.
- Names and topics (*København, Oslo, kr*) help but can mislead in cross-border news.

## 4. Decision checklist

1. Any *æ/ø/å* or a Scandinavian function word (*og, ikke, jeg, er*)? If not, check Dutch (`nld_Latn/chalis.md`).
2. Count Tier A markers for each side. Two or more on one side and none on the other: decide.
3. Otherwise count Tier B (word and spelling) markers.
4. Still tied: Tier C tendencies.
5. Nynorsk forms (*ikkje, eg, ein, kva, frå, berre*) point away from Danish.
6. If nothing discriminates, report low confidence rather than inventing a reason.

## 5. Illustrative snippets (constructed examples)

- *"Vi har ikke fået noget at vide endnu, men det bliver nok i morgen."* → **dan**. *fået, noget, at vide* (at + infinitive), *endnu, bliver*. Bokmål: *fått noe å vite ennå ... blir*.
- *"Jeg synes det var lidt for meget, ærligt talt."* → **dan**. *lidt, meget, ærligt* (-igt). Bokmål: *litt for mye, ærlig talt*.
- *"Det er godt for dem."* → **undecidable** between dan and nob; every word is shared.
