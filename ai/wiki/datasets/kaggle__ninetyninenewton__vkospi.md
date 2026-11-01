---
type: "dataset"
id: "kaggle/ninetyninenewton/vkospi"
source: "kaggle"
url: "https://www.kaggle.com/datasets/ninetyninenewton/vkospi"
downloads: 950
summary: "한국 주식시장 KOSPI200 옵션 기반 변동성 지수 VKOSPI 관련 시계열 데이터입니다."
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
  - "[[조건부 이용]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/ninetyninenewton/vkospi

> dataset · [Kaggle](https://www.kaggle.com/datasets/ninetyninenewton/vkospi)

한국 주식시장 KOSPI200 옵션 기반 변동성 지수 VKOSPI 관련 시계열 데이터입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `focused on volatility and relevant factors to it` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `Each row represents a trading day.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `Each row represents a trading day.` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Each row represents a trading day.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Each row represents a trading day.` · 신뢰도 low
