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
  splits:
  - name: train
    num_bytes: 533935472
    num_examples: 100000
  download_size: 244137926
  dataset_size: 533935472
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
- en
pretty_name: Korean FineTome 100K
---

Korean FineTome 100K 데이터셋은 arcee-ai/The-Tome 의 하위 집합으로 (arcee-ai/qwen2-72b-magpie-en 제외), HuggingFaceFW/fineweb-edu-classifier 를 사용하여 다시 필터링된 데이터셋 [mlabonne/FineTome-100k](https://huggingface.co/datasets/mlabonne/FineTome-100k) 을 한국어로 번역했어요.

### 2025.02.13 Update

시스템 프롬프트와 질문의 성격에 따라서 나누어진 데이터 세트가 나왔어요!

- [kkksklsn/Korean-FineTome-100k-tagging](https://huggingface.co/datasets/kkksklsn/Korean-FineTome-100k-tagging)