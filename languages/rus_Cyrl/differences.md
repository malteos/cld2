# Distinguishing Russian from Closely Related Languages

Russian is the default "Cyrillic guess" for many classifiers, so the main risk is over-labelling Ukrainian, Belarusian, Bulgarian, Rusyn or even Serbian/Macedonian text as Russian. The cues below are ordered from most to least machine-checkable. For romanized text see `chalis.md`.

## Quick Letter Test (Cyrillic)

| Letter(s) present | Points to |
|---|---|
| і, ї, є, ґ, word-internal apostrophe (ʼ, ', ’) | Ukrainian (і also Belarusian/Rusyn) |
| ў | Belarusian |
| ј, љ, њ, џ, ђ, ћ | Serbian |
| ј, љ, њ, џ, ѓ, ќ, ѕ | Macedonian |
| ы, э, ъ (rare, after prefix), ё | Russian (ы/э/ё also Belarusian; ы also Rusyn) |
| ъ frequent inside words, no ы | Bulgarian |

A text containing **ы** or **э** and **none** of і/ї/є/ґ/ў/ј is almost certainly Russian. One stray і or ї in an otherwise Russian text can be a quoted Ukrainian name (*Київ*), so require repeated evidence.

## Russian vs. Ukrainian (most confusable)

- **Alphabet:** Russian has ы, э, ъ, ё; Ukrainian has і, ї, є, ґ and the apostrophe. Russian и = /i/, Ukrainian и = [ɪ] and і = /i/.
- **Function words** (`chalis/discriminators.md`): Russian *что, это, как, от, но, он, его, есть, если, когда, или, они, года, был/была, здесь, себя, тебя, очень* vs. Ukrainian *що, це, як, від, але, він, його, є, якщо, коли, або, вони, року, був/була, тут, себе, тебе, дуже*. Shared and non-diagnostic: *в, и/і, на, не, с/з, я, по, а, за, для, о, к, то, у, все, так, же, до*.
- **Morphology:** past masc. -л (*сказал*) vs. -в (*сказав*); infinitive -ть vs. -ти (*делать* / *робити*); gen. pl. -ов vs. -ів; adjective -ый/-ая/-ое vs. -ий/-а/-е (*новый, новая, новое* / *новий, нова, нове*); fem. oblique -ой vs. -ої; 3sg -ет vs. -є (*читает* / *читає*); verbal nouns -ние vs. -ння.
- **Ikavism:** Ukrainian і where Russian has о/е in closed syllables: *кот/кіт*, *нос/ніс*, *вечер/вечір*, *от/від*.
- **Lexicon:** Russian *спасибо, сейчас, сегодня, говорить, хорошо, нужно* vs. Ukrainian *дякую, зараз, сьогодні, говорити/казати, добре, потрібно/треба*.

## Russian vs. Belarusian

- Belarusian has **ў** and **і**, no и, no щ (uses шч), no ъ (uses apostrophe). Russian has и, щ, ъ and no ў/і.
- Belarusian writes akanye: unstressed о → а (*малако*, *горад* but *гарады*); Russian keeps о.
- Dzekanye/tsekanye: Belarusian дз, ц before soft vowels (*дзень, цёпла*) vs. Russian д, т (*день, тепло*).
- Words: Belarusian *гэта, што, але, калі, ён, яны, вельмі, таксама* vs. Russian *это, что, но, когда, он, они, очень, тоже/также*.
- Both share ы, э, ё, so these letters do not rule out Belarusian; ў, і, шч, and дз do.

## Russian vs. Bulgarian

- Bulgarian has no ы, э, ё; ъ is a frequent vowel (*съм, със, към, България*). Russian ы is common; ъ is rare.
- Bulgarian is analytic: **postposed definite articles** (*-ът/-а, -та, -то, -те*: *градът, жената, детето, хората*), no infinitive (uses *да* + present), almost no case endings on nouns.
- Function words: Bulgarian *ще, са, това, като, най, към, няма, съм, които, трябва, какво* vs. Russian *будет, (они) есть / zero copula, это, как, самый, к, нет, (я) zero copula, которые, нужно/надо, что*.
- Shared non-diagnostic items: *в, и, на, не, с, по, за, но, то, от, до, да, без, много, между* (`chalis/discriminators.md`). Note that *да* ("yes" in Russian) is a frequent conjunction in Bulgarian, Serbian and Macedonian.
- See `bul_Cyrl/differences.md`.

## Russian vs. Serbian and Macedonian

- Serbian Cyrillic: ј, љ, њ, ћ, ђ, џ; Macedonian: ј, љ, њ, ѓ, ќ, ѕ, џ. Neither has я, ю, ё, й, ы, э, щ, ъ, ь. Any **я/ю/й/ь** in a passage therefore excludes them.
- Serbian markers: *је, није, шта, ово, смо, ће, који, још*; Macedonian: *ќе, што, дека, во, тоа, многу, сум*. Russian: *что, это, он, был, только, когда*.
- Serbian and Macedonian are also written in Latin script (Serbian Gaj alphabet is standard), which is handled in `chalis.md`.

## Russian vs. Rusyn (rue)

Rusyn is not one of the benchmark labels here, but it can appear as a distractor. Carpathian Rusyn orthographies (Slovakia/Ukraine) combine letters of both neighbours: **ы together with і, ї, є, ґ** (and sometimes ё, ъ). Pannonian (Vojvodina) Rusyn uses ї, є, ґ but no і or ы (stated from general knowledge; orthographies vary — treat as uncertain). Typical Rusyn words such as *єм, тай, бо, ці, але* are Ukrainian-like. A text mixing ы with і/ї is therefore unlikely to be Russian (or Ukrainian).

## Machine-Checkable Checklist

1. Count letters: ы, э, ъ, ё (Russian) vs. і, ї, є, ґ, ʼ (Ukrainian) vs. ў (Belarusian) vs. ј/љ/њ/ѓ/ќ/ћ/ђ (Serbian/Macedonian).
2. Look for *что/это/как/был* (Russian) vs. *що/це/як/був* (Ukrainian) vs. *това/като/ще/са* (Bulgarian).
3. Check endings: -ый/-ая/-ое/-ого, -ов, -л past, -ть infinitive = Russian.
4. Any postposed article pattern (-ът, -та, -то, -те on nouns) plus ъ = Bulgarian.
5. Require two or more independent cues before overriding the letter test; short texts may consist only of shared words (*и, на, не, по, за*).
