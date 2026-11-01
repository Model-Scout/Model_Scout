---
dataset_info:
  features:
  - name: source_text
    dtype: string
  - name: positive
    dtype: string
  - name: negative
    dtype: string
  splits:
  - name: train
    num_bytes: 36578283
    num_examples: 18750
  download_size: 12845627
  dataset_size: 36578283
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
