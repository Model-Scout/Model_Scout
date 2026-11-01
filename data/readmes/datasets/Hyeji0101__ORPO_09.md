---
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: id
    dtype: string
  - name: chunk_id
    dtype: int64
  - name: domain
    dtype: string
  - name: source_chunk
    dtype: string
  splits:
  - name: train
    num_bytes: 189634858
    num_examples: 198400
  download_size: 66220031
  dataset_size: 189634858
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
---
