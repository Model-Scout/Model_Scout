---
type: "dataset"
id: "kaggle/jishnukoliyadan/gold-price-1979-present"
source: "kaggle"
url: "https://www.kaggle.com/datasets/jishnukoliyadan/gold-price-1979-present"
downloads: 3127
summary: "1979년부터 현재까지 주요 국가의 금 시세 시계열 데이터로 가격 분석 및 예측에 활용 가능"
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
# kaggle/jishnukoliyadan/gold-price-1979-present

> dataset · [Kaggle](https://www.kaggle.com/datasets/jishnukoliyadan/gold-price-1979-present)

1979년부터 현재까지 주요 국가의 금 시세 시계열 데이터로 가격 분석 및 예측에 활용 가능

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `This is a Time Series data.` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — ner · readme = `Time series analysis and forecasting the future price` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:tabular_prediction = `3 `csv` files for representing Daily, Monthly and Quarterly gold prices` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `This is a Time Series data.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `Gold price discovery is crucial for any market.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Whats possible with this data ? * Time series analysis and forecasting the future price` · 신뢰도 low
