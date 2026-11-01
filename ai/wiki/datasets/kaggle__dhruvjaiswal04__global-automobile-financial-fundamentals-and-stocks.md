---
type: "dataset"
id: "kaggle/dhruvjaiswal04/global-automobile-financial-fundamentals-and-stocks"
source: "kaggle"
url: "https://www.kaggle.com/datasets/dhruvjaiswal04/global-automobile-financial-fundamentals-and-stocks"
downloads: 22
summary: "글로벌 자동차 산업의 시계열 주식 시세와 분기별 재무 데이터를 제공하는 금융 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/dhruvjaiswal04/global-automobile-financial-fundamentals-and-stocks

> dataset · [Kaggle](https://www.kaggle.com/datasets/dhruvjaiswal04/global-automobile-financial-fundamentals-and-stocks)

글로벌 자동차 산업의 시계열 주식 시세와 분기별 재무 데이터를 제공하는 금융 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — tag_match · readme, tags = `classification` · 신뢰도 medium
- **작업**: [[표 데이터 예측]] — ner · readme = `태그: finance, automobiles and vehicles, time series analysis, classification, regression` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:tabular_prediction = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme = `Hourly OHLCV Market Data and Quarterly Financial Fundamentals for 11 Global Auto` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme = `Hourly OHLCV Market Data and Quarterly Financial Fundamentals for 11 Global Auto` · 신뢰도 low
- **상업 이용**: [[비상업 전용]] — metadata · license = `CC BY-NC-SA 4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset provides a multi-dimensional view of the global automobile industry, spanning from 2024 to mid-2026.` · 신뢰도 low
