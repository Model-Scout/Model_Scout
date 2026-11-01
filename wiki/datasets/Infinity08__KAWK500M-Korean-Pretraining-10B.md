---
type: "dataset"
id: "Infinity08/KAWK500M-Korean-Pretraining-10B"
source: "huggingface"
url: "https://huggingface.co/datasets/Infinity08/KAWK500M-Korean-Pretraining-10B"
downloads: 20
summary: "한국어 중심 500M급 decoder-only 모델 학습용 사전 토큰화 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Infinity08/KAWK500M-Korean-Pretraining-10B

> dataset · [Hugging Face](https://huggingface.co/datasets/Infinity08/KAWK500M-Korean-Pretraining-10B)

한국어 중심 500M급 decoder-only 모델 학습용 사전 토큰화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `한국어 중심 500M급 decoder-only 모델을 처음부터 학습하기 위한 사전 토큰화 데이터입니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `각 행의 input_ids는 uint16[2049]이며 앞의 2,048개 토큰을 causal-LM 입력·레이블로 사용합니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `각 행의 input_ids는 uint16[2049]이며 앞의 2,048개 토큰을 causal-LM 입력·레이블로 사용합니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `영어·코드 전용 데이터는 포함하지 않으며 한국어 문서에 자연스럽게 포함된 영문·숫자·기호만 유지` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `train: 5,075,616 rows / 10,399,937,184 stored tokens` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Infinity08__KAWK-1.5-500M-Korean-Base|Infinity08/KAWK-1.5-500M-Korean-Base]]
- [[Infinity08__KAWK-500M-Korean-Instruct-v1|Infinity08/KAWK-500M-Korean-Instruct-v1]]
