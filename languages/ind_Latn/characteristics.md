# Indonesian LID characteristics

## Script signals

Plain 26-letter Latin with no diacritics. The presence of *hyphenated
reduplication* (`anak-anak`, `pelan-pelan`, `tiba-tiba`, `orang-orang`) is a
strong positive signal for Indonesian/Malay against other Latin-script
languages. The digraphs `ny`, `ng`, `kh`, `sy` are common; `x`, `q` occur
mainly in loanwords; the letter `f` is rare in native words but frequent in
Arabic and European loans.

## Top function words

`yang`, `dan`, `di`, `ke`, `dari`, `untuk`, `pada`, `dengan`, `dalam`,
`akan`, `sudah`, `belum`, `tidak`, `bukan`, `ini`, `itu`, `adalah`, `ada`,
`tetapi`, `atau`, `juga`, `saja`, `saya`, `kamu`, `dia`, `mereka`, `kita`,
`kami`, `oleh`, `hanya`, `bisa`, `karena`, `sebagai`.

## N-gram / spelling patterns

- `yang` is one of the highest-frequency tokens in any Indonesian text.
- `-nya` clitic (3SG possessive / definitising) appears word-finally very
  often: `rumahnya`, `ibunya`, `katanya`.
- `-kan` and `-i` verb suffixes: `memberikan`, `mendekati`.
- `meN-` prefix surfaces as `mem-`, `men-`, `meng-`, `meny-`, `me-`
  depending on stem initial: `membaca`, `menulis`, `mengambil`, `menyapu`.
- `ber-` reciprocal/stative verbs: `berjalan`, `bermain`, `berbicara`.
- `peN-...-an` nominalisation: `pendidikan`, `pengembangan`, `penelitian`.
- Reduplication with hyphen is a very high-precision n-gram.

## Morphology hooks

Detect the full derivational frame `{me|di|ber|ter|pe|se|ke}` + stem +
`{kan|i|an|nya}`. Circumfix `ke-...-an` nominalises abstract qualities
(`keadilan`, `kemerdekaan`, `kesehatan`). The bound pronouns `-ku`, `-mu`,
`-nya` form a compact closed set.

## Punctuation / orthography quirks

Standard ASCII punctuation. Currency is `Rp` (rupiah) before digits with
`.` as thousands separator (`Rp 200.000`). Dates often `DD MMMM YYYY` with
Indonesian month names (`Januari … Desember`).
