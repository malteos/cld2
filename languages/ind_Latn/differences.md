# Indonesian vs confusable languages

Indonesian sits in the CLD2 confusable group **Indonesian / Malay
(msa, zsm)**. Short web snippets are frequently ambiguous; use lexical
evidence rather than orthography.

## vs Malaysian Malay (msa, zsm)

- **Lexical swaps**: Indonesian `mau` / Malay `mahu`; `karena` / `kerana`;
  `anggota` / `ahli`; `bisa` / `boleh`; `mobil` (ID) vs `kereta` (MY, a car)
  — in Malaysia `kereta api` or `keretapi` means train, in Indonesia
  `kereta` alone usually means train and `mobil` means car.
- **Dutch-era vocabulary is Indonesian-specific**: `apotek`, `kantor`,
  `bioskop`, `polisi`, `gratis`, `kamar`, `universitas`, `kualitas` vs
  Malay `farmasi`, `pejabat`, `pawagam`, `polis`, `percuma`, `bilik`,
  `universiti`, `kualiti`.
- **Function words**: `adalah` / `ialah` copula split — Indonesian strongly
  prefers `adalah`, Malay strongly prefers `ialah` for equative clauses.
- **Safest single-word tells**: `kerana`, `mahu`, `ahli`, `ialah`, `boleh`,
  `iaitu` → Malay; `karena`, `mau`, `anggota`, `bisa`, `kantor`, `yaitu`
  → Indonesian.

## vs Javanese (jav) and Sundanese

Javanese/Sundanese web text regularly borrows Indonesian; detection should
demand native Javanese markers (`mboten`, `sampeyan`, `ingkang`, `kulo`) or
Sundanese markers (`abdi`, `urang`, `teu`, `aya`) — without these, default
to Indonesian. Short snippets under ~40 characters are often irresolvable.
