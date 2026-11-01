---
dataset_info:
  features:
  - name: key
    dtype: large_string
  - name: part
    dtype: large_string
  - name: book
    dtype: large_string
  - name: chapter
    dtype: int64
  - name: verse
    dtype: int64
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
    num_bytes: 3310586
    num_examples: 1081
  - name: validation
    num_bytes: 183513
    num_examples: 65
  download_size: 1880630
  dataset_size: 3494099
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
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
task_categories:
- translation
- sentence-similarity
tags:
- tokipona
- toki pona
- bible
- multilingual
pretty_name: Toki Pona Bible Dataset with Translations
size_categories:
- 1K<n<10K
---