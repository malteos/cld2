# Norwegian Bokmål (norsk bokmål) - Language Identification Characteristics

## Distinctive Characters

Bokmål uses the 26 Latin letters plus **æ, ø, å** (alphabetized after z), exactly like Danish and Nynorsk. These letters separate the Dano-Norwegian group from Swedish (ä, ö) and German (ä, ö, ü, ß) but do **not** separate Bokmål from Danish by their mere presence.

Their relative proportions do differ. In the twelve UD passages in `examples/ud_*.txt` (a small sample, so treat the numbers as indicative only) **æ** is about 0.24% of letters in Bokmål versus about 0.8% in the Danish UD passages, while **å** is higher in Bokmål (about 1.5% vs 1.1%). Two reasons:

- Danish *æ* often corresponds to Bokmål *e*: *tænke/tenke, kæmpe/kjempe, læse/lese, kendt (Da) / kjent (Nb)*. Among the top 5,000 words, about 374 Danish words contain æ versus 66 Bokmål words (counted from the two `vocabulary.json` files).
- Bokmål *å* is boosted by the infinitive marker *å* (rank 5) and the frequent *nå* (rank 40).

Accented letters are rare: *é* in loans and in *én/ét* "one" (emphatic), *ò* in *òg* "also" (marginal, mostly Nynorsk), *ô* in *fôr* "fodder".

Old spelling *aa* for å survives in some proper names (Aasen, Haakon) but not in running text.

## Characteristic Letter Combinations

Counted over the top 5,000 entries of `nob_Latn/vocabulary.json` vs `dan_Latn/vocabulary.json`:

| Sequence | Bokmål words | Danish words | Examples (Nb) |
|---|---|---|---|
| ei | 84 | 1 | vei, nei, eier, arbeid |
| øy | 33 | 0 | øye, høy, gøy, nøyaktig |
| kj | 66 | 4 | kjenne, kjøpe, kjent, kjøre |
| gj | 47 | 4 | gjøre, gjennom, igjen, gjerne |
| sj | 100 | 9 | sjon, sjelden, sjef, sjø |
| nn | 201 | 48 | mann, vann, finne, inn, enn |
| tt | 249 | 100 | litt, fått, hatt, rett, sett |
| pp | 104 | 31 | opp, gruppe, toppen |
| ej / øj | 0 / 0 | 67 / 28 | (Danish: vej, nej, øje, høj) |

(Example lists are illustrative; the counts are substring counts and include unrelated words.) *ei/øy/kj/gj/sj* are strongly Norwegian; *ej/øj* are strongly Danish.

Frequent character trigrams in the UD sample: `er_`, `en_`, `et_`, `_de`, `det`, `_og`, `for`, `ar_`, `om_`, `kke`, `til`, `han`, `den`, `lle`, `ste` - almost all shared with Danish, so trigram profiles alone separate the two poorly.

## Top 50 Words (vocabulary.json, rank order)

i, og, er, det, å, på, som, til, en, av, for, ikke, med, har, jeg, at, de, du, om, den, så, vi, fra, var, kan, et, men, han, seg, dette, noe, skal, noen, ble, vil, bare, også, ut, da, nå, hva, etter, eller, meg, være, blir, hadde, alle, når, her

Of these, the following are Bokmål-specific relative to Danish (absent from or very rare in the Danish 10k list): **å, av, seg, noe, noen, ble, ut, nå, hva, etter, meg, blir, hadde**. The rest (i, og, er, det, på, som, til, en, for, ikke, med, har, jeg, at, de, du, om, den, så, vi, fra, var, kan, et, men, han, skal, vil, bare, også, da, eller, være, alle, når, her) are shared and carry no Danish/Bokmål signal. See `chalis/discriminators.md` for the full marker lists.

## Morphological Patterns

### Suffixes and Endings

- **-het / -heten:** *mulighet, sikkerhet, frihet, kjærlighet* (Danish *-hed*).
- **-sjon:** *informasjon, situasjon, stasjon, nasjon* (30 words in the Bokmål top 5,000 vs 1 with *-tion*).
- **-skap:** *vennskap, selskap, kunnskap* (Danish *-skab*).
- **-ene** definite plural (*årene, jentene, pengene*); Danish has *-erne* in the same slots (*årene* is shared, but *bilene/bilerne*).
- **-a** feminine definite and weak past (*jenta, boka, kasta*), optional.
- **-et** weak past and participle (*startet, jobbet, laget*) where Danish has *-ede/-et*.
- **-lig / -ig** adjectives with no neuter -t; **no word in the Bokmål 10k list ends in *-igt***, whereas Danish has 117 (*vigtigt, muligt, hurtigt*).
- **-ning, -else, -ere, -isk** are shared with Danish.

### Short Verb Forms

*bli/blir/ble, ha, si/sier/sa, ta/tar/tok, gi/gir/ga* - Danish has longer forms with soft consonants (*blive/bliver/blev, have, sige/siger, tage/tager, give/giver*).

## Orthographic Conventions

- Lower-case nouns (unlike German), lower-case days and months (*mandag, januar*).
- Compounds written as one word (*nasjonalstatsnivå, tilbaketrekning*).
- Abbreviations: *bl.a.* (blant annet), *f.eks.* (for eksempel), *osv.* (og så videre), *ca.*, *kr*.
- Genitive *-s* without apostrophe (*Norges, EUs*), apostrophe only after s/x/z (*Hans'*).
- Quotation marks: «sjevroner» are standard in edited text; straight quotes are common online (`examples/ud_01.txt`).
- Optional-form variation means a single text may mix *boken/boka*, *frem/fram*, *kastet/kasta*.

## Key Identification Heuristics

1. Infinitive marker **å** before a verb (*for å, å være*) is the single most frequent Bokmål-only word.
2. **av, ble, noe/noen, hva, etter, meg/deg/seg, ut, opp, nå, mye, litt, igjen** vs Danish *af, blev, noget/nogen, hvad, efter, mig/dig/sig, ud, op, nu, meget, lidt, igen*.
3. Spellings with **ei, øy, kj, gj, skj, -sjon, -het**, final double consonants.
4. Adjective forms without *-igt*, double definiteness (*den store bilen*), *det er* as existential.
5. If *ikkje, eg, ein/eit, kva, ho, berre, frå* appear, consider Nynorsk instead (`nno_Latn/`).
