---
dataset_info:
  features:
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: source
    dtype: string
  - name: score
    dtype: float64
  splits:
  - name: train
    num_bytes: 258074273
    num_examples: 100000
  download_size: 116174234
  dataset_size: 258074273
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
