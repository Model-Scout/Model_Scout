---
language:
- ko
license: apache-2.0
dataset_info:
  features:
  - name: id
    dtype: string
  - name: url
    dtype: string
  - name: title
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 21056059
    num_examples: 10000
  download_size: 11978196
  dataset_size: 21056059
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

[20240501 update](https://huggingface.co/datasets/lcw99/wikipedia-korean-20240501)