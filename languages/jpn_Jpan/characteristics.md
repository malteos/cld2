# Japanese LID characteristics

## Script signals

- **Hiragana block** (U+3040–U+309F): の は を が に で と も へ や か ね よ な の です ます した して くる いる ある. Presence of any Hiragana is a near-certain Japanese signal.
- **Katakana block** (U+30A0–U+30FF): コンピュータ, アメリカ, サービス, データ, インターネット. Foreign loanwords in Katakana are extremely common in modern Japanese.
- **Kanji** shared with Chinese (CJK Unified Ideographs) — but in Japanese they co-occur with kana within the same sentence.
- **Halfwidth/fullwidth mix**: full-width ASCII (ＡＢＣ), full-width digits (１２３), and Western Latin coexist.

## Top function words

の, は, を, が, に, で, と, も, へ, から, まで, や, か, ね, よ, です, だ, ます, した, して, いる, ある, ない, ない, この, その, あの, どの, これ, それ, あれ, どれ, こと, もの, よう, ため, そして, しかし, でも, また.

## N-gram / spelling patterns

- Particle-plus-punctuation bigrams: `は、` `を、` `に、` `で、` `です。` `ます。`.
- Sentence-final `です。` / `ます。` / `でした。` is an overwhelmingly strong Japanese signal.
- Kanji followed immediately by a hiragana inflection (e.g. 食べる, 行った, 見ている) — Chinese never shows this pattern.
- Katakana sequences of length ≥3 with the prolongation mark ー (e.g. コンピューター, サーバー).

## Morphology hooks

- Verb stem + hiragana tail: 書く, 書いた, 書かない, 書きます.
- Adjective 〜い inflection: 高い → 高くない → 高かった.
- Copula だ / です / でした.
- Honorific prefix お〜 / ご〜 (お茶, ご家族).

## Punctuation / orthography quirks

- Sentence stop `。` (full-width circle, not a dot).
- Comma `、` (ten) — shape is different from Chinese `，`.
- Quotation `「」` and `『』`.
- Katakana middle dot `・` separating compound foreign names: ジョン・スミス.
- Prolongation mark `ー` in Katakana loanwords — does not occur in Chinese.
