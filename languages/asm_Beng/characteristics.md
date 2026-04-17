# Assamese LID characteristics

## Script signals

- **ৰ** (U+09F0, *assamese ra*) and **ৱ** (U+09F1, *wavy ba / wa*) are Assamese-exclusive inside the Bengali-script block. A single occurrence of either is a near-perfect diagnostic against Bengali.
- Assamese text otherwise uses the same letter set as Bengali, including independent vowels, conjunct formation, virāma **্**, anusvāra **ং**, candrabindu **ঁ**, and visarga **ঃ**.
- The use of **ক্ষ, জ্ঞ, ৎ** mirrors Bengali; no unique glyphs beyond ৰ and ৱ.

## Top function words

আৰু (and), কিন্তু, অথবা, বা, যে, যি, যিসকল, ই, সি, তাই, তেওঁ, মই, আমি, তই, তুমি, আপুনি, আছে, নাই, হয়, হ'ল, হ'ব, আছিল, নাছিল, কৰা, কৰে, কৰিছে, এতিয়া, তেতিয়া, ইয়াত, তাত, কেনেকৈ, কিয়, কোন, কি, ক'ত, ক'লৈ, নে (question), লাগে, পাৰে.

## N-gram and spelling patterns

- The single most diagnostic bigram is any word containing **ৰ** — e.g. **আৰু** ("and"), **কৰা**, **ঘৰ**, **পৰা**, **বোৰ**. Bengali equivalents use **র**.
- Wavy-ba **ৱ** appears in words like **ৱেব** (web), **ৱৰ্ল্ড**, and native **ৱে** particles.
- Plural enclitic **-বোৰ** on inanimate nouns.
- Perfective / 1sg verb ending **-ওঁ / -ঁ** (e.g. **মই কৰিলোঁ** "I did"), with nasalisation — distinct from Bengali **-ছে / -ছি**.
- Negative copula **নাই** is far more frequent than its Bengali cognate **নেই**.

## Morphology hooks

- Genitive **-ৰ** (note the Assamese *ra* letter), dative/accusative **-ক**, locative **-ত**, instrumental **-এৰে**.
- Classifier + numeral agglomerations (এজন মানুহ "one man").
- Honorific verb endings: **-ছে** (neutral) vs **-িছে / -িছিল / -িল** and polite **-ছে / -ছিল**.

## Punctuation / orthography quirks

- Sentence terminator **।** (*daṛi*), shared with Bengali/Devanagari.
- Digits are typically the Bangla set ০–৯, sometimes Latin.
- ZWNJ is used to break conjuncts where explicit halant is desired.
