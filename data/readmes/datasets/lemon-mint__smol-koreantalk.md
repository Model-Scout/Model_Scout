---
dataset_info:
  features:
  - name: messages
    list:
    - name: content
      dtype: string
    - name: content_en
      dtype: string
    - name: role
      dtype: string
  - name: custom_id
    dtype: string
  splits:
  - name: train
    num_bytes: 3880686436
    num_examples: 460281
  download_size: 1967369962
  dataset_size: 3880686436
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
task_categories:
- question-answering
- text-generation
- text2text-generation
- translation
- summarization
- text-classification
language:
- ko
- en
pretty_name: 'Smol-KoreanTalk: Korean SmolTalk Dataset'
---

SmolLM2의 인스트럭션 훈련 데이터 [HuggingFaceTB/smol-smoltalk](https://huggingface.co/datasets/HuggingFaceTB/smol-smoltalk)를 한국어로 번역했어요.
