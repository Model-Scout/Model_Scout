---
type: "dataset"
id: "CyberMax-tools/smartthings-review-mood-sept-2026"
source: "huggingface"
url: "https://huggingface.co/datasets/CyberMax-tools/smartthings-review-mood-sept-2026"
downloads: 234
summary: "2026년 9월 삼성 스마트싱스 앱 냉장고 펌웨어 사고 관련 앱 리뷰 감정 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# CyberMax-tools/smartthings-review-mood-sept-2026

> dataset · [Hugging Face](https://huggingface.co/datasets/CyberMax-tools/smartthings-review-mood-sept-2026)

2026년 9월 삼성 스마트싱스 앱 냉장고 펌웨어 사고 관련 앱 리뷰 감정 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `share of 1–2 star reviews, and how many reviews mention the fridge, an update/firmware, or going offline/losing connection (keywords matched in Korean and Engli` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `review count, average rating, share of 1–2 star reviews, and how many reviews mention the fridge, an update/firmware, or going offline/losing connection` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `A review-mood signal can still flag an incident within a day.` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-classification` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality, task:tabular_prediction = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:retrieval = `app reviews around one September 2026 incident` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `SmartThings app review mood around the Sept 2026 fridge firmware incident` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This free file is a snapshot (app reviews around one September 2026 incident)` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
