---
dataset_info:
  features:
  - name: 법령명
    dtype: string
  - name: 법령ID
    dtype: string
  - name: 헤더
    dtype: string
  - name: 법령본문
    dtype: string
  splits:
  - name: train
    num_bytes: 237143097
    num_examples: 5502
  download_size: 83744003
  dataset_size: 237143097
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-4.0
language:
- ko
tags:
- laws
---

2025년 08월 기준으로 open.law.go.kr 에서 수집한 한국 법령 데이터셋입니다.
