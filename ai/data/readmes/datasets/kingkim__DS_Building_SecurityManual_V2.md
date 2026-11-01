---
language:
- ko
dataset_info:
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 53319
    num_examples: 300
  download_size: 6765
  dataset_size: 53319
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
