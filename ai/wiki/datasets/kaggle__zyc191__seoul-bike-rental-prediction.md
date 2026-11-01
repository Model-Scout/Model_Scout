---
type: "dataset"
id: "kaggle/zyc191/seoul-bike-rental-prediction"
source: "kaggle"
url: "https://www.kaggle.com/datasets/zyc191/seoul-bike-rental-prediction"
downloads: 422
summary: "서울시 자전거 대여 수요 예측을 위한 시간별 자전거 대여량 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/zyc191/seoul-bike-rental-prediction

> dataset · [Kaggle](https://www.kaggle.com/datasets/zyc191/seoul-bike-rental-prediction)

서울시 자전거 대여 수요 예측을 위한 시간별 자전거 대여량 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Predict Number of bikes to be made available for renting, from the given dataset` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme = `The dataset contains weather information (Temperature, Humidity, Windspeed, Visibility, Dewpoint, Solar radiation, Snowfall, Rainfall), the number of bikes rent` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `Predict Number of bikes to be made available for renting, from the given dataset` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — ner · readme = `Currently, Rental bikes are introduced in many urban cities for the enhancement of mobility comfort.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset contains weather information (Temperature, Humidity, Windspeed, Visibility, Dewpoint, Solar radiation, Snowfall, Rainfall), the number of bikes rent` · 신뢰도 low
