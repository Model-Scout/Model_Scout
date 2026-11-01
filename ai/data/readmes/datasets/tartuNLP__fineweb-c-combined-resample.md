---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: text
    dtype: string
  - name: label
    dtype: int64
  - name: label_name
    dtype: string
  - name: probs
    list: float64
  - name: n_tokens
    dtype: int64
  - name: language_code
    dtype: string
  - name: source
    dtype: string
  - name: original_annotation
    list: string
  splits:
  - name: train
    num_bytes: 162689350.0
    num_examples: 44547
  - name: dev
    num_bytes: 8070748.0
    num_examples: 2213
  download_size: 97958929
  dataset_size: 170760098.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: dev
    path: data/dev-*
---
