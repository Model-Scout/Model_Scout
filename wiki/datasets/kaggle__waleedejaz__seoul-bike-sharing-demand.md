---
type: "dataset"
id: "kaggle/waleedejaz/seoul-bike-sharing-demand"
source: "kaggle"
url: "https://www.kaggle.com/datasets/waleedejaz/seoul-bike-sharing-demand"
downloads: 202
summary: "서울시 공공자전거 시간별 대여량과 기상 정보를 포함한 수요 예측 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/waleedejaz/seoul-bike-sharing-demand

> dataset · [Kaggle](https://www.kaggle.com/datasets/waleedejaz/seoul-bike-sharing-demand)

서울시 공공자전거 시간별 대여량과 기상 정보를 포함한 수요 예측 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `The crucial part is the prediction of bike count required at each hour for the stable supply of rental bikes.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The dataset contains weather information (Temperature, Humidity, Windspeed, Visibility, Dewpoint, Solar radiation, Snowfall, Rainfall), the number of bikes rent` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Rented Bike count - Count of bikes rented at each hour` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Attribution 4.0 International (CC BY 4.0)` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — ner · readme = `Currently Rental bikes are introduced in many urban cities for the enhancement of mobility comfort.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset contains count of public bicycles rented per hour in the Seoul Bike.` · 신뢰도 low
