---
language:
- ko
license: cc-by-nc-sa-4.0
task_categories:
- question-answering
- text-generation
tags:
- legal
- law
- korean
dataset_info:
  features:
  - name: messages
    sequence:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 3845913
    num_examples: 1000
  download_size: 1693372
  dataset_size: 3845913
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# Legal QA 1k Dataset (Korean Civil Law)

## 1. 데이터셋 개요
이 데이터셋은 AI Hub의 `민사법 LLM 사전학습 및 Instruction Tuning 데이터`를 기반으로 1,000개를 랜덤 샘플링하여 제작한 정제된 데이터셋입니다. 
주로 Llama 3.x 모델의 한국어 법률 도메인 파인튜닝(SFT) 실습을 목적으로 합니다.

## 2. 데이터 구조
데이터셋은 다음 세 가지 주요 컬럼으로 구성됩니다.

- `messages`: Llama 3 Chat Template 형식에 맞춘 대화 데이터 (System, User, Assistant)
- `question`: 원본 법률 질문 텍스트
- `answer`: 법률 전문가 스타일의 답변 텍스트

## 3. 활용 방법
허깅페이스 `datasets` 라이브러리를 사용하여 즉시 로드할 수 있습니다.

```python
from datasets import load_dataset

dataset = load_dataset("rudalson/legal-qa-1k-dataset", split="train")
print(dataset[0])