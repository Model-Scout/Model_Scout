---
language:
- ko
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 63657452
    num_examples: 24924
  download_size: 29357795
  dataset_size: 63657452
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

본 데이터셋은 kiqu-70b 모델의 출력 샘플입니다.

Sionic AI에서 GPU 자원을 지원받아 제작되었습니다.