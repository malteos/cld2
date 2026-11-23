# Danish (dansk) - Differences from Similar Languages

## Overview of Confusability

Danish is one of the most challenging languages for automatic language identification due to its extreme similarity to Norwegian Bokmål. The two languages share centuries of intertwined history: Danish was the written language of Norway for over 400 years during the Danish-Norwegian union (1380-1814), and Norwegian Bokmål was developed directly from Danish, retaining much of its vocabulary, grammar, and spelling conventions. This makes Danish-Norwegian Bokmål the single most difficult language pair for CLD2 and similar language identification systems.

## Danish vs Norwegian Bokmål (CRITICAL CONFUSABLE PAIR)

### Historical Context

Norwegian Bokmål (literally "book language") evolved from the written Danish used in Norway during the union period. After Norway's independence in 1814, the written language was gradually "Norwegianized" through a series of orthographic reforms, but the fundamental structure remains very close to Danish. Many sentences are identical in written Danish and Norwegian Bokmål. Both use the same special letters æ, ø, å, so the character set does not separate them.

### Spelling Differences

Despite the overwhelming similarity, systematic spelling differences exist:

| Pattern | Danish | Norwegian Bokmål | Examples |
|---------|--------|-----------------|----------|
| Double consonants | Often single | Often double | Danish "altid" vs Norwegian "alltid", "al" vs "all" |
| -ft- vs -tt- | -ft- | -tt- | Danish "efter" vs Norwegian "etter" |
| -tion suffix | -tion | -sjon | Danish "information" vs Norwegian "informasjon" |
| -ere suffix | -ere | -ere (same) | Both: "interessere" |
| hv- words | hvad, hvor, hvem, hvordan, hvorfor | hva, hvor, hvem, hvordan, hvorfor | Danish "hvad" vs Norwegian "hva" |
| -ighed suffix | -ighed | -ighet | Danish "vigtighed" vs Norwegian "viktighet" |
| -ig adjectives | Some differ | Some differ | Danish "vigtig" vs Norwegian "viktig" |
| -else nouns | -else | -else (same) | Both: "følelse" |
| Soft consonants after vowels | b, d, g | p, t, k | Danish "mad, gade, vide, købe, bog" vs Norwegian "mat, gate, vite, kjøpe, bok" |
| kj-/skj- spellings | k, sk | kj, skj | Danish "købe, forskellig" vs Norwegian "kjøpe, forskjellig" |

### Key Vocabulary Differences

These vocabulary items are among the most reliable indicators for distinguishing Danish from Norwegian Bokmål:

| English | Danish | Norwegian Bokmål |
|---------|--------|-----------------|
| after | efter | etter |
| what | hvad | hva |
| time/hour | time | time (same) |
| now | nu | nå |
| also/too | også | også (same) |
| speak/talk | tale | snakke (more common) / tale |
| boy | dreng | gutt |
| girl | pige | jente |
| food | mad | mat |
| water | vand | vann |
| street | gade | gate |
| money | penge | penger |
| to find | finde | finne |
| to know | vide | vite |
| to buy | købe | kjøpe |
| to write | skrive | skrive (same) |
| school | skole | skole (same) |
| language | sprog | språk |
| question | spørgsmål | spørsmål |
| answer | svar | svar (same) |
| always | altid | alltid |
| never | aldrig | aldri |
| perhaps | måske | kanskje |
| beautiful | smuk | vakker |
| ugly | grim | stygg |
| different | anderledes/forskellig | annerledes/forskjellig |
| of | af | av |
| to take | tage | ta |

### Grammatical Differences

The grammatical structures of Danish and Norwegian Bokmål are nearly identical, but some differences exist:

- **Pronoun forms**: Danish "jeg" (I) vs Norwegian "jeg" (same). Danish "hun" (she) vs Norwegian "hun" (same). But Danish "hende" (her, object) vs Norwegian "henne."
- **Verb forms**: Most verb conjugations are identical, but some irregular verbs differ: Danish "få" (past: "fik") vs Norwegian "få" (past: "fikk"). Weak past tense: Danish "-ede" (arbejdede) vs Bokmål often "-et"/"-a" (arbeidet, arbeida).
- **Infinitive marker**: Danish "at" vs Norwegian "å" (Danish "at gå" vs Norwegian "å gå").
- **Noun plurals**: Generally similar patterns, but specific words may differ: Danish "bøger" vs Norwegian "bøker" (books).
- **Definiteness with adjectives**: Danish "det store hus" vs Norwegian "det store huset" (Norwegian uses double definiteness, Danish does not).

### Diagnostic Words and Patterns for LID

The following features, when found in combination, strongly suggest Danish rather than Norwegian Bokmål:

1. **"efter"** (not "etter") - one of the single best indicators
2. **"hvad"** (not "hva")
3. **"-tion"** endings (not "-sjon"): "station," "information," "nation"
4. **"nu"** (not "nå")
5. **"dreng"** (not "gutt")
6. **"pige"** (not "jente")
7. **"mad"** (not "mat")
8. **"måske"** (not "kanskje")
9. **"sprog"** (not "språk")
10. **"aldrig"** (not "aldri")
11. **"-ighed"** suffix (not "-ighet")
12. **"altid"** (not "alltid")
13. **"af"** and infinitive **"at"** (not "av" and "å")

### Shared Features That Do NOT Help Distinguish

The following features are essentially identical in Danish and Norwegian Bokmål and therefore provide no discriminative signal:

- Function words: og, i, er, med, på, for, til, det, en (but note Danish "af" vs Norwegian "av")
- The letters æ, ø, å
- Suffixed definite articles: -en, -et (both languages use these)
- V2 word order (identical)
- Passive -s construction (both use it)
- Most common verbs: har, er, komme, gå (but Danish infinitives "have, være, tage" vs Norwegian "ha, være, ta")

## Danish vs Norwegian Nynorsk

Norwegian Nynorsk (literally "New Norwegian") is significantly more different from Danish than Bokmål is. Nynorsk was constructed in the 19th century by Ivar Aasen based on Norwegian dialects, deliberately distancing itself from Danish influence. Key differences include:

| Feature | Danish | Norwegian Nynorsk |
|---------|--------|------------------|
| the (masc.) | -en | -en (same) |
| the (fem.) | (no feminine) | -a |
| we | vi | vi/me |
| they | de | dei |
| infinitive marker | at | å |
| weak past tense | -ede/-te | -a/-te |
| what | hvad | kva |
| who | hvem | kven |
| not | ikke | ikkje |
| also | også | også/og |
| after | efter | etter |
| I | jeg | eg |

Nynorsk preserves three grammatical genders (masculine, feminine, neuter) versus Danish's two (common, neuter), and its definite suffixed articles reflect this: "-en" (masculine), "-a" (feminine), "-et" (neuter). The presence of feminine -a endings on nouns is a strong indicator of Nynorsk rather than Danish.

The infinitive marker "å" in Nynorsk (and Bokmål) vs. Danish "at" is a reliable distinguishing feature. Nynorsk "ikkje" (not), "eg" (I) and "kva" (what) versus Danish "ikke", "jeg", "hvad" are other clear signals.

## Danish vs Swedish

Danish and Swedish, while both East Scandinavian historically, have diverged more noticeably than Danish and Norwegian Bokmål. The differences are more systematic and easier for LID systems to detect:

### Orthographic Differences

- **æ/ø vs ä/ö**: Danish (and Norwegian) use æ and ø, while Swedish uses ä and ö for the corresponding vowels. All three languages share å. This single character-level difference is highly diagnostic: any text containing æ or ø is not Swedish; any text containing ä or ö is not Danish (apart from foreign names and loanwords).
- **Swedish uses ö where Danish uses ø**: Danish "rød" vs Swedish "röd" (red), Danish "grøn" vs Swedish "grön" (green), Danish "dør" vs Swedish "dörr" (door).
- **Swedish uses ä where Danish uses æ**: Danish "være" vs Swedish "vara"/"är", Danish "læse" vs Swedish "läsa" (read), Danish "mænd" vs Swedish "män" (men).

### Vocabulary Differences

| English | Danish | Swedish |
|---------|--------|---------|
| and | og | och |
| not | ikke | inte |
| what | hvad | vad |
| who | hvem | vem |
| how | hvordan | hur |
| also | også | också |
| after | efter | efter (same) |
| I | jeg | jag |
| they | de | de (same, but pronounced differently) |
| but | men | men (same) |
| or | eller | eller (same) |
| is/are | er | är |
| would | ville | skulle/ville |
| one/you (impersonal) | man | man (same) |
| boy | dreng | pojke |
| girl | pige | flicka |
| to speak | tale | tala |
| language | sprog | språk |
| question | spørgsmål | fråga |

### Key Diagnostic Features for LID

1. **Character set**: æ/ø (Danish) vs ä/ö (Swedish) - the single most reliable feature
2. **"og" vs "och"**: and
3. **"ikke" vs "inte"**: not
4. **"jeg" vs "jag"**: I
5. **"også" vs "också"**: also
6. **"er" vs "är"**: is/are

The æ/ø vs ä/ö distinction alone is often sufficient to distinguish Danish from Swedish with very high confidence. In ASCII-only text, where these letters are stripped, rely on items 2-6.

## Danish vs Icelandic

Icelandic, while historically related as a fellow North Germanic language, is vastly different from modern Danish. Icelandic has preserved the Old Norse inflectional system (four cases, three genders, complex verb conjugation), archaic vocabulary, and a conservative orthography. The two languages are not mutually intelligible, and LID confusion between them is very rare. Icelandic uses distinctive characters such as thorn (þ) and eth (ð), as well as accented vowels (á, é, í, ó, ú, ý) and ö, that immediately distinguish it from Danish. (Icelandic also uses æ, so æ alone does not rule out Icelandic; Icelandic does not use ø or å.)

## Danish vs Faroese

Faroese, spoken in the Faroe Islands where Danish is co-official, is another North Germanic language that has retained more archaic features than Danish. It uses distinctive characters such as eth (ð) and accented vowels (á, í, ó, ú, ý), alongside æ and ø, which it shares with Danish (Faroese does not use å). Its grammar preserves three genders and a partial case system. Confusion with Danish is uncommon in LID systems due to these orthographic differences.

## Danish vs German

Despite belonging to the same Germanic family and geographic proximity, Danish and German are readily distinguishable. German retains three genders with articles (der/die/das), a four-case system, and capitalizes all nouns. Danish function words (og, er, ikke, med, på) are quite different from German equivalents (und, ist, nicht, mit, auf). The presence of æ, ø, å in Danish and ä, ö, ü, ß in German provides clear orthographic signals.

## Summary: Difficulty Ranking for LID Confusion

1. **Norwegian Bokmål** - EXTREMELY difficult (near-identical in writing, same letters æ/ø/å; requires word-level and statistical analysis)
2. **Norwegian Nynorsk** - Moderately difficult (more differences, but still Scandinavian)
3. **Swedish** - Moderate (æ/ø vs ä/ö is highly diagnostic, plus vocabulary differences)
4. **Icelandic / Faroese** - Low difficulty (very different orthography and morphology)
5. **German / Dutch / English** - Very low difficulty (clearly different languages)
