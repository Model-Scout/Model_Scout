---
annotations_creators:
- machine-generated
language_creators:
- found
language:
- ko
multilinguality:
- monolingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- text-classification
pretty_name: psyche/korean_idioms
tags: []
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
- config_name: idioms
  data_files:
  - split: train
    path: idioms/train-*
dataset_info:
  config_name: idioms
  features:
  - name: question
    dtype: string
  - name: answer
    dtype: string
  - name: dialogue
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 2528452
    num_examples: 7984
  download_size: 1311065
  dataset_size: 2528452
---

NLI를 위한 한국어 속담 데이터셋입니다.

'question'은 속담의 의미와 보기(5지선다)가 표시되어 있으며,

'label'에는 정답의 번호(0-4)가 표시되어 있습니다.

licence: cc-by-sa-2.0-kr (원본 출처:국립국어원 표준국어대사전)

|Model| psyche/korean_idioms |
|:------:|:---:|
|klue/bert-base|0.7646|