---
language:
- ko
dataset_info:
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 233402
    num_examples: 250
  download_size: 99916
  dataset_size: 233402
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
