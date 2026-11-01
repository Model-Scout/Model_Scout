---
license: apache-2.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: kor_sent
    dtype: string
  - name: eng_sent
    dtype: string
  - name: source
    dtype: string
  - name: similarity
    dtype: float64
  - name: from
    dtype: string
  - name: __index_level_0__
    dtype: float64
  splits:
  - name: train
    num_bytes: 784539402
    num_examples: 3332436
  download_size: 374217193
  dataset_size: 784539402
task_categories:
- translation
language:
- en
- ko
pretty_name: loki
size_categories:
- 1M<n<10M
---