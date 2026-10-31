---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: id
    dtype: string
  - name: dump
    dtype: string
  - name: url
    dtype: string
  - name: date
    dtype: string
  - name: file_path
    dtype: string
  - name: offset
    dtype: int64
  - name: token_count
    dtype: int64
  - name: language
    dtype: string
  - name: page_average_lid
    dtype: string
  - name: page_average_lid_score
    dtype: float64
  - name: full_doc_lid
    dtype: string
  - name: full_doc_lid_score
    dtype: float64
  - name: per_page_languages
    sequence: string
  - name: is_truncated
    dtype: bool
  - name: extractor
    dtype: string
  - name: page_ends
    sequence: int64
  splits:
  - name: train
    num_bytes: 43555926210
    num_examples: 1092545
  download_size: 19968133074
  dataset_size: 43555926210
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: odc-by
language:
- ko
---

데이터 확인을 편하게 하려고 [HuggingFaceFW/finepdfs](https://huggingface.co/datasets/HuggingFaceFW/finepdfs)에서 한국어 subset만 따로 분리했습니다.