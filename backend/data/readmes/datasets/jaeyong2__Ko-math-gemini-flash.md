---
dataset_info:
  features:
  - name: content
    dtype: string
  - name: response
    dtype: string
  splits:
  - name: train
    num_bytes: 501535679
    num_examples: 72400
  download_size: 238029964
  dataset_size: 501535679
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
---

### 참고 자료 : [Aarushhh/finemath-refined](https://huggingface.co/datasets/Aarushhh/finemath-refined)
### 생성 모델 : gemini-2.0-flash-exp