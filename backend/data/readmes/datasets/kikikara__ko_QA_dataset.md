---
dataset_info:
  features:
  - name: input
    dtype: string
  - name: output
    dtype: string
  splits:
  - name: train
    num_bytes: 78438658
    num_examples: 127476
  download_size: 42122393
  dataset_size: 78438658
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- question-answering
language:
- ko
license: apache-2.0
---


maywell/korean_textbooks 의 dataset을 Q&A 형식으로 재구성한 dataset입니다.