---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: text
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          '0': '0'
          '1': '1'
  - name: id
    dtype: int64
  - name: ko_text
    dtype: string
  splits:
  - name: train
    num_bytes: 2964245922.375
    num_examples: 8197
  download_size: 2964114455
  dataset_size: 2964245922.375
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
- en
size_categories:
- 1K<n<10K
---