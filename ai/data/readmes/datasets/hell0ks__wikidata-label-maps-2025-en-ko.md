---
dataset_info:
  features:
  - name: id
    dtype: large_string
  - name: en
    dtype: large_string
  - name: ko
    dtype: large_string
  splits:
  - name: train
    num_bytes: 123450903
    num_examples: 1676471
  download_size: 53074622
  dataset_size: 123450903
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc0-1.0
language:
- ko
- en
tags:
- wikidata
---

Subset of [en,ko] pair version of [yashkumaratri/wikidata-label-maps-2025-all-languages](https://huggingface.co/datasets/yashkumaratri/wikidata-label-maps-2025-all-languages)

Null entries are removed.