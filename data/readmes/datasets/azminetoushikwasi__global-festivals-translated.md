---
dataset_info:
  features:
  - name: title
    dtype: string
  - name: country
    dtype: string
  - name: language
    dtype: string
  - name: description
    dtype: string
  splits:
  - name: train
    num_bytes: 822473
    num_examples: 1800
  download_size: 465100
  dataset_size: 822473
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
task_categories:
- text-generation
language:
- en
- fr
- es
- de
- hi
- ja
- ko
- tr
- it
tags:
- GLOBAL_FESTIVALS_DATASET = 'ciol-research/global-festivals-wiki'
pretty_name: A multilingual festival description dataset
size_categories:
- 10K<n<100K
---