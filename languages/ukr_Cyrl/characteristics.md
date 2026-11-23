# Ukrainian (українська) — Cyrillic Script: Language Characteristics

## Alphabet and Diagnostic Letters

The Ukrainian alphabet has 33 letters plus the apostrophe:

а б в г ґ д е є ж з и і ї й к л м н о п р с т у ф х ц ч ш щ ь ю я  (+ ʼ)

Diagnostic letters:

- **і** — /i/. Very frequent: in the UD sample `examples/ud_*.txt` it is the fifth most frequent letter, ahead of т and в. Shared with Belarusian and Rusyn (and Kazakh/other non-Slavic Cyrillic), absent from Russian, Bulgarian, Serbian, Macedonian.
- **ї** — /ji/. Unique to Ukrainian among the major Slavic standards (also Rusyn). Very common in *її, їх, їм, України, української, -ої* endings.
- **є** — /jɛ/. Ukrainian (and Rusyn). In *є* "is", *своє*, *-ється*, *Європа*.
- **ґ** — /g/. Rare but unique; many texts in the wild substitute г.
- **Apostrophe ʼ** — inside words (*пʼять, імʼя, звʼязку, обʼєкт*). The modern standard prefers U+02BC (ʼ), but real text mostly uses U+0027 (') or U+2019 (’); `examples/` contains both (' and ’), and `vocabulary.json` uses '.
- **и** — [ɪ]; frequent (third most frequent letter in the sample). Unlike Russian, Ukrainian writes и after к/г/х (*руки, книги*), so sequences **ки, ги, хи** are frequent where Russian has the same but romanizations differ (see `chalis.md`).

**Absent from Ukrainian:** ы, э, ъ, ё (Russian/Belarusian), ў (Belarusian), ј, љ, њ, ѓ, ќ (Serbian/Macedonian). The absence of ы and э in a long Cyrillic passage is itself strong evidence against Russian and Belarusian. (Ukrainian *ьо* and *йо* replace Russian ё: *його, сьогодні, льон*.)

## Top 50 Function Words

From `vocabulary.json` (wordfreq ranks 1-110, nouns and proper names omitted), in order:

в, на, не, і, у, з, що, та, до, це, за, а, я, як, про, для, від, так, але, він, його, все, то, є, ви, по, ми, й, ще, які, під, вже, коли, якщо, або, було, вони, із, мене, щоб, мені, ж, тут, чи, який, просто, ти, був, буде, нас

Further: ну, тому, її, також, дуже, може, після, через, їх, хто, де, там, тільки, можна, вона, всі, ні, того, цього, бути, при, без, яка, має, цей, треба, більше, чому, була, були, зі, бо, зараз, один, щодо, навіть, лише, тепер, нічого, сьогодні, багато, немає, між, завжди, добре.

`chalis/discriminators.md` lists the strongest Ukrainian markers absent from the Russian top-10k: *що, це, як, від, але, він, його, ви, ще, які, під, вже, коли, якщо, або, року, було, вони, із, мене, щоб, мені, чи, який*. (*ви* and *мене* are listed because the Russian forms are *вы* and *меня*.)

Corpus note: the frequency list also contains *и* (rank ~89) and *что* (rank ~290), which reflect quotations, Russian-language material and surzhyk in web text; do not treat a single Russian word as proof against Ukrainian.

## Frequent Character N-grams

From the 12 UD passages (about 2,700 words; indicative only):

- Most frequent letters: о, а, и, н, і, т, в, р, е, с. Note **е** is far less frequent than in Russian (Ukrainian often has и or і where Russian has е/и), and **і** is in the top five.
- Frequent bigrams: **ти, на, ро, ст, по, ат, ва, ко, ор, ов, го, та, ві, ог, ви**.
- Characteristic sequences: **ння** (*питання, рішення*), **ій/ої/ою** (adjective endings), **ів** (gen. pl.), **ськ/цьк** (*український, німецький*), **ться/ється**, **ць** (*-ець* nouns such as *українець*, gen. pl. *місць*, *-цьк-*), **ии** essentially absent; **ії** (*історії, Росії, комісії*) frequent where Russian has **ии** (*истории*).

## Morphological Endings Useful for LID

### Verbs
- Infinitive **-ти/-тися** (*робити, сподобатися*); Russian **-ть/-ться**.
- 3sg **-є/-ить**, 3pl **-ють/-ять/-уть**, 1pl **-мо** (*маємо, робимо, будемо*). In the UD sample -ть endings (3sg/3pl -ить, -ють, -ять) are frequent, and **-ться** also occurs (*займається, робиться*), so -ться alone does not distinguish from Russian.
- Past masc. **-в** (*був, сказав, став*), fem. **-ла**.
- Synthetic future **-тиму/-тимеш/-тиме**.

### Nouns
- Verbal/abstract nouns **-ння/-ття** (*питання, рішення, життя, значення*).
- **-ість** abstract nouns (*кількість, діяльність*), Russian **-ость**.
- Gen. pl. **-ів/-їв**; dat./loc. masc. **-ові/-еві**; instr. fem. **-ою**.
- Agentive **-ець** (*українець*), diminutive **-ик, -чик**.

### Adjectives and pronouns
- **-ий, -ій; -а; -е; -і; -ого, -ому; -ої, -ій, -ою; -их, -им, -ими**.
- **-ський/-цький** with ь (*український, німецький*); Russian **-ский/-цкий** without ь.
- Pronoun forms *цей/ця/це/ці*, *його/її/їх*.

## Orthographic Variation

- A minority tradition (*kharkivskyi pravopys*, diaspora usage) and the 2019 orthography introduced variants (e.g. *проєкт* vs. older *проект*). These do not affect identification.
- Surzhyk (Russian-Ukrainian mixed speech) occurs in informal text; it typically still shows і/ї/є alongside Russian lexemes.
