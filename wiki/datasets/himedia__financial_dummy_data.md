---
type: "dataset"
id: "himedia/financial_dummy_data"
source: "huggingface"
url: "https://huggingface.co/datasets/himedia/financial_dummy_data"
downloads: 8
summary: "금융 지표를 기반으로 신용 등급을 예측하는 금융 신용 등급 예측 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# himedia/financial_dummy_data

> dataset · [Hugging Face](https://huggingface.co/datasets/himedia/financial_dummy_data)

금융 지표를 기반으로 신용 등급을 예측하는 금융 신용 등급 예측 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme = `Columns: credit_rating revenue operating_profit net_income total_assets total_liabilities total_equity capital operating_cash_flow interest_bearing_debt debt_ra` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Task: Predict credit_rating based on financial indicators` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `Credit Rating Prediction Dataset` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Validation | 100` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train | 44,900` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
