---
language:
- ko
tags:
- finance
pretty_name: TATQA-Retrieval-ko
license: cc-by-nc-sa-4.0
size_categories:
- 1K<n<10K
configs:
- config_name: corpus
  data_files:
  - split: train
    path: corpus/train-*
- config_name: default
  data_files:
  - split: train
    path: data/train-*
- config_name: queries
  data_files:
  - split: train
    path: queries/train-*
dataset_info:
- config_name: corpus
  features:
  - name: _id
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 568874
    num_examples: 1000
  download_size: 309056
  dataset_size: 568874
- config_name: default
  features:
  - name: query-id
    dtype: int64
  - name: corpus-id
    dtype: int64
  - name: score
    dtype: int64
  splits:
  - name: train
    num_bytes: 24000
    num_examples: 1000
  download_size: 12104
  dataset_size: 24000
- config_name: queries
  features:
  - name: _id
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 104654
    num_examples: 1000
  download_size: 46627
  dataset_size: 104654
---

## TATQA-Retrieval-ko
- Constructed a **TAT (Textual and Tabular) QA dataset** based on information collected from **Korean financial reports**.
