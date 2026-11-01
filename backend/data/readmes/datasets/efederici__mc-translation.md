---
language:
- en
- sw
- es
- de
- zh
- bn
- it
- hi
- ja
- ko
- pt
- ar
- id
license: mit
size_categories:
- 100K<n<1M
task_categories:
- translation
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: output
    dtype: string
  - name: in_lang
    dtype: string
  - name: out_lang
    dtype: string
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  splits:
  - name: train
    num_bytes: 722699027
    num_examples: 209115
  download_size: 349500393
  dataset_size: 722699027
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
tags:
- multiple-choice
- eval
---

This dataset contains professional human translations from OpenAI's MMMLU dataset, repurposed to train translation models that can help translate future evaluation datasets.

## Why This Dataset?

Translation of evaluation benchmarks is a critical but challenging task. While automated translations may introduce errors or biases, professional human translations are expensive and time-consuming. This dataset leverages existing professional translations (MMMLU) to train specialized translation models that can assist in translating future evaluation sets.