# Serbian Grammar (srp_Cyrl)

Summary of the grammatical features that shape Serbian text and matter for identification. Forms are given in Cyrillic with Gaj Latin in parentheses where useful.

## Typological Profile

- **Word order:** SVO as default, but free for information structure thanks to case marking.
- **Morphology:** highly **synthetic/fusional** -- seven cases, three genders, two numbers, rich verbal inflection.
- **No articles** (unlike Macedonian/Bulgarian).
- **Clitics** obey the "second position" (Wackernagel) rule.
- **Pro-drop**: subject pronouns are usually omitted.
- **Prosody:** pitch accent with four accent types and vowel length; not marked in normal writing.

## Nouns and Cases

Seven cases: nominative, genitive, dative, accusative, vocative, instrumental, locative. Typical paradigms:

| | град (m.) "city" | жена (f.) "woman" | село (n.) "village" |
|---|---|---|---|
| N sg | град | жена | село |
| G sg | града | жене | села |
| D/L sg | граду | жени | селу |
| A sg | град | жену | село |
| V sg | граде | жено | село |
| I sg | **градом** | **женом** | **селом** |
| N pl | градови | жене | села |
| G pl | градова | жена | села |
| D/I/L pl | **градовима** | **женама** | **селима** |

Diagnostic endings in running text: **-ом/-ем** (instr. sg.), **-има/-ама** (dat./instr./loc. pl.), **-у** (loc./acc.), **-е** (gen. sg. fem.). Masculine animate accusative = genitive (*видео сам брата*). Long-form adjectival endings: **-ог(а), -ом(е), -ој, -их, -им(а)** (*новог, новом, новој, нових*). Example from `examples/ud_01.txt`: *у Бриселу* (loc.), *са Приштином* (instr.), *у животима косовских Срба* (loc. pl., gen. pl.).

## Pronouns

Personal: *ја, ти, он, она, оно, ми, ви, они, оне, она*. Clitic forms: acc. *ме, те, га, је, нас, вас, их*; dat. *ми, ти, му, јој, нам, вам, им*. Note **је** is both "is" and "her" (acc.). Interrogatives: **шта** (*šta*, "what"; *што* also occurs, especially for "why" and in ijekavian/literary usage), **ко** (*ko*, "who"; Croatian *tko*), **који, која, које**, **где** (*gde*; ijek. *гдје*), **када/кад**, **зашто**, **како**, **колико**.

## Verbs

**Infinitive** in **-ти** or **-ћи** (*бити, радити, писати, рећи, ићи*). Serbian frequently replaces the infinitive with **да + present** (*хоћу да идем* "I want to go", *морам да радим*), whereas Croatian prefers the infinitive (*hoću ići*, *moram raditi*). Both are possible in Serbian.

Present (*радити* "to work"): **радим, радиш, ради, радимо, радите, раде**.

Copula *бити* (clitic / negative / stressed):

| | clitic | negated | stressed |
|---|---|---|---|
| 1sg | сам | **нисам** | јесам |
| 2sg | си | ниси | јеси |
| 3sg | **је** | **није** | јесте |
| 1pl | смо | нисмо | јесмо |
| 2pl | сте | нисте | јесте |
| 3pl | **су** | **нису** | јесу |

**Perfect** (main past tense): clitic *бити* + l-participle: *радио сам* (*radio sam*), *рекао је* (*rekao je*), *рекла је*, *били су*. The participle endings **-о/-ла/-ло/-ли/-ле** (*рекао, била, било, били*) are very frequent; masculine *-ао/-ио/-ео* comes from historical *-л* (*рекао, био, видео*).

**Future I**: clitic *ћу, ћеш, ће, ћемо, ћете, ће* + infinitive. Serbian orthography **fuses** the clitic with an infinitive in *-ти* when the clitic follows: *радићу* (*radiću*), *биће* (*biće*), whereas Croatian writes *radit ću*, *bit će*. When the clitic precedes: *ја ћу радити* / *ја ћу да радим* (the latter is typically Serbian). Negative future: *нећу, нећеш, неће...*

Other forms: aorist (*рекох, рече*) is rare and stylistically marked; imperfect is archaic. Conditional: *би* + l-participle (*бих волео*). Imperative: *реци, хајде, слушај, чекај, немој*.

Aspect: perfective/imperfective pairs (*урадити/радити*, *рећи/говорити*); secondary imperfectives in **-ава-/-ива-** (*признавати*). Verbs borrowed with the international suffix are typically **-овати/-исати** in Serbian (*организовати, коментарисати, сугерисати*) where Croatian prefers **-ирати** (*organizirati, komentirati, sugerirati*); attested in `examples/ud_01.txt` (*сугеришу*, *коментаришући*).

## Questions and Negation

- Yes/no questions: **да ли** + finite verb (*Да ли си ту?*) is the typical Serbian pattern; the inverted *Јеси ли ту?* is also used. Croatian prefers *je li* / verb + *li*.
- Negation **не** before the verb; fused negatives *нисам, нећу, немам, нема*.

## Clitic Order

Second position, in the order: *ли* > verbal aux. (*сам, си, смо, сте, ћу...*) > dative > accusative > reflexive *се* > *је*: *Дао сам му га*, *Рекао ми је*, *Да ли ћеш му га дати?*

## Prepositions and Conjunctions

Frequent prepositions: *у, на, за, од, са/с, из, до, о, по, код, кроз, према, без, између, због, после (ijek. послије), пре (прије)*. Conjunctions: *и, а, али, или, да, што, јер, ако, кад(а), док, него, па, већ*. The particle **ли** and the subordinator **да** are among the most frequent words.

## Sample Sentences

- *Неки сугеришу **да су** споразуми корак ка коначном признавању Косова.* (`examples/ud_01.txt`)
- *Терористички напади ... пре једне деценије данас су мало **вероватни**, рекао је координатор ЕУ.* (ekavian *пре*, *вероватни*; `examples/ud_03.txt`)
