---
dataset_info:
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: content_en
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 65371495
    num_examples: 1000
  download_size: 30003204
  dataset_size: 65371495
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
task_categories:
- text-generation
- text2text-generation
language:
- ko
- en
pretty_name: s1K 1.1 Korean
---

https://huggingface.co/datasets/simplescaling/s1K-1.1