---
language:
- ko
dataset_info:
  features:
  - name: QUESTION
    dtype: string
  - name: ANSWER
    dtype: string
  splits:
  - name: train
    num_bytes: 92971
    num_examples: 447
  download_size: 42006
  dataset_size: 92971
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
