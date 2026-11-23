# Norwegian Bokmål (nob_Latn) - Language Overview

## Basic Information

- **Language Name:** Norwegian Bokmål (norsk bokmål)
- **ISO 639-3 Code:** nob (the macrolanguage "Norwegian" is `nor`; the other written standard, Nynorsk, is `nno`)
- **ISO 639-1 Code:** nb
- **Script:** Latin (Latn), with the extra letters æ, ø, å
- **Language Family:** Indo-European > Germanic > North Germanic
- **Typology:** Mostly analytic with some fusional morphology; V2 word order in main clauses
- **Users:** Norway has about 5.5 million inhabitants; Bokmål is the written standard chosen by the large majority of them (commonly quoted as roughly 85-90%; see also `nno_Latn/overview.md`)

## What Bokmål Is

Bokmål ("book language") is a *written standard*, not a spoken dialect. Norwegians speak regional dialects and write either Bokmål or Nynorsk. Bokmål descends directly from the Danish written language that was used in Norway during the union with Denmark (1380-1814). After independence from Denmark the written language was gradually "Norwegianized": spelling was adapted to Norwegian pronunciation (hard p/t/k instead of Danish b/d/g after vowels, -sjon instead of -tion, double final consonants, diphthongs ei/øy/au), and Norwegian vocabulary and grammar were admitted.

## Brief History

- **Before 1907:** Dano-Norwegian, essentially Danish orthography with Norwegian vocabulary.
- **1907 and 1917 reforms:** Hard consonants and Norwegian forms introduced; the standard became known as *Riksmål*.
- **1929:** Riksmål officially renamed *Bokmål*; Landsmål became *Nynorsk*.
- **1938 and 1959 reforms:** Part of the "samnorsk" policy of moving the two standards toward each other, introducing many radical (dialect-based) forms.
- **1981 and 2005 reforms:** Samnorsk was abandoned; many conservative forms were readmitted. The 2005 norm is the basis of current Bokmål. The private *Riksmål* standard (Det Norske Akademi) still exists and is more Danish-like.

Because the norm has historically permitted many optional forms, Bokmål text varies more than Danish text: e.g. feminine forms *boka/jenta* alongside *boken/jenten*, *fram/frem*, *sju/syv*, past tense *kasta/kastet*.

## Geographic Distribution and Status

Bokmål dominates in eastern and northern Norway and in the cities (Oslo, Trondheim, Stavanger, mostly also Bergen). It has equal legal status with Nynorsk under the Language Act. It is the language of most Norwegian newspapers, books, websites and administration. Norwegian is not an official EU language (Norway is not an EU member).

## Relationship to Neighboring Languages

- **Danish (dan):** The closest written relative; very many sentences differ only in a few spellings. This is the hardest pair for language identification and the focus of CHALIS (see `nob_Latn/chalis.md`, `chalis/discriminators.md`).
- **Nynorsk (nno):** The other Norwegian standard; differs in many high-frequency words (*ikkje, eg, ein, kva, ho*).
- **Swedish (swe):** Mutually intelligible in speech to a large degree, but Swedish spelling (ä, ö, *och, inte, jag*) separates it easily in writing.

## Resource Level

Bokmål is a well-resourced language: large web corpora, the Norwegian Dependency Treebank / UD_Norwegian-Bokmaal (source of `examples/ud_*.txt`), NB-BERT and other models from the National Library. In many multilingual datasets Norwegian is labeled only as `no`/`nor`, so Bokmål and Nynorsk can be mixed in training data.
