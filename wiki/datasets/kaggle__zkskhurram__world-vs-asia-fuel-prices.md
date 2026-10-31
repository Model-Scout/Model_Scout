---
type: "dataset"
id: "kaggle/zkskhurram/world-vs-asia-fuel-prices"
source: "kaggle"
url: "https://www.kaggle.com/datasets/zkskhurram/world-vs-asia-fuel-prices"
downloads: 2221
summary: "60개국과 22개 아시아 국가의 소매 연료 가격과 원유 동향을 비교한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[시계열 예측]]"
  - "[[정보 추출]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# kaggle/zkskhurram/world-vs-asia-fuel-prices

> dataset · [Kaggle](https://www.kaggle.com/datasets/zkskhurram/world-vs-asia-fuel-prices)

60개국과 22개 아시아 국가의 소매 연료 가격과 원유 동향을 비교한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Cross-country economic comparison` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Machine learning: price prediction models` · 신뢰도 low
- **작업**: [[시계열 예측]] — ner · readme = `Time-series forecasting & trend detection` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `Energy policy & subsidy analysis` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Fuel price EDA & visualization` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `| 1 | `global_fuel_prices.csv` | 60 | Retail gasoline & diesel for 60 countries (March 2026) |` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:information_extraction, task:retrieval = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `| 1 | `global_fuel_prices.csv` | 60 | Retail gasoline & diesel for 60 countries (March 2026) |` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC BY-SA 4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `oil and gas` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Time-series forecasting & trend detection` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Machine learning: price prediction models` · 신뢰도 low
