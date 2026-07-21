# Danish (dansk) - Differences from Similar Languages

## Overview of Confusability

Danish is one of the most challenging languages for automatic language identification due to its extreme similarity to Norwegian Bokmal. The two languages share centuries of intertwined history: Danish was the written language of Norway for over 400 years during the Danish-Norwegian union (1380-1814), and Norwegian Bokmal was developed directly from Danish, retaining much of its vocabulary, grammar, and spelling conventions. This makes Danish-Norwegian Bokmal the single most difficult language pair for CLD2 and similar language identification systems.

## Danish vs Norwegian Bokmal (CRITICAL CONFUSABLE PAIR)

### Historical Context

Norwegian Bokmal (literally "book language") evolved from the written Danish used in Norway during the union period. After Norway's independence in 1814, the written language was gradually "Norwegianized" through a series of orthographic reforms, but the fundamental structure remains very close to Danish. Many sentences are identical in written Danish and Norwegian Bokmal.

### Spelling Differences

Despite the overwhelming similarity, systematic spelling differences exist:

| Pattern | Danish | Norwegian Bokmal | Examples |
|---------|--------|-----------------|----------|
| Double consonants | Often single | Often double | Danish "efter" vs Norwegian "etter" |
| -tion suffix | -tion | -sjon | Danish "information" vs Norwegian "informasjon" |
| -ere suffix | -ere | -ere (same) | Both: "interessere" |
| hv- words | hvad, hvor, hvem, hvordan, hvorfor | hva, hvor, hvem, hvordan, hvorfor | Danish "hvad" vs Norwegian "hva" |
| -ighed suffix | -ighed | -ighet | Danish "vigtighed" vs Norwegian "viktighet" |
| -ig adjectives | Some differ | Some differ | Danish "vigtig" vs Norwegian "viktig" |
| -else nouns | -else | -else (same) | Both: "foelelse" |
| Soft d | d preserved in spelling | d often preserved | Similar patterns |

### Key Vocabulary Differences

These vocabulary items are among the most reliable indicators for distinguishing Danish from Norwegian Bokmal:

| English | Danish | Norwegian Bokmal |
|---------|--------|-----------------|
| after | efter | etter |
| what | hvad | hva |
| time/hour | time | time (same) |
| now | nu | naa |
| also/too | ogsaa | ogsaa (same, but "og" pronunciation differs) |
| speak/talk | tale | snakke (more common) / tale |
| boy | dreng | gutt |
| girl | pige | jente |
| food | mad | mat |
| water | vand | vann |
| street | gade | gate |
| money | penge | penger |
| to find | finde | finne |
| to know | vide | vite |
| to buy | koebe | kjaeepe |
| to write | skrive | skrive (same) |
| school | skole | skole (same) |
| language | sprog | spraak |
| question | spoergsmaal | spoersmaal |
| answer | svar | svar (same) |
| always | altid | alltid |
| never | aldrig | aldri |
| perhaps | maaske | kanskje |
| beautiful | smuk | vakker |
| ugly | grim | stygg |
| different | anderledes/forskellig | annerledes/forskjellig |

### Grammatical Differences

The grammatical structures of Danish and Norwegian Bokmal are nearly identical, but some differences exist:

- **Pronoun forms**: Danish "jeg" (I) vs Norwegian "jeg" (same). Danish "hun" (she) vs Norwegian "hun" (same). But Danish "hende" (her, object) vs Norwegian "henne."
- **Verb forms**: Most verb conjugations are identical, but some irregular verbs differ: Danish "faa" (past: "fik") vs Norwegian "faa" (past: "fikk").
- **Noun plurals**: Generally similar patterns, but specific words may differ: Danish "boeger" vs Norwegian "boeker" (books).

### Diagnostic Words and Patterns for LID

The following features, when found in combination, strongly suggest Danish rather than Norwegian Bokmal:

1. **"efter"** (not "etter") - one of the single best indicators
2. **"hvad"** (not "hva")
3. **"-tion"** endings (not "-sjon"): "station," "information," "nation"
4. **"nu"** (not "naa")
5. **"dreng"** (not "gutt")
6. **"pige"** (not "jente")
7. **"mad"** (not "mat")
8. **"maaske"** (not "kanskje")
9. **"sprog"** (not "spraak")
10. **"aldrig"** (not "aldri")
11. **"-ighed"** suffix (not "-ighet")
12. **"altid"** (not "alltid")

### Shared Features That Do NOT Help Distinguish

The following features are essentially identical in Danish and Norwegian Bokmal and therefore provide no discriminative signal:

- Function words: og, i, er, med, paa, for, af/av, til, det, en
- Suffixed definite articles: -en, -et (both languages use these)
- V2 word order (identical)
- Passive -s construction (both use it)
- Most common verbs: have/har, vaere/er, komme, gaa, tage

## Danish vs Norwegian Nynorsk

Norwegian Nynorsk (literally "New Norwegian") is significantly more different from Danish than Bokmal is. Nynorsk was constructed in the 19th century by Ivar Aasen based on Norwegian dialects, deliberately distancing itself from Danish influence. Key differences include:

| Feature | Danish | Norwegian Nynorsk |
|---------|--------|------------------|
| the (masc.) | -en | -en (same) |
| the (fem.) | (no feminine) | -a |
| we | vi | vi/me |
| they | de | dei |
| infinitive marker | at | aa |
| weak past tense | -ede/-te | -a/-te |
| what | hvad | kva |
| who | hvem | kven |
| not | ikke | ikkje |
| also | ogsaa | ogsaa/og |
| after | efter | etter |

Nynorsk preserves three grammatical genders (masculine, feminine, neuter) versus Danish's two (common, neuter), and its definite suffixed articles reflect this: "-en" (masculine), "-a" (feminine), "-et" (neuter). The presence of feminine -a endings on nouns is a strong indicator of Nynorsk rather than Danish.

The infinitive marker "aa" in Nynorsk (vs. Danish "at") is a reliable distinguishing feature. Nynorsk "ikkje" (not) versus Danish "ikke" is another clear signal.

## Danish vs Swedish

Danish and Swedish, while both East Scandinavian historically, have diverged more noticeably than Danish and Norwegian Bokmal. The differences are more systematic and easier for LID systems to detect:

### Orthographic Differences

- **ae/oe vs ae/oe**: Danish (and Norwegian) use ae and oe, while Swedish uses ae and oe. This single character-level difference is highly diagnostic. Any text containing ae is not Swedish; any text containing ae is not Danish.
- **Swedish uses oe where Danish uses oe**: Danish "roed" vs Swedish "roed" (red), Danish "groen" vs Swedish "groen" (green).

### Vocabulary Differences

| English | Danish | Swedish |
|---------|--------|---------|
| and | og | och |
| not | ikke | inte |
| what | hvad | vad |
| who | hvem | vem |
| how | hvordan | hur |
| also | ogsaa | ocksaa |
| after | efter | efter (same) |
| I | jeg | jag |
| they | de | de (same, but pronounced differently) |
| but | men | men (same) |
| or | eller | eller (same) |
| would | ville | skulle/ville |
| one/you (impersonal) | man | man (same) |
| boy | dreng | pojke |
| girl | pige | flicka |
| to speak | tale | tala |
| language | sprog | spraak |
| question | spoergsmaal | fraaga |

### Key Diagnostic Features for LID

1. **Character set**: ae/oe (Danish) vs ae/oe (Swedish) - the single most reliable feature
2. **"og" vs "och"**: and
3. **"ikke" vs "inte"**: not
4. **"jeg" vs "jag"**: I
5. **"ogsaa" vs "ocksaa"**: also

The ae/oe vs ae/oe distinction alone is often sufficient to distinguish Danish from Swedish with very high confidence.

## Danish vs Icelandic

Icelandic, while historically related as a fellow North Germanic language, is vastly different from modern Danish. Icelandic has preserved the Old Norse inflectional system (four cases, three genders, complex verb conjugation), archaic vocabulary, and a conservative orthography. The two languages are not mutually intelligible, and LID confusion between them is very rare. Icelandic uses distinctive characters such as thorn and eth, as well as accented vowels (aa, ee, oe, uu, yy, oe), that immediately distinguish it from Danish.

## Danish vs Faroese

Faroese, spoken in the Faroe Islands where Danish is co-official, is another North Germanic language that has retained more archaic features than Danish. It uses distinctive characters such as eth and accented vowels (aa, ii, oo, uu, yy, ae, oe), and its grammar preserves three genders and a partial case system. Confusion with Danish is uncommon in LID systems due to these orthographic differences.

## Danish vs German

Despite belonging to the same Germanic family and geographic proximity, Danish and German are readily distinguishable. German retains three genders with articles (der/die/das), a four-case system, and capitalizes all nouns. Danish function words (og, er, ikke, med, paa) are quite different from German equivalents (und, ist, nicht, mit, auf). The presence of ae, oe, aa in Danish and ae, oe, ue, ss in German provides clear orthographic signals.

## Summary: Difficulty Ranking for LID Confusion

1. **Norwegian Bokmal** - EXTREMELY difficult (near-identical in writing; requires word-level and statistical analysis)
2. **Norwegian Nynorsk** - Moderately difficult (more differences, but still Scandinavian)
3. **Swedish** - Moderate (ae/oe vs ae/oe is highly diagnostic, plus vocabulary differences)
4. **Icelandic / Faroese** - Low difficulty (very different orthography and morphology)
5. **German / Dutch / English** - Very low difficulty (clearly different languages)
