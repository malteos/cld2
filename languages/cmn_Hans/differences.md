# Mandarin vs. confusable languages

## cmn (Hans) ↔ zho (Hans) — macrocode overlap

- `zho` is the ISO-639-3 macrolanguage; `cmn` is the specific standard Mandarin variety. In CommonLID both rows ship as `_Hans` and in running text are effectively indistinguishable. Prefer `cmn` when the text is specifically Putonghua/Guoyu; `zho` when the source is tagged generically "Chinese".
- No reliable surface signal separates the two at sentence level.

## cmn (Hans) ↔ yue (Hant) — Mandarin vs Cantonese

- Character set differs: Simplified (国, 个, 来, 会) vs Traditional (國, 個, 來, 會).
- Cantonese-only lexicon: 嘅 (possessive/de), 係 (copula), 咗 (perfective), 喺 (at), 佢 (3sg), 冇 (not-have), 啲 (plural/some), 乜 (what), 嚟 (come).
- Final particles 啦 喇 咩 呀 喎 cluster in Cantonese; Mandarin uses 吗 吧 呢 啊.

## cmn ↔ wuu — Mandarin vs Wu Chinese

- Wu uses Simplified Han but inserts topolect characters: 勿 (not), 搿 (this), 儂 (you), 格 (de/possessive/linker), 阿拉 (we, Shanghainese), 伊 (3sg).
- Wu often preserves topic-comment syntax more visibly and uses 垃 / 拉 as locative/progressive markers where Mandarin uses 在.

## cmn ↔ jpn — Chinese vs Japanese

- Presence of Hiragana (の は を が に で と も) or Katakana (ア-ン range) instantly disambiguates to Japanese. Pure-Kanji short strings can be ambiguous; any kana settles it.
- Japanese uses 、 and 。 but also mixes Katakana loanwords heavily; Chinese does not.
