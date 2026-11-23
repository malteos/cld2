# Norwegian Bokmål (norsk bokmål) - Grammar

Bokmål grammar is very close to Danish; the notes below emphasize the points where written forms differ, since those are the ones useful for identification.

## Phonology and Its Reflection in Spelling

Spoken Norwegian has a pitch accent (two tonal word accents) and no Danish-style *stød*. For written LID the relevant fact is that Bokmål spelling follows Norwegian pronunciation more closely than Danish spelling does:

- **Hard stops after vowels:** *bake, gate, mat, uke, kjøpe, skip* (Danish *bage, gade, mad, uge, købe, skib*).
- **Palatal spellings kj-, gj-, skj-:** *kjenne, kjøre, gjøre, skje* (Danish *kende, køre, gøre, ske*).
- **Diphthongs ei, øy, au:** *vei, nei, øye, høy* (Danish *vej, nej, øje, høj*).
- **Assimilated clusters -nn/-ll:** *mann, vann, finne* (Danish *mand, vand, finde*).
- **Double final consonant after short vowel:** *takk, fikk, opp, litt, hatt* (Danish *tak, fik, op, lidt, haft*).

## Noun System

### Gender

Bokmål has three genders: masculine, feminine and neuter. The feminine is optional in most words: the norm allows *en bok - boken* (two-gender, Danish-like) or *ei bok - boka* (three-gender). Most modern texts use at least some feminine forms (*jenta, boka, dattera*), but conservative and formal texts may avoid them. The indefinite feminine article *ei* (rank 509 in `vocabulary.json`) does not exist in Danish.

### Articles and Definiteness

| | Masculine | Feminine | Neuter | Plural |
|---|---|---|---|---|
| Indefinite | en bil | ei/en jente | et hus | biler, hus |
| Definite (suffix) | bilen | jenta/jenten | huset | bilene, husene |

- Definite plural is **-ene** (*bilene, årene, jentene*); Danish uses **-erne** after -er plurals (*bilerne, pigerne*). Bokmål *-erne* occurs only where the stem itself ends in -er (agent nouns: *spillerne, innbyggerne*).
- **Double definiteness:** with an adjective, Bokmål marks definiteness twice: *den store bilen, det nye huset*. Danish uses only the front article: *den store bil, det nye hus*. This is one of the most reliable grammatical differences.
- **Postposed possessives** are common: *bilen min, huset vårt, mora mi* alongside *min bil*. Danish normally places possessives first.

### Plural

Main patterns: -er (*biler*), zero for many monosyllabic neuters (*hus, barn, år*), umlaut plurals (*mann - menn, bok - bøker*). The neuter definite singular -et is identical to Danish.

### Case

Only pronouns have case: *jeg/meg, du/deg, han/ham, hun/henne, vi/oss, dere/dere, de/dem*, reflexive *seg*. Note *meg, deg, seg* (Danish *mig, dig, sig*), *oss* (Danish *os*) and *dere* (Danish *I/jer*). Possessives: *min, din, sin, vår, deres*; *sitt/mitt/ditt* (neuter) - Danish *sit/mit/dit*.

## Verb System

### Infinitive

The infinitive marker is **å** (*å gjøre, for å se*); this is rank 5 in `vocabulary.json`. Danish uses *at* for both "that" and "to"; in Bokmål *at* is only the conjunction "that". *kommer til å* (future) corresponds to Danish *kommer til at*.

### Present and Past

- Present: **-er** for nearly all verbs (*kaster, gjør, blir, sier*), unmarked for person.
- Weak past, class 1: **-et** or **-a** (*kastet/kasta, jobbet, startet*), Danish **-ede** (*kastede, startede*).
- Weak past, class 2: **-te** (*kjøpte, leste*), class 3: **-de** (*levde*), class 4: **-dde** (*bodde*).
- Strong verbs: *bli - ble/blei - blitt; få - fikk - fått; gå - gikk - gått; si - sa - sagt; ha - hadde - hatt; gjøre - gjorde - gjort*.
- Short forms are standard: *bli/blir* (Danish *blive/bliver*), *ha* (Danish *have*), *si/sier* (Danish *sige/siger*), *ta/tar* (Danish *tage/tager*).

### Perfect and Passive

Perfect with *ha* (*har gjort*); *være* is possible with motion verbs (*er kommet*). Passive with *-s* (*det sies, vedtas*) or *bli* + participle (*ble stemt ned*). The Bokmål form *ble* (Danish *blev*) is one of the most frequent identifying words.

### Modals

*kan, vil, skal, må, bør* plus past *kunne, ville, skulle, måtte, burde* - identical to Danish.

## Syntax

### V2

Main clauses are verb-second: *I dag kommer han.* Subordinate clauses put sentence adverbs before the finite verb: *at han ikke kommer* - the same as Danish.

### Questions

Yes/no questions invert verb and subject: *Kommer du?* Question words: *hva, hvem, hvor, hvordan, hvorfor, hvilken, når*. *hva* (Danish *hvad*) is the key form.

### Existential Clauses

Bokmål uses **det** as the dummy subject: *Det er mange folk her.* Danish usually uses **der**: *Der er mange mennesker her.* This raises Danish *der* to rank 16 versus rank 73 in Bokmål (`vocabulary.json` files).

### Negation

*ikke* (shared with Danish); Nynorsk has *ikkje*.

## Adjectives

Indefinite: base (common gender), **-t** (neuter), **-e** (plural/definite): *stor - stort - store*. Adjectives in **-ig/-lig** take **no -t** in the neuter: *et viktig møte, et vanlig hus*; Danish adds -t: *et vigtigt møde, et almindeligt hus*. No word ending in *-igt* occurs in the Bokmål 10k list.

## Numerals

Tens: *tjue, tretti, førti, femti, seksti, sytti, åtti, nitti* (Danish uses vigesimal *tyve, tredive, fyrre, halvtreds, tres, halvfjerds, firs, halvfems*). Seven is *sju* or *syv*.
