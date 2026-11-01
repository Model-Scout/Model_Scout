---
license: cc-by-nc-4.0
language:
- en
- nl
- et
- fi
- de
- el
- he
- it
- ko
- 'no'
- ru
- es
- tr
pretty_name: MECO character-level eye-tracking (preprocessed)
tags:
- eye-tracking
- reading-times
- psycholinguistics
- meco
---

# MECO character-level eye-tracking data

Preprocessed fixation data derived from the **MECO** (Multilingual Eye-tracking
Corpus) reading-time dataset, character-indexed.

## Contents

| Folder | Description |
|---|---|
| `processed/` | Flat per-language analysis files: `<lang>.csv` (one row per fixation across all readers/trials) and `stimulus_<lang>.csv` (per-character stimulus table). Consumed by [REPLICA](https://github.com/samuki/psycho-gym)'s `replica fetch meco_char`. |
| `meco_preproc/<lang>/` | Corrected per-(reader, text) fixation CSVs (linebreak/quote fixes applied). |
| `meco_preproc_raw/<lang>/` | Raw per-(reader, text) fixation CSVs before corrections. |
| `raw_texts/` | Extracted stimulus text per language (`raw_text_<lang>.csv`). |
| `visualizations/<lang>/` | PNG fixation visualizations for a sample of (reader, trial) pairs. |
| `meco_source/` | MECO source CSVs (`passage_data_version1.3.csv`, `sentences.csv`, `supp_texts.csv`). |

File naming for fixation CSVs: `<lang>/<lang>_<subject>_<trial>.csv`.

## Languages (13)

Dutch (du), Estonian (ee), English (en), Finnish (fi), German (ge), Greek (gr),
Hebrew (he), Italian (it), Korean (ko), Norwegian (no), Russian (ru),
Spanish (sp), Turkish (tr).

## Source

Derived from MECO (Siegelman et al., 2022, *Expanding horizons of
cross-linguistic research on reading*). Refer to the original MECO license and
terms for the underlying data.
