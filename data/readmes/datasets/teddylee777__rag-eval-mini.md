---
language:
- ko
license: mit
dataset_info:
  features:
  - name: contexts
    dtype: string
  - name: evolution_type
    dtype: string
  - name: metadata
    dtype: string
  - name: episode_done
    dtype: bool
  - name: question
    dtype: string
  - name: ground_truth
    dtype: string
  splits:
  - name: train
    num_bytes: 309562
    num_examples: 95
  - name: korean_v1
    num_bytes: 309562
    num_examples: 95
  download_size: 157278
  dataset_size: 619124
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: korean_v1
    path: data/korean_v1-*
---
