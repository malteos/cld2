# Macedonian Identification Characteristics (mkd_Cyrl)

## Alphabet and Diagnostic Letters

Macedonian Cyrillic has 31 letters:

а б в г д **ѓ** е ж з **ѕ** и **ј** к л **љ** м н **њ** о п р с т **ќ** у ф х ц ч **џ** ш

**Unique to Macedonian** (among Cyrillic standard languages):
- **ѓ** (/ɟ/, cognate of Serbian ђ, Bulgarian жд): *меѓу* "between", *луѓе* "people", *туѓ* "foreign"
- **ќ** (/c/, cognate of Serbian ћ, Bulgarian щ): *ќе* (future particle), *повеќе* "more", *веќе* "already", *куќа* "house", *бидејќи* "because"
- **ѕ** (/dz/): *ѕвезда* "star", *ѕид* "wall" (rare in running text)

**Shared with Serbian, absent from Bulgarian/Russian:** **ј** (very frequent: *јас*, *ја*, *која*, *мојот*), **љ**, **њ**, **џ**.

**Absent from Macedonian:** **щ, ъ, ь, ю, я, й** (all Bulgarian), **ы, э, ё** (Russian), **є, і, ї, ґ** (Ukrainian), **ђ, ћ** (Serbian). A single occurrence of any of these in otherwise Macedonian-looking text is strong counter-evidence (except in quoted foreign names).

Grave-accented **ѐ** and **ѝ** occur in standard spelling (*сѐ* "everything", *ѝ* "to her"); they are distinctively Macedonian, though many web writers omit the accent.

## Letter Frequency (rough)

In the small sample `examples/ud_*.txt` (about 1,000 words), the most frequent letters were а, е, о, и, т, н, д, в, с, р; **ј** was about 2% of letters, **ш** about 2%, **ќ** about 0.5%. Treat these as indicative only (fiction sample, small size).

## Top 50 Frequent Words (from `vocabulary.json`, ranks 1-50)

на, и, во, да, се, од, за, е, со, не, го, ќе, што, дека, ги, како, ја, тоа, а, кој, кои, си, по, ми, до, ти, многу, но, или, само, има, кога, беше, сите, тој, ако, така, може, која, ова, јас, година, еден, нема, сум, биде, му, треба, време, македонија

Key glosses: **во** "in", **од** "from/of", **со** "with", **ќе** future particle, **што** "what/that", **дека** "that" (complementizer), **ги** "them" (clitic), **ја** "her" (clitic), **тоа/ова** "that/this", **кој/која/кои** "who/which", **многу** "very, much", **сите** "all", **јас** "I", **сум** "I am", **биде** "be (subjunctive)".

Next tier includes повеќе, уште, тие, сега, каде, луѓе, овој, оваа, таа, дали, кај, додека, зошто, бидејќи, меѓу.

Marker words relative to cousins (computed in `../chalis/discriminators.md`): vs. Bulgarian -- *од, ќе, што, дека, како, ја, тоа, кој, многу, сите, тој, ова, јас, еден, нема, сум, биде, треба, повеќе, уште, тие, каде, луѓе*; vs. Serbian -- *во, ќе, дека, ги, тоа, кои, многу, сите, јас, сум, биде, повеќе, уште, тие, сега, каде, луѓе, оваа, таа, кај, додека*.

## Character N-grams

Frequent bigrams/trigrams in the sample include word-initial *на, не, се, по, до, да, за, ја, го, ќе, шт(о)* and word-final *-от, -та, -то, -ам, -ше, -ме*. Distinctive (as opposed to merely frequent) patterns:

- **-от#** word-finally: masculine definite article (*градот, човекот, патот, светот*); Bulgarian would have *-ът/-а*.
- **ќе#**, **#ќе**: future particle; **-еќе** in *повеќе, веќе*.
- **-ѓе / -ѓу**: *луѓе, меѓу*.
- **-ов#, -он#, -ва#, -во#**: proximal/distal articles (*денов*, *овој*; though *-ов* also ends many surnames and possessives).
- **-ше#**: imperfect/aorist 2-3sg (*беше, требаше, мислеше*).
- **-аат#**: present 3pl (*сакаат, имаат, знаат*).
- **-ам#**: present 1sg (*сакам, мислам, знам, имам*).
- **-иња**: neuter plural (*момчиња, кучиња*).
- **#ј** clusters: *ја, јас, ј* inside words (*која, мојот, својата*).

## Common Endings

- Nouns with article: **-от, -та, -то, -те**; plural + article **-ите, -овите**: *луѓето, градовите, децата*.
- Adjectives: masc. **-и** with article **-иот** (*новиот, првиот, неговиот*), fem. **-а / -ата** (*новата*), neut. **-о / -ото**, pl. **-и / -ите**. The endings **-иот** and **-ата/-ите** on adjectives are very frequent and diagnostic vs. Bulgarian (*-ият/-ия*).
- Verbs: **-ам, -аш, -а, -аме, -ате, -аат**; past **-в, -ше, -вме, -вте, -а(а)**; l-forms **-л, -ла, -ло, -ле**; verbal noun **-ње** (*читање, учење*); verbal adverb **-јќи** (*одејќи*).

## Definite Article Summary

| | Macedonian | Bulgarian (for contrast) |
|---|---|---|
| masc. | **-от** / -ов / -он | -ът, -ят / -а, -я |
| fem. | -та / -ва / -на | -та |
| neut. | -то / -во / -но | -то |
| plural | -те / -ве / -не | -те |

Only the masculine form and the extra proximal/distal sets are distinctive; *-та, -то, -те* are shared with Bulgarian.

## Highly Diagnostic Features (summary)

1. Letters **ѓ, ќ, ѕ** (unique) and **ј, љ, њ, џ** (shared only with Serbian), with no щ/ъ/ю/я.
2. Function words **во, со, од, ќе, што, дека, сум, јас, многу, сите**.
3. Masculine article **-от** and adjectival **-иот**.
4. Clitic doubling patterns: *го/ја/ги* + verb + definite noun.
5. No case endings (contrast with Serbian *-ом, -има, -ога*), no infinitive in *-ти/-ть*.

## Caveats

- `vocabulary.json` is built from wordfreq (web text), so it contains proper names (*македонија, скопје*) and some English tokens (*the*).
- Macedonian and Bulgarian share most top-200 words (*на, и, да, е, за, се, не, си, по, а*...); these carry no discriminative weight between the two.
