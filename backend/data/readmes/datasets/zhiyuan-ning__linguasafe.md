---
dataset_info:
  features:
  - name: id
    dtype: float64
  - name: lang
    dtype: string
  - name: level
    dtype: int64
  - name: prompt
    dtype: string
  - name: source
    struct:
    - name: content
      dtype: string
    - name: dataset
      dtype: string
  - name: specific
    dtype: bool
  - name: subtype
    dtype: string
  - name: type
    dtype: string
  splits:
  - name: train
    num_bytes: 17016498
    num_examples: 45705
  download_size: 7088059
  dataset_size: 17016498
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-nc-sa-4.0
language:
- ar
- bn
- en
- zh
- cs
- ru
- ko
- th
- ms
- sr
- hu
- vi
tags:
- not-for-all-audiences
size_categories:
- 10K<n<100K
---