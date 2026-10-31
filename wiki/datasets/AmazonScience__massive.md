---
type: "dataset"
id: "AmazonScience/massive"
source: "huggingface"
url: "https://huggingface.co/datasets/AmazonScience/massive"
downloads: 12226
summary: "MASSIVE는 52개 언어의 100만 개 이상 발화로 구성된 다국어 자연어 이해용 병렬 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# AmazonScience/massive

> dataset · [Hugging Face](https://huggingface.co/datasets/AmazonScience/massive)

MASSIVE는 52개 언어의 100만 개 이상 발화로 구성된 다국어 자연어 이해용 병렬 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `Natural Language Understanding tasks of intent prediction and slot annotation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:question_answering = `utterances` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `annotations for the Natural Language Understanding tasks of intent prediction and slot annotation` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `general Intelligent Voice Assistant single-shot interactions` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The dataset can be used to train a model for `natural-language-understanding` (NLU)` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[ethicalabs__Echo-DSRN-v0.1.3-Intent-CLF|ethicalabs/Echo-DSRN-v0.1.3-Intent-CLF]]
- [[palette-lab__songgot-x-0.8b|palette-lab/songgot-x-0.8b]]
