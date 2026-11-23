# Macedonian vs. Confusable Languages

Macedonian is most often confused with **Bulgarian** (closest relative, overlapping vocabulary and grammar) and with **Serbian** (shared Vukovian alphabet letters ј, љ, њ, џ). Russian and Ukrainian are less similar but are frequent default guesses for any Cyrillic text. In Latin transliteration (see `chalis.md`), Croatian, Bosnian and Montenegrin also become candidates.

## Machine-Checkable Cues (Cyrillic)

| Cue | Indicates |
|---|---|
| any of **ѓ ќ ѕ** | Macedonian |
| **ѐ, ѝ** (accented) | Macedonian |
| **ј, љ, њ, џ** present, **ђ, ћ** absent | Macedonian or Serbian -> check words |
| **ђ** or **ћ** | Serbian |
| **щ, ъ, ю, я, й, ь** | Bulgarian (or Russian/Ukrainian) -- not Macedonian |
| **ы, э, ё** | Russian |
| **є, і, ї, ґ** | Ukrainian |
| future particle **ќе** | Macedonian (Bulgarian **ще**, Serbian **ће**) |
| copula 3sg **е** + no **је** | Macedonian/Bulgarian (Serbian **је**) |

## Macedonian vs. Bulgarian

The hardest pair. Many top words are identical (*на, и, да, е, за, се, не, си, по, а, ми, но, до, го, има, ако, може, само, ли*; see `../chalis/discriminators.md`). Decide using:

| Function | Macedonian | Bulgarian |
|---|---|---|
| future | **ќе** | **ще** |
| in / with / from | **во / со / од** | **в, във / с, със / от** |
| that (compl.) | **дека**, оти | **че** |
| what | **што** | **какво**, що (colloquial) |
| this / that | **ова, овој, оваа / тоа** | **това, този, тази** |
| I / I am | **јас / сум** | **аз / съм** |
| they are | **се** | **са** |
| very | **многу** | **много** |
| there is not | **нема** | **няма** |
| all | **сите** | **всички** |
| people | **луѓе** | **хора** |
| more / already | **повеќе / веќе** | **повече / вече** |
| who/which | **кој, која, кои** | **който, която, които** |
| must | **треба** | **трябва** |
| be (subj.) | **биде** | **бъде** |

Morphology: masc. article **-от** vs. Bulgarian **-ът/-а** (*градот* / *градът*, *града*); adjectival **-иот** vs. **-ият/-ия**; Macedonian 1sg **-ам** in all verbs (*мислам*) vs. Bulgarian *-я/-а* in many (*мисля, пиша*); Macedonian **има**-perfect (*имам видено*), absent in standard Bulgarian. Orthography: Bulgarian *ъ* <-> Macedonian *о/а* (*сън/сон, вълк/волк*); Bulgarian *щ, жд* <-> Macedonian *ќ, ѓ* (*къща/куќа, между/меѓу*); Bulgarian *я* <-> Macedonian *е* (*голям/голем, бял/бел*).

## Macedonian vs. Serbian

Shared letters ј, љ, њ, џ make orthographic overlap high, and some words coincide (*да, не, се, ти, ми, за, ли, ја, само, од, како, добро*), but:

- Serbian has **ђ, ћ**; Macedonian has **ѓ, ќ, ѕ**.
- Serbian has **seven cases**: endings *-ом, -има, -ама, -ога/-ог, -ему*, *-у* (locative/accusative) are pervasive; Macedonian has none.
- Serbian has **infinitives** in **-ти/-ћи** (*бити, радити, рећи*); Macedonian has none.
- Serbian has **no articles**; Macedonian *-от/-та/-то/-те* is everywhere.
- Function words: Serbian **је, су, у, са, није, шта, ће, ћу, који, из, још, више** vs. Macedonian **е, се, во, со, не е, што, ќе, кој, од, уште, повеќе**.
- Note the false friend **ја**: "I" in Serbian, feminine object clitic "her" in Macedonian (*ја видов* "I saw her").

## Macedonian vs. Russian

Russian has **ы, э, ё, й, щ, ъ, ь, ю, я** and no **ј, ѓ, ќ**. Russian has six cases (endings *-ого, -ому, -ыми, -ах*), infinitives in **-ть** (*делать*), and no articles. High-frequency Russian words *что, это, как, он, она, был, для, его, только* do not occur in Macedonian (Macedonian *што, ова/тоа, како, тој, таа*).

## Macedonian vs. Ukrainian

Ukrainian **і, ї, є, ґ** and soft sign **ь** are absent from Macedonian. Ukrainian words *що, це, як, від, він, його, вже, але* have no Macedonian equivalents of the same form. Ukrainian infinitives end in **-ти**, plus a full case system.

## Macedonian vs. Croatian, Bosnian, Montenegrin

These are Latin-script (Montenegrin and Bosnian also use Cyrillic), case-inflecting, article-less Shtokavian languages; in Cyrillic Montenegrin/Bosnian text the Serbian cues above apply (ђ, ћ, cases, *је*, infinitives), plus ijekavian *ије/је* reflexes (*вријеме, дјеца*). Macedonian has no ijekavian reflexes (*време, деца*, like ekavian Serbian). In Latin transliteration, Macedonian is identified by *vo, so, od, kje/ke, deka, shto/sto, -ot*, and the absence of case endings; see `chalis.md`.

## Pitfalls

- Bulgarian text written by Macedonian speakers (or vice versa) and dialectal/colloquial Bulgarian from the south-west (e.g. *ке* future in Pirin dialects -- uncertain how frequent in written data) can blur the distinction; rely on several cues, not one.
- Very short texts consisting only of shared words (*да, не, на, и, се*) cannot be reliably separated.
