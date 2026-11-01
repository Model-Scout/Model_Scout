---
type: "dataset"
id: "kaggle/taeyangg4/south-korea-power-grid-5-minute"
source: "kaggle"
url: "https://www.kaggle.com/datasets/taeyangg4/south-korea-power-grid-5-minute"
downloads: 70
summary: "2015년부터 2026년까지 한국 전력망 5분 단위 운영 데이터로 전력 수요 및 발전량 분석에 활용"
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[시계열 예측]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[환경·기상]]"
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/taeyangg4/south-korea-power-grid-5-minute

> dataset · [Kaggle](https://www.kaggle.com/datasets/taeyangg4/south-korea-power-grid-5-minute)

2015년부터 2026년까지 한국 전력망 5분 단위 운영 데이터로 전력 수요 및 발전량 분석에 활용

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `1,008,249,180 normalized Korea Power Exchange (KPX) five-minute rows from 2015-08 through 2026-07` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `columns `timestamp`, `source`, `generator_id`, and `value_mw`` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `1,008,249,180 normalized Korea Power Exchange (KPX) five-minute rows` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `columns `timestamp`, `source`, `generator_id`, and `value_mw`` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[환경·기상]] — ner · readme = `energy, time series analysis, tabular, electricity` · 신뢰도 low
- **도메인**: [[행정·민원]] — tag_match · tags = `government` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Analysis-ready South Korea power-grid operations data` · 신뢰도 low
