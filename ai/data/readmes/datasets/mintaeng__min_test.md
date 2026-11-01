---
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 1834197
    num_examples: 2200
  download_size: 1015650
  dataset_size: 1834197
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- text-generation
- question-answering
language:
- ko
---

## llama3_8b_ 모델 파인튜닝 테스트용 데이터입니다. 
원본 데이터 : databricks-dolly-15k-ko.jsonl
응답 형식 변환 후 자체 질의응답 세트 추가
