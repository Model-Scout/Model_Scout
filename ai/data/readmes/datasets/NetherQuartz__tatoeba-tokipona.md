---
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: source_id
    dtype: int64
  - name: target_id
    dtype: int64
  - name: source
    dtype: large_string
  - name: source_lang
    dtype: large_string
  - name: tok
    dtype: large_string
  - name: en
    dtype: large_string
  - name: ru
    dtype: large_string
  - name: uk
    dtype: large_string
  - name: be
    dtype: large_string
  - name: fr
    dtype: large_string
  - name: es
    dtype: large_string
  - name: pt
    dtype: large_string
  - name: it
    dtype: large_string
  - name: de
    dtype: large_string
  - name: vi
    dtype: large_string
  - name: ja
    dtype: large_string
  - name: zh
    dtype: large_string
  - name: ko
    dtype: large_string
  - name: ar
    dtype: large_string
  - name: he
    dtype: large_string
  - name: pl
    dtype: large_string
  - name: tr
    dtype: large_string
  - name: la
    dtype: large_string
  - name: el
    dtype: large_string
  splits:
  - name: train
    num_bytes: 79706323.00236647
    num_examples: 74668
  - name: validation
    num_bytes: 4195181.997633528
    num_examples: 3930
  download_size: 49512467
  dataset_size: 83901505.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
task_categories:
- translation
language:
- tok
- en
- ru
- uk
- be
- fr
- es
- pt
- it
- de
- vi
- ja
- zh
- ko
- ar
- he
- pl
- tr
- la
- el
tags:
- tokipona
pretty_name: Tatoeba Toki Pona Dataset
size_categories:
- 10K<n<100K
license: cc-by-2.0
---
