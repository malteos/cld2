# Distinguishing Ukrainian from Closely Related Languages

Ukrainian is most often mislabelled as Russian (shared Cyrillic, much shared vocabulary, frequent code-switching) and less often as Belarusian, Rusyn or Bulgarian. For Latin-script (romanized) Ukrainian see `chalis.md`.

## Quick Letter Test (Cyrillic)

| Evidence | Points to |
|---|---|
| ї, є, ґ, word-internal apostrophe, і without ы/э | Ukrainian |
| ы, э, ъ, ё, no і | Russian |
| ў, і, no и, no щ | Belarusian |
| ы together with і/ї/є | Carpathian Rusyn (uncertain; see below) |
| frequent ъ inside words, no і/ы | Bulgarian |
| ј, љ, њ (+ ћ, ђ / ѓ, ќ, ѕ) | Serbian / Macedonian |

A passage with several **і** and at least one **ї** or **є**, and no **ы/э/ў**, is Ukrainian with very high confidence.

## Ukrainian vs. Russian

- **Letters:** Ukrainian і, ї, є, ґ, ʼ; Russian ы, э, ъ, ё. Ukrainian и is a different vowel from Russian и; Russian *и* "and" corresponds to Ukrainian *і/й/та*.
- **Top function words** (`chalis/discriminators.md`): Ukrainian *що, це, як, від, але, він, його, є, ще, які, під, вже, коли, якщо, або, року, було, вони, щоб, мені, чи* vs. Russian *что, это, как, от, но, он, его, есть, ещё, какие, под, уже, когда, если, или, года, было, они, чтобы, мне, ли*. Note *було* vs. *было*, *був* vs. *был*: the same word differs by one letter, which is a reliable check.
- **Endings:**
  - past masc. *-в* (*сказав*) vs. *-л* (*сказал*);
  - infinitive *-ти* (*робити*) vs. *-ть* (*делать*);
  - 1pl *-мо* (*маємо*) vs. *-ем* (*имеем*);
  - gen. pl. *-ів* (*років*) vs. *-ов*;
  - adjectives *-ий/-а/-е/-і* vs. *-ый/-ая/-ое/-ые*; fem. gen. *-ої* vs. *-ой*;
  - nouns *-ння/-ття* vs. *-ние/-тие* (*рішення* / *решение*);
  - *-ії* vs. *-ии* (*історії* / *истории*);
  - *-ський* vs. *-ский*.
- **Ikavism:** *кіт/кот, рік/год* (but *року*), *ніч/ночь, від/от, сім/семь*.
- **Lexicon:** *дякую* (*спасибо*), *зараз* (*сейчас*), *дуже* (*очень*), *треба/потрібно* (*нужно/надо*), *тільки/лише* (*только/лишь*), *мова* (*язык*), *гроші* (*деньги*), *питання* (*вопрос*), *майже* (*почти*), *разом* (*вместе*).
- **Shared, non-diagnostic:** *в, на, не, і/и, з/с, я, по, а, за, для, о, у, то, так, все, до, без, там, тут, нас, вас, просто, ну, два, люди*.
- **Caution:** Ukrainian web text often quotes Russian (the Ukrainian frequency list contains *что* and *и*), and surzhyk mixes lexemes; weigh orthography (і/ї/є vs. ы/э) over isolated words.

## Ukrainian vs. Belarusian

- Belarusian has **ў**, **э**, **ы**, **ё**, and **шч** instead of щ; it has no и (uses ы and і), no ї, є, ґ. Ukrainian has и, ї, є, щ and no ў/ы/э.
- Belarusian writes akanye (*малако, галава*); Ukrainian keeps о (*молоко, голова*).
- Belarusian dzekanye: *дзень, дзеці*; Ukrainian *день, діти*.
- Function words: Belarusian *гэта, што, ён, яны, калі, вельмі, таксама, і* vs. Ukrainian *це, що, він, вони, коли, дуже, також, і*. Shared: *але, і, бо, тут*.
- See `bel_Cyrl/differences.md`.

## Ukrainian vs. Rusyn (rue)

Rusyn is Ukrainian-like in vocabulary and spelling, and some Ukrainian scholars treat it as a dialect group. Carpathian Rusyn (Prešov, Transcarpathia) orthographies typically use **ы** alongside і, ї, є, ґ, and some add ё, ъ or ô/ӱ; words such as *єм* ("I am"), *тай*, *што*, *дакус* are characteristic. Pannonian Rusyn (Serbia/Croatia) has its own orthography without і. These descriptions are general knowledge and orthographies vary between standards; treat as uncertain. Practical rule: **ы + і/ї in one text is not standard Ukrainian**.

## Ukrainian vs. Bulgarian

- Bulgarian has frequent ъ, no і/ї/є/ґ, no ы. Ukrainian has no ъ.
- Bulgarian has **postposed articles** (*-ът, -та, -то, -те*) and no infinitive; Ukrainian has full case morphology and infinitives in -ти.
- Bulgarian markers *ще, са, това, като, към, съм, няма, какво* vs. Ukrainian *буде, є, це, як, до, є, немає, що*. Note Bulgarian *ще* = future particle, Ukrainian *ще* = "still/yet": same spelling, different function. Bulgarian *е* "is" vs. Ukrainian *є*.
- See `bul_Cyrl/differences.md`.

## Ukrainian vs. Serbian and Macedonian

- Serbian/Macedonian Cyrillic use ј, љ, њ (+ ћ, ђ or ѓ, ќ, ѕ) and lack я, ю, є, ї, і, й, щ, ь. Any of ї/є/і/ь excludes them.
- Serbian *шта, је, није, ће*; Macedonian *што, ќе, дека, во*; Ukrainian *що, є, не є, буде*. Romanized, Ukrainian *shcho* vs. Macedonian *shto* vs. Serbian *sta/sto* (see `chalis.md`).

## Machine-Checkable Checklist

1. Letters: count і, ї, є, ґ, ʼ vs. ы, э, ъ, ё vs. ў vs. ј.
2. Words: *що, це, як, він, його, був, було, від, але, якщо, щоб, чи* (any two = strong Ukrainian).
3. Endings: -ння, -ої, -ів, -ти, -в (past), -мо, -ськ-, -ії.
4. If і is present but ы also appears frequently, consider Belarusian (with ў) or Rusyn.
5. Short texts made of shared words (*на, не, за, в, до, так*) need letter-level evidence.
