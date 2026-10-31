---
language:
- ko
dataset_info:
  features:
  - name: system
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  - name: prompt
    dtype: string
  splits:
  - name: train
    num_bytes: 260168570
    num_examples: 72522
  download_size: 128044938
  dataset_size: 260168570
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/662b0e178f99c264f1745716/RZ5ovDBgiY9b-9LsQ2Hop.png)


위 표에 기재된 데이터셋들을 merge했습니다.

rating이 있는 데이터셋의 경우 chosen 점수가 높은 것만 선택됐습니다.

