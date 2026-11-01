---
type: "dataset"
id: "tabularisai/swahili-sentiment-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/tabularisai/swahili-sentiment-dataset"
downloads: 191
summary: "저자들이 발표한 스와힐리어 감성 분석을 위한 합성 데이터 생성 파이프라인 연구 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[sw]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# tabularisai/swahili-sentiment-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/tabularisai/swahili-sentiment-dataset)

저자들이 발표한 스와힐리어 감성 분석을 위한 합성 데이터 생성 파이프라인 연구 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Synthetic Data Generation Pipeline for Low-Resource Swahili Sentiment Analysis` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Synthetic Data Generation Pipeline for Low-Resource Swahili Sentiment Analysis` · 신뢰도 low
- **언어**: [[sw]] — metadata · languages = `sw` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `297` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Synthetic Data Generation Pipeline for Low-Resource Swahili Sentiment Analysis` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Synthetic Data Generation Pipeline for Low-Resource Swahili Sentiment Analysis` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1186자 ≈ 297 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[tabularisai__multilingual-sentiment-analysis|tabularisai/multilingual-sentiment-analysis]]
