---
dataset_info:
- config_name: '20240701'
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1225610764
    num_examples: 705657
  download_size: 640456155
  dataset_size: 1225610764
- config_name: 20240701-filtered
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 600434338.1436992
    num_examples: 312455
  download_size: 373845314
  dataset_size: 600434338.1436992
configs:
- config_name: '20240701'
  data_files:
  - split: train
    path: 20240701/train-*
- config_name: 20240701-filtered
  data_files:
  - split: train
    path: 20240701-filtered/train-*
license: cc-by-sa-4.0
task_categories:
- text-generation
language:
- ko
size_categories:
- 100K<n<1M
---