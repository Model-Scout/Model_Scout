---
dataset_info:
  features:
  - name: domain
    dtype: string
  - name: subdomain
    dtype: string
  - name: style
    dtype: string
  - name: target
    dtype: string
  - name: source
    dtype: string
  - name: target_text
    dtype: string
  - name: source_text
    dtype: string
  - name: len
    dtype: int64
  splits:
  - name: train
    num_bytes: 491938775.5883989
    num_examples: 1189572
  download_size: 245141914
  dataset_size: 491938775.5883989
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

Aihub 번역 통합데이터셋[(nayohan/aihub-en-ko-translation-12m)](https://huggingface.co/datasets/nayohan/aihub-en-ko-translation-12m)의 10% 샘플링  / 1,189,572개