---
license: cc-by-4.0
task_categories:
- text-classification
language:
- ko
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
dataset_info:
  features:
  - name: text
    dtype: string
  - name: labels
    dtype:
      class_label:
        names:
          '0': ai
          '1': human
  splits:
  - name: train
    num_bytes: 402593
    num_examples: 1800
  - name: validation
    num_bytes: 43588
    num_examples: 200
  - name: test
    num_bytes: 83016
    num_examples: 400
  download_size: 237914
  dataset_size: 529197
---

# Korean Idiom Detection: Human vs AI

이 데이터셋은 한국어 관용구 문장에 대해, 해당 문장이 인간이 작성했는지 AI가 작성했는지를 구분하는 이진 분류 태스크에 사용됩니다.

## Features
- `text`: 프롬프트 형식 문장
- `labels`: 0=ai, 1=human
