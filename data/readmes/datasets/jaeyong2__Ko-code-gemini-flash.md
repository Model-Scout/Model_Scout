---
dataset_info:
  features:
  - name: query
    dtype: string
  - name: response
    dtype: string
  splits:
  - name: train
    num_bytes: 323069827
    num_examples: 32500
  download_size: 147393929
  dataset_size: 323069827
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
---
 
## 질문 : [nayohan/CodeFeedback-Filtered-Instruction-ko](https://huggingface.co/datasets/nayohan/CodeFeedback-Filtered-Instruction-ko)
## 답변 모델 : gemini-2.0-flash-thinking