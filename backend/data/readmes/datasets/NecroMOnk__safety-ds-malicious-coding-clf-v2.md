---
license: mit
pretty_name: Multilingual Malicious Coding Intent Dataset
language:
  - en
  - zh
  - hi
  - es
  - ar
  - bn
  - pt
  - ru
  - ja
  - de
  - fr
  - tr
  - ko
  - vi
  - it
  - id
  - pl
multilinguality:
  - multilingual
annotations_creators:
  - machine-generated
language_creators:
  - machine-generated
source_datasets:
  - original
size_categories:
  - 100K<n<1M
task_categories:
  - text-classification
tags:
  - safety
  - malware
  - code
  - multilingual
  - text
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train.parquet
      - split: validation
        path: data/val.parquet
      - split: test
        path: data/test.parquet
      - split: obfuscated
        path: data/test_obfuscated.parquet
      - split: malware_code
        path: data/test_malware_code.parquet
dataset_info:
  - config_name: default
    description: >
      Multilingual malicious-coding-intent dataset (lexicon positives, template + HF benign
      negatives). Hold-out splits for obfuscated lexicon and real malware code. Targets
      code/prompt safety classifiers (e.g. BGE-m3 + logistic heads). Total rows: 235171.
    features:
      - name: text
        dtype: string
      - name: malicious
        dtype: int64
      - name: categories
        sequence: string
      - name: source
        dtype: string
    splits:
      - name: train
        num_bytes: 12746862
        num_examples: 181436
      - name: validation
        num_bytes: 1612098
        num_examples: 22751
      - name: test
        num_bytes: 1589994
        num_examples: 22984
      - name: obfuscated
        num_bytes: 75876
        num_examples: 4000
      - name: malware_code
        num_bytes: 1845458
        num_examples: 4000
    download_size: 17870288
    dataset_size: 17870288
---

# Multilingual Malicious Coding Intent Dataset

Multilingual **malicious coding intent** dataset (Safety DS v2) for training/evaluating binary + multilabel classifiers.

## Splits (parquet)

| File | Rows | Role |
|------|------|------|
| `data/train.parquet` | 181436 | train |
| `data/val.parquet` | 22751 | validation |
| `data/test.parquet` | 22984 | in-distribution test |
| `data/test_obfuscated.parquet` | 4000 | hold-out (obfuscated lexicon) |
| `data/test_malware_code.parquet` | 4000 | hold-out (malware code pool) |

## Schema

- `text` — code or prompt snippet
- `malicious` — `0` benign, `1` malicious
- `categories` — list of harm category ids (multilabel; empty list if benign)
- `source` — provenance (e.g. `lexicon_multilingual`, `template_negative`, `hf:…`)

See `labels.json` and `dataset_report.json`.

## Build

- Variant: `v2_multilingual`
- `hf_in_train`: `neg-only` — HF benign negatives in train; HF positives for benchmark only.

## Dataset Viewer

The Hub shows a **paginated preview** (not a full in-browser scan of all 235,171 rows). Use `load_dataset` for full access. Hold-out `malware_code` rows can be large (~12k chars); statistics may be partial on heavy splits.
