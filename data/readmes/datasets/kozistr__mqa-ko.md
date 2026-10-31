---
language:
- ko
dataset_info:
  features:
  - name: question
    dtype: string
  - name: context
    dtype: string
  splits:
  - name: train
    num_bytes: 448326390
    num_examples: 1141547
  download_size: 133294539
  dataset_size: 448326390
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
