# Chinese macro vs. confusable languages

## zho (Hans) ↔ cmn (Hans) — macrocode overlap

- `zho` is the macrolanguage; `cmn` is the specific standard Mandarin variety. At the surface level in Simplified Han, the two rows are **effectively identical** in running text. Select `cmn` when Putonghua/Guoyu is explicit; `zho` when the variety is unknown or mixed. No robust sentence-level signal distinguishes them.

## zho (Hans) ↔ yue (Hant) — macro Simplified vs Cantonese Traditional

- Script differs: Simplified vs Traditional variants (国/國, 会/會, 来/來, 个/個).
- Cantonese-specific written morphemes 嘅 係 咗 喺 佢 冇 啲 乜 嚟 are absent from `zho_Hans`.
- Final particles 啦 喇 咩 呀 喎 cluster densely in Cantonese; `zho_Hans` uses 吗 吧 呢 啊.

## zho ↔ wuu — Mandarin-style vs Wu Chinese

- Both use Simplified script. Wu inserts topolect forms 勿 搿 儂 格 垃 伊 阿拉; standard written Chinese (`zho`) does not.
- Wu texts often keep topic-comment syntax overtly and use 垃/拉 locatives where `zho` uses 在.

## zho ↔ jpn — Chinese vs Japanese

- Any Hiragana (の は を が に) or Katakana character instantly disambiguates to Japanese. Pure-Han sequences are ambiguous but short; any kana or mixed script settles the call.

## zho ↔ kor — Chinese vs Korean

- Modern Korean text is almost entirely Hangul syllables (U+AC00–U+D7AF). Presence of Hangul is decisive. Han characters in modern Korean are rare and usually parenthesised.
