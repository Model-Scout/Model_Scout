---
type: "dataset"
id: "keywordbarrage/coupang-scraper"
source: "huggingface"
url: "https://huggingface.co/datasets/keywordbarrage/coupang-scraper"
downloads: 0
summary: "쿠팡 SKU 재고 소진 및 WAF 텔레메트리 데이터를 포함한 기업용 고빈도 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[시계열 예측]]"
  - "[[문서 검색]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# keywordbarrage/coupang-scraper

> dataset · [Hugging Face](https://huggingface.co/datasets/keywordbarrage/coupang-scraper)

쿠팡 SKU 재고 소진 및 WAF 텔레메트리 데이터를 포함한 기업용 고빈도 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `suitable for real-time vector database updates and inventory velocity monitoring` · 신뢰도 low
- **작업**: [[시계열 예측]] — metadata · task_categories = `time-series-forecasting` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `assist quantitative analysts and data engineering teams in evaluating robust extraction pipelines` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · readme, task_categories = `tabular-classification` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:tabular_prediction = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Unique Coupang Product/Vendor identifier` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `This repository contains an open 1,000-row verified benchmark sample of the Coupang SKU depletion feed` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This repository contains an open 1,000-row verified benchmark sample of the Coupang SKU depletion feed` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
