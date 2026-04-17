# Mandarin (Simplified) LID characteristics

## Script signals

- CJK Unified Ideographs (U+4E00–U+9FFF) with **Simplified** forms. Strong positive simplified markers: 的 了 是 在 和 我 你 他 这 那 们 为 会 个 说 对 还 里 从 国 学 发 关 来 过 东 车.
- Absence of Traditional variants: 個 萬 實 國 會 發 關 學 東 車 對 來 過. If any of those appear in bulk, the text is likely `zho_Hant`/`yue_Hant`.
- Full-width punctuation: 。 ， 、 ； ： 「」 （） ！ ？. No spaces between words.

## Top function words

的, 了, 是, 在, 我, 你, 他, 她, 们, 这, 那, 有, 不, 和, 也, 就, 都, 要, 会, 能, 把, 被, 跟, 给, 从, 到, 对, 为, 因为, 所以, 但是, 如果, 可以, 一个, 什么, 怎么, 没有, 自己.

## N-gram / spelling patterns

- Bigrams: `的+名词`, `了+。/，`, `在+地点`, `是+名词`, `不+动词`, `我们`, `他们`, `什么`, `一个`.
- Character 了 after a verb followed by 。 or ， is a near-certain Chinese signal.
- Four-character chengyu (成语) idioms appear frequently; reduplications like 很多很多, 高高兴兴.
- Arabic numerals often mixed with 年/月/日/元/个: `2024年`, `15元`, `3个人`.

## Morphology hooks

- 的 / 地 / 得 distinction (attributive / adverbial / complement).
- Plural 们 only on animate pronouns/nouns.
- Aspect clitics 了 过 着 immediately after the verb.
- Classifier insertion: `Num + CL + N`.

## Punctuation / orthography quirks

- Full-width comma `，` differs from enumeration comma `、`.
- Quotation marks 「」『』 (Taiwan-style) vs “” (PRC publications); both occur.
- Ellipsis is rendered as `……` (six dots, two characters wide).
- Titles often wrapped in 《》 book-title marks.
