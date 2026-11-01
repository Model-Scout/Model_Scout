---
dataset_info:
  features:
  - name: judgment_chunk
    dtype: string
  - name: legal_term
    dtype: string
  - name: transform
    dtype: string
  - name: summary
    dtype: string
  splits:
  - name: train
    num_bytes: 1577917385
    num_examples: 501333
  download_size: 646399552
  dataset_size: 1577917385
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
task_categories:
- summarization
language:
- ko
tags:
- legal
size_categories:
- 100K<n<1M
---