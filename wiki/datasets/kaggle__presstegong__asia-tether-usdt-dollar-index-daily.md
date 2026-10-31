---
type: "dataset"
id: "kaggle/presstegong/asia-tether-usdt-dollar-index-daily"
source: "kaggle"
url: "https://www.kaggle.com/datasets/presstegong/asia-tether-usdt-dollar-index-daily"
downloads: 2
summary: "아시아 주요국에서 USDT 1달러의 일별 실제 USD 가치를 기록한 금융 시계열 데이터입니다."
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
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/presstegong/asia-tether-usdt-dollar-index-daily

> dataset · [Kaggle](https://www.kaggle.com/datasets/presstegong/asia-tether-usdt-dollar-index-daily)

아시아 주요국에서 USDT 1달러의 일별 실제 USD 가치를 기록한 금융 시계열 데이터입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Daily USD value of one USDT in Korea, India, Indonesia, Thailand, Philippines` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `This dataset records, for each market and each day since 1 January 2025, what one USDT actually cost in US dollars.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:tabular_prediction = `table` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme, task:forecasting = `Daily USD value of one USDT in Korea, India, Indonesia, Thailand, Philippines` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `Daily USD value of one USDT in Korea, India, Indonesia, Thailand, Philippines` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Attribution 4.0 International (CC BY 4.0)` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This file is linked to the live source and refreshed from it daily.` · 신뢰도 low
