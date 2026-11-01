---
dataset_info:
  features:
  - name: messages
    large_list:
    - name: content
      dtype: large_string
    - name: role
      dtype: large_string
  - name: source_dataset
    dtype: large_string
  splits:
  - name: train
    num_bytes: 1452460394.0
    num_examples: 515911
  download_size: 708508292
  dataset_size: 1452460394.0
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-sa-4.0
task_categories:
- question-answering
language:
- ko
source_datasets:
- coastral/korean-writing-style-instruct
- lemon-mint/smol-koreantalk
- CarrotAI/ko-instruction-dataset
- MarkrAI/KOpen-HQ-Hermes-2.5-60K
- beomi/KoAlpaca-RealQA
- HAERAE-HUB/qarv-instruct-ko
- maywell/koVast
---

## devngho/korean-instruction-mix

한국어 instruction 데이터셋 mix. 이 데이터셋을 사용해 학습된 모델은 아래 원본 데이터셋을 함께 인용해주세요.

- [coastral/korean-writing-style-instruct](https://huggingface.co/datasets/coastral/korean-writing-style-instruct)(apache-2.0): 5.62%, x1.0
- [lemon-mint/smol-koreantalk](https://huggingface.co/datasets/lemon-mint/smol-koreantalk)(apache-2.0): 26.77%, x0.3
- [CarrotAI/ko-instruction-dataset](https://huggingface.co/datasets/CarrotAI/ko-instruction-dataset)(apache-2.0): 2.73%, x2.0
- [MarkrAI/KOpen-HQ-Hermes-2.5-60K](https://huggingface.co/datasets/MarkrAI/KOpen-HQ-Hermes-2.5-60K)(mit): 23.28%, x2.0
- [beomi/KoAlpaca-RealQA](https://huggingface.co/datasets/beomi/KoAlpaca-RealQA)(cc by-sa 4.0): 7.18%, x2.0
- [HAERAE-HUB/qarv-instruct-ko](https://huggingface.co/datasets/HAERAE-HUB/qarv-instruct-ko)(apache-2.0): 7.89%, x4.0
- [maywell/koVast](https://huggingface.co/datasets/maywell/koVast)(mit): 26.54%, x0.2