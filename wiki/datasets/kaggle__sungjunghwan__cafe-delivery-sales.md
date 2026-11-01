---
type: "dataset"
id: "kaggle/sungjunghwan/cafe-delivery-sales"
source: "kaggle"
url: "https://www.kaggle.com/datasets/sungjunghwan/cafe-delivery-sales"
downloads: 939
summary: "2020-21년 한국 배달 앱 카페 배달 매출과 코로나 현황, 날씨 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[시계열 예측]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[상거래·상품]]"
  - "[[환경·기상]]"
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/sungjunghwan/cafe-delivery-sales

> dataset · [Kaggle](https://www.kaggle.com/datasets/sungjunghwan/cafe-delivery-sales)

2020-21년 한국 배달 앱 카페 배달 매출과 코로나 현황, 날씨 데이터입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `time series analysis` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `2020-21 data on cafe delivery sales and corona status.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `Sales amount` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Sales amount` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `CC BY-NC-SA 4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `카페 배달 매출 데이터` · 신뢰도 low
- **도메인**: [[환경·기상]] — ner · readme = `날씨 데이터` · 신뢰도 medium
- **도메인**: [[의료·보건]] — ner · readme = `코로나 현황 데이터` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Sales data for about one year for delivery sales (delivery app in south korea). (January to November 2021)` · 신뢰도 low
