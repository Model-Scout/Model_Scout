---
dataset_info:
  features:
  - name: neg
    sequence: string
  - name: pos_scores
    sequence: int64
  - name: neg_scores
    sequence: int64
  - name: pos
    sequence: string
  - name: query
    dtype: string
  splits:
  - name: train
    num_bytes: 681314029
    num_examples: 13348
  download_size: 96204831
  dataset_size: 681314029
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
---