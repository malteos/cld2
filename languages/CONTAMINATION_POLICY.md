# Contamination policy (train–test leakage)

## Why this exists

This knowledge base is intended to support in-context typological language
identification. The **evaluation set** for that task is
[CommonLID](https://huggingface.co/datasets/commoncrawl/CommonLID). If any
CommonLID-annotated text ends up in the `examples/` or `vocabulary.json`
that a model sees during prompting, we get train–test leakage: the model
has effectively been trained on its own test set.

This is a hard constraint. No exceptions.

## What is banned

The following sources must **never** supply text that appears in any file
inside `languages/<code>_<Script>/` other than purely descriptive prose
that the project author wrote themselves:

| Source | Reason |
|--------|--------|
| `commoncrawl/CommonLID` (TSV, HF) | Our own evaluation set. Direct leakage. |
| `openlanguagedata/flores_plus` | Widely used LID/MT benchmark. |
| `allenai/MADLAD-400` | CommonLID's parent pool; direct upstream of CommonLID. |
| `Helsinki-NLP/opus-100` | Standard MT benchmark. |
| WMT test sets (any year) | Standard MT benchmark. |
| `tatoeba` (community set) | Often used as LID benchmark, volatile provenance. |
| Any dataset explicitly labelled "eval" / "test" / "benchmark" | Same reasoning. |

## What is allowed

Real-world websites in the target language:

- **Wikipedia** via the `wikimedia/wikipedia` HuggingFace dump or directly.
  Each article carries provenance (title + URL) in the saved example file.
- **Government / state websites** (e.g. gov.br, bundesregierung.de).
- **News publishers** in the target language (e.g. Al Jazeera, BBC, RTHK,
  Yle, DW, Xinhua, regional papers).
- **Cultural / encyclopaedic institutions** (academies, literature portals).
- **Civil-society translations**: UN, UNHCR, UNESCO, Red Cross, UDHR.
- **Religious publications translated into rare languages** (jw.org for
  many creoles and low-resource African languages; Bible Gateway, Vatican
  Latin archives, Sefaria for Biblical Hebrew, etc.).

Per-language curated URLs live in `scripts/sources_catalog.py`.

## How the policy is enforced

- `scripts/fetch_web_examples.py` and `scripts/fetch_web_vocabulary.py`
  are the only supported paths for refreshing examples and vocabulary.
  They pull from Wikipedia (via HF) and the curated URL catalogue —
  never from the banned list.
- Every example file carries a `# Source: <URL> (<description>)` header
  so provenance can be audited at a glance.
- `sources_manifest.json` is regenerated on every fetch and records the
  URLs whose content contributed to each language.
- `scripts/check_contamination.py` compares every `examples/*.txt` line
  and every `vocabulary.json` source attribution against the CommonLID
  TSV and FLORES+. Any exact-line match, 80-character substring match,
  or banned source-attribution is flagged. CI should fail if the script
  exits non-zero.

## Refresh workflow

```bash
source .venv/bin/activate
python languages/scripts/fetch_web_examples.py --all           # wipe + re-source
python languages/scripts/fetch_web_vocabulary.py --all         # rebuild vocab
python languages/scripts/check_contamination.py                # PROVE no leakage
python languages/scripts/build_progress.py                     # refresh tracker
```

Never bypass the contamination check. If it finds a hit, the fix is to
delete the hit and re-source that language from a different URL in the
catalogue — not to silence the checker.

## Contact / policy owner

This policy is authoritative for anything under `languages/`. When
adding a new source URL to `scripts/sources_catalog.py`, verify that:

1. The URL is publicly reachable and serves text in the target language.
2. The URL is **not** part of any known LID or MT benchmark.
3. The site's terms of use permit non-commercial research use.
4. The content carries clear provenance (publisher name, article title,
   or timestamp).
