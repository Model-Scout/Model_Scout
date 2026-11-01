---
type: "dataset"
id: "kaggle/presstegong/korean-won-tether-usdt-premium-daily"
source: "kaggle"
url: "https://www.kaggle.com/datasets/presstegong/korean-won-tether-usdt-premium-daily"
downloads: 9
summary: "2025년부터 한국 원화와 테더(USDT) 프리미엄 일별 환율 데이터로 금융 분석에 활용됨."
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
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/presstegong/korean-won-tether-usdt-premium-daily

> dataset · [Kaggle](https://www.kaggle.com/datasets/presstegong/korean-won-tether-usdt-premium-daily)

2025년부터 한국 원화와 테더(USDT) 프리미엄 일별 환율 데이터로 금융 분석에 활용됨.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `time series analysis` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `Daily USDT/KRW premium vs the USD/KRW reference rate on Upbit, 2025-present` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:tabular_prediction = `table` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme, task:forecasting = `Daily USDT/KRW premium vs the USD/KRW reference rate on Upbit, 2025-present` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `Daily USDT/KRW premium vs the USD/KRW reference rate on Upbit, 2025-present` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Attribution 4.0 International (CC BY 4.0)` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `One row per day since **2025-01-01**. This dataset is linked to the live source and refreshed from it.` · 신뢰도 low
