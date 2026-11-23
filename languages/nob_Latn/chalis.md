# Norwegian Bokmål (nob) in CHALIS - Practical Identification Guide

In CHALIS (Tichý & Libovický 2026) Bokmål is tested against its cousin **Danish (dan)**. Gold labels are ISO 639-3: Bokmål is `nob` (not `nor`, not `nno`). Marker lists come from `chalis/discriminators.md` and `chalis/discriminators/dan-nob.tsv`; ranks from `nob_Latn/vocabulary.json` and `dan_Latn/vocabulary.json`. Details: `nob_Latn/differences.md`, `nob_Latn/characteristics.md`.

## 1. Bokmål vs Danish cues, ranked by reliability

**Tier A - very frequent, practically categorical**

| Bokmål (rank) | Danish (rank) |
|---|---|
| **å** + infinitive (5): *å gjøre, for å* | *at* + infinitive |
| **av** (10) | **af** (4) |
| **seg, meg, deg** (29, 44, 53) | **sig, mig, dig** |
| **noe, noen** (31, 33) | **noget, nogen, nogle** |
| **ble, blir, bli, blitt** (34, 46, ...) | **blev, bliver, blive, blevet** |
| **hva** (41) | **hvad** |
| **etter** (42) | **efter** |
| **hadde** (47) | **havde** |
| no *-igt* adjectives: *viktig, mulig* | *vigtigt, muligt* (Danish only) |

**Tier B - reliable, less frequent or with known exceptions**

- Words: *litt, mye, veldig, igjen, fikk, opp, ut, inn, enn, mot, oss, dere, vår/våre, kanskje, slik/sånn, bra, takk, vet, alltid, aldri, mellom, gjennom, tilbake, uten, sier*.
- *nå* (40) vs *nu*: Danish uses *nå* as an interjection ("well"), so *nå* at the start of a sentence followed by a comma is weak evidence.
- Spellings: **kj/gj/skj** (*kjenne, gjøre, skje*), **ei/øy** (*vei, nei, øye, høy*), hard stops after vowels (*mat, gate, bake, uke, måte, kjøpe*), **-het**, **-sjon**, **-skap**, **nn/ll** (*mann, finne, kvinne*), final double consonants (*takk, opp, litt, hatt*).
- Weak past/participle **-et/-a** (*startet, jobbet, kasta*) where Danish has *-ede*.
- Feminine forms: article *ei*, definite *-a* (*jenta, boka*); Danish has no feminine.
- Decimal numerals *tjue, tretti, femti* vs Danish *tyve, tredive, halvtreds*.

**Tier C - tendencies**

- Double definiteness *den store bilen*; postposed possessive *bilen min, huset vårt*.
- Existential *det er* rather than Danish *der er*.
- No comma before *at*-clauses (*Jeg tror at ...*); Danish often writes one.
- Lower proportion of *æ* than Danish (see `nob_Latn/characteristics.md`).

## 2. Cues that survive æ/ø/å replacement or stripping

With *ø→oe/o, å→aa/a, æ→ae/e*: the Tier A words *av, seg, meg, deg, noe, noen, ble, blir, hva, etter, hadde* are pure ASCII and survive intact, as do *litt, mye, igjen, fikk, opp, ut, enn, mot, oss, dere, kanskje, bra, takk*, every *kj/gj/skj, ei, -sjon, -het, -et* form, and hard-stop spellings (*mat, gate*). *gjøre→gjore/gjoere* still shows *gj*.

Lost or weakened: the infinitive marker *å* becomes *a* or *aa* (still usable: *for a*, *a gjore* are not English or Danish patterns), *nå→na/naa*, *vår→var* (collides with *var* "was"), *øy→oy/oey*. Danish *måske→maske* and *gør→gor* also lose their shape.

## 3. Short-text pitfalls

- Shared words are **not diagnostic**: *i, og, er, det, at, en, til, på, jeg, har, for, ikke, med, den, der, de, du, kan, som, så, et, var, vi, om, han, fra, men, skal, ved, vil, også, være, hvor, man, hvis, eller, her, alle, godt, da*.
- *at* is "that" in both; only *at* + bare infinitive is Danish.
- Conservative/Riksmål Norwegian can write *efter, nu, sprog, meget*; look for *hva, ble, noe, kj/gj* before choosing Danish.
- Informal Danish *hva'*, *ha'*, *ta'*, *gi'* resemble Bokmål *hva, ha, ta, gi* (uncertain frequency in CHALIS).
- Norwegian dialect writing (*æ* = "I", *ikkje, ka, mæ, dæ, sæ, itj*) is common online; it is Norwegian but may not be standard Bokmål - CHALIS gold for such text is not known to me, so treat `nob` vs `nno` as uncertain there. It is not Danish.
- One Nynorsk-looking token (*eg, ein, ikkje*) appears in Bokmål corpora too (ranks 1647, 5301, 6893 in the Bokmål list); require several before switching to `nno`.

## 4. Decision checklist

1. Scandinavian text? (*og, ikke, er, det*, æ/ø/å). If *ä/ö* → Swedish; if *ij, het, van, een* → Dutch.
2. Count Tier A markers on each side; a clear majority decides.
3. Otherwise Tier B words and spellings (*kj/gj/ei/-sjon/-het* vs *-tion/-hed/ej/soft d*).
4. Then Tier C syntax/punctuation tendencies.
5. Several Nynorsk forms (*ikkje, eg, kva, frå, berre, ho, mykje*) → `nno` rather than `nob`.
6. Only shared words → say it is ambiguous; do not default silently.

## 5. Illustrative snippets (constructed examples)

- *"Jeg tror ikke det er så lett å få tak i billetter nå."* → **nob**. *å få* (infinitive), *lett* (Da *let*), *nå*, *få tak i* (Da usually *få fat i*), no comma before the clause. Danish: *Jeg tror ikke, at det er så let at få fat i billetter nu.*
- *"Jeg tror ikke det er sa lett a fa tak i billetter na."* (stripped) → still **nob**: *lett*, *a fa* = *å få*, *na* = *nå*.
- *"Det ble mye bråk etter kampen, og politiet kom til slutt."* → **nob**: *ble, mye, etter*. Danish: *Der blev meget larm efter kampen ...*
