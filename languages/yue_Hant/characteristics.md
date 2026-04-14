# Cantonese LID characteristics

## Script signals

- **Traditional Han**: 國 個 會 來 為 萬 實 學 發 東 車 對 過 書 電 門 關. Any Simplified variant (国 个 会 来) in a yue text is unusual.
- **Cantonese-only characters** — strong positive signals: 嘅 係 咗 喺 嚟 佢 冇 啲 乜 嘢 睇 識 唔 畀 噉 咁 嚿 氹. Seeing even one or two of 嘅/係/咗/喺/佢 in a CJK document moves the posterior strongly toward `yue_Hant`.
- Sentence-final particle stack: 啦 喇 咩 呀 喎 囉 嘅 吖 嘛. Multiple particles clustering sentence-finally (e.g. 嘅啫, 嘅喇, 咗啦) are distinctively Cantonese.

## Top function words

嘅, 係, 咗, 喺, 嚟, 佢, 冇, 啲, 乜, 嘢, 唔, 畀, 我, 你, 佢哋, 我哋, 你哋, 噉, 咁, 過, 呢, 嗰, 同, 都, 會, 可以, 要, 想, 啦, 喇, 咩, 呀, 喎, 囉, 嘛.

## N-gram / spelling patterns

- 係 as copula rather than 是.
- 唔 + verb for negation (唔係, 唔去, 唔得).
- 咗 immediately after a verb marks perfective (食咗, 去咗).
- 喺度 / 喺香港 — 喺 as locative 'at'.
- Demonstratives 呢 (this) and 嗰 (that) instead of 這/那.
- Possessive/relative 嘅 replaces 的.

## Morphology hooks

- Post-verbal aspect clitics 咗 / 緊 / 住 / 過 / 晒 / 返.
- Plural pronominal suffix 哋 (我哋, 你哋, 佢哋) — unique to Cantonese writing.
- Classifier-as-definite: bare `CL + N` without demonstrative reads as definite.

## Punctuation / orthography quirks

- Hong Kong convention favours 「…」『…』 quotation marks.
- Titles in 《》; chapter titles in 〈〉.
- Full-width punctuation throughout; no inter-word spaces.
