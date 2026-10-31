---
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: uuid
    dtype: string
  - name: language
    dtype: string
  - name: site
    dtype: string
  - name: url
    dtype: string
  - name: mhtml
    dtype: string
  splits:
  - name: train
    num_bytes: 84012036587
    num_examples: 29081
  download_size: 63542382099
  dataset_size: 84012036587
language:
- en
- es
- ru
- ar
- fr
- pt
- hr
- zh
- de
- ko
tags:
- web
- multilingual
- extraction
- news
size_categories:
- 10K<n<100K
---

# MHTML Sources for [NewsXLM dataset](https://huggingface.co/datasets/ispras-crawlers/newsxlm)

**Columns Explanation**

`mhtml`: MHTML snapshots of pages where `wtl-uid` and `wtl-parent-uid` attributes have been added to every element in \<body\>, following the [WTL algorithm](https://github.com/klarna-incubator/webtraversallibrary/blob/master/webtraversallibrary/js/get_element_metadata.js).