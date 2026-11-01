---
task_categories:
- question-answering
- text-generation
language:
- ko
license: mit
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: output
    dtype: string
  - name: generation
    dtype: int64
  - name: root
    dtype: string
  - name: trace
    dtype: string
  - name: origin
    dtype: string
  splits:
  - name: train
    num_bytes: 1631431
    num_examples: 1078
  download_size: 818498
  dataset_size: 1631431
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

WizardLM: Empowering Large Language Models to Follow Complex Instructions(https://arxiv.org/abs/2304.12244)의 evol-instrcut 기법을 참고하여 만든 한국어 데이터셋 입니다.
다른 evol-instruct 데이터셋과 달리 opensource 모델(deepseek-v3)을 사용하여 상업적으로 사용 가능한 데이터셋입니다.