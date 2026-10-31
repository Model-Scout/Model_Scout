---
dataset_info:
  features:
  - name: 사건명
    dtype: string
  - name: 헌재결정례ID
    dtype: string
  - name: 헤더
    dtype: string
  - name: 헌재결정례본문
    dtype: string
  splits:
  - name: train
    num_bytes: 246435999
    num_examples: 35246
  download_size: 104740893
  dataset_size: 246435999
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-4.0
language:
- ko
---
2025년 08월 기준으로 open.law.go.kr 에서 수집한 헌재결정례 데이터셋입니다.