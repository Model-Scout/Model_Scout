---
language:
- ko
- en
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: language
    dtype: string
  - name: case_study_info
    dtype: string
  - name: prompt
    dtype: string
  - name: original_info
    dtype: string
  - name: stakeholder
    dtype: string
  - name: motivation
    dtype: string
  - name: model
    dtype: string
  - name: elapsed_time
    dtype: float64
  - name: endpoint
    dtype: string
  splits:
  - name: english
    num_bytes: 7428824
    num_examples: 891
  - name: chinese
    num_bytes: 5841513
    num_examples: 885
  - name: english_failed
    num_bytes: 427126
    num_examples: 152
  - name: chinese_failed
    num_bytes: 447124
    num_examples: 158
  download_size: 4810795
  dataset_size: 14144587
configs:
- config_name: default
  data_files:
  - split: english
    path: data/english-*
  - split: chinese
    path: data/chinese-*
  - split: english_failed
    path: data/english_failed-*
  - split: chinese_failed
    path: data/chinese_failed-*
---
