---
language:
- ko
tags:
- finance
license: cc-by-nc-sa-4.0
pretty_name: FSSFinDict-Retrieval-ko
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
    num_bytes: 233486
    num_examples: 1000
  download_size: 132396
  dataset_size: 233486
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
    num_bytes: 63042
    num_examples: 1000
  download_size: 32071
  dataset_size: 63042
---

## FSSFinDict-Retrieval-ko
- Constructed a **Retrieval** dataset based on the [financial dictionary](https://www.fsc.go.kr/in090301) provided by the Korean Financial Supervisory Service (FSS).
