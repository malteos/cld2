# Macedonian Grammar (mkd_Cyrl)

Overview of the grammatical features most relevant to recognising Macedonian text and separating it from Bulgarian, Serbian and Russian.

## Typological Profile

- **Word order:** basically SVO, but flexible for topic/focus; clitics follow strict ordering rules.
- **Morphological type:** largely **analytic** in the nominal system (no noun cases), but rich verbal morphology (tense, aspect, evidentiality).
- **Balkan features:** postposed definite article, no infinitive, clitic doubling, *има*-perfect, evidential (renarrative) forms.
- **Stress:** fixed on the **antepenultimate** syllable in words of three or more syllables (e.g. *РА-бо-та* "work", *ра-БО-ти-ме* "we work"; two-syllable words take initial stress: *ВО-да*); not marked in writing. This differs from free stress in Bulgarian and Russian.

## Nouns

Three genders (masculine, feminine, neuter) and two numbers; there is also a special **count form** for masculine nouns after numerals (*два града*, *три молива*, vs. plural *градови*, *моливи*).

There are **no case endings** on nouns; grammatical relations are expressed by prepositions and word order. The preposition **на** marks possession and indirect objects (*книгата на Петар* "Peter's book"; *му реков на Петар* "I told Peter"). A vestigial vocative exists (*Петре!*, *мајко!*).

Typical plural endings: masculine **-и / -ови / -еви** (*градови*, *мажи*), feminine **-и** (*жени*), neuter **-а / -иња** (*села*, *момчиња*; irregular *деца* "children").

## Definite Article: Triple System

Macedonian is unusual in having **three sets** of postposed articles, encoding distance:

| | unmarked / neutral | proximal ("this here") | distal ("that there") |
|---|---|---|---|
| masc. sg. | **-от** (*градот*) | **-ов** (*градов*) | **-он** (*градон*) |
| fem. sg. | **-та** (*жената*) | **-ва** (*женава*) | **-на** (*женана*) |
| neut. sg. | **-то** (*селото*) | **-во** (*селово*) | **-но** (*селоно*) |
| plural | **-те** (*градовите*) | **-ве** | **-не** |

The unmarked set is by far the most frequent in written text; *-ов/-он* forms are common in expressions like *денов* "today, this day" and in colloquial speech. The masculine **-от** (vs. Bulgarian **-ът/-а**) is one of the strongest grammatical discriminators. The article attaches to the first word of the noun phrase: *новиот автомобил* "the new car", *мојот татко* "my father".

## Pronouns

Personal: *јас, ти, тој, таа, тоа, ние, вие, тие*. Clitics:

| | accusative | dative |
|---|---|---|
| 1sg | ме | ми |
| 2sg | те | ти |
| 3sg m/n | го | му |
| 3sg f | **ја** | **ѝ** |
| 1pl | нè | ни |
| 2pl | ве | ви |
| 3pl | ги | им |

Note *ја* is the feminine object clitic in Macedonian, while in Serbian *ја* means "I". Relative/interrogative: *кој, која, кое, кои*, *што*, *кој што*, *каде*, *кога*, *зошто*, *како*, *колку*.

**Clitic doubling** is obligatory with definite direct objects and with indirect objects: *Го видов Петар* (lit. "him I-saw Peter"), *Ја прочитав книгата* "I read the book", *Му ја дадов книгата на Марко*.

## Verbs

Verbs inflect for person, number, tense, aspect (perfective/imperfective pairs) and mood. There is **no infinitive**; the citation form is the 3sg present (*пише* "to write"). Complement clauses use **да** + present: *сакам да одам* "I want to go".

Present tense (*сака* "want"): **сакам, сакаш, сака, сакаме, сакате, сакаат**. The 1sg ending **-ам** (*мислам*, *одам*, *пишувам*; also *-ам* after *ј*: *пијам*) and the 3pl **-аат/-ат** are characteristic (cf. Bulgarian 1sg *-а/-я* in many verbs: *пиша*, *мисля*).

Copula *сум*: **сум, си, е, сме, сте, се** (note 3pl **се** "they are", homographic with the reflexive *се*; Bulgarian has *съм ... са*).

Past tenses:
- **Aorist** (perfective): *видов, виде, виде, видовме, видовте, видоа*
- **Imperfect**: *сакав, сакаше, сакаше, сакавме, сакавте, сакаа* -- the 2/3sg ending **-ше** (*беше*, *требаше*, *студеше*) is very frequent in narrative text.
- **L-form perfect / evidential**: *сум видел*, 3sg *видел* without auxiliary for reported events (*Тој дошол* "he reportedly came").
- **Има-perfect** (Balkan "have" perfect): *имам видено* "I have seen", *има дојдено*. Bulgarian lacks this as a standard construction.

**Future:** invariable particle **ќе** + present: *ќе дојдам* "I will come"; negative **нема да** + present (*нема да дојдам*). Conditional: **би** + l-form (*би сакал*).

Imperative: *дојди!*, *отвори!*, plural *дојдете!*; negative *не* + imperative or *немој* + да-clause.

## Prepositions and Particles

Very frequent: *на, во, од, со, за, до, по, кон, низ, меѓу, преку, покрај, без, пред, зад, под, над, врз, кај*. Note **во** (Bulgarian *в/във*), **со** (Bulgarian *с/със*), **од** (Bulgarian *от*), **кај** "at, by (someone's place)".

Conjunctions: *и, а, но, ама, или, дека* ("that"), *оти*, *што*, *ако*, *кога*, *додека*, *бидејќи*, *затоа што*, *иако*, *туку*. Question particle **ли** (*Дали доаѓаш?* / *Доаѓаш ли?*).

## Syntax Notes

- Clitic cluster order: (*ќе*) (*не*) dative before accusative, before the verb in finite clauses: *Ќе ти го дадам*; after the verb with imperatives and gerunds: *Дај ми го!*
- Negation *не* immediately precedes the clitic cluster: *Не го знам*.
- Pro-drop: subject pronouns are often omitted.

## Sample Sentences (from `examples/ud_01.txt`, `ud_02.txt`)

- *Мислам **дека** врне.* "I think (that) it is raining."
- *Соседот на Петар **ја** исфарба оградата црвена.* (article *-от*, *-та*; clitic doubling with *ја*)
- *Сонцето час **ќе** се појавеше час **ќе** се скриеше зад облаците.* (*ќе* + imperfect = habitual/future-in-past)
