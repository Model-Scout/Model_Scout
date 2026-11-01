---
language:
- ko
tags:
- finance
pretty_name: FinMarketReport-Retrieval-ko
size_categories:
- 1K<n<10K
license: cc-by-nc-sa-4.0
configs:
- config_name: corpus
  data_files:
  - split: train
    path: corpus/train-*
- config_name: default
  data_files:
  - split: train
    path: data/train-*
- config_name: queries
  data_files:
  - split: train
    path: queries/train-*
dataset_info:
- config_name: corpus
  features:
  - name: _id
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 252643
    num_examples: 1000
  download_size: 146259
  dataset_size: 252643
- config_name: default
  features:
  - name: query-id
    dtype: int64
  - name: corpus-id
    dtype: int64
  - name: score
    dtype: int64
  splits:
  - name: train
    num_bytes: 24000
    num_examples: 1000
  download_size: 12104
  dataset_size: 24000
- config_name: queries
  features:
  - name: _id
    dtype: int64
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 61857
    num_examples: 1000
  download_size: 32536
  dataset_size: 61857
---

## FinMarketReport-Retrieval-ko
- Constructed a **Retrieval** dataset based on the [**Bank of Korea Financial Dictionary**](https://www.bok.or.kr/portal/ecEdu/ecWordDicary/search.do?menuNo=200688).
