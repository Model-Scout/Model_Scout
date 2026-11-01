---
type: "dataset"
id: "kaggle/saurabhshahane/seoul-bike-sharing-demand-prediction"
source: "kaggle"
url: "https://www.kaggle.com/datasets/saurabhshahane/seoul-bike-sharing-demand-prediction"
downloads: 9245
summary: "서울 자전거 대여 수요와 기상 정보를 포함한 예측 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/saurabhshahane/seoul-bike-sharing-demand-prediction

> dataset · [Kaggle](https://www.kaggle.com/datasets/saurabhshahane/seoul-bike-sharing-demand-prediction)

서울 자전거 대여 수요와 기상 정보를 포함한 예측 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Predict the Bike Demand in specific day` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Data include weather information (Temperature, Humidity, Windspeed, Visibility, Dewpoint, Solar radiation, Snowfall, Rainfall), the number of bikes rented per h` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `Predict the Bike Demand in specific day` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Attribution 4.0 International (CC BY 4.0)` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — ner · readme = `Predict how atmospheric conditions affect the number of bikes rented` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `태그: beginner, intermediate, tabular, regression` · 신뢰도 low
