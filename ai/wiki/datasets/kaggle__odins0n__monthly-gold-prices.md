---
type: "dataset"
id: "kaggle/odins0n/monthly-gold-prices"
source: "kaggle"
url: "https://www.kaggle.com/datasets/odins0n/monthly-gold-prices"
downloads: 8873
summary: "1979년부터 2021년까지 18개국의 월별 금 시세 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
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
# kaggle/odins0n/monthly-gold-prices

> dataset · [Kaggle](https://www.kaggle.com/datasets/odins0n/monthly-gold-prices)

1979년부터 2021년까지 18개국의 월별 금 시세 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Monthly gold prices of 18 different countries starting from January 1979.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Monthly gold prices of 18 different countries` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `Monthly gold prices of 18 different countries starting from January 1979.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `Historic Gold Prices of 18 different countries` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Expected to be updated quarterly.` · 신뢰도 low
