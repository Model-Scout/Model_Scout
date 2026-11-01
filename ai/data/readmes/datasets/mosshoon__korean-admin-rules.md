---
dataset_info:
  features:
  - name: 행정규칙명
    dtype: string
  - name: 행정규칙ID
    dtype: string
  - name: 헤더
    dtype: string
  - name: 행정규칙본문
    dtype: string
  splits:
  - name: train
    num_bytes: 967017297
    num_examples: 23413
  download_size: 275259520
  dataset_size: 967017297
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-4.0
language:
- ko
---

2025년 08월 기준으로 open.law.go.kr 에서 수집한 행정법령규칙 데이터셋입니다.