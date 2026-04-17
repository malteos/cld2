#!/usr/bin/env python3
"""One-shot writer for the 31 per-language markdown files that the first
subagent wave didn't finish before hitting the API quota. Each entry produces
four files (overview.md, grammar.md, characteristics.md, differences.md).

This script is a data file with a tiny bit of glue. It's kept around for
reproducibility — running it again is idempotent and safe because it always
overwrites to the same content.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LANG_DIR = ROOT / "languages"

# ---------------------------------------------------------------------------
# Content for the 31 remaining languages. Each value is a dict with four keys
# (overview / grammar / characteristics / differences) holding full markdown.
# ---------------------------------------------------------------------------

CONTENT: dict[str, dict[str, str]] = {}


def lang(folder: str, overview: str, grammar: str, chars: str, diffs: str) -> None:
    CONTENT[folder] = {
        "overview.md": overview,
        "grammar.md": grammar,
        "characteristics.md": chars,
        "differences.md": diffs,
    }


# ---- Acehnese (ace) --------------------------------------------------------
lang("ace_Latn",
"""# Acehnese (ace)

## Summary

Acehnese (endonym **Bahsa Acèh**) is a Malayo-Polynesian language of the
Chamic subgroup in the Austronesian family. It is spoken by roughly
3–3.5 million people, mainly in **Aceh province on Sumatra, Indonesia**,
with smaller diaspora populations in Malaysia and elsewhere. ISO code:
`ace` (639-3); there is no 639-1 code.

## Writing system

Modern Acehnese is written in the **Latin script** with the diacritics **è**,
**é**, and the schwa marker **ë**. Glottal stops are transcribed with an
apostrophe `'` (e.g. **aneu'** 'child'). Older literature uses the
Arabic-based *Jawi* (Jawoe) script, but virtually all web text is Latin.

## Historical note

Despite geographic proximity to Malay, Acehnese is linguistically distant
from it: its phonology preserves earlier Chamic features (rich vowel system,
final glottalisation, pronominal clitics on verbs) that Malay lost. Web text
frequently code-mixes with Indonesian.
""",
"""# Grammar: Acehnese (ace)

- **Word order:** SVO with pragmatic topic-fronting.
- **Morphology:** **Isolating/analytic**. Unlike Indonesian, which has
  productive `ber-/me-/di-/pe-` affixes, Acehnese relies on particles and
  serial verbs.
- **Nouns:** No grammatical gender, no case, no obligatory plural marking;
  pluralisation via reduplication (**aneuk-aneuk** 'children') or the
  quantifier **bandum** 'all'.
- **Pronouns:** Free forms plus clitic series — **lôn** (I), **kah / gata /
  droeneuh** (you, informal → polite), **jih** (he/she), **geu-** and **ji-**
  (honorific / non-honorific 3SG clitics agglutinated to the verb).
- **Verbs:** Uninflected stems with preverbal aspect markers: **ka**
  (perfective), **teungoh** (progressive), **akan** (future). Subject
  agreement via the pronominal clitic chain (`geu-`, `ji-`, `ku-`) — a Chamic
  feature absent from standard Malay.
- **Phonology:** Ten distinct oral vowels plus nasalised vowels; frequent
  final glottal stop; final **-h**, **-k**, **-ng**, **-t** extremely common.
  Long vowels written double.
- **Syntax:** Freely pro-drop. Negation uses **han / hana** (not **tidak**);
  prohibitive **bèk**. Copula is **na / nyoë**, not **adalah**.
""",
"""# LID Characteristics: Acehnese (ace)

- **Script signals:** Latin with **è**, **é**, **ë** (schwa) and a
  meaning-bearing apostrophe. The **ë** is a strong discriminator vs. ind/
  msa/zsm (neither uses it) and vs. jav (which prefers **ê**).
- **Top function words:** *na, nyoë, nyan, han, hana, bèk, ka, lôn, kah,
  gata, droeneuh, jih, geu, ji, ngon, keu, bak, nyang, dua, sidroe, tuha,
  ureueng, bandum, uleue, akan, meu-, di, atawa, meunyo, sabab, teuma*.
- **N-gram / spelling patterns:** Triphthong-like sequences **-euë-**,
  **-ieue-**, **-oë-**; frequent word-final **-ng**, **-eh**, **-oh**;
  apostrophe–vowel endings (**'oh**, **'uh**).
- **Morphology hooks:** Pronominal clitics `geu-`/`ji-`/`ku-` fused to verbs
  (**geupajoh** 'he eats it'); preverbal aspect clitic **ka**.
- **Punctuation / orthography quirks:** Apostrophe is a letter, not stylistic.
  Double vowels (**uu**, **oo**) signal length, not hiatus.
""",
"""# Differences from confusable languages: Acehnese (ace)

Main confusability risk is **Indonesian (ind)** and **Malay (msa / zsm)**;
web text often code-mixes.

**ace vs. ind / msa / zsm**
- Expect **ë**, and triphthong strings **ieu**, **euë**, **uë** unique to
  Acehnese.
- Negation **han / hana / bèk** vs. **tidak / bukan / jangan**.
- Copula **na / nyoë** vs. **adalah / ada**.
- Pronouns **lôn / gata / droeneuh** vs. **saya / aku / kamu / Anda**.
- Acehnese lacks productive **ber-/me-/pe-/-kan** — expect short stems with
  clitic pronouns instead of Indonesian-style prefix chains.

**ace vs. jav (Javanese)**
- Both Austronesian-Latin-script, but Javanese uses **é / è / ê**
  (circumflex schwa); Acehnese uses **ë**, never **ê**.
- Javanese high-register words **panjenengan**, **sampeyan** don't occur in
  Acehnese.

Short snippets lacking these markers are genuinely ambiguous; look for
**ë**, **bèk**, **han**, **droeneuh** as high-precision Acehnese signals.
""")


# ---- Saint Lucian Creole (acf) --------------------------------------------
lang("acf_Latn",
"""# Saint Lucian Creole (acf)

## Summary

Saint Lucian Creole (endonym **Kwéyòl** or **Patwa**) is a French-based
creole of the **Lesser Antillean Creole** continuum. It is the everyday
vernacular of most of Saint Lucia's ~160,000 inhabitants, with overlap in
Dominica and diaspora communities in the UK and Canada. ISO code: `acf`
(639-3); no 639-1/2 code.

## Writing system

Written in the **Latin script** using a phonemic orthography promoted by the
Folk Research Centre. Key graphemes: **ò** [ɔ], **è** [ɛ], and **y** used
for [j]. Silent French etymological letters are dropped (**sé** for *c'est*,
**péyi** for *pays*, **zòt** for *vous*).

## Historical note

The lexicon is overwhelmingly French-derived, but the grammar is creole —
analytic with preverbal TMA particles **ka / té / kay**. Contact with
English is pervasive and many modern speakers code-switch, but the core
function-word inventory is stable.
""",
"""# Grammar: Saint Lucian Creole (acf)

- **Word order:** Rigid SVO; questions use sentence-final intonation or an
  initial question word — no inversion.
- **Morphology:** **Analytic**. Verbs never inflect for person, number, or
  tense; nouns don't mark gender or case.
- **Nouns:** Definite article is **postposed**: **chyen-an** 'the dog',
  **tab-la** 'the table' (allomorphs `-a / -la / -an / -lan`). Plural is
  expressed with **sé … -la** or the clitic **-a**.
- **Pronouns:** **mwen** (I), **ou** (you sg), **i** (he/she/it), **nou**
  (we), **zòt** (you pl), **yo** (they). Possessives are simply juxtaposed:
  **kay mwen** 'my house'.
- **Verbs:** Aspect/tense is a preverbal-particle triple:
  - **ka** — progressive / habitual.
  - **té** — anterior (past/pluperfect).
  - **kay / ké** — irrealis / future.
  Combinations stack: **té kay** 'would have' (conditional).
- **Phonology:** Simplified vowel inventory; systematic r-deletion
  (**zòt** from *les autres*). Nasal vowels align with French.
- **Syntax:** Equational copula **sé**; locative expressed with **an** or
  **asou** without a copula. Negation is preverbal **pa**.
""",
"""# LID Characteristics: Saint Lucian Creole (acf)

- **Script signals:** Latin with **ò**, **è**; heavy use of **y** where
  French would write **i** or **ill**. Apostrophes are rare (unlike French
  **l'**, **c'**).
- **Top function words:** *sé, é, ka, té, kay, ké, mwen, ou, i, nou, zòt,
  yo, pa, pou, si, an, en, la, lan, lè, kon, koté, poutji / pou ki,
  sa, tout, épi, èk, pyès*.
- **N-gram / spelling patterns:** Word-final clitic article **-a / -la /
  -an**; pronouns **mwen / nou / yo / zòt**; strings **kay**, **kon**,
  **pé**, **vé** recurring in verb phrases.
- **Morphology hooks:** No verb inflection — scan for the invariant
  preverbal triple **ka / té / kay**. Plural/def article postposed.
- **Punctuation / orthography quirks:** Phonemic spellings replace French
  silent letters: **é** for *ez/er*, **w** for *oi/ou* (**mwen** from
  *moi*), **kw** for *cr* (**kwè** from *crois*).
""",
"""# Differences from confusable languages: Saint Lucian Creole (acf)

The close set is **gcf** (Guadeloupean), **gcr** (Guianese), **rcf**
(Réunion) and the French lexifier **fra**.

**acf vs. gcf**
- Largely mutually intelligible; orthographic conventions differ only
  slightly. Short snippets are very hard to tell apart — content-based
  cues (Saint Lucia vs. Guadeloupe place names, currency) help more than
  grammar.

**acf vs. gcr**
- Guianese admixes more Portuguese and Amerindian loans, and permits more
  French-lookalike spellings. **sa ka** cleft is more frequent in gcr.

**acf vs. rcf**
- Réunion Creole uses **lé** as copula where acf uses **sé**; rcf has
  **zot** (unaccented) vs acf **zòt**; rcf has nasal digraphs **anm**,
  **onm** that acf lacks.

**acf vs. fra**
- No French verb inflection (`je suis / tu es / il est`), no French
  articles **le / la / les** (acf uses postposed **-la / -a**), and
  phonemic spellings (**mwen**, **péyi**) replace French orthography.
  Any run of **le / la / les / de / du / des** patterns signals French,
  not acf.
""")


# ---- Central Bikol (bcl) and Bikol macro (bik) ----------------------------
_BIK_OVERVIEW = """## Summary

**Bikol** refers to a cluster of Central-Philippine Austronesian languages
spoken in the Bicol Region of Luzon (Philippines), roughly 4–5 million
speakers overall. **Central Bikol** (`bcl`, endonym **Bikol Sentral** /
**Bikol Naga**) is the prestige standard centred on Naga City; the
macrocode **bik** covers the whole cluster (Rinconada, Albay, Miraya,
Masbateño, etc.). ISO codes: `bcl`, `bik` (639-3); no 639-1.

## Writing system

Latin script with the modern Filipino alphabet. Accent marks may appear on
vowels (**á, é, í, ó, ú**) for stress and **–** for glottal-final stress
(**batá'**). In practice web text is unaccented.

## Historical note

Bikol shares its function-word inventory (**an, sa, na, mga, ng**) with
Tagalog but its lexicon diverges substantially (e.g. Bikol **saro** 'one'
vs. Tagalog **isa**, **magayon** 'beautiful' vs. **maganda**).
"""

_BIK_GRAMMAR = """- **Word order:** Verb-initial (VSO/VOS) by default, with fronting for
  focus — a typical Philippine-type pattern.
- **Morphology:** **Agglutinative** with rich voice morphology
  (**mag-, mi-, pag-, pag…-an, pig-, pinag-**). The focus/voice system
  marks whether the subject is agent, patient, location, benefactive, or
  instrument.
- **Nouns:** Case is expressed by **case particles**: **an** (nominative,
  definite), **nin / kan / ki** (genitive / oblique), **sa** (dative /
  locative). Plural is optional, marked by **mga** before the noun.
- **Pronouns:** Three sets (nominative, genitive, oblique). 1SG:
  **ako / ko / sa sako**; 2SG: **ika / mo / sa saimo**; 3SG:
  **siya / niya / sa saiya**.
- **Verbs:** Aspect-prominent; affixes encode completed
  (**nag-, nin-**), incompleted/progressive (**nag-…+reduplication**), and
  contemplated/future (**ma-, mag-**). Reduplication of the first syllable
  marks imperfective aspect.
- **Phonology:** Five vowels; the inventory includes a glottal stop that
  is often unwritten word-initially but phonemic word-finally.
- **Syntax:** Particles **daw** (question), **man** (too/also),
  **naman / baga** (contrastive) chain after the predicate.
"""

_BIK_CHARS = """- **Script signals:** Plain Latin, unaccented in most web text. The
  grapheme inventory matches Tagalog; differentiation is lexical.
- **Top function words:** *an, sa, na, nin, kan, ki, mga, asin, pero, o,
  pag, kaya, alagad, dai, garo, siring, ini, iyan, iyo, saro, duwa, tulo,
  iyo na, sana, lang, man, ngani, garo man, sabi, basta, kun, kundi*.
- **N-gram / spelling patterns:** Common endings **-on / -an / -han** on
  verbs; **ma-**, **mag-**, **nag-** prefixes; syllable reduplication
  (**nagbabasa**, **naghihiling**).
- **Morphology hooks:** Focus-marker affixes **-on, -an, i-, ipag-**
  attached to bases. Reduplication pattern `C1V1-C1V1-stem` marks
  progressive.
- **Punctuation / orthography quirks:** Few quirks — plain Spanish-era
  orthography. Bikol ñ appears in Spanish loans (**paño, doña**).
"""

_BIK_DIFFS = """Main confusability is with **Tagalog (tgl)** and **Filipino (fil)**;
occasional overlap with **Cebuano** (not in CommonLID).

**bik vs. tgl / fil**
- Shared function words (**an, sa, na, mga, ng**) are low-entropy signals.
- Content-word diagnostics:
  - 'one' — bik **saro**, tgl **isa**.
  - 'beautiful' — bik **magayon**, tgl **maganda**.
  - 'good' — bik **marhay**, tgl **mabuti**.
  - 'yes / no' — bik **iyo / dai**, tgl **oo / hindi**.
- **dai** as negation is a near-certain Bikol signal (Tagalog uses **hindi**).
- Emphatic **garo** and affirmative **ngani** also favour Bikol.

**bcl (Central) vs. bik (macro)**
- Central Bikol is the Naga-area standard; the macrocode pools it with
  Albay, Rinconada, etc. Rinconada uses schwa **ë** / **ö**; Central Bikol
  doesn't. Short snippets without schwa are indistinguishable from bcl.
"""

lang("bcl_Latn",
"""# Central Bikol (bcl)

""" + _BIK_OVERVIEW,
"""# Grammar: Central Bikol (bcl)

""" + _BIK_GRAMMAR,
"""# LID Characteristics: Central Bikol (bcl)

""" + _BIK_CHARS,
"""# Differences from confusable languages: Central Bikol (bcl)

""" + _BIK_DIFFS)

lang("bik_Latn",
"""# Bikol (macro) (bik)

""" + _BIK_OVERVIEW + """
## Note on the macrocode

`bik` is the ISO-639-3 macrolanguage tag that spans Central Bikol (`bcl`),
Rinconada Bikol, Albay Bikol, Miraya Bikol, Masbateño, and other varieties.
Web text tagged `bik` may be any of them.
""",
"""# Grammar: Bikol (macro) (bik)

""" + _BIK_GRAMMAR,
"""# LID Characteristics: Bikol (macro) (bik)

""" + _BIK_CHARS + """
- **Rinconada diagnostic:** the schwa letters **ë / ö** appear in Rinconada
  but not in Central Bikol. Their presence within a `bik`-tagged sample
  indicates the Rinconada variety specifically.
""",
"""# Differences from confusable languages: Bikol (macro) (bik)

""" + _BIK_DIFFS)


# ---- Breton (bre) ---------------------------------------------------------
lang("bre_Latn",
"""# Breton (bre)

## Summary

Breton (endonym **Brezhoneg**) is an **Insular Celtic** language of the
Brittonic branch (Indo-European → Celtic → Brittonic), closely related to
Cornish and Welsh. It is spoken in **Brittany, north-western France**, by
roughly 200,000 people, the majority of whom are older; revitalisation
efforts through Diwan schools and media exist. ISO codes: `br` (639-1),
`bre` (639-3).

## Writing system

Latin script with the peuvan-based *peurunvan* (unified) orthography of
1941, supplemented by the *skolveurieg* (university) variant. Distinctive
feature: the trigraph **c'h** [x], the digraph **ch** [ʃ], and pairs
**zh** (~ / z in dialects). Other letters: **ñ** for nasalised vowels, and
**ù / ê / â** rarely.
""",
"""# Grammar: Breton (bre)

- **Word order:** VSO by default, with fronting of nouns, adverbs, or
  verbal nouns for focus — the surface is often SVO or OVS because focus
  fronting is the unmarked prose pattern.
- **Morphology:** Celtic-style **initial mutations** — a preceding word
  can soft-mutate, spirant-mutate, hard-mutate, or mixed-mutate the next
  word's initial consonant (**tad** → **e dad** 'his father' /
  **he zad** 'her father' / **o zad** 'their father').
- **Nouns:** Two genders (masculine, feminine); number is singular /
  plural / dual / collective, marked by suffixes like **-où**, **-ioù**,
  **-ed**, **-ien**, **-on**. Definite articles **an / ar / al** trigger
  mutation.
- **Pronouns:** Free and infixed; possessives trigger different mutations
  (e.g. **va zad** 'my father' with spirant mutation).
- **Verbs:** Inflected for person, number, tense, mood; extensive use of
  the particle **a** / **e** before finite verbs (**a lenn** 'reads',
  **e lenn** if subject fronted), plus the auxiliary **bezañ** ('be') in
  compound tenses. Imperative has distinctive shapes.
- **Phonology:** Nasal vowels, **c'h** /x/, **gw-** /gw/; stress on the
  penult in most dialects, except KLT vs. Gwened variation.
- **Syntax:** Negation is a two-part clitic **ne … ket**. Verb-subject
  agreement is suppressed when the subject is overt (synthetic vs. analytic
  concordance rule).
""",
"""# LID Characteristics: Breton (bre)

- **Script signals:** Trigraph **c'h** (single apostrophe inside) is a
  near-certain Breton signal; digraphs **ch**, **zh**; nasal letter **ñ**
  in **añ / eñ / oñ**.
- **Top function words:** *an, ar, al, ur, ul, un, ha, hag, e, er, el, em,
  d', da, war, e-barzh, evit, ez, ne, ket, eo, ez eo, emañ, zo, a, pe,
  met, hogen, ma, ouzh, gant, nemet, seul, holl, mat, kalz, tout*.
- **N-gram / spelling patterns:** Plural endings **-où**, **-ioù**,
  **-ien**, **-ed**; mutation evidence: **g→c'h** (**gar** → **va c'har**),
  **t→z** (**tad** → **va zad**). Initial **k-, g-, t-, d-, b-, p-**
  alternate with softer or spirantised forms.
- **Morphology hooks:** Particles **a** and **e** before finite verbs;
  the auxiliary **bezañ** with **oc'h** + verbal noun for progressive.
- **Punctuation / orthography quirks:** Apostrophe inside **c'h** is
  load-bearing — never a stylistic quote.
""",
"""# Differences from confusable languages: Breton (bre)

Within CommonLID there are no other Brittonic languages. Confusability is
low; risks are **French (fra)** (shared region, many loanwords) and
superficial lookalikes.

**bre vs. fra**
- Trigraph **c'h** and digraph **zh** are unique to Breton.
- **ñ** appears in Breton nasal vowels; French only in Spanish loanwords
  (**señor**, very rare).
- Breton function words **an / ar / al / ez / emañ / zo / eo / ket** are
  absent from French.
- Breton lacks French accent mix (**é è ê à ç ù â**), though **ê** and
  **â** do sporadically appear.

**bre vs. Welsh / Cornish** (not in CommonLID)
- Welsh has **w** as a vowel and **ll** (voiceless l), which Breton lacks.
- Cornish is closer but is not a CommonLID label.

If a Latin-script snippet contains **c'h**, **zh**, or the cluster
**an / ar + noun**, it is almost certainly Breton.
""")


# ---- Modern Greek (ell) ---------------------------------------------------
lang("ell_Grek",
"""# Modern Greek (ell)

## Summary

Modern Greek (endonym **Ελληνικά**, *Elliniká*) is the sole surviving
branch of the Hellenic family (Indo-European → Hellenic). It is the
official language of **Greece** (~10.7 million speakers) and **Cyprus**
(~800,000, alongside the Cypriot variety), with diaspora communities
worldwide. ISO codes: `el` (639-1), `ell` / `gre` (639-2/-3).

## Writing system

Greek script (`Grek`), using the 24-letter alphabet **Α–Ω** plus the
diacritical system. Since 1982 the **monotonic** orthography is standard:
only an **acute accent ´** and the diaeresis **¨**. Older texts use
**polytonic** orthography with breathings (῾, ᾿) and additional accents
(῀, ῞, ῟) — this is the single strongest diagnostic between Modern (ell)
and Ancient (grc).

## Historical note

Katharevousa/Dimotiki diglossia was resolved in 1976 in favour of Dimotiki
(the demotic/vernacular), which underlies written Modern Greek. Katharevousa
forms (e.g. genitive endings **-εως / -ως** for **-ης / -ος**) still appear
in legal and ecclesiastical registers.
""",
"""# Grammar: Modern Greek (ell)

- **Word order:** SVO is default but very free; fronting is extensive.
- **Morphology:** **Fusional** with retained nominal and verbal inflection.
  Nouns and adjectives mark case (nominative, genitive, accusative,
  vocative; no dative — replaced by **σε + accusative**), number, gender
  (M/F/N). Adjectives agree in gender, number, case.
- **Nouns:** Three genders. Articles: **ο / η / το** (nom sg), **τον / την /
  το** (acc sg), **οι / οι / τα** (nom pl).
- **Pronouns:** Strong (**εγώ, εσύ, αυτός**) and clitic (**με, σε, τον,
  την, το, μας, σας, τους**) series; clitics attach proclitically in most
  verb forms, enclitically to imperatives.
- **Verbs:** Two aspects (imperfective / perfective) realised as distinct
  stems (**γράφω** 'I write' / **έγραψα** 'I wrote'); two voices (active
  / mediopassive); mood morphology via subjunctive particle **να** or
  future particle **θα**. **Infinitives are absent** — subordinate clauses
  use finite verbs introduced by **να** / **ότι** / **που**.
- **Phonology:** Five vowels; phonotactically transparent. Stress is
  phonemic and always written with the acute.
- **Syntax:** Pro-drop; negation **δεν** (indicative) / **μην** (subjunctive
  + imperative). Copula **είμαι** 'to be' is obligatory.
""",
"""# LID Characteristics: Modern Greek (ell)

- **Script signals:** Greek alphabet (U+0370–03FF). Characters unique to
  Greek: **Θ θ**, **Ξ ξ**, **Ψ ψ**, **Ω ω**. Final **-ς** (sigma) occurs
  only word-finally.
- **Top function words:** *ο, η, το, οι, τα, τον, την, του, της, των,
  στο, στην, στους, και, να, θα, δεν, μη, μην, είναι, έχει, για, από,
  με, σε, αλλά, όταν, που, ως, ή, κι, πιο, εκεί, εδώ, αυτό, αυτή, αυτός,
  όμως, μόνο, πολύ, κάθε*.
- **N-gram / spelling patterns:** High frequency of **-ος, -ης, -ας, -ες,
  -ων** endings (case/gender markers); **μπ** (voiced b), **ντ** (voiced
  d), **γκ** (voiced g), **τσ** (ts), **τζ** (dz) are common digraphs.
- **Morphology hooks:** Verb endings **-ω, -εις, -ει, -ουμε, -ετε, -ουν**
  (present active); future **θα + verb**; subjunctive **να + verb**.
- **Punctuation / orthography quirks:** Question mark is **; (U+037E)**
  (visually a semicolon); semicolon is **· (ano teleia, U+0387)**. Only
  monotonic acute and diaeresis; no breathings or circumflex.
""",
"""# Differences from confusable languages: Modern Greek (ell)

Principal confusability pair in CommonLID is **Ancient Greek (grc)**.

**ell vs. grc**
- **Monotonic vs. polytonic accentuation** is the single strongest signal.
  Presence of **῾ ᾿ ῀ ῞ ῟** or iota-subscript letters (**ᾳ ῃ ῳ**) in more
  than trace amounts indicates grc.
- Ancient Greek uses **ε / αι, ο / ω, η / ει / ῃ** in morphologically
  relevant ways now lost; Modern Greek pronounces all of these as /e/ and
  /i/, yielding different spelling choices in modern neologisms.
- Function words diverge: grc **μέν … δέ, ἂν, οὖν, γάρ**; ell **να, θα,
  δεν, μην, όμως, λοιπόν**.
- Verb morphology: grc infinitives **-ειν, -ναι** don't exist in ell;
  ell has the subjunctive particle **να** + finite verb.

**ell vs. any Latin-script language:** script alone is sufficient.

**ell vs. other Greek-script labels** — there are no others in CommonLID
besides grc.
""")


# ---- Finnish (fin) --------------------------------------------------------
lang("fin_Latn",
"""# Finnish (fin)

## Summary

Finnish (endonym **Suomi**) is a **Uralic** language of the Finnic branch
(Uralic → Finnic → Finnish). It is the main national language of
**Finland** (official alongside Swedish, ~5 million speakers) with
minority speakers in Sweden (Tornedalian), Norway, Estonia, Russia (Karelia)
and diaspora. ISO codes: `fi` (639-1), `fin` (639-2/-3).

## Writing system

Latin script with **ä** and **ö** as distinct letters; **å** exists for
Swedish loanwords only. No other diacritics in native words. Orthography
is highly phonemic — one letter per phoneme with few exceptions.

## Historical note

Finnish orthography was standardised by Mikael Agricola in the 16th century
and reshaped into its modern form in the 19th century (Kalevala era). The
language is noted for its vowel harmony and agglutinative morphology.
""",
"""# Grammar: Finnish (fin)

- **Word order:** SVO by default but very free; information structure
  drives ordering.
- **Morphology:** **Agglutinative** with extensive suffixation. A noun can
  carry a chain: stem + plural + case + possessive + clitic (e.g.
  **taloissammekin** 'also in our houses' = *talo-i-ssa-mme-kin*).
- **Nouns:** 15 cases (nominative, genitive, accusative, partitive,
  essive, translative, inessive, elative, illative, adessive, ablative,
  allative, abessive, comitative, instructive). No grammatical gender.
- **Pronouns:** Inflected for case like nouns. Personal: **minä, sinä,
  hän, me, te, he**; demonstrative: **tämä, tuo, se, nämä, nuo, ne**.
  Note: **hän** is gender-neutral.
- **Verbs:** Four tenses (present, imperfect, perfect, pluperfect) built
  from two aspectual stems; five moods (indicative, conditional,
  potential, imperative, optative). Passive is impersonal. Negation is a
  **conjugated negative verb** **en, et, ei, emme, ette, eivät** + main
  verb stem.
- **Phonology:** Front/back **vowel harmony** — front **ä ö y** vs. back
  **a o u** can't coexist in a native stem; neutral **i e** do not trigger
  harmony. Consonant gradation: strong/weak alternation (**katu / kadun**,
  **kukka / kukan**).
- **Syntax:** No articles, no future tense morphology (present covers
  future). Possession expressed by **olla** 'to be' + adessive:
  **minulla on …** 'I have …'.
""",
"""# LID Characteristics: Finnish (fin)

- **Script signals:** **ä** and **ö** everywhere, **å** almost never in
  native words, no **š / ž / õ / ø / æ**.
- **Top function words:** *ja, on, ei, että, tämä, se, ne, mutta, myös,
  jos, kun, niin, nyt, vain, vielä, jo, sekä, kuin, sillä, koska, vai,
  tai, joka, mikä, kaikki, kuitenkin, ehkä, hyvin, paljon, voi, pitää,
  tehdä, sanoa*.
- **N-gram / spelling patterns:** Long vowels **aa, ee, ii, oo, uu, ää,
  öö, yy** extremely common; geminate consonants **tt, kk, pp, ss, ll,
  mm, nn, rr** frequent; double letters mark length, not stress.
  Suffix chains ending in **-ssa / -sta / -lla / -lle / -mme / -nne /
  -kin / -kaan** are highly diagnostic.
- **Morphology hooks:** Negative verb **en/et/ei + bare stem** is
  unmistakable (**en tiedä** 'I don't know'). Vowel harmony visible in
  suffixes (**-ssa/-ssä**, **-lla/-llä**).
- **Punctuation / orthography quirks:** No special punctuation; sentence-
  initial capitalisation normal. Absence of **š** / **ž** distinguishes
  Finnish from Sami orthographies.
""",
"""# Differences from confusable languages: Finnish (fin)

The close pair in CommonLID is **Estonian (est)**; both are Finnic.

**fin vs. est**
- **ä, ö** are shared, but **õ** is Estonian-only. Any **õ** → Estonian.
- Finnish has vowel harmony; Estonian does **not** (Estonian freely
  combines back and front vowels).
- Finnish has double-vowel geminates (**aa, ee**) and double consonants
  (**tt, kk**); Estonian uses **three degrees of consonant length**
  (Q1/Q2/Q3), often written the same but stressed differently.
- Negation: fin uses **en, et, ei, emme** (conjugated); est uses the
  invariant particle **ei**.
- Case inventory is similar (~14 in est vs. 15 in fin), but suffix shapes
  differ: fin **-ssa / -sta / -lla / -lle**; est **-s / -st / -l / -le**.
- Pronoun system: fin **minä, sinä, hän**; est **mina, sina, tema**.

**fin vs. other Uralic** (none in CommonLID besides est): no practical
confusability within this dataset.

**fin vs. Swedish** (not in CommonLID): Swedish uses **å**, **ø** (Norwegian)
or **ä/ö** (Swedish itself). A snippet with **å** or typically Swedish
function words **och, det, är, inte, också** is not Finnish.
""")


# ---- Estonian (est) -------------------------------------------------------
lang("est_Latn",
"""# Estonian (est)

## Summary

Estonian (endonym **Eesti keel**) is a Uralic language of the Finnic branch
(Uralic → Finnic → South-Estonian/North-Estonian). It is the official
language of **Estonia** (~1.1 million speakers) with diaspora communities
in Finland, Sweden, Russia, Canada, and the US. ISO codes: `et` (639-1),
`est` (639-2/-3).

## Writing system

Latin script with letters **ä, ö, ü, õ**, and **š, ž** in loanwords. The
**õ** (close back unrounded vowel, IPA /ɤ/) is effectively unique to
Estonian among the major European languages — a very strong LID signal.

## Historical note

Estonian lost vowel harmony (a Uralic inheritance that Finnish retains) and
reduced its case system from its Finnic ancestor. Orthography was
standardised in the mid-19th century under Baltic-German influence, then
reformed in the 20th century.
""",
"""# Grammar: Estonian (est)

- **Word order:** SVO by default with V2 tendencies in main clauses.
- **Morphology:** **Agglutinative** with some fusion. Nouns inflect for
  **14 cases** and 2 numbers. Consonant **quantity gradation** (Q1/Q2/Q3)
  distinguishes forms that look identical orthographically
  (**linn** 'town' vs. **linna** 'city-GEN' vs. **linna** 'city-PART').
- **Nouns:** No grammatical gender. Plural is marked by **-d** (NOM PL) or
  stem change plus case. Partitive is heavily used, covering objects of
  negated / ongoing actions.
- **Pronouns:** Strong/weak pairs — **mina / ma, sina / sa, tema / ta,
  meie / me, teie / te, nemad / nad**. Gender-neutral in 3rd person.
- **Verbs:** Present, imperfect, perfect, pluperfect; five moods
  (indicative, conditional, jussive, quotative/oblique, imperative). The
  **quotative** (**-vat**) is a reportative evidential — an unusual
  category for Europe. Negation is invariant **ei** + main verb stem.
- **Phonology:** Three-way quantity opposition (short/long/overlong) is
  phonemic. No vowel harmony (unlike Finnish). Palatalisation of consonants
  before front vowels is phonemic but not orthographically marked in most
  positions.
- **Syntax:** No articles. Possession via **mul/sul/tal on …** (adessive +
  'is').
""",
"""# LID Characteristics: Estonian (est)

- **Script signals:** **õ** is the single most diagnostic letter (near
  unique among CommonLID languages). Also **ä, ö, ü, š, ž**.
- **Top function words:** *on, ei, ja, et, aga, kuid, või, kui, siis, ka,
  veel, juba, väga, nii, palju, kõik, see, need, mina, ma, sina, sa,
  tema, ta, meie, me, teie, te, nemad, nad, oli, olnud, olema, minema,
  tegema, saama, pidama, võib, tahab*.
- **N-gram / spelling patterns:** Final **-d** for plural; endings **-s /
  -st / -sse / -l / -lt / -le / -ks / -ga** (cases); verb 3SG **-b**
  (**teeb, räägib**); quotative **-vat** (**olevat, minevat**). Geminate
  consonants **tt, kk, pp, ss** common but shorter than Finnish's.
- **Morphology hooks:** Negative marker is invariant **ei** (contrast with
  Finnish conjugated **en/et/ei**). The **-vat** suffix is nearly unique.
- **Punctuation / orthography quirks:** No special punctuation. **š, ž**
  appear mostly in loans.
""",
"""# Differences from confusable languages: Estonian (est)

Primary confusability pair: **Finnish (fin)**.

**est vs. fin**
- **õ** is Estonian, never Finnish.
- **No vowel harmony in Estonian** — **ä** and **a** coexist freely
  within a native word, whereas Finnish forbids it.
- Negation: est **ei + stem** (invariant); fin **en / et / ei / emme /
  ette / eivät + stem** (conjugated).
- Pronouns: est **mina, sina, tema** vs. fin **minä, sinä, hän**.
- Verb 3SG ends in **-b** in est (**teeb**) and **-aa/-ee/...** in fin
  (**tekee**).
- Quantity: est writes the same geminate for Q2/Q3, disambiguated
  phonetically; fin writes all length phonemically with double letters.
- Loan vocabulary: est loans from Low German / German / Russian
  (**raamat** 'book', **kool** 'school'); fin from Swedish and older
  Germanic (**kirja**, **koulu**).

**est vs. other Baltic (lav / lvs / ltg)** (Latvian is NOT Uralic but
shares geography): Latvian uses macrons **ā ē ī ū** and cedillas
**ķ ļ ņ ģ**; Estonian uses none. No real confusion risk.
""")


# ---- Old French (fro) -----------------------------------------------------
lang("fro_Latn",
"""# Old French (fro)

## Summary

Old French (**Franceis**, **Roman**, **Lenga d'Oïl**) is the collective
term for the langues d'oïl spoken in northern France and associated
territories roughly from the **9th to the 14th century**. It is the
direct ancestor of Modern French (fra) and the language of foundational
medieval literature — **Chanson de Roland**, **Tristan**, **Chrétien de
Troyes**, and the early Arthurian cycle. ISO code: `fro` (639-3); no
639-1; 639-2 `fro`.

## Writing system

Latin script with medieval scribal conventions: **u** and **v** are one
letter, **i** and **j** are one letter, **w** is rare. No acute / grave /
circumflex / cedilla. Orthography varies heavily by scribe and region
(Francien, Norman, Picard, Anglo-Norman). Manuscript abbreviations
(tildes over vowels marking a nasal, **ꝑ** for *per/par*) may survive
into edited transcriptions.

## Historical note

Old French retained a **two-case noun system** (nominative / oblique)
that Middle and Modern French lost. Its lexicon is closer to Latin and
has heavy influence on Middle English via the Norman Conquest.
""",
"""# Grammar: Old French (fro)

- **Word order:** V2 / SVO with considerable freedom; the two-case system
  allows fronting of obliques. Subject pro-drop is common.
- **Morphology:** **Fusional** with more Latin-inherited inflection than
  Modern French.
- **Nouns:** **Two cases** — *cas sujet* (nominative) and *cas régime*
  (oblique/accusative). Masculine sg: NOM **li murs** 'the wall', OBL
  **le mur**; PL: NOM **li mur**, OBL **les murs**. Feminines largely
  lack case distinction.
- **Articles:** **li, la, le, les, el, al, del, dou, as**. Contracted
  forms (**el** from *en le*, **al** from *a le*) are frequent.
- **Pronouns:** Strong and weak series — **je, tu, il, nos, vos, il /
  eles**; objects **me, te, se, le, la, les, lui, lor**.
- **Verbs:** Conjugation like Modern French but with preservation of
  older Latin patterns: preterite (passé simple) is living prose tense;
  subjunctive is actively used; imperfect **-oie / -oies / -oit /
  -iiens / -iiez / -oient** (modern **-ais / -ait / -ions**).
- **Phonology:** Diphthongs **oi, ai, ei, oe, ue, ie** were still
  pronounced as diphthongs; the later levelling to modern monophthongs
  had not happened.
- **Syntax:** Verb-second with topic fronting; negation is preverbal
  **ne** (no **pas**/**point** reinforcement yet obligatory).
""",
"""# LID Characteristics: Old French (fro)

- **Script signals:** Plain Latin, **no acute / grave / circumflex /
  cedilla / diaeresis**. Orthography interchangeable **u/v** and **i/j**
  in many editions.
- **Top function words:** *li, la, le, les, el, al, del, dou, as, e, et,
  si, ne, ja, mais, mes, et si, or, ore, mout, molt, seignor, dame,
  de, par, pour, por, a, ou, qui, que, quant, com, comme, donc, ainz,
  onques, nus, nule, plus, bien, mal, tost*.
- **N-gram / spelling patterns:** Frequent **-oi-, -oie-, -eit-, -oit-,
  -ent, -ai, -ier** (especially verb endings); infinitives **-er, -ir,
  -oir, -re**; diphthong **oe / ue / ie** spellings preserved.
- **Morphology hooks:** Case alternation **-s / zero** in masculine
  nouns; imperfect endings **-oie / -oies / -oit / -iiens / -iiez /
  -oient**.
- **Punctuation / orthography quirks:** Edited texts often retain a
  pilcrow-style section marker or have slashes **/** as mid-sentence
  breaks. Tilde-over-vowel nasal abbreviations surface in scholarly
  editions.
""",
"""# Differences from confusable languages: Old French (fro)

Primary confusability pair: **Modern French (fra)**.

**fro vs. fra**
- **No French accents:** absence of **é è ê à ç ù â î ï** is a strong
  fro signal (edited/normalised editions may add an acute on final **-é**
  but not systematically).
- **Two-case nouns:** endings alternating **-s / zero** on nouns in
  non-plural contexts (**li murs / le mur**); Modern French has no case.
- **Definite articles:** **li, le, la, les, el, al, del** (fro) vs.
  **le, la, les, du, des, au, aux** (fra). **li** is a near-certain
  fro-only item.
- **Imperfect endings:** **-oie, -oit, -iiens, -oient** (fro) vs.
  **-ais, -ait, -ions, -aient** (fra).
- **Diphthong spellings:** **oe, ue, ai, ei** preserved; **çoi, reçoi,
  chanteir** etc. where Modern French has **cela, reçoit, chanter**.

**fro vs. Occitan (oci)** (langue d'oc): Occitan is a different branch
(d'oc vs. d'oïl). Occitan uses **ç** and **ò**, and function words
**lo, la, e, o, mas**; fro uses **li, la, e, et, mais** and no **ç** / **ò**.

**fro vs. Latin (lat):** Latin has **-us / -um / -is / -orum / -arum**
Case endings; fro has a much more reduced system. Latin has neither
**li / le / la / les** nor French-like word order.
""")


# ---- Guadeloupean Creole (gcf) & Guianese Creole (gcr) --------------------
lang("gcf_Latn",
"""# Guadeloupean Creole (gcf)

## Summary

Guadeloupean Creole (endonym **Kréyol Gwadloupéyen**) is a French-based
creole of the Lesser Antilles, spoken by roughly 400,000 people on
**Guadeloupe** and in Guadeloupean diaspora communities in metropolitan
France. It is part of the Lesser Antillean Creole continuum with
Martinican (mar not in set), Dominican, and **Saint Lucian (acf)**.
ISO code: `gcf` (639-3); no 639-1/2.

## Writing system

Latin script, GEREC/GEREC-F phonemic orthography: **ò, è, ñ, w, y**;
silent French etymological letters are dropped. Older texts sometimes
retain French-style spelling (hybrid orthography).

## Historical note

Derives from 17th–18th-century French dialects spoken by settlers and
contract labourers, shaped by contact with West-African languages brought
by enslaved people and, later, English and Spanish.
""",
"""# Grammar: Guadeloupean Creole (gcf)

- **Word order:** SVO; no subject–verb inversion in questions.
- **Morphology:** **Analytic**; no noun case, no verb inflection, no
  gender agreement.
- **Nouns:** Definite article **-la** postposed (**tab-la** 'the table',
  **zot-la** 'the people'); indefinite zero; plural **sé … -la** or
  the suffix **-la** on the noun.
- **Pronouns:** **an / mwen** (I), **ou** (you sg), **i / li** (he/she),
  **nou** (we), **zot** (you pl), **yo** (they). Possessive is pronoun
  after noun: **kay an-mwen** or **kaz-an-mwen** 'my house'.
- **Verbs:** Preverbal TMA triple:
  - **ka** progressive / habitual;
  - **té** anterior;
  - **ké / kay** irrealis / future.
  Stacking: **té ké** 'would', **té ka** 'was VERB-ing'.
- **Phonology:** r-drop (**pawòl** for *parole*); nasal vowels like
  French but fewer; **ò** [ɔ], **è** [ɛ].
- **Syntax:** Equational copula **sé** / **se**; locative uses preposition
  only (no copula). Negation preverbal **pa**.
""",
"""# LID Characteristics: Guadeloupean Creole (gcf)

- **Script signals:** Latin with **ò**, **è**, rare **ñ**; **w** frequent
  (**mwen, pawòl**); **y** for [j].
- **Top function words:** *sé, an, mwen, ou, i, li, nou, zot, yo, ka, té,
  ké, kay, pa, pou, si, la, lan, an, épi, èvè, èk, mé, mé non, oswa,
  adan, asi, oti, pwèmyé, dé*.
- **N-gram / spelling patterns:** Clitic article **-la / -lan** suffixed
  to nouns; pronouns **mwen / nou / yo / zot**; preverbal **ka / té / ké
  / kay** before verb stems.
- **Morphology hooks:** Zero verbal inflection — scan for the TMA triple.
  Plural/def article postposed to N rather than preposed like French.
- **Punctuation / orthography quirks:** Phonemic spelling replaces French
  silent letters; **kw** for *cr* (**kwè**), **w** for *oi/ou* (**mwen**),
  no cedilla.
""",
"""# Differences from confusable languages: Guadeloupean Creole (gcf)

Close set: **acf** (Saint Lucian), **gcr** (Guianese), **rcf** (Réunion);
lexifier **fra** (French).

**gcf vs. acf**
- Very similar; acf uses **sé** consistently, gcf also **sé** but some
  speakers use **se** orthographically. Short snippets ambiguous — use
  place names (Pointe-à-Pitre, Basse-Terre vs. Castries, Soufrière) and
  lexical markers (**doudou**, **ti-moun**).

**gcf vs. gcr**
- Guianese admixes Portuguese, Amerindian, and English; gcf is more
  homogeneous French-lexified. gcr tends to preserve more French-like
  spelling in informal texts.

**gcf vs. rcf**
- rcf uses **lé** as copula vs. gcf **sé**; rcf has nasal digraphs
  **anm**, **onm**; gcf does not.

**gcf vs. fra**
- No verb inflection (`je suis / tu es / il est`), postposed **-la**
  instead of preposed **le / la / les**, phonemic spellings **mwen**,
  **zot**, **sé**. Any run of French verb endings **-ais / -ait / -ons /
  -ez / -ent** means fra, not gcf.
""")

lang("gcr_Latn",
"""# Guianese Creole (gcr)

## Summary

Guianese Creole (endonym **Kréyòl Gwiyanè**) is a French-based creole
spoken in **French Guiana** (overseas département of France, capital
Cayenne). Speakers number roughly 50,000–100,000. It forms part of the
broader Lesser Antillean Creole continuum but with heavier contact
effects from Portuguese (Brazilian border) and Amerindian languages.
ISO code: `gcr` (639-3); no 639-1/2.

## Writing system

Latin script. Orthography oscillates between phonemic (GEREC-style, with
**ò, è, w, y**) and French-etymological (keeping silent letters). Web
text mixes both.

## Historical note

Emerged in the 17th–18th century from French settler speech in contact
with West-African substrates and neighbouring Portuguese / English /
Amerindian languages. Mutual intelligibility with Antillean creoles
(gcf, acf) is high but lexical divergence is noticeable.
""",
"""# Grammar: Guianese Creole (gcr)

- **Word order:** SVO; no inversion in questions.
- **Morphology:** **Analytic**; no inflection, no gender, no case.
- **Nouns:** Postposed definite article **-a / -an / -la** (**chyen-an**
  'the dog'). Plural via **yé** or clitic **-ya**.
- **Pronouns:** **mo** (I; uniquely short form, cf. Haitian **mwen**,
  gcf **mwen**), **to** (you sg), **li / i** (he/she/it), **nou** (we),
  **zòt** (you pl), **yé** (they).
- **Verbs:** Preverbal TMA: **ka** (progressive / habitual), **té**
  (anterior), **ké** (irrealis / future). The cleft **sa ka** ('it's
  the case that…') is frequent and characteristic.
- **Phonology:** r-drop, nasal vowels, lowered mid vowels (**ò, è**).
- **Syntax:** Copula **sa** (equational, often in **sa … ka …** clefts);
  negation preverbal **pa**.
""",
"""# LID Characteristics: Guianese Creole (gcr)

- **Script signals:** Latin; **mo** (1SG) is a strong marker vs. Antillean
  **mwen**. Sometimes French-style diacritics persist in hybrid spellings.
- **Top function words:** *mo, to, li, i, nou, zòt, yé, sa, sé, ka, té,
  ké, pa, pou, èk, èvè, la, lan, an, épi, mé, oswa, koté, ki, lè, pandan,
  adan, asou*.
- **N-gram / spelling patterns:** Pronoun **mo / to** instead of **mwen
  / ou**; cleft **sa ka**; postposed **-a / -an / -la**.
- **Morphology hooks:** TMA triple **ka / té / ké**; cleft **sa ka**;
  3PL pronoun **yé**.
- **Punctuation / orthography quirks:** Mixed French-etymological and
  phonemic spelling — expect inconsistencies within a single document.
""",
"""# Differences from confusable languages: Guianese Creole (gcr)

Close set: **gcf, acf, rcf, fra**. And Portuguese (por) appears in code-mix.

**gcr vs. gcf / acf**
- Strongest single signal: **mo** and **to** as 1SG / 2SG pronouns (gcr)
  vs. **mwen / ou** (gcf / acf).
- Cleft **sa ka** is more frequent in gcr.
- gcr admixes Portuguese loanwords (**bèl / bèla**, **djabo**).

**gcr vs. rcf**
- rcf 1SG is **mi** (not **mo** or **mwen**); rcf copula is **lé**.
- rcf has nasal digraphs **anm / onm** not found in gcr.

**gcr vs. fra**
- Absence of verb inflection, postposed articles **-a / -an**,
  phonemic spellings, pronouns **mo / to / yé**.

**gcr vs. por**
- Portuguese admixture is common in border areas; look for **ka / té /
  ké** as creole-only — they are alien to Portuguese grammar.
""")


# ---- Scottish Gaelic (gla) & Irish (gle) ----------------------------------
lang("gla_Latn",
"""# Scottish Gaelic (gla)

## Summary

Scottish Gaelic (endonym **Gàidhlig**) is a Goidelic Celtic language of the
Indo-European family (Indo-European → Celtic → Goidelic → Scottish
Gaelic). It is spoken by roughly **57,000 fluent speakers**, principally
in the **Outer Hebrides, Inner Hebrides, and parts of the Scottish
Highlands**, with smaller communities in Nova Scotia (Canadian Gaelic).
ISO codes: `gd` (639-1), `gla` (639-2/-3).

## Writing system

Latin script with only the **grave accent** on long vowels: **à, è, ì, ò,
ù**. No acute. Digraphs **bh, ch, dh, fh, gh, mh, ph, sh, th** represent
lenited consonants. Eclipsis is not orthographically standard in gla
(unlike Irish).

## Historical note

Gaelic split from Irish in the early medieval period; the standardised
modern orthography (post-1981 reforms) is leaner than Irish and has
**no acute accent**.
""",
"""# Grammar: Scottish Gaelic (gla)

- **Word order:** **VSO** (verb-initial), with information-structure
  fronting.
- **Morphology:** Celtic **initial mutations**: *lenition* (bh-, ch-,
  etc.) and *nasalisation* are lexically and grammatically conditioned.
- **Nouns:** Two genders (masc / fem), three cases (nominative, genitive,
  dative), number sg/pl. Article **an / a' / am / an t-** with strict
  mutation rules.
- **Pronouns:** Simple (**mi, thu, e, i, sinn, sibh, iad**) plus
  prepositional pronouns (**dhomh, dhut, dha, dhi, dhuinn, dhuibh,
  dhaibh** 'to me/you/him…'), which is a very Celtic feature.
- **Verbs:** Three tenses (past, present-habitual/future, future);
  non-past is normally expressed periphrastically with **tha + ag +
  verbal-noun**. The **verbal noun** + preposition **ag / a'** is the
  usual progressive (**tha mi ag ithe** 'I am eating').
- **Phonology:** Broad/slender consonant distinction (palatalisation
  signalled by surrounding **i / e**). No tone.
- **Syntax:** Copula **is** for identification; substantive **tha** for
  situation/location. Negation **cha** (past: **cha do**; non-past:
  **chan**).
""",
"""# LID Characteristics: Scottish Gaelic (gla)

- **Script signals:** Grave accent **only** — **à, è, ì, ò, ù**; **no
  acute**. Digraphs **bh, ch, dh, fh, gh, mh, ph, th**.
- **Top function words:** *a, an, am, a', an t-, is, tha, bha, bidh, bhios,
  cha, cha do, chan, gu, ag, a', anns, ann, air, aig, ri, le, do, de,
  agus, is, no, ach, nach, ged, ma, nuair, gun, gum, gur, bho, o, mar*.
- **N-gram / spelling patterns:** Initial digraphs **bh-, mh-, dh-, gh-,
  fh-, th-** on lenited forms; slender-vowel rule ("caol ri caol, leathann
  ri leathann") gives many **-idh, -aidh, -aibh** endings. Very common
  **-eadh, -eachd, -ichean, -aibh, -ean** word-finals.
- **Morphology hooks:** **ag / a' + verbal-noun** progressive;
  prepositional pronouns **dhomh, dhut, dha, ris, rium**.
- **Punctuation / orthography quirks:** Hyphens in **an t-Albannach**,
  **an t-aran** for article + vowel-initial noun.
""",
"""# Differences from confusable languages: Scottish Gaelic (gla)

Primary pair: **Irish (gle)**; also contact with **English (eng)**.

**gla vs. gle**
- **Accent**: gla uses **grave only** (à, è, ì, ò, ù); gle uses
  **acute only** (á, é, í, ó, ú). This single contrast is essentially
  definitive.
- **Eclipsis orthography:** gle writes eclipsis (**nd-, gc-, bp-, mb-,
  ng-, bhf-**); gla does not (eclipsis is absent or unwritten).
- Article forms differ: gla **an / a' / am / an t-** vs. gle
  **an / na / an t-**.
- Verb conjugation personal endings in gla are reduced (the analytic
  **tha mi / bha thu** pattern), whereas Irish is more synthetic.
- Common function words: gla **agus, ach, ann, air**; gle **agus, ach,
  ann, ar** — near-identical, but surrounding diacritics disambiguate.

**gla vs. bre / eng**: Trivial — Breton is Brittonic (uses **c'h, zh**),
English lacks Celtic mutations and acute/grave on vowels.
""")

lang("gle_Latn",
"""# Irish (gle)

## Summary

Irish (endonym **Gaeilge**) is a Goidelic Celtic language (Indo-European
→ Celtic → Goidelic → Irish). It is the first official language of the
**Republic of Ireland**, an official language of the European Union, and
a recognised language in Northern Ireland. Estimates of active speakers
(Gaeltacht + fluent L2) range from 70,000 daily to ~1.9 million occasional.
ISO codes: `ga` (639-1), `gle` (639-2/-3).

## Writing system

Latin script with the **acute accent only** (the *síneadh fada*):
**á, é, í, ó, ú**. Digraphs for lenited consonants (**bh, ch, dh, fh,
gh, mh, ph, sh, th**). Eclipsis is written explicitly:
**nd-, gc-, bp-, mb-, ng-, bhf-** — preceding letter disappears when
spoken.

## Historical note

Standard written Irish (*An Caighdeán Oifigiúil*) was codified in 1958;
dialect variation (Munster, Connacht, Ulster) remains visible in word
choice and spelling.
""",
"""# Grammar: Irish (gle)

- **Word order:** **VSO** — verb first, subject next.
- **Morphology:** Celtic **initial mutations**: *lenition* (séimhiú,
  written with **h** after the consonant) and *eclipsis* (urú, written
  by prefixing a letter).
- **Nouns:** Two genders (masc / fem), five declension classes, cases
  nominative / genitive / vocative / (dative fossilised). Articles **an
  / na** trigger specific mutations.
- **Pronouns:** Independent (**mé, tú, sé, sí, sinn, sibh, siad**) and
  prepositional pronoun series (**dom, duit, dó, di, dúinn, daoibh,
  dóibh** 'to me/you/him…'), an identifying Celtic feature.
- **Verbs:** Two primary tense systems (past vs. present / habitual,
  plus synthetic future and conditional). Synthetic vs. analytic
  alternation: **glanaim** 'I clean' synthetic, **glanann tú** 'you
  clean' analytic.
- **Phonology:** Broad (velarised) vs. slender (palatalised) consonant
  pairs; the surrounding vowel indicates quality ("caol le caol, leathan
  le leathan"). No tone.
- **Syntax:** Copula **is** (classification) vs. substantive **bí /
  tá / bhí** (location/state). Negation **ní** (non-past), **níor**
  (past perfective), **cha/chan** (Ulster only).
""",
"""# LID Characteristics: Irish (gle)

- **Script signals:** **Acute accent only** (á, é, í, ó, ú). Written
  eclipsis: word-initial **gc-, bp-, mb-, nd-, ng-, dt-, bhf-**. Lenition
  digraphs **bh-, mh-, ch-, dh-, fh-, gh-, ph-, sh-, th-**.
- **Top function words:** *an, na, a, ar, ag, ach, agus, is, tá, tá sé,
  bhí, beidh, ní, níor, nach, go, gur, a, leis, le, de, do, faoi, chuig,
  gan, nuair, má, dá, más, cé, cá, cén*.
- **N-gram / spelling patterns:** Endings **-aíonn, -íonn, -aim, -aigh,
  -íos, -aíodh, -aíos, -eacht, -acht, -íocht, -ann, -inn**. Genitive
  markers **-a / -e / -ach / -each**.
- **Morphology hooks:** Eclipsis clusters (**gc**, **nd**, **bp**) are
  essentially only Irish among CommonLID languages. Prepositional pronoun
  chain **dom, duit, dó, di, dúinn**.
- **Punctuation / orthography quirks:** Hyphen after article **t-** or
  **n-** before vowel (**an t-uisce**, **na n-amhrán**).
""",
"""# Differences from confusable languages: Irish (gle)

**gle vs. gla (Scottish Gaelic)**
- Accent: gle uses **acute** (á, é, í, ó, ú); gla uses **grave** (à, è,
  ì, ò, ù). Accent style alone is near-definitive.
- Eclipsis: orthographically written in gle (**gc-, bp-, bhf-, nd-,
  mb-, ng-, dt-**). Not written in gla.
- Copula/situational verb choice: gle **is / tá**; gla **is / tha**.
- Pronoun: gle **mé, tú, sé, sí**; gla **mi, thu, e, i**.
- Past particle + verb: gle **do + past stem**; gla **do + past stem**
  similarly but lenition / endings differ.

**gle vs. bre (Breton)**: Breton is Brittonic Celtic, not Goidelic. Has
**c'h**, **zh**, **ñ**; lacks Irish mutations and fadas.

**gle vs. eng (English)**: Obvious; Irish has synthetic verb forms
(**ceannóidh mé** 'I will buy'), fadas, and characteristic initial
mutation clusters never found in English.
""")


# ---- Goan Konkani (gom, Devanagari) ---------------------------------------
lang("gom_Deva",
"""# Goan Konkani (gom)

## Summary

Goan Konkani (endonym **कोंकणी** *Konkanī*) is a Southern Indic
(Indo-Aryan) language in the Indo-European family. It is the official
language of the **Indian state of Goa** and has official status in
**Karnataka** and **Kerala** as well, with ~2.5 million speakers in
coastal western India and in diaspora. ISO codes: `gom` (639-3); no
639-1; 639-2 `kok` for the macrocode.

## Writing system

Written in **Devanagari** in this folder (the `_Deva` suffix). Konkani is
notable for its **multiple scripts** historically: Devanagari (the
official Goan script), **Roman** (**Romi Konknni**, heavily used in
Goan diaspora and Catholic community publications), **Kannada** (in
Karnataka), and **Malayalam** (in Kerala). Only the Devanagari variety
is covered here.

## Historical note

Konkani was suppressed under Portuguese rule in Goa and went through
revival movements in the 19th–20th centuries. Its vocabulary includes
substantial Portuguese borrowings (**mez** 'table', **janel** 'window',
**botel** 'bottle**), a distinctive mark from other Indic languages.
""",
"""# Grammar: Goan Konkani (gom)

- **Word order:** **SOV**, like other Indic languages.
- **Morphology:** Indic-fusional with agglutinative-like case stacking.
  Three genders (masculine, feminine, neuter), two numbers.
- **Nouns:** Case system expressed mainly by postpositions:
  **-क, -न, -थांय (-k, -n, -thãy)** etc. Plural marked by stem changes
  and suffixes **-े, -ो, -ां**.
- **Pronouns:** 1SG **हांव / मी (hānv / mī)**, 2SG **तूं / तुज्यो (tū̃ /
  tujyo)**, 3SG **तो / ती (to / tī)**, 1PL **आमी (āmī)**, 2PL
  **तुमी (tumī)**, 3PL **ते / त्यो (te / tyo)**.
- **Verbs:** Copula **आसा (āsā)** 'is' (analogous to Marathi **आहे**) —
  *note*: this is a strong Konkani signal, distinct from Hindi **है (hai)**.
  Past tense via **-ले/-ली/-लें (-le / -lī / -lẽ)**. Gender+number
  agreement with the object in some tenses (ergative patterns).
- **Phonology:** Retroflex consonants (ट, ठ, ड, ढ, ण, ळ); the lateral
  **ळ (ḷ)** is frequent. Schwa deletion varies.
- **Syntax:** Postpositional. Extensive Portuguese-origin loan
  vocabulary co-occurring with native Indic morphology.
""",
"""# LID Characteristics: Goan Konkani (gom)

- **Script signals:** Devanagari (U+0900–097F). **ळ** (retroflex l) is
  shared with Marathi. Character inventory almost identical to Marathi /
  Hindi / Sanskrit.
- **Top function words:** *आसा (āsā 'is'), ना (nā 'no/not'), आनी (āni
  'and'), पूण (pūṇ 'but'), की (kī), वा (vā 'or'), कित्याक (kityāk 'why'),
  कोण (koṇ 'who'), म्हज्यो (mhajyo 'my'), तुज्यो (tujyo 'your'),
  हांव (hā̃v 'I'), तूं (tū̃ 'you'), तो (to 'he'), ती (tī 'she'),
  ते (te), आमी (āmī 'we'), तुमी (tumī 'you-pl'), आसात (āsāt 'are'),
  जाता (jātā 'becomes'), केलें (kelẽ 'did')*.
- **N-gram / spelling patterns:** Verb endings **-ता (-tā)**, **-लें
  (-lẽ)**, **-तात (-tāt)**; possessive **-चो / -ची / -चें** like Marathi;
  question marker **गी (gī)** sentence-finally (colloquial).
- **Morphology hooks:** Copula **आसा (āsā)** is the single most useful
  signal — Marathi uses **आहे**, Hindi **है**, Sanskrit **अस्ति**.
- **Punctuation / orthography quirks:** Portuguese-origin loans written
  in Devanagari produce sequences rare elsewhere (**पाव (pāv)** 'bread',
  **कापेल (kāpel)** 'chapel').
""",
"""# Differences from confusable languages: Goan Konkani (gom)

All Devanagari-script Indic languages in CommonLID form the confusion set:
**hin** (Hindi), **mar** (Marathi), **san** (Sanskrit), and sometimes
loanwords into **urd** (but urd uses Arabic script).

**gom vs. hin (Hindi)**
- Copula: gom **आसा** vs. hin **है** (strongest single diagnostic).
- Retroflex **ळ** (present in gom and mar, absent in hin).
- Possessive suffix: gom **-चो / -ची / -चें** vs. hin **का / की / के**.
- Loan vocabulary: Portuguese loans **मेज, जनेल, कापेल** in gom,
  Persian/Arabic loans **ख़ास, मशहूर** in hin.

**gom vs. mar (Marathi)**
- Closest pair. Shared: **ळ**, **-चो/-ची/-चें**, **आसा**-type copula
  (Marathi has **आहे**).
- Marathi's 'is' is **आहे** (āhe); Konkani's is **आसा** (āsā). These
  two words alone disambiguate most text.
- Marathi ergative particle **ने (ne)** is used in past transitive;
  Konkani uses **-न (-n)** or object-agreement without an overt ergative
  particle.
- Loanword signature: Portuguese in gom, Persian/English in mar.

**gom vs. san (Sanskrit)**
- Sanskrit has dense conjunct consonants and verb endings **-ति / -ामि
  / -स्ति**; gom has modern analytic syntax, no Vedic/Classical endings.
- Colloquial **आसा, आनी, म्हज्यो** are unknown in Sanskrit.
""")


# ---- Ancient Greek (grc) --------------------------------------------------
lang("grc_Grek",
"""# Ancient Greek (grc)

## Summary

Ancient Greek (endonym **Ἑλληνική**, *Hellēnikḗ*) is the historical
Indo-European language (Indo-European → Hellenic → Ancient/Koine) that
covers roughly **800 BCE to 600 CE**: from Homeric through Classical
(Ionic, Attic, Doric, Aeolic), Koine, and early Byzantine. It is the
language of the **Homeric epics, the Classical corpus (Plato,
Thucydides, tragedians), the Septuagint, and the Greek New Testament**.
ISO code: `grc` (639-3); 639-2 also `grc`; no 639-1.

## Writing system

Greek script with **polytonic** accentuation: the three Classical
accents — acute **ά**, grave **ὰ**, circumflex **ᾶ** — plus the two
breathings — rough **῾** (ἁ) and smooth **᾿** (ἀ) — on vowel-initial
words. Iota subscript **ᾳ, ῃ, ῳ** marks historical long diphthongs.
All of these are absent from Modern Greek's monotonic orthography.

## Historical note

In CommonLID `grc` text is drawn from scanned / digitised corpora
(Perseus, TLG-derived) and typically presents edited Classical or Koine
Greek with full polytonic accentuation.
""",
"""# Grammar: Ancient Greek (grc)

- **Word order:** Free but with strong clause-level conventions; verb
  tends to be clause-final in prose.
- **Morphology:** **Highly fusional**. Five cases (nominative, genitive,
  dative, accusative, vocative), three numbers (singular, dual, plural),
  three genders.
- **Nouns:** Three declensions; distinctive dative cases in **-ῳ / -ι /
  -ᾳ**; dual forms **-ω / -οιν**.
- **Pronouns:** Personal **ἐγώ, σύ, ἡμεῖς, ὑμεῖς**; 3rd-person substitutes
  (**αὐτός, ἐκεῖνος, οὗτος**); reflexive **ἑαυτοῦ**; relative **ὅς, ἥ,
  ὅ**.
- **Verbs:** Six tenses × four moods × three voices × three persons × two
  numbers; extensive participles and infinitives. Aspect (imperfective,
  aorist, perfect) is central; augment **ἐ-** prefixes past-tense finite
  indicatives; reduplication marks perfect.
- **Phonology (reconstructed):** Pitch accent (not stress); long/short
  vowels phonemic; aspirated consonants **θ, φ, χ**.
- **Syntax:** Rich particle system (**μέν … δέ, γάρ, οὖν, ἄρα, δή**);
  negation **οὐ / οὐκ / οὐχ** (indicative) vs. **μή** (non-indicative);
  infinitive and participle are foundational subordinators.
""",
"""# LID Characteristics: Ancient Greek (grc)

- **Script signals:** Greek with **polytonic** accents — grave **ὰ**,
  circumflex **ᾶ**, breathings **῾ ᾿** on initial vowels, iota subscript
  **ᾳ ῃ ῳ**. Presence of any of these, in more than trace amounts, is
  essentially definitive vs. Modern Greek.
- **Top function words:** *ὁ, ἡ, τό, τοῦ, τῆς, τῶν, τοῖς, ταῖς, καί,
  δέ, μέν, τε, γάρ, οὖν, γε, δή, ἄρα, ἀλλά, ἤ, εἰ, ἐάν, ἵνα, ὥστε,
  ὅτι, ὡς, ἐν, ἐπί, διά, κατά, μετά, περί, πρός, σύν, ὑπό, ἀπό, εἰς, ἐκ,
  οὐ, οὐκ, οὐχ, μή, γὰρ, οὕτως*.
- **N-gram / spelling patterns:** Endings **-ος, -ου, -ῳ, -ον, -οι, -ων,
  -οις; -η, -ης, -ῃ, -ην; -α, -ας, -ᾳ, -αν** (case forms); verb endings
  **-ω, -εις, -ει, -ομεν, -ετε, -ουσι; -ειν, -σθαι** (infinitives).
- **Morphology hooks:** Augment **ἐ-** before past stems (**ἔγραψα,
  ἐλθόν**); reduplication prefix (**γέγραφα**); the particle pair **μέν
  … δέ** is unique to Greek.
- **Punctuation / orthography quirks:** Greek question mark **;** (U+037E)
  and ano teleia **·** (U+0387) as above. Polytonic diacritics are the
  single strongest signal.
""",
"""# Differences from confusable languages: Ancient Greek (grc)

Primary confusability pair: **Modern Greek (ell)**.

**grc vs. ell**
- **Polytonic vs. monotonic** — any grave / circumflex / breathing / iota
  subscript strongly indicates grc.
- Vocabulary: grc **μέν … δέ, γάρ, οὖν, δή, ἄρα**; ell **όμως, λοιπόν,
  να, θα, όταν**.
- Morphology: grc has **infinitives** (**γράφειν, λαβεῖν**) and dative
  case (**τῷ ἀνδρί**); ell has no infinitive and the dative is replaced
  by **σε + accusative**.
- Augment **ἐ-** and reduplication **γε-** in past / perfect stems —
  present in grc, orthographically absent in modern constructions.
- Script additions in ell: newer loans with modern digraphs **μπ / ντ /
  γκ / τσ / τζ** appear very differently (grc uses **β, δ, γ, σ, ζ**
  without modern transliteration conventions).

**grc vs. Latin (lat)**: Obvious script distinction (Greek vs. Latin
alphabets), but Classical writers on mixed subject matter may code-mix.
Greek letters are the conclusive signal.
""")


# ---- Paraguayan Guarani (gug) ---------------------------------------------
lang("gug_Latn",
"""# Paraguayan Guarani (gug)

## Summary

Paraguayan Guarani (endonym **Avañe'ẽ**) is a Tupian language (Tupian →
Tupi-Guarani → Paraguayan Guarani). It is co-official with Spanish in
**Paraguay**, where roughly 90% of the population speaks it (~6 million
speakers), including many as a first language or in daily Spanish-Guarani
code-mixing known as **Jopara**. ISO code: `gug` (639-3); there is also
a macrocode `gn` (639-1) / `grn` (639-2) covering several Guarani
varieties.

## Writing system

Latin script with the **glottal stop** marked by an apostrophe **'**
(*puso*), and **nasalised vowels** marked by a tilde: **ã, ẽ, ĩ, õ, ũ,
ỹ**. The letter **y** represents the high central vowel [ɨ].
Phonemic orthography — each letter one phoneme. Digraphs **ch** and
**mb, nd, ng, nt** mark prenasalised stops.

## Historical note

Unique in the Americas for being the primary language of a non-
indigenous-majority country. **Jopara** (Guarani/Spanish code-mixing)
pervades informal written text; purer Guarani (*Guaraníete*) appears in
literature and formal contexts.
""",
"""# Grammar: Paraguayan Guarani (gug)

- **Word order:** Flexible with SVO tendency; verb-subject order common
  in discourse.
- **Morphology:** **Agglutinative / polysynthetic** — verbs can carry
  subject, object, tense, aspect, mood, evidentiality, and second-order
  modifiers in a single word.
- **Nouns:** No grammatical gender. Plural via **-kuéra** (often reduced
  to **kwera**). Possessive prefixes on nouns (**che**-, **nde**-, **i**-,
  **ñande**-, **pende**-) rather than separate pronouns.
- **Pronouns:** **che** (I), **nde / ne** (you), **ha'e / ha'ekuéra**
  (he/she/they), **ñande / ore** (inclusive / exclusive 'we' — a defining
  Tupian feature), **peẽ** (you pl). Subject is cross-referenced on the
  verb.
- **Verbs:** Two verb classes — *active* (subject prefixes **a-, re-,
  o-, ja-/ña-, ro-, pe-, o-**) vs. *stative* (prefixes **che, nde, i,
  ñande, ore, pende, i**). Tense/aspect via suffixes **-ta** (future),
  **-kuri / -ra'e** (past), **-va'ekue** (past habitual).
- **Phonology:** Contrastive oral and nasal vowels; **y** [ɨ] and **ỹ**
  [ɨ̃]; prenasalised voiced stops **mb, nd, ng**; glottal stop phonemic.
- **Syntax:** Heavy use of particles (**voi, niko, katu, nipo'ã**). The
  *negative circumfix* **nd(a)- … -i** wraps verbs (**ndaikuaái** 'I
  don't know').
""",
"""# LID Characteristics: Paraguayan Guarani (gug)

- **Script signals:** Nasalised vowels **ã, ẽ, ĩ, õ, ũ, ỹ**; apostrophe
  (glottal stop) mid-word; the letter **y** used as a vowel;
  prenasalised digraphs **mb-, nd-, ng-** at word starts.
- **Top function words:** *ha, ha'e, ha'ekuéra, niko, katu, voi, peẽ,
  ñande, ore, che, nde, ne, ko, pe, peteĩ, mokõi, opa, heta, mba'e,
  mba'éichapa, mba'éicha, mamo, mamópa, araka'e, ikatu, iporã, nderejavyi,
  upéi, upéva, jepi, avei, jepe, -kuéra, -ma, -nte, -pa, -rõ, -ta*.
- **N-gram / spelling patterns:** Apostrophe inside words (**ñe'ẽ,
  che'ra, ha'e**); prenasalised **mb, nd, ng** onsets; possessive
  prefix chains (**cheróga** 'my house', **nderóga** 'your house',
  **iróga** 'his house').
- **Morphology hooks:** Negative circumfix **nd(a)- … -i**; future suffix
  **-ta**; plural **-kuéra**; subject prefixes **a-, re-, o-, ja-/ña-,
  ro-, pe-**.
- **Punctuation / orthography quirks:** The apostrophe is a letter, not
  a stylistic quote. Jopara text mixes Spanish sentences liberally — do
  not be fooled by embedded Spanish.
""",
"""# Differences from confusable languages: Paraguayan Guarani (gug)

Within CommonLID, Guarani is typologically isolated — no other Tupian
language is present. Main confusability is with **Spanish (spa)** because
of Jopara code-mixing.

**gug vs. spa**
- Nasal vowels **ã ẽ ĩ õ ũ ỹ** are Guarani; Spanish lacks them.
- Apostrophe-as-glottal-stop inside words (**ñe'ẽ**) is Guarani.
- The letter **y** as a vowel (**ypykuéra**, **yvy** 'earth') is
  Guarani; Spanish uses **y** only as a consonant / conjunction.
- Prenasalised onsets **mb-, nd-, ng-** are Guarani.
- Morphology: **nd- … -i** negative circumfix, **-kuéra** plural,
  **che/nde/ñande** possessive prefixes are Guarani.
- Jopara detection: Spanish sentences or clauses may appear with Guarani
  morphology wrapping them (**la casa-kuéra**, **nombre-pe**). Presence
  of any Guarani marker in a Spanish-looking sentence → tag as gug, not
  spa.

**gug vs. other Latin-script languages:** nasalised vowel letters
**ã ẽ ĩ õ ũ** are also used by Portuguese (**ã, õ** only) and
Vietnamese. Combined with apostrophe glottals and **mb-/nd-/ng-**
Guarani is unmistakable.
""")


# ---- Gujarati (guj) -------------------------------------------------------
lang("guj_Gujr",
"""# Gujarati (guj)

## Summary

Gujarati (endonym **ગુજરાતી** *Gujarātī*) is an Indo-Aryan language
(Indo-European → Indo-Iranian → Indic → Western Indic). It is the
official language of the **Indian state of Gujarat** and one of the 22
scheduled languages of India. Around **56 million first-language
speakers**, concentrated in Gujarat and in substantial diaspora
communities in East Africa, the UK, and North America. ISO codes: `gu`
(639-1), `guj` (639-2/-3).

## Writing system

Written in the **Gujarati script (Gujr, U+0A80–0AFF)**, a Brahmic
abugida derived from Devanagari. Its most visually distinctive feature
is the **absence of the shirorekha** (the top horizontal line that
covers Devanagari characters): Gujarati letters 'float'. Inherent vowel
is /ə/; vowel signs attach to consonants.

## Historical note

Gujarati emerged as a distinct literary language in the medieval period
(12th–15th c.); modern prose was shaped by **Narmad** and **Dalpatram**
in the 19th century, and further by **M. K. Gandhi**, for whom it was
the first language.
""",
"""# Grammar: Gujarati (guj)

- **Word order:** **SOV** with a relatively rigid verb-final tendency.
- **Morphology:** **Fusional / agglutinative**. Three genders (masculine,
  feminine, neuter), two numbers, several cases realised through
  postpositions.
- **Nouns:** Mas sg **-o / -o / consonant**, fem sg **-ī / -a**, neuter
  sg **-ũ**. Plural formed by stem change and suffixes. Case by
  postpositions: **-ને (-ne)** dative/accusative, **-થી (-thī)** ablative/
  instrumental, **-માં (-mā̃)** locative, **-ના / -ની / -નું (-nā / -nī /
  -nũ)** genitive with gender agreement.
- **Pronouns:** 1SG **હું (hũ)**, 2SG **તું (tũ)** / polite **તમે
  (tame)**, 3SG **તે / એ (te / e)**, 1PL **અમે / આપણે (ame / āpaṇe —
  exclusive / inclusive)**, 2PL **તમે (tame)**, 3PL **તેઓ / એઓ (teo /
  eo)**.
- **Verbs:** Copula **છે (che)** 'is' (present)/ **હતો/હતી/હતું (hato /
  hatī / hatũ)** (past). Tenses built by auxiliary chains. Ergative
  case marker **-એ (-e)** with transitive past verbs (Indo-Aryan
  ergative split).
- **Phonology:** Retained vowel **ə** in final syllables (unlike Hindi
  which deletes it); retroflex consonants (**ટ, ઠ, ડ, ઢ, ણ, ળ**) like
  other Indic; no breathy voiced consonants lost as in some sister
  languages.
- **Syntax:** Postpositional. Echo-word duplication common (**ચાપાણી
  chā-pāṇī** 'tea and stuff').
""",
"""# LID Characteristics: Gujarati (guj)

- **Script signals:** Gujr script; **no shirorekha** (visually the
  strongest distinguishing cue among Brahmic scripts). Letters
  **ક (k), ગ (g), ય (y), લ (l), ર (r), મ (m), ન (n)** have distinctive
  Gujarati shapes without the top bar.
- **Top function words:** *છે (che 'is'), હતો/હતી/હતું (hato/hatī/hatũ
  'was'), નથી (nathī 'is not'), અને (ane 'and'), કે (ke 'that/or'),
  પણ (paṇ 'but'), જ (ja 'only/emphatic'), માં (mā̃ 'in'), ને (ne
  'to/DAT'), થી (thī 'from/with'), નો / ની / નું (no / nī / nũ 'of'),
  મારું / તારું / એનું (mārũ / tārũ / enũ 'my / your / his'),
  કયું (kayũ 'which'), આ (ā 'this'), તે (te 'that'), એ (e 'that'),
  હું (hũ 'I'), તું (tũ 'you'), તમે (tame 'you-pl'), અમે (ame 'we'),
  ક્યાં (kyā̃ 'where'), શું (śũ 'what')*.
- **N-gram / spelling patterns:** Neuter ending **-ũ (-ું)** on nouns
  / possessives is extremely frequent (**છોકરું, ઘરનું, મારું**). Verb
  ending **-ે (-e)** for 3SG present, **-ો (-o)** for 2PL/polite imperative.
- **Morphology hooks:** Copula **છે** is a near-unique mark. Ergative
  **-એ** on subjects of transitive past. Genitive **-નો/-ની/-નું** agrees
  with head noun.
- **Punctuation / orthography quirks:** Uses Devanagari danda **।** and
  double danda **॥**, though Western punctuation is common in web text.
""",
"""# Differences from confusable languages: Gujarati (guj)

In CommonLID, Brahmic confusability sits across **Devanagari** (hin, mar,
san, gom), **Bengali** (ben, asm), **Gurmukhi** (pan), **Oriya** (ory),
**Tamil** (tam), **Telugu** (tel), **Kannada** (kan), **Malayalam** (mal),
and **Gujarati** itself.

**guj vs. hin / mar / san / gom (Devanagari)**
- Script alone is definitive: Gujarati letters lack the **shirorekha**
  top bar; Devanagari has it. Any text with a uniform top bar is
  Devanagari, not Gujarati.
- If script is Gujr, it is Gujarati.

**guj vs. ben / asm (Bengali script)**
- Very different letter shapes; no confusion at the character level.

**guj vs. pan (Gurmukhi)**
- Gurmukhi also lacks a continuous shirorekha but has a different letter
  inventory; scripts do not share Unicode blocks.

**guj vs. Gujarati varieties within India**
- In CommonLID there is no further split, so any Gujarati-script text is
  tagged `guj`. Code-mixing with **English** is common in modern web text;
  the presence of **છે, નથી, માં, નું** anywhere is diagnostic.
""")


# ---- Kikuyu (kik) ---------------------------------------------------------
lang("kik_Latn",
"""# Kikuyu (kik)

## Summary

Kikuyu (endonym **Gĩkũyũ**) is a Bantu language of the Niger-Congo family
(Niger-Congo → Atlantic-Congo → Bantu → Northeast Bantu → Kikuyu). It is
spoken by roughly **7 million people**, primarily the Kikuyu people of
**central Kenya**, and is one of Kenya's largest indigenous languages.
ISO codes: `ki` (639-1), `kik` (639-2/-3).

## Writing system

Latin script with the distinctive letters **ĩ** (i with tilde) and
**ũ** (u with tilde), which represent mid-close front and back vowels
respectively. No other diacritics. Digraph **nj, mb, nd, ng** for
prenasalised consonants.

## Historical note

Standardised orthography dates to the early 20th century (Kenya Language
Board and subsequent revisions). The tilde-vowel convention distinguishes
a seven-vowel system on the page.
""",
"""# Grammar: Kikuyu (kik)

- **Word order:** SVO.
- **Morphology:** **Agglutinative** with the characteristic Bantu noun-
  class system (~18 classes, with prefix pairs singular/plural).
- **Nouns:** Class prefixes **mũ- / a-, kĩ- / i-, rũ- / mĩ-, ũ- / ma-**
  etc. Plural is formed by replacing the singular prefix with the paired
  plural one: **mũndũ / andũ** 'person / people', **gĩthomo / ithomo**
  'school / schools'.
- **Pronouns:** 1SG **nĩĩ / niĩ**, 2SG **wee**, 3SG **we**, 1PL **ithuĩ**,
  2PL **inyuĩ**, 3PL **oo / acio**. Pronoun concord prefixes agree with
  the subject's class on the verb.
- **Verbs:** Complex verbal template: **(subj prefix)-(tense / aspect /
  mood)-(obj prefix)-ROOT-(extensions)-(final vowel)**. Tense morphology
  includes **-ra-** (present), **-a-** (remote past), **-rĩ-** (future),
  **-ĩ-** (near past).
- **Phonology:** Seven vowels (**a, e, ẽ=ĩ, i, o, õ=ũ, u**); tone is
  phonemic but not normally written. Prenasalisation **mb, nd, ng, nj**.
- **Syntax:** Subject/object agreement on the verb; noun-class concord
  extends to adjectives, demonstratives, and possessives.
""",
"""# LID Characteristics: Kikuyu (kik)

- **Script signals:** **ĩ** and **ũ** (vowels with tilde) are nearly
  diagnostic among Bantu languages in CommonLID. Kikuyu also uses plain
  Latin vowels. No other diacritics.
- **Top function words:** *na, nĩ, kana, no, no nĩ, ndarĩ, ndirĩ, gũtirĩ,
  kũrĩ, rĩrĩa, angĩ, arĩa, ũcio, ũyũ, ĩyĩ, ĩrĩa, tondũ, nĩgũkorwo, nĩundũ,
  tũkũ, twĩ, rĩu, tene, kaba, gũtuma, mũciĩ, mũthenya, mũthamaki*.
- **N-gram / spelling patterns:** Tilde-vowel sequences **ĩrĩa, ũyũ, ũcio,
  ũhoro**; prenasalised onsets **nj-, mb-, nd-, ng-**; noun-class prefix
  pairs (**mũ-/a-, kĩ-/i-, gĩ-/i-, ũ-/ma-**).
- **Morphology hooks:** Class-concord prefixes on adjectives and verbs
  (**mũndũ mwega** 'good person', **andũ ega** 'good people'); tense
  infixes **-ra-, -rĩ-, -a-, -ĩ-**.
- **Punctuation / orthography quirks:** Word-internal **ĩ / ũ** is
  load-bearing, not typographic decoration.
""",
"""# Differences from confusable languages: Kikuyu (kik)

In CommonLID the Bantu cluster is **swa / swh, zul, xho, sna, nso, sot,
lug, lin, nyn** plus Kikuyu. Austronesian **mlg** is Latin-script but
distinctive.

**kik vs. swa / swh (Swahili)**
- No **ĩ / ũ** in Swahili; Swahili has heavy Arabic vocabulary
  (**kitabu, sababu, rais**) that Kikuyu lacks.
- Kikuyu's noun-class prefixes **mũ-, gĩ-, rũ-** are visually different
  from Swahili's **m-, ki-, u-**.

**kik vs. lug / nyn (Uganda Bantu)**
- Luganda has geminate consonants written double (**bbuye, ddala**) and
  prefixes **ol-, ok-, ob-**. Kikuyu doesn't write geminates.
- Nyankole is close to Luganda; neither uses **ĩ / ũ**.

**kik vs. zul / xho (Nguni)**
- Nguni languages have click letters **c, q, x** used for clicks.
  Kikuyu has no clicks.

**kik vs. sna (Shona)**
- Shona uses digraphs like **zh, sv, tsv, nh** that Kikuyu lacks, and
  has no tilde-vowels.

The tilde-vowel diagnostic is close to definitive: any **ĩ** or **ũ** in
a Bantu-shaped text is Kikuyu in this dataset.
""")


# ---- Ligurian (lij) -------------------------------------------------------
lang("lij_Latn",
"""# Ligurian (lij)

## Summary

Ligurian (endonym **Ligure**, **Zeneize** for the Genoese dialect) is a
Gallo-Italic Romance language (Indo-European → Italic → Romance →
Gallo-Italic → Ligurian). It is spoken in **Liguria, north-western
Italy**, plus Monaco (where **Monégasque** is a Ligurian variety) and
parts of Sardinia, Corsica, and Gibraltar. ~500,000–800,000 speakers,
mostly older. ISO codes: `lij` (639-3); no 639-1; 639-2 `roa` (catch-all).

## Writing system

Latin script. Standard Genoese orthography (*Grafia Ofiçiâ*) uses:
**ç** (where Italian has *z* or *c*), **ö** (open mid front), **ae**
or **æ** in some spellings, and **x** [ʃ], a very distinctive Ligurian
grapheme.

## Historical note

Medieval Ligurian was a prestige Mediterranean trading language (Genoa).
Modern written Ligurian has a small but active literary scene; web text
alternates between the standard and older French-influenced spellings.
""",
"""# Grammar: Ligurian (lij)

- **Word order:** SVO, like Standard Italian.
- **Morphology:** **Fusional**; similar to Italian but with many
  reductions and loss of final vowels.
- **Nouns:** Two genders, two numbers. Plural often marked by vowel
  change plus **-i / -e** rather than consistent **-s / -i**.
- **Articles:** **o / a / i / e** (definite) — not Italian **il / la /
  gli / i / le**; indefinite **un / unna**.
- **Pronouns:** 1SG **mi**, 2SG **ti**, 3SG **lê / lê-a**, 1PL **noî**,
  2PL **voî**, 3PL **lô**. Subject clitic system (common in Gallo-Italic)
  before conjugated verbs.
- **Verbs:** Three conjugations (**-â, -é, -î**). Clitic subjects before
  verbs (**ti ê** 'you are', **o l'ê** 'he is'). Auxiliaries **avei**
  'have' and **êse** 'be'.
- **Phonology:** Reduced vowel inventory with open **ö** and **ae**;
  lenition of intervocalic consonants; word-final truncations common.
- **Syntax:** Subject clitics mandatory in many dialects; **no** before
  verbs for negation.
""",
"""# LID Characteristics: Ligurian (lij)

- **Script signals:** **ç**, **ö**, apostrophe in subject-clitic
  contractions (**l'ê, o l'à**); **x** used as [ʃ] (**xilu, pexo**);
  **ae** or **æ** in some spellings.
- **Top function words:** *o, a, i, e, do, da, a-o, a-a, a-i, a-e, de,
  pe, con, senza, ma, però, anche, ascì, che, comme, quande, se, sotta,
  sciù, zu, in, dâ, doa, ô, â, no, nisciun, aonde, ascì, ninte, tutto*.
- **N-gram / spelling patterns:** Very high frequency of **ç** and **ö**;
  subject-clitic contractions **l'ê, ti ê, o l'à, a l'é**; word-final
  truncation (*homm* for *uomo*, *cönn* for *canone*).
- **Morphology hooks:** Clitic subject + **l'** + auxiliary is a
  hallmark (e.g. **o l'à mangiòu** 'he has eaten'). Verb ending in
  **-òu / -êu / -îu** past participle.
- **Punctuation / orthography quirks:** Apostrophe is load-bearing in
  clitic contractions, not decorative.
""",
"""# Differences from confusable languages: Ligurian (lij)

Close set: **Italian (ita)**, **Venetian (vec)**, **Occitan (oci)** —
all Gallo-Italic/Romance with partial overlap.

**lij vs. ita**
- **ç, ö, x, æ** are Ligurian, not Italian.
- Articles: lij **o / a / i / e**; ita **il / la / gli / i / le**.
- Subject clitics (**o l'è, a l'é, ti ê**) are Ligurian / Gallo-Italic,
  absent in Italian.
- Lexicon: **pê** (father) vs. ita **padre**, **donna** kept in ita but
  lij prefers **fomma**.

**lij vs. vec (Venetian)**
- Venetian uses **ł** (barred l) and **s'c** in phonology. Ligurian uses
  **x** for [ʃ] and **ç**.
- Articles: vec **el / la / i / le**; lij **o / a / i / e**.
- Subject clitics: both have them but with different phonological shape
  (vec **te / el**; lij **ti / o / a**).

**lij vs. oci (Occitan)**
- Occitan uses **ò, ç, u**; Ligurian uses **ö, ç, x**.
- Occitan function words **lo, la, los, las, e, o, mas, quin**; Ligurian
  **o, a, i, e, e, ma**.
- Verb endings differ: oci **-a / -ava / -ará / -ant**; lij **-a / -ava /
  -à / -ando**.

**lij vs. Standard Italian (ita)** is the most frequent confusion for
web text; the **ç / ö / x / subject-clitic** constellation is the
disambiguator.
""")


# ---- Lingala (lin) --------------------------------------------------------
lang("lin_Latn",
"""# Lingala (lin)

## Summary

Lingala (endonym **Lingála**) is a Bantu language (Niger-Congo →
Atlantic-Congo → Bantu → Northwest Bantu → Bangi-Ntomba → Lingala).
It is spoken by roughly **30–40 million people** across the Congo
Basin, principally in the **Democratic Republic of the Congo** and
the **Republic of the Congo** (Brazzaville, Kinshasa), with additional
speakers in Angola and the Central African Republic. ISO codes: `ln`
(639-1), `lin` (639-2/-3).

## Writing system

Latin script, with accent marks indicating tone in careful writing:
**á, é, í, ó, ú** (high tone) and **à, è, ì, ò, ù** (low tone). In
everyday web text tone diacritics are often omitted. Additional letters:
**ɛ** (open e) and **ɔ** (open o) in some orthographies.

## Historical note

Lingala developed as a lingua franca along the Congo River in the 19th
century from the Bobangi/Mangala trade languages. It absorbed heavy
French loan vocabulary in the colonial period and continues to code-mix
with French in Kinshasa and Brazzaville.
""",
"""# Grammar: Lingala (lin)

- **Word order:** SVO.
- **Morphology:** **Agglutinative** Bantu with simplified noun-class
  morphology compared to other Bantu languages (some classes have merged).
- **Nouns:** Classes marked by prefixes **mo-/ba- (1/2), mo-/mi- (3/4),
  li-/ma- (5/6), e-/bi- (7/8), m-/n- (9/10), lo-/n- (11/10)**. Plural by
  prefix change.
- **Pronouns:** 1SG **ngáí**, 2SG **yó**, 3SG **yě / azali**, 1PL **bísó**,
  2PL **bínó**, 3PL **bangó**. Subject concord prefixes on verbs:
  **na-, o-, a-, to-, bo-, ba-**.
- **Verbs:** Tense/aspect via infixes:
  - present / habitual: **-koN-** or bare stem;
  - past: **-a-**;
  - future: **-ko-**.
  Template: **SUBJ-TENSE-ROOT-VOWEL**.
- **Phonology:** Two-tone (H / L); seven vowels (a, e, ɛ, i, o, ɔ, u).
  No clicks.
- **Syntax:** Preverbal negation **té** (often sentence-final in colloquial
  speech). Copula **azali / ezali**. Many French loans (**loisir, moto,
  restaurant, kaka**).
""",
"""# LID Characteristics: Lingala (lin)

- **Script signals:** Latin with sporadic **á é í ó ú** and **à è ì ò ù**;
  possibly **ɛ, ɔ** in linguistic texts. Many French loanwords carry
  French diacritics (**café, école**).
- **Top function words:** *na, pe, te, tó, bó, bá, ngáí, yó, bísó, bínó,
  bangó, aza, azali, ezali, nazali, tozali, bozali, bazali, kasi, soki,
  tango, wapi, nini, pona, mpo, libosó, mingi, moke, kala, lelo, lobi,
  ndenge, bongo, oyo, wana, ya, na, to, kokende, koloba, komona, kolia*.
- **N-gram / spelling patterns:** Subject-agreement prefixes on verbs
  (**nakokende**, **tokolia**, **bakoloba**); prefix **ko-** for infinitive;
  reduplication for intensification (**kala-kala**, **malamu-malamu**).
- **Morphology hooks:** Class pair **mo-/ba-** (person / persons);
  tense infix **-ko-** (future). Copula **azali / ezali**.
- **Punctuation / orthography quirks:** French quotation marks **« »**
  in formal text; accents often dropped in informal web use.
""",
"""# Differences from confusable languages: Lingala (lin)

Close set: **swa / swh, zul, xho, sna, sot, nso, kik, lug, nyn** (all
Bantu); French (**fra**) contact looms large.

**lin vs. swa / swh (Swahili)**
- Both Bantu, but Swahili has strong Arabic loan vocabulary
  (**kitabu, sababu**); Lingala has French loans (**moto, loisir**).
- Subject prefix inventories differ: swa **ni-, u-, a-, tu-, m-, wa-**;
  lin **na-, o-, a-, to-, bo-, ba-**.

**lin vs. kik**
- Kikuyu has **ĩ / ũ** diacritics; Lingala doesn't.
- Kikuyu has complex noun-class prefixes (**mũ-, gĩ-, rũ-**); Lingala is
  simplified.

**lin vs. lug / nyn (Uganda Bantu)**
- Luganda writes geminate consonants double (**bb, dd, kk, mm**);
  Lingala doesn't.
- Nyankole uses **ky-, gy-** clusters rare in Lingala.

**lin vs. sna (Shona)**
- Shona uses **zh, nh, sv, tsv**; Lingala doesn't.

**lin vs. fra (French)**
- French loans in Lingala are embedded but the Bantu morphology wraps
  them (**na moto moko**, **na ecole**). Presence of subject prefixes
  **na-/to-/bo-/ba-** or the copula **azali / ezali** tags lin.
""")


# ---- Latgalian (ltg) ------------------------------------------------------
lang("ltg_Latn",
"""# Latgalian (ltg)

## Summary

Latgalian (endonym **latgalīšu volūda** or simply **latgalīšu**) is an
East Baltic language (Indo-European → Balto-Slavic → Baltic → East
Baltic → Latvian/Latgalian). Opinions differ on whether it is a distinct
language or a dialect of Latvian; Latvian law recognises it as a
**historic variant of Latvian with special status**. Roughly **150,000–
200,000 speakers** in the **Latgale region of eastern Latvia**. ISO code:
`ltg` (639-3); no 639-1; 639-2 `bat` catch-all.

## Writing system

Latin script with both Latvian letters (**ā, ē, ī, ū, č, š, ž, ķ, ļ, ņ,
ģ**) and additional letters characteristic of Latgalian: **y** (close
mid central vowel, borrowed from Polish/Belarusian orthographic habits),
**ō** (long o), and the cluster **dz, dž**. The letter **y** is the
single strongest visual diagnostic versus Standard Latvian, which does
not use it.

## Historical note

Written Latgalian developed independently within the Catholic
Polish-Lithuanian sphere, diverging orthographically from the Protestant
Latvian tradition further west. Suppressed in the Soviet era, it has
undergone revival since 1990.
""",
"""# Grammar: Latgalian (ltg)

- **Word order:** SVO, with considerable freedom; similar to Latvian.
- **Morphology:** **Fusional** Baltic. Seven cases (nominative, genitive,
  dative, accusative, instrumental, locative, vocative), two numbers,
  two genders (masculine, feminine).
- **Nouns:** Similar declension classes to Latvian with slightly
  different endings: **-s / -ys** (M NOM SG), **-a / -o** (F NOM SG),
  plural **-i / -ys / -ys**.
- **Pronouns:** 1SG **es / iz**, 2SG **tu**, 3SG **jis / jei**, 1PL
  **mes**, 2PL **jius**, 3PL **jī / jis**.
- **Verbs:** Three conjugation classes like Latvian, with endings that
  can differ (Latvian 3SG present often **-a**, Latgalian may use
  **-ā** or **-ej** depending on class). Reflexive **-ys** (cf. Latvian
  **-ās**).
- **Phonology:** Additional central vowel **y** [ɨ] not present in
  Latvian; three-tone system in some dialects (level, falling, broken);
  palatalisation more marked than in Standard Latvian.
- **Syntax:** Similar to Latvian, including negative concord (**nikod
  nav** 'never isn't').
""",
"""# LID Characteristics: Latgalian (ltg)

- **Script signals:** **y** as a vowel (not a consonant) is the single
  most diagnostic letter — Latvian does **not** use **y**. Also **ō**
  (long o); long-vowel macrons **ā, ē, ī, ū**; and the Latvian soft
  consonants **ķ, ļ, ņ, ģ**.
- **Top function words:** *i, ir, navā, nav, nu, ni, na, da, iz, bez, pi,
  ar, uz, pa, par, kas, kurs, kura, kurō, kai, cik, voi, bet, i, kai,
  tys, ta, ti, te, šis, taidys, kurys, myušu, jyuso, mes, jius*.
- **N-gram / spelling patterns:** Words containing internal **y**
  (**myuns 'us'**, **tyvuškas 'father'**, **byut**). Diphthong spellings
  **ei, uo, ai**; long vowels marked with macron.
- **Morphology hooks:** 3SG verb endings often **-ej / -ā**; negation
  **ni-**; demonstratives **tys / ta / ti**.
- **Punctuation / orthography quirks:** **y** appears freely inside
  words; Latvian uses only **i**.
""",
"""# Differences from confusable languages: Latgalian (ltg)

Closest pair by a wide margin: **Latvian (lav / lvs)**. Also geographically
adjacent **lit** (Lithuanian — not in CommonLID) and **rus** (Russian).

**ltg vs. lvs / lav**
- **y** is Latgalian-only. Any **y** inside a Baltic-looking word → ltg.
- Spelling of long vowels and diphthongs differs: ltg **myus, jyus, tyvs,
  muti**; Latvian **mūs, jūs, tēvs, mūsu**.
- Verb endings diverge in the 3rd person and reflexive: ltg **-ej, -ys**;
  Latvian **-a, -ās**.
- Function words: ltg **i, nav, kai, myušu**; Latvian **un, nav, kā,
  mūsu**.

**ltg vs. lav (macro)**
- `lav` is the Latvian macrocode that technically covers ltg. In CommonLID
  the labels `lvs` (Standard Latvian) and `ltg` (Latgalian) are the two
  realisations; `lav` falls between them as the macrocode — treat it
  accordingly.

**ltg vs. rus (Russian)**
- Different script — Latgalian is Latin, Russian Cyrillic.
- Latgalian does have Polish / Russian loan vocabulary, but written in
  Latin it is easily distinguished.
""")


# ---- Luganda (lug) --------------------------------------------------------
lang("lug_Latn",
"""# Luganda (lug)

## Summary

Luganda (endonym **Oluganda**) is a Bantu language (Niger-Congo →
Atlantic-Congo → Bantu → Great Lakes Bantu → Nyoro-Ganda → Luganda). It
is the most widely spoken indigenous language in **Uganda** (~5–7 million
L1 speakers plus many L2), especially in the central Buganda region
around **Kampala**. ISO codes: `lg` (639-1), `lug` (639-2/-3).

## Writing system

Latin script. Distinctive feature: **geminate consonants are written
double** — **bb, dd, gg, kk, mm, nn, pp, ss, tt, ww, yy, zz**. Long
vowels also written double. The letter **c** represents [tʃ] and **j**
represents [dʒ]. No clicks; no tone marks in standard orthography.

## Historical note

First written by European missionaries in the 1870s; the modern
orthography was standardised by the Orthography Committee of the Buganda
Government (1947), and later by the Luganda Orthography Committee.
""",
"""# Grammar: Luganda (lug)

- **Word order:** SVO.
- **Morphology:** **Agglutinative** Bantu with a full 18-class noun
  system.
- **Nouns:** Class prefix pairs: **omu-/aba- (1/2), omu-/emi- (3/4),
  eki-/ebi- (7/8), en-/en- (9/10), olu-/en- (11/10)** etc. Initial
  vowel (augment) **o-, e-, a-** is required on most nominals.
- **Pronouns:** 1SG **nze**, 2SG **ggwe**, 3SG **ye**, 1PL **ffe**, 2PL
  **mmwe**, 3PL **bo**. Subject concord prefixes on verbs: **n-, o-,
  a-, tu-, mu-, ba-**.
- **Verbs:** Extended template:
  **SM-NEG-TENSE-OBJ-ROOT-EXTENSIONS-FV**. Extensions include applicative
  **-ir-**, causative **-is-**, passive **-ibw-**, reciprocal **-agan-**.
  Tense infixes: near past **-a-**, far past **-a...ye**, future **-li-**.
- **Phonology:** Three vowel heights, five qualities (a e i o u), each
  short or long. Tonal with three surface tones but not written.
  Prenasalised stops **mb, nd, ng, nj**.
- **Syntax:** Subject / object agreement on verbs, noun-class concord on
  adjectives, demonstratives, possessives. Heavy use of **-e-** and
  **-o-** particles in relatives.
""",
"""# LID Characteristics: Luganda (lug)

- **Script signals:** Double consonants **bb, dd, gg, kk, mm, nn, pp,
  ss, tt, yy, zz** are a near-definitive Luganda signal. Double vowels
  are frequent too.
- **Top function words:** *ne, oba, n'olwekyo, bw'atyo, naye, era, kubanga,
  newaakubadde, awamu, ebbaluwa, ekyo, ekyokulabirako, kino, ekyo, oyo,
  abo, bw'omu, nti, nga, wabula, olwo, olwokubanga, ddala, nnyo, buli,
  awatali, awamu, w'emabega, kyo, lwakyo*.
- **N-gram / spelling patterns:** Doubled consonants (**kkulu, bbiri,
  kk, mm**); augment prefix **o-/e-/a-** before noun-class prefixes
  (**omusajja, embwa, ekitabo**); negation prefix **te-**.
- **Morphology hooks:** Geminate consonants as a word-internal feature;
  class concord agreement on modifiers; verb root with multiple
  extensions (**-laba 'see' → -labikira 'appear for'**).
- **Punctuation / orthography quirks:** Apostrophe appears in proclitic
  contractions (**n'olwekyo** 'therefore', **w'omu** 'where-in').
""",
"""# Differences from confusable languages: Luganda (lug)

Close set: **nyn (Nyankole)** (same Lakes subgroup), **swa / swh, kik,
lin, sna, zul, xho, sot, nso** — the rest of the CommonLID Bantu pool.

**lug vs. nyn (Nyankole)**
- Both Lakes Bantu. Luganda has **geminate consonants written double**
  (**bbiri, kkulu**); Nyankole does not. This is the single strongest
  visual diagnostic.
- Class-prefix inventories overlap but specific lexemes differ:
  lug **omuntu 'person'**, nyn **omuntu** (same); lug **ennyumba 'house'**,
  nyn **enju**.

**lug vs. swa / swh**
- Swahili has no noun-class augment **o-/e-/a-**; Luganda uses it on
  virtually every noun.
- Swahili Arabic loans (**kitabu, sababu**) contrast with Luganda
  Ganda / English-loan inventory.

**lug vs. kik**
- Kikuyu has **ĩ / ũ** tilde vowels; Luganda doesn't.

**lug vs. zul / xho**
- No clicks in Luganda; click letters **c, q, x** in Nguni languages
  signal Nguni, not Ganda.

**lug vs. eng (English)**
- English code-switching is common in Kampala web text; augment prefixes
  **o-/e-/a-** and class concord are the Luganda markers.
""")


# ---- Malagasy (mlg) -------------------------------------------------------
lang("mlg_Latn",
"""# Malagasy (mlg)

## Summary

Malagasy (endonym **Malagasy**) is an Austronesian language
(Austronesian → Malayo-Polynesian → Barito → Malagasy). It is the
national language of **Madagascar** (~25 million speakers, counting all
varieties), and is remarkably **geographically isolated** from the rest
of its family — its closest relatives are Ma'anyan and other Southeast
Barito languages of Borneo. ISO codes: `mg` (639-1), `mlg` (639-2/-3).

## Writing system

Latin script with minimal diacritics: accent marks on vowels (**á, é,
í, ó**) are occasional for stress disambiguation; otherwise plain Latin.
The orthography avoids **c, q, u, w, x** in native words.

## Historical note

Malagasy arrived with Austronesian settlers from Borneo around 350–550
CE, later layered with Bantu and Arabic influence. The Latin
orthography was standardised in the 19th century during the Merina
monarchy.
""",
"""# Grammar: Malagasy (mlg)

- **Word order:** **VOS** (verb-object-subject) by default — highly
  unusual for Austronesian, and a strong typological marker.
- **Morphology:** Moderately agglutinative. Voice / focus alternations
  are the core verb morphology: *actor voice* (prefix **m-**), *patient
  voice* (circumfix **a- … -o / -ina**), *circumstantial voice*
  (**an- … -ana / -ina**).
- **Nouns:** No gender. Plural is optional; marked by **ireo / ny** or
  reduplication. Case-like roles are carried by preceding articles or
  prepositions (**an', amin'ny, ho an'ny**).
- **Pronouns:** Free and enclitic. 1SG **aho / -ko**, 2SG **ianao / -nao
  / -nareo**, 3SG **izy / -ny**, 1PL incl. **isika / -ntsika**, 1PL
  excl. **izahay / -nay**, 2PL **ianareo / -nareo**, 3PL **izy ireo /
  -ny**.
- **Verbs:** Tense: present **m-**, past **n-**, future **h-**.
  (**manoratra** 'writes', **nanoratra** 'wrote', **hanoratra** 'will
  write'.) Voice prefix integrates with tense.
- **Phonology:** Five vowels; penultimate stress; frequent **tr, dr, ts,
  ps** clusters; initial **mp-, nt-, nk-, mb-, nd-, ng-** prenasalisation
  like some Indonesian languages.
- **Syntax:** Clause-final subject (the 'trigger') is syntactically
  prominent. Distinct articles **ny** (definite) and **ilay** (specific).
""",
"""# LID Characteristics: Malagasy (mlg)

- **Script signals:** Plain Latin. Words frequently **end in -a, -y, -o**
  and are often **long** (6–12+ characters). Absence of **c, q, u, w, x**
  in native words.
- **Top function words:** *ny, no, dia, fa, kanefa, ary, na, sy, ho,
  ao, ato, ery, etsy, any, aza, efa, mbola, anie, hoe, tsy, tsia, eny,
  ahoana, inona, iza, manao ahoana, aoka, raha, satria, dia ny,
  izay, izao, hatramin'ny, tamin'ny, ao anatin'ny*.
- **N-gram / spelling patterns:** Common clusters **tr, dr, ts** (**trano
  'house', hiratraka**); prenasalised onsets **mp-, nt-, nk-, mb-, nd-,
  ng-** at word start (**ntsika, mpianatra**); endings **-ana, -ina, -o,
  -eo, -y**.
- **Morphology hooks:** Tense-voice prefix **m- / n- / h-** on verbs
  (**manoratra, nanoratra, hanoratra**). Possessive enclitics **-ko,
  -nao, -ny, -ntsika**. Article **ny** everywhere.
- **Punctuation / orthography quirks:** Apostrophes in contracted forms
  **amin'ny, ao amin'ny, ho an'ny** are load-bearing.
""",
"""# Differences from confusable languages: Malagasy (mlg)

Within CommonLID, Malagasy is typologically isolated — other Austronesian
languages (ind, msa, zsm, jav, fil, tgl, bcl, bik, ace) share the family
but are phonologically very different. Main distinguishing features:

**mlg vs. ind / msa / zsm**
- Function words: mlg **ny, dia, fa, sy, tsy**; ind/msa **yang, di, dan,
  tidak, adalah**.
- Clusters **tr, dr, ts, mp, nt, nk** are Malagasy; Indonesian avoids
  these.
- Word endings: mlg **-ana, -ina, -y**; ind/msa **-kan, -i, -nya, -an**.

**mlg vs. jav (Javanese)**
- Javanese uses **é / è / ê**; Malagasy avoids them.
- Javanese honorific vocabulary (**panjenengan, sampeyan**) absent.

**mlg vs. fil / tgl**
- Tagalog/Filipino uses **ang, ng, sa, na** (Philippine-type voice
  system); Malagasy uses **ny, dia, fa** and has VOS order vs. Tagalog
  VSO.

**mlg vs. any Latin-script African language**
- Malagasy's prenasalised clusters **mp-, nt-, nd-, mb-, ng-** and
  clusters **tr, dr** are essentially unique in this dataset.
""")


# ---- Nyankole (nyn) -------------------------------------------------------
lang("nyn_Latn",
"""# Nyankole (nyn)

## Summary

Nyankole (also *Nkore* or *Runyankore*; endonym **Orunyankole** / **
Runyankore**) is a Bantu language (Niger-Congo → Atlantic-Congo →
Bantu → Great Lakes → Nyoro-Ganda → Runyankore-Rukiga). It is spoken by
roughly **3–4 million people** in **south-western Uganda**, chiefly in
the Ankole region. Closely related to Rukiga (with which it forms the
Runyankore-Rukiga standard pair). ISO code: `nyn` (639-3); no 639-1;
639-2 `nyn`.

## Writing system

Latin script with no special diacritics. Similar to Luganda but:
Nyankole **does not write geminate consonants double**. Tone is phonemic
but unmarked.

## Historical note

Runyankore-Rukiga is taught jointly in Ugandan schools; the common
orthography was standardised in the 20th century by the East African
missionary and educational boards.
""",
"""# Grammar: Nyankole (nyn)

- **Word order:** SVO.
- **Morphology:** Agglutinative Bantu with full noun-class concord.
- **Nouns:** Class-prefix pairs and augment vowel:
  **omu-/aba- (1/2), omu-/emi- (3/4), eki-/ebi- (7/8), en-/en- (9/10),
  oru-/en- (11/10), oku-/ama- (15/6)**.
- **Pronouns:** 1SG **nyowe**, 2SG **iwe**, 3SG **we**, 1PL **itwe**,
  2PL **imwe**, 3PL **bo**. Subject prefixes: **n-, o-, a-, tu-, mu-,
  ba-**.
- **Verbs:** Template:
  **SM-(NEG)-TENSE-ROOT-EXTENSIONS-FV**. Tenses include present **-ri-**,
  past **-a-**, future **-rya-**.
- **Phonology:** Five-vowel system with length distinction; two tones.
  No geminate consonants orthographically.
- **Syntax:** Like other Great Lakes Bantu: concord on all agreeing
  elements, extensive verb-suffix derivation.
""",
"""# LID Characteristics: Nyankole (nyn)

- **Script signals:** Plain Latin, no diacritics. Augment vowel
  **o-/e-/a-** in front of noun-class prefixes (**omuntu, ekitabo, amata**).
- **Top function words:** *aha, oku, omu, na, kandi, obu, nokwo, kwonka,
  nikwo, omanya, orikuba, obu, orikwenda, nigu, nibu, itwe, imwe,
  bo, we, aba, abo, bari, buri, ngu, shi, ku, za, za-, na-, obwo, kumanya*.
- **N-gram / spelling patterns:** Noun-class prefix augment **o-/e-/a-**
  is extremely frequent. Verb prefix **ni-** (present progressive).
  Vowel sequences **aa, ee, ii, oo, uu** mark length.
- **Morphology hooks:** Subject concord prefix chain on verbs
  (**ariija** 'he comes', **turiija** 'we come'); class-agreeing
  modifiers.
- **Punctuation / orthography quirks:** Sparse punctuation; apostrophe
  in contractions rare (unlike Luganda's **n'olwekyo** pattern).
""",
"""# Differences from confusable languages: Nyankole (nyn)

Closest confusability: **lug (Luganda)** (same Lakes Bantu family), then
the broader Bantu set **kik, swa, swh, sna, zul, xho, nso, sot, lin**.

**nyn vs. lug**
- **Luganda writes geminate consonants double** (**bbiri, kkulu, ssente**);
  Nyankole **does not**. Any text with **bb, dd, kk, mm, ss, tt, yy, zz**
  signals Luganda, not Nyankole.
- Apostrophe contractions **n'olwekyo, w'omu** are Luganda-specific.
- Lexical differences: lug **omuntu, ennyumba, ekitabo**; nyn **omuntu,
  enju, ekitabo** (some overlap, but **enju** vs. **ennyumba** is
  diagnostic).

**nyn vs. kik**
- Kikuyu has **ĩ / ũ** tilde vowels; Nyankole doesn't.

**nyn vs. swa / swh**
- Swahili has no augment vowel **o-/e-/a-** before class prefixes;
  Nyankole does.
- Swahili Arabic loans (**kitabu, sababu, rais**) absent from Nyankole.

**nyn vs. lin**
- Lingala has French loanwords and simplified class morphology; Nyankole
  has English loans and full class concord.

The augment-vowel + no-gemination + lack-of-tilde-vowels combination
narrows Nyankole down within the Bantu pool.
""")


# ---- Odia (ory) -----------------------------------------------------------
lang("ory_Orya",
"""# Odia (ory)

## Summary

Odia (formerly spelt *Oriya*; endonym **ଓଡ଼ିଆ** *Oṛiā*) is an Indo-Aryan
language (Indo-European → Indo-Iranian → Indic → Eastern Indic → Odia).
It is the official language of the **Indian state of Odisha** (~40 million
first-language speakers) and a classical language of India (declared 2014).
ISO codes: `or` (639-1), `ory` / `ori` (639-2/-3).

## Writing system

Written in the **Odia script (Orya, U+0B00–0B7F)**, a Brahmic abugida
whose letter forms are typically **rounded / circular** due to having
been traditionally carved on palm leaves. Distinctive features: no
shirorekha top line (like Gujarati, Kannada, Telugu); characteristic
round **ଓ, ୟ, କ, ର, ଲ, ମ** shapes.

## Historical note

Odia has the oldest continuous literary tradition among the eastern
Indic languages (Charyapada, 8th–12th c. CE). It was among the first
to receive classical-language status from the Government of India.
""",
"""# Grammar: Odia (ory)

- **Word order:** **SOV**, with relatively rigid verb-final placement.
- **Morphology:** **Fusional / agglutinative** Indic. No grammatical
  gender (unusual among major Indic languages — Odia has **lost
  gender**). Number: sg / pl.
- **Nouns:** Case marked by postpositions: **-ର (-ra)** genitive,
  **-କୁ (-ku)** dative/accusative, **-ରେ (-re)** locative, **-ରୁ (-ru)**
  ablative, **-ଦ୍ୱାରା (-dwārā)** instrumental.
- **Pronouns:** 1SG **ମୁଁ (muñ)**, 2SG **ତୁ / ତୁମେ (tu / tume)**, honorific
  2SG **ଆପଣ (āpaṇa)**, 3SG **ସେ (se)**, 1PL **ଆମେ (āme)**, 2PL **ତୁମେମାନେ
  (tumemāne)**, 3PL **ସେମାନେ (semāne)**.
- **Verbs:** Copula **ଅଛି (achi) / ଅଛନ୍ତି (achanti)** 'is / are' —
  note: distinct from Hindi **है**, Bengali **আছে (āche)**, Marathi
  **आहे**. Past tense **-ିଲା / -ିଲେ (-ilā / -ile)**; future
  **-ିବ / -ିବେ (-iba / -ibe)**.
- **Phonology:** Retained schwa in word-final syllables (unlike Hindi);
  retroflex series (**ଟ, ଠ, ଡ, ଢ, ଣ, ଳ**); aspirated stops.
- **Syntax:** Postpositional; cleft constructions common.
""",
"""# LID Characteristics: Odia (ory)

- **Script signals:** Odia script (U+0B00–0B7F). Rounded glyphs —
  visually unmistakable vs. Devanagari (shirorekha), Bengali (triangular
  tops), or Gujarati (top-bar-less but different shapes).
- **Top function words:** *ଅଛି (achi 'is'), ଅଛନ୍ତି (achanti 'are'),
  ନାହିଁ (nāhĩ 'is not'), ଏବଂ (ebaṁ 'and'), କିନ୍ତୁ (kintu 'but'),
  ଯେଉଁ (yeun̄ 'which'), ସେଉଁ (seun̄ 'that'), କିଏ (kie 'who'),
  କ'ଣ (ka'ṇa 'what'), ର (ra 'of'), କୁ (ku 'to'), ରେ (re 'in/at'),
  ରୁ (ru 'from'), ବି (bi 'also'), ମଧ୍ୟ (madhya 'also'),
  ସେ (se 'he/she'), ମୁଁ (muñ 'I'), ଆମେ (āme 'we'), ତୁମେ (tume 'you'),
  ଆପଣ (āpaṇa 'you-polite'), ଏଇ / ଏହି (ei / ehi 'this'), ସେଇ (sei 'that')*.
- **N-gram / spelling patterns:** Verb endings **-ୁଛି / -ୁଛନ୍ତି (-uchi
  / -uchanti)** (present progressive), **-ିଲା / -ିଲେ** (past),
  **-ିବ / -ିବେ** (future). Genitive postposition **ର** appears very
  frequently.
- **Morphology hooks:** Copula **ଅଛି** is distinctive. Plural marker
  **-ମାନେ** (human plural) is a strong signal.
- **Punctuation / orthography quirks:** Danda **।** as sentence ender
  is traditional; modern text also uses full-stop **.** .
""",
"""# Differences from confusable languages: Odia (ory)

Within CommonLID the Indic / Brahmic script family contains: Devanagari
(hin, mar, san, gom), Bengali (ben, asm), Gurmukhi (pan), Gujarati
(guj), Tamil (tam), Telugu (tel), Kannada (kan), Malayalam (mal), and
Odia itself.

**ory vs. any other Brahmic**
- Odia uses the **Orya** Unicode block (U+0B00–0B7F); any text in that
  block is Odia. Other Indic languages use different blocks (Deva, Beng,
  Gujr, Guru, Taml, Telu, Knda, Mlym).
- No character overlap at the Unicode level.

**ory vs. ben (Bengali)**
- ben uses a triangular-top script with shirorekha-like feature on some
  letters; ory is rounded. Scripts are entirely distinct.

**ory vs. hin (Hindi, Devanagari)**
- Copula: ory **ଅଛି**; hin **है**. Completely different scripts.

**ory vs. English loans**
- Like other Indian languages, Odia web text may code-mix English; the
  Odia-script segments unambiguously signal Odia.
""")


# ---- Punjabi (pan, Gurmukhi) ---------------------------------------------
lang("pan_Guru",
"""# Punjabi (pan, Gurmukhi)

## Summary

Punjabi (endonym **ਪੰਜਾਬੀ** *Paṅjābī*) is an Indo-Aryan language
(Indo-European → Indo-Iranian → Indic → Northwestern Indic). It is
spoken by roughly **120 million people**, making it one of the most
widely spoken Indic languages. Eastern Punjabi (this folder, written in
**Gurmukhi**) is the official language of the **Indian state of Punjab**;
Western Punjabi is largely written in **Shahmukhi** (Perso-Arabic
script) in Pakistan. ISO codes: `pa` (639-1), `pan` (639-2/-3).

## Writing system

Written in the **Gurmukhi script (Guru, U+0A00–0A7F)**, a Brahmic
abugida developed by the second Sikh Guru, Guru Angad, in the 16th
century. The script has a distinctive **top bar (though less continuous
than Devanagari)** and characteristic shapes. Punjabi is a **tonal**
language — three tones distinguished phonetically but not written.

## Historical note

Gurmukhi is closely associated with the **Guru Granth Sahib**, the central
religious text of Sikhism. Literary Punjabi flourished with Sufi and Sikh
poetry from the 15th century onward.
""",
"""# Grammar: Punjabi (pan)

- **Word order:** **SOV**, verb-final.
- **Morphology:** **Fusional / agglutinative** Indic. Two genders
  (masculine, feminine), two numbers (sg, pl), case marked mostly by
  postpositions.
- **Nouns:** Direct / oblique stem pairs; masculines often end in **-ਾ
  (-ā)** (direct) / **-ੇ (-e)** (oblique sg). Postpositions include **ਦਾ
  / ਦੀ / ਦੇ (dā / dī / de)** genitive (gender-agreeing), **ਨੂੰ (nū̃)**
  dative, **ਵਿਚ (vic)** locative, **ਤੋਂ (tō̃)** ablative.
- **Pronouns:** 1SG **ਮੈਂ (maĩ)**, 2SG **ਤੂੰ (tū̃)**, polite 2SG **ਤੁਸੀਂ
  (tusī̃)**, 3SG **ਉਹ / ਇਹ (uh / ih)**, 1PL **ਅਸੀਂ (asī̃)**, 2PL **ਤੁਸੀਂ
  (tusī̃)**, 3PL **ਉਹ (uh)**.
- **Verbs:** Copula **ਹੈ / ਹਨ (hai / han)** 'is / are' — similar to Hindi
  **है / हैं** but distinct in script. Past **-ਿਆ / -ੀ / -ੇ (-iā / -ī /
  -e)** with gender agreement. Ergative **ਨੇ (ne)** marks transitive
  past subjects.
- **Phonology:** Three-tone system (rising, level, falling) conditioned
  historically by the voiced aspirated series; retroflex consonants
  **ਟ ਠ ਡ ਢ ਣ ੜ**; tonal letters **ਘ ਝ ਢ ਧ ਭ** (voiced aspirates in writing).
- **Syntax:** Postpositional; gender agreement cascades through the
  clause.
""",
"""# LID Characteristics: Punjabi (pan)

- **Script signals:** Gurmukhi (U+0A00–0A7F). Characteristic letters
  **ਓ, ਅ, ਕ, ਖ, ਗ, ਘ, ਚ, ਜ, ਝ, ਞ, ਟ, ਠ, ਡ, ਢ, ਣ, ਤ, ਥ, ਦ, ਧ, ਨ, ਪ, ਫ,
  ਬ, ਭ, ਮ, ਯ, ਰ, ਲ, ਵ, ਸ, ਹ, ੜ** and distinctive additions **ਸ਼, ਖ਼, ਗ਼,
  ਜ਼, ਫ਼** for Perso-Arabic loanwords.
- **Top function words:** *ਹੈ (hai 'is'), ਹਨ (han 'are'), ਸੀ (sī
  'was'), ਨਹੀਂ (nahī̃ 'not'), ਅਤੇ (ate 'and'), ਪਰ (par 'but'), ਜਾਂ
  (jā̃ 'or'), ਦਾ / ਦੀ / ਦੇ (dā / dī / de 'of'), ਨੂੰ (nū̃ 'to/DAT'),
  ਵਿਚ (vic 'in'), ਤੋਂ (tō̃ 'from'), ਨੇ (ne 'ERG'), ਉਹ (uh 'he/she/that'),
  ਇਹ (ih 'this'), ਮੈਂ (maĩ 'I'), ਤੂੰ (tū̃ 'you'), ਤੁਸੀਂ (tusī̃ 'you-pl'),
  ਅਸੀਂ (asī̃ 'we'), ਕੀ (kī 'what'), ਕਦੋਂ (kadō̃ 'when'), ਕਿਉਂ (kiū̃ 'why')*.
- **N-gram / spelling patterns:** Verb endings **-ਦਾ / -ਦੀ / -ਦੇ (-dā /
  -dī / -de)** for present imperfective; **-ਿਆ / -ੀ / -ੇ** past.
  Frequent use of **ੇ** (e-maatra) and **ਾ** (a-maatra) as vowel signs.
- **Morphology hooks:** Ergative **ਨੇ** on past-tense transitive subjects.
  Gender-agreeing postposition **ਦਾ / ਦੀ / ਦੇ**.
- **Punctuation / orthography quirks:** Traditional danda **।**; also
  full stop **.**, comma **,**.
""",
"""# Differences from confusable languages: Punjabi (pan)

**pan vs. hin (Hindi)**
- Completely different scripts (Gurmukhi vs. Devanagari) — script is
  definitive.
- Copula: pan **ਹੈ / ਹਨ / ਸੀ** vs. hin **है / हैं / था**.

**pan vs. urd (Urdu)**
- urd uses **Perso-Arabic script** (Nastaliq style). Eastern Punjabi is
  in Gurmukhi. The two scripts never overlap.
- (Western Punjabi in Shahmukhi is NOT represented in CommonLID.)

**pan vs. other Brahmic (guj, ben, asm, ory, tam, tel, kan, mal)**
- Script is the conclusive signal — Gurmukhi occupies its own Unicode
  block (U+0A00–0A7F).

**pan vs. English code-mix**
- English loans are common in web text; Gurmukhi-script segments tag
  the content as Punjabi irrespective of English interleaving.
""")


# ---- Nigerian Pidgin (pcm) ------------------------------------------------
lang("pcm_Latn",
"""# Nigerian Pidgin (pcm)

## Summary

Nigerian Pidgin (endonym **Naijá**, sometimes **Broken** or simply
**Pidgin**) is an English-based creole/pidgin spoken as a lingua franca
across **Nigeria** (>75 million users including L2) and in Nigerian
diaspora communities. Increasingly used in written contexts including
news (BBC Pidgin), music lyrics, and social media. ISO code: `pcm`
(639-3); no 639-1/2.

## Writing system

Latin script. Orthography is not fully standardised; English-etymological
spellings are common alongside phonemic spellings. Some writers use
**é / ɛ / ɔ** for open mid vowels, but web text overwhelmingly uses
plain Latin letters.

## Historical note

Arose from 17th–18th-century trade pidgins between English traders and
West African coast communities; stabilised in the 19th century. In
2022 the Lagos Legislature held a debate in Pidgin, a milestone in its
official use.
""",
"""# Grammar: Nigerian Pidgin (pcm)

- **Word order:** SVO.
- **Morphology:** **Analytic**; no verb inflection, no case, no gender.
- **Nouns:** Number optional; plural marked by **dem** postposed
  (**pikin dem** 'children') or by the quantifier itself.
- **Pronouns:** 1SG **I / mi / me**, 2SG **yu / you**, 3SG **e / im /
  am**, 1PL **wi / we**, 2PL **una**, 3PL **dem / de**. The
  second-person plural **una** is a distinctive non-English pronoun.
- **Verbs:** Preverbal tense/aspect markers:
  - bare verb — generic / present;
  - **dey** — progressive / habitual;
  - **don** — perfective ('have done');
  - **go** — future.
  Negation: **no** before the verb (**I no sabi** 'I don't know').
- **Phonology:** Seven vowels (a, e, ɛ, i, o, ɔ, u); simplified consonant
  clusters; no tone marking in writing.
- **Syntax:** Serial verb constructions (**take go, come pass**); cleft
  with **na** ('it is') — **na mi dey go**.
""",
"""# LID Characteristics: Nigerian Pidgin (pcm)

- **Script signals:** Plain Latin, minimal diacritics; English-like on
  the surface.
- **Top function words:** *na, dey, don, go, no, wey, say, make, if, but,
  for, with, sabi, come, dem, una, e, im, am, oga, waka, abeg, oyibo,
  wahala, abi, o, ja, shey, chop, wetin, ah ah, nothing, kai, kuku,
  enter, one kain*.
- **N-gram / spelling patterns:** Short English-like words peppered with
  **dey / don / go / wey / say** as function words. Frequent serial
  verbs (**take go**, **come see**).
- **Morphology hooks:** No verb inflection — scan for **dey / don / go**
  before bare verbs. Cleft **na X …** is a near-certain signal.
- **Punctuation / orthography quirks:** Web text often lacks diacritics;
  interjections (**ah ah, chai, kai, abi**) are a stylistic marker.
""",
"""# Differences from confusable languages: Nigerian Pidgin (pcm)

Primary confusability: **English (eng)** because the lexicon overlaps
heavily. The grammar is the distinguisher.

**pcm vs. eng**
- Function words: pcm **dey, don, go, wey, say, na, una, dem, sabi, abeg,
  wahala, oga** — none are standard English.
- Grammar: no verb inflection (**he don go**, not **he has gone**);
  pluralisation with postposed **dem** (**pikin dem**); cleft **na**
  (**na me dey talk**).
- Pronouns: **una** (2PL) is a near-certain pcm signal.
- Spelling: **wetin** (what), **abeg** (please), **sabi** (know),
  **pikin** (child) — content words unique to pcm.

**pcm vs. other Niger-Congo (hau, yor, ibo)**
- Those languages do not use Latin-script English lexicon; they have
  tone diacritics (yor, ibo) or hooked letters (hau **ɓ ɗ ƙ**).
- pcm is Latin-lexified from English, not native West African.

**pcm vs. other creoles (gcf, acf, rcf, gcr)**
- Those are French-based; pcm is English-based. Pronouns and TMA
  particles (**dey / don / go** vs. **ka / té / ké**) disambiguate.

The combination **dey / don / go** + **na** cleft + **una / dem** is
essentially definitive for pcm.
""")


# ---- Réunion Creole (rcf) -------------------------------------------------
lang("rcf_Latn",
"""# Réunion Creole (rcf)

## Summary

Réunion Creole (endonym **Kréol Rénioné**) is a French-based creole
spoken on **Réunion Island** (French overseas département, Indian Ocean),
by about **550,000 speakers**. Linguistically in the Bourbonnais Creole
group with Mauritian, Rodriguan, and Seychellois (none of which appear
in CommonLID). ISO code: `rcf` (639-3); no 639-1/2.

## Writing system

Latin script. Orthographies: *Tangol* (phonemic) and *Lékritir 77 /
KWZ* variants are used; web text mixes them and French-etymological
spellings. Characteristic letters: **ò, è, ñ**; digraphs **anm, onm**
for nasal + m consonants.

## Historical note

Emerged from 17th–18th-century French settler speech in contact with
Malagasy, South Indian languages, and East African substrates. Réunion
Creole is distinct from Antillean creoles (gcf, acf, gcr) in phonology
and some lexicon.
""",
"""# Grammar: Réunion Creole (rcf)

- **Word order:** SVO.
- **Morphology:** **Analytic**; no inflection, no gender, no case.
- **Nouns:** Definite article **lo / la / lé** (sometimes preposed,
  sometimes postposed as **-la**); plural **bann** before noun or **-la**
  suffix.
- **Pronouns:** **mwin / mi** (I), **ou / toué / zot** (you), **li / el**
  (he / she), **nou** (we), **zot** (you pl), **zot / bannla** (they). The
  1SG **mi** is a distinctive rcf signal.
- **Verbs:** TMA particles, somewhat different from Antillean creoles:
  - **i** / **lé** — stative / present;
  - **la** — anterior / past;
  - **va / sra** — future;
  - **té** — imperfect / past progressive.
- **Phonology:** Lowered mid vowels **ò, è**; nasal + m sequences written
  **anm, onm**; r-retention (unlike Antillean r-drop).
- **Syntax:** Copula **lé** (stative) / **sé** (equational). Negation
  preverbal **pa**. Heavy use of **i** before verbs.
""",
"""# LID Characteristics: Réunion Creole (rcf)

- **Script signals:** Latin with **ò, è**; nasal digraphs **anm, onm**
  (unique to rcf among creoles in CommonLID). Pronouns **mi, mwin,
  bannla** are visual markers.
- **Top function words:** *lé, i, la, va, sra, té, pa, mi, mwin, ou,
  zot, li, el, nou, bannla, sé, an, in, ein, lo, la, le, bann, mé,
  ek, avek, dann, sou, si, tou, tout, ke, mé, son, pou, sa, sak, ousa,
  kan, kom, kouk*.
- **N-gram / spelling patterns:** Preverbal **i** (**i koz, i viv**) is
  frequent; nasal endings **anm, onm** (**manm** 'mama', **bonm** 'bomb').
  Pronoun **mi** for 1SG is a near-unique rcf marker.
- **Morphology hooks:** TMA triple **la / va / té**; article **bann**;
  preverbal **i**.
- **Punctuation / orthography quirks:** Mixed orthographies (Tangol vs.
  Lékritir) produce internal spelling variation; French-etymological
  spellings may creep in.
""",
"""# Differences from confusable languages: Réunion Creole (rcf)

Close set: **gcf, acf, gcr** (Antillean / French Caribbean creoles),
and lexifier **fra**.

**rcf vs. gcf / acf / gcr (Antillean creoles)**
- 1SG pronoun: rcf **mi / mwin** vs. Antillean **mwen**; rcf **mi** is
  essentially unique in CommonLID.
- Copula: rcf **lé** (stative) vs. Antillean **sé** only; rcf has both.
- Nasal digraphs **anm, onm** are rcf-specific among these.
- Preverbal TMA: rcf **la / va / té / i**; Antillean **ka / té / ké /
  kay**. Presence of **ka** strongly suggests Antillean, not rcf.

**rcf vs. fra**
- No French verb inflection, analytic grammar, postposed **-la**,
  pronoun **mi**, copula **lé**.

**rcf vs. Seychellois Creole / Mauritian Creole** (not in CommonLID):
broadly Bourbonnais-family with shared features; in this dataset there
is no direct confusion.
""")


# ---- Sanskrit (san, Devanagari) ------------------------------------------
lang("san_Deva",
"""# Sanskrit (san)

## Summary

Sanskrit (endonym **संस्कृतम्** *Saṃskṛtam*) is a **classical Indo-Aryan
language** (Indo-European → Indo-Iranian → Indic → Sanskrit). It is the
language of Vedic and Classical Indian literature — the Vedas, the
Upaniṣads, the Mahābhārata, the Rāmāyaṇa, the Purāṇas, and the vast
corpus of Classical Sanskrit kāvya, śāstra, and āgama texts. ISO codes:
`sa` (639-1), `san` / `skt` (639-2/-3). Scheduled classical language
of India.

## Writing system

In CommonLID this folder uses **Devanagari** (the most common script for
Sanskrit today). Historically Sanskrit has been written in almost every
Brahmic script (Śāradā, Grantha, Brahmi, Kannada, Bengali, Malayalam,
Telugu, Tamil-Grantha, etc.). Devanagari for Sanskrit retains features
like **ं, ः, ऽ** (anusvāra, visarga, avagraha) used systematically; and
very dense conjunct consonants (**क्ष, ज्ञ, श्र, त्र, द्व, स्त्र**).

## Historical note

Classical Sanskrit was codified by **Pāṇini** in the Aṣṭādhyāyī (c. 4th
c. BCE). It has remained a scholarly and liturgical language through
contemporary times; modern Sanskrit publication continues in India.
""",
"""# Grammar: Sanskrit (san)

- **Word order:** Free in poetry, tending to SOV in prose. Case does
  most of the syntactic work.
- **Morphology:** **Highly fusional**. Eight cases (nominative, accusative,
  instrumental, dative, ablative, genitive, locative, vocative), three
  numbers (singular, **dual**, plural), three genders (masculine,
  feminine, neuter).
- **Nouns:** Dense inflection; e.g. a masculine *a*-stem like **देव
  (deva)** 'god' has 24 forms across 8 cases × 3 numbers.
- **Pronouns:** **अहम् (aham)** 'I', **त्वम् (tvam)** 'you', **सः (saḥ)**
  'he', **सा (sā)** 'she', **तत् (tat)** 'that/it'; dual and plural fully
  inflected.
- **Verbs:** Conjugation classes (10), voices (active / middle /
  passive), moods (indicative / imperative / optative / subjunctive /
  injunctive), tenses (present / imperfect / perfect / aorist / future /
  conditional). Reduplicated perfect, -reduplicated present (class 3),
  aorist with various formations.
- **Phonology:** Three retroflex consonants, the anusvāra **ं /ṃ/**, the
  visarga **ः /ḥ/**, the aspirated series **ख घ छ झ ठ ढ थ ध फ भ**, and
  the avagraha **ऽ** for elision. **sandhi** (euphonic) rules transform
  word boundaries.
- **Syntax:** Case-driven; verbs optionally omitted in nominal clauses.
  Compounds (samāsa) can be enormous.
""",
"""# LID Characteristics: Sanskrit (san)

- **Script signals:** Devanagari as for hin/mar/gom, but Sanskrit shows
  an extremely **dense conjunct-consonant load** (**क्ष, ज्ञ, श्र, स्त्र,
  द्व, त्त्व, न्त्र, र्त्स्न**) and frequent **ं**, **ः**, **ऽ**.
- **Top function words:** *च (ca 'and'), वा (vā 'or'), न (na 'not'),
  एव (eva 'only'), हि (hi 'for/indeed'), तु (tu 'but'), किं (kiṃ
  'what'), यः / या / यत् (yaḥ / yā / yat 'who/which'), सः / सा / तत्
  (saḥ / sā / tat 'he/she/that'), अयम् / इयम् / इदम् (ayam / iyam /
  idam 'this'), अस्ति (asti 'is'), सन्ति (santi 'are'), भवति (bhavati
  'becomes'), अहम् (aham 'I'), त्वम् (tvam 'you'), वयम् (vayam 'we')*.
- **N-gram / spelling patterns:** Ending **-म् (-m, visarga-like final
  halant)** is frequent (**देवम्, रामम्, गृहम्**) — neuter/masculine
  accusative. Ending **-ः (-ḥ, visarga)** on nominative masculine
  singulars (**देवः, रामः**). These are Sanskrit-specific among
  Devanagari languages.
- **Morphology hooks:** **-ति (-ti)** 3SG present ending (**भवति,
  पश्यति**); **-न्ति (-nti)** 3PL (**पश्यन्ति**); aorist augment **अ-
  (a-)**; reduplication (**ददाति, चकार**).
- **Punctuation / orthography quirks:** Danda **।** and double-danda **॥**
  at metrical / verse boundaries. Avagraha **ऽ** marks elision of
  initial **अ** after **-ए / -ओ**.
""",
"""# Differences from confusable languages: Sanskrit (san)

Same script (Devanagari) as **hin**, **mar**, **gom** — and ancestrally
related.

**san vs. hin / mar / gom**
- **Visarga ः** and final **-म्** halanta are Sanskrit-specific. Modern
  Indic languages have largely lost these.
- **Dual number** (दुए, द्वे) exists in san; modern Indic has only
  sg/pl.
- Verb endings: san **-ति / -सि / -मि / -न्ति / -थ / -म**; hin uses
  auxiliary **है / हूँ** chains and participial constructions.
- Sanskrit classical vocabulary (**देव, ब्रह्मन्, धर्म, आत्मन्**)
  contrasts with modern Hindi/Marathi colloquial words.
- No Persian / English loanwords; heavy presence of Sanskrit names,
  deities, philosophical terms.

**san vs. grc (Ancient Greek)**
- Completely different scripts, but both are Classical IE languages with
  inherited morphology. Devanagari letters are unambiguous script
  signals.

**san vs. lat (Latin)**
- Different scripts; functional roles (case system) similar but
  orthographically disjoint.
""")


# ---- Tagalog (tgl) --------------------------------------------------------
lang("tgl_Latn",
"""# Tagalog (tgl)

## Summary

Tagalog (endonym **Tagalog** or **Wikang Tagalog**) is an Austronesian
language (Austronesian → Malayo-Polynesian → Philippine → Central Philippine
→ Tagalog). It is the basis of **Filipino**, the national language of the
**Philippines**, with ~28 million L1 speakers and most of the country as
L2. ISO codes: `tl` (639-1), `tgl` (639-2/-3). Filipino (`fil`) is the
standardised national variety and in CommonLID is labelled separately.

## Writing system

Modern Latin alphabet (Spanish-era spelling updated in 1987 to include
**c, f, j, ñ, q, v, x, z** for loanwords). Characteristic Philippine
orthography. Historical scripts: **Baybayin** (pre-colonial abugida),
no longer standard but seen in symbolic/decorative contexts.

## Historical note

Tagalog served as the basis for Filipino during the 20th-century
standardisation effort. Distinctions between Tagalog and Filipino in
written form are minimal; Filipino is more permissive of loan phoneme
graphemes.
""",
"""# Grammar: Tagalog (tgl)

- **Word order:** **Verb-initial** (predicate-initial) — VSO / VOS.
  Topic/focus particles reorder constituents.
- **Morphology:** **Agglutinative** with a rich **focus / voice** system
  on verbs. Key affixes: **mag-, um-, i-, -in, -an, ipag-, ipa-** marking
  whether the subject is agent, patient, location, benefactive, etc.
- **Nouns:** Case is expressed by **case markers** (Philippine-type):
  **ang** (nominative/topic, definite), **ng** (genitive/oblique, actor
  of patient-voice), **sa** (dative/locative). Plural is optional, marked
  by **mga** [maŋa].
- **Pronouns:** Three sets (NOM, GEN, DAT). 1SG: **ako / ko / akin**;
  2SG: **ikaw, ka / mo / iyo**; 3SG: **siya / niya / kanya**; 1PL incl.
  **tayo / natin / atin**; 1PL excl. **kami / namin / amin**; 2PL **kayo
  / ninyo / inyo**; 3PL **sila / nila / kanila**.
- **Verbs:** Aspect-prominent: completed (**nag-, um-, naka-**),
  incompleted (**nag- + reduplication**), contemplated (**mag-, i-,
  …-in**). Focus affix determines which argument is topic.
- **Phonology:** Five vowels; glottal stop is phonemic but often
  unwritten; penultimate stress typical.
- **Syntax:** Predicate-initial; topic marked by **ay** in subject-first
  clauses. **nga, naman, daw, din/rin, man** are discourse particles.
""",
"""# LID Characteristics: Tagalog (tgl)

- **Script signals:** Latin. No special diacritics in standard web text;
  occasional stress-marking acutes in dictionaries (**báhay, úpo**).
- **Top function words:** *ang, ng, sa, na, at, ay, pero, o, kung, kasi,
  para, kapag, habang, dahil, pati, lang, nga, naman, daw, din, rin,
  man, ito, iyan, iyon, sila, tayo, kami, kayo, ako, ikaw, siya, mga,
  hindi, oo, opo, sana, kaya, ngunit, subalit, subalit, pwede, dapat*.
- **N-gram / spelling patterns:** Frequent **mga** (plural marker),
  **ng** (genitive particle), **ay** (topic linker), **ng** as a
  digraph for /ŋ/ inside words (**bangka, mangga**). Reduplication
  syllables (**nag-aaral, nagsasabi**). Verb affixes **mag-, um-, i-,
  -in, -an**.
- **Morphology hooks:** Three-way case marker **ang / ng / sa** is a
  near-definitive Philippine-type signal; focus infix **-in-** in verbs
  (**binili, dinala, ininom**).
- **Punctuation / orthography quirks:** **ñ** in Spanish loans (**Señor,
  niño**); letters **c, f, j, q, v, x, z** appear only in loans.
""",
"""# Differences from confusable languages: Tagalog (tgl)

Closest confusability: **Filipino (fil)** (standardised Tagalog),
**Central Bikol / Bikol macro (bcl, bik)**, and other Philippine
languages (Cebuano, Ilocano — not in CommonLID).

**tgl vs. fil**
- Formally the same — the national standard is Tagalog. Filipino is more
  permissive of **f, j, v, z, c** in loanwords (e.g. **fotokopya** vs.
  **photokopya**). In practice, short web snippets are indistinguishable;
  content-based heuristics (official/government text tends to be fil)
  help weakly.

**tgl vs. bcl / bik (Bikol)**
- Shared function words **an/ang, sa, na, mga, ng** make these visually
  similar. Content-word diagnostics:
  - 'one' — tgl **isa**, bcl **saro**.
  - 'yes / no' — tgl **oo / hindi**, bcl **iyo / dai**.
  - 'good' — tgl **mabuti / maganda**, bcl **marhay / magayon**.
  - **dai** as negation is bcl; tgl uses **hindi**.

**tgl vs. ind / msa / zsm**
- Tagalog case-marker triad **ang / ng / sa** is Philippine-type and
  absent from Indonesian/Malay (which use **yang, di, ke, untuk**).
- Reduplication in tgl (**nagbabasa**) is Philippine-aspect, not Malay.

**tgl vs. spa (Spanish)**
- Heavy Spanish loan vocabulary (Kumusta, Señor, eskuwela) can superficially
  lookalike, but Philippine-type case markers (**ang/ng/sa**) and affixes
  (**mag-, um-, -in**) disambiguate.
""")


# ---- Venetian (vec) -------------------------------------------------------
lang("vec_Latn",
"""# Venetian (vec)

## Summary

Venetian (endonym **Vèneto** or **Łengua Vèneta**) is a Gallo-Italic /
Italo-Romance language (Indo-European → Italic → Romance → Italo-Dalmatian
/ Gallo-Italic — classification debated). It is spoken by roughly
**3.9 million** people in **Veneto region of northeast Italy**, plus
parts of Trentino, Friuli, Istria (Croatia/Slovenia), and in South-American
communities (especially Brazil — *Talian*). ISO codes: `vec` (639-3); no
639-1; 639-2 `roa` catch-all.

## Writing system

Latin script with characteristic letters **ł** (barred l, a distinctive
Venetian grapheme), **s'c** (written apostrophe inside for a phoneme
cluster distinction), apostrophes in clitic contractions, and **ç**
sporadically. Many spelling conventions coexist (Grafia Veneta
Unificata, Grafia Veneta Moderna, local spellings).

## Historical note

Venetian was the prestige language of the Venetian Republic (697–1797)
and had a pan-Mediterranean trade reach. Modern written Venetian
flourishes on social media, signage, and regional literature; it retains
robust spoken vitality, especially outside Venice proper.
""",
"""# Grammar: Venetian (vec)

- **Word order:** SVO.
- **Morphology:** **Fusional** Romance with some reductions; final
  vowels often drop.
- **Nouns:** Two genders, two numbers. Plural in **-i / -e** (**omo /
  omini**, **fémena / fémene**), unlike standard Italian's **-i / -e**
  fully fused into article morphology.
- **Articles:** **el, ła, i, łe / le**; contracted **de'l, de ła, a'l**;
  indefinite **un, una**.
- **Pronouns:** Subject-clitic system — mandatory clitic subjects
  before verbs (**ti te par** 'you speak', **el parla** 'he speaks', **i
  parla** 'they speak'). Strong pronouns **mi, ti, elo / eła, noàltri,
  voàltri, łori / łore**.
- **Verbs:** Three conjugations (**-ar, -er, -ir**). Clitic-doubling of
  subjects is standard. Compound past with auxiliary **verar / aver** +
  past participle.
- **Phonology:** **ł** (velar l) is the characteristic consonant; final
  vowels of native lexicon often drop (apocope); voicing of intervocalic
  consonants common.
- **Syntax:** Obligatory clitic subjects; negation **no** preverbal.
""",
"""# LID Characteristics: Venetian (vec)

- **Script signals:** **ł** (barred l) is a near-unique Venetian
  grapheme. Also **s'c** (apostrophe inside a consonant cluster), **ç**,
  clitic-contraction apostrophes (**l'ò, g'à**), and final apocope
  (**compagn'**).
- **Top function words:** *el, ła, i, łe, le, un, una, e, de, a, co,
  par, sensa, ma, anca, anche, cofà, come, quando, se, sóto, sora, zó,
  su, fora, no, gnente, gnanca, tuti, tute, łóri, łóre, che, cussì,
  béo, bèło, qual, ki, ke*.
- **N-gram / spelling patterns:** Frequent **ł** mid-word (**ałtro, połpo,
  bało**); final apostrophes on truncated forms; subject-clitic patterns
  **ti te, el, i**; auxiliary contractions **l'ò, g'à, g'ò**.
- **Morphology hooks:** Obligatory subject clitics before verbs (Italian
  lacks these); ending **-òn / -èn / -ìn** in 1/2 PL verbs.
- **Punctuation / orthography quirks:** **ł** is a real letter, not a
  typographic trick. Apostrophe inside **s'c** is load-bearing (distinguishes
  /s/+/tʃ/ from **sc** /ʃ/).
""",
"""# Differences from confusable languages: Venetian (vec)

Close set: **Italian (ita)**, **Ligurian (lij)**, **Occitan (oci)**.

**vec vs. ita**
- **ł, s'c, ç** are Venetian, not Italian.
- Subject clitics (**ti te, el, i**) mandatory in vec, absent in ita.
- Articles: vec **el, ła, i, łe**; ita **il, la, i, le, gli**.
- Final apocope in vec (truncated stems); ita keeps final vowels.

**vec vs. lij (Ligurian)**
- Ligurian uses **ç, ö, x**; Venetian uses **ł, s'c**.
- Ligurian articles **o, a, i, e**; Venetian **el, ła, i, łe**.
- Both have subject clitics but the phonology differs (lij **ti ê, o l'à**;
  vec **ti te, el ga**).

**vec vs. oci**
- Occitan uses **ò, ç, lh, nh**; Venetian uses **ł, s'c**.
- Function words: oci **lo, la, los, las, e, o, mas**; vec **el, ła, i,
  łe, e, o, ma**.

**vec vs. Standard Italian in web text** is by far the most common
confusion; look for **ł**, clitic-subject patterns, and apocopated
infinitives (**magnar, saver, far**) as the Venetian-specific signals.
""")


# ---- Write everything ------------------------------------------------------

def main() -> int:
    written = 0
    for folder, files in CONTENT.items():
        d = LANG_DIR / folder
        d.mkdir(parents=True, exist_ok=True)
        for name, body in files.items():
            path = d / name
            path.write_text(body, encoding="utf-8")
            written += 1
    print(f"[info] wrote {written} files across {len(CONTENT)} languages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
