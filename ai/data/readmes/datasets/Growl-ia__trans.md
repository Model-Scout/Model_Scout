---
pretty_name: Growl-ia Trans
license: other
task_categories:
- translation
tags:
- machine-translation
- multilingual
- quality-estimation
- cometkiwi
- synthetic-translation
language:
- ar
- de
- en
- es
- fr
- hi
- it
- ja
- ko
- pt
- ru
- th
- vi
- zh
---

# Growl-ia/trans

`Growl-ia/trans` is a multilingual translation dataset package that contains model-generated bilingual sentence pairs and COMETKiwi quality scores.

The repository currently includes:

- `2601724` scored examples across all released model variants
- `182` language pairs
- OPUS-derived source corpora: `OpenSubtitles, TED2020, GlobalVoices, News-Commentary, WikiMatrix`
- Language coverage: `ar, de, en, es, fr, hi, it, ja, ko, pt, ru, th, vi, zh`

## What Is Inside

Each model release contains two CSV files directly under `MODEL/`:

- `train-scored.csv`: sentence-level bilingual data with COMETKiwi scores
- `threshold.csv`: pair-level score quantiles for threshold-based filtering

The currently published threshold files are provided for: `hunyuan, madlad, nllb`.

- huanyuan：tencent/Hunyuan-MT-7B
- madlad：google/madlad400-3b-mt
- nllb：facebook/nllb-200-3.3B

## Repository Layout

```text
.
|-- README.md
|-- metadata
|   |-- dataset_summary.csv
|   `-- file_manifest.json
|-- hunyuan
|   |-- threshold.csv
|   `-- train-scored.csv
|-- madlad
|   |-- threshold.csv
|   `-- train-scored.csv
`-- nllb
    |-- threshold.csv
    `-- train-scored.csv
```

## Model-Level Summary

| Model | Source Subset | Rows | Pairs | Corpora | Kiwi Mean | Kiwi P95 | Scored CSV (MB) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| hunyuan | kiwi | 841284 | 182 | 5 | 0.7899 | 0.8881 | 187.78 |
| madlad | kiwi | 880223 | 182 | 6 | 0.7406 | 0.8842 | 191.88 |
| nllb | kiwi | 880217 | 182 | 5 | 0.7390 | 0.8840 | 191.67 |

## Threshold Summary

| Model | Source Subset | Rows | Percentile Columns | Min Samples | Max Samples | Threshold CSV (MB) |
| --- | --- | --- | --- | --- | --- | --- |
| hunyuan | kiwi | 182 | p5, p10, p15, p20, p25, p30, p40, p50, p60, p70, p80, p95 | 4138 | 4859 | 0.02 |
| madlad | kiwi | 182 | p5, p10, p15, p20, p25, p30, p40, p50, p55, p60, p65, p70, p75, p80, p95 | 4797 | 4864 | 0.02 |
| nllb | kiwi | 182 | p5, p10, p15, p20, p25, p30, p40, p50, p55, p60, p65, p70, p75, p80, p95 | 4797 | 4864 | 0.02 |

## Data Fields

### `train-scored.csv`

- `pair`: language pair in `src-tgt` format, for example `ru-zh`
- `corpus`: upstream OPUS corpus name, such as `OpenSubtitles` or `TED2020`
- `src`: cleaned source sentence
- `tgt`: model-generated target sentence
- `src_lang`: normalized source language code
- `tgt_lang`: normalized target language code
- `kiwi`: sentence-level COMETKiwi score from `models/wmt22-cometkiwi-da`

### `threshold.csv`

- `pair`: language pair
- `pXX`: pair-specific score percentile, for example `p50`, `p80`, `p95`
- `samples`: number of scored examples used to compute the percentile table

## Construction Pipeline

1. Download parallel data from OPUS, including `OpenSubtitles`, `TED2020`, `GlobalVoices`, `News-Commentary`, and `WikiMatrix`.
2. Sample sentence pairs from the compressed corpora with language-aware member matching, prefix filtering, script-consistency checks, and corpus-specific fallback rules.
3. Clean the sampled data with local filtering rules, including URL and noise removal, length-ratio checks, character cleanliness, FastText language identification, and global deduplication.
4. Use the cleaned `src` sentences as prompts for MT generation with `hunyuan-mt`, `madlad`, and `nllb`.
5. Score each generated pair with `models/wmt22-cometkiwi-da` to produce the final `kiwi` column.
6. Compute pair-level quantile thresholds and export them to `threshold.csv` for downstream filtering.

## Recommended Filtering

Use `threshold.csv` when you need a high-confidence subset.

Example policy:

- Use `p50` for a balanced training subset
- Use `p80` for stricter semantic alignment
- Use `p95` for the highest-confidence slice

Example in Python:

```python
import pandas as pd

train_df = pd.read_csv("nllb/train-scored.csv")
threshold_df = pd.read_csv("nllb/threshold.csv")

target_pair = "ru-zh"
cutoff = float(threshold_df.loc[threshold_df["pair"] == target_pair, "p80"].iloc[0])
high_conf_df = train_df[(train_df["pair"] == target_pair) & (train_df["kiwi"] >= cutoff)]
```

## Metadata Files

- `metadata/dataset_summary.csv`: compact per-model statistics generated during upload
- `metadata/file_manifest.json`: file manifest and summary payload for reproducible packaging

## Caveats

- `tgt` is model-generated text rather than human reference translation.
- Scores are quality-estimation signals, not ground-truth human judgments.
- The repository aggregates data derived from multiple OPUS corpora, which may carry different original licenses or usage constraints.
- Some language pairs and corpora are noisier than others even after filtering; threshold-based subsetting is strongly recommended.

## Intended Uses

- Filtering synthetic translation data with score-based cutoffs
- Studying multilingual MT quality-estimation behavior
- Building curriculum or confidence-aware translation training sets
- Comparing generated parallel data from different MT systems

## Citation

If you use this dataset, please cite:

1. The original OPUS corpora used in your experiment
2. The MT systems used to generate `tgt`
3. COMETKiwi / `wmt22-cometkiwi-da` for sentence-level scoring

If a project-specific citation entry is added later, update this section accordingly.
