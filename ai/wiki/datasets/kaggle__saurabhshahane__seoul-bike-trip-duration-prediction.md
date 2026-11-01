---
type: "dataset"
id: "kaggle/saurabhshahane/seoul-bike-trip-duration-prediction"
source: "kaggle"
url: "https://www.kaggle.com/datasets/saurabhshahane/seoul-bike-trip-duration-prediction"
downloads: 1528
summary: "서울 자전거 대여 시스템의 대기 환경 요소를 고려한 자전거 여행 시간 예측 데이터셋입니다."
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
# kaggle/saurabhshahane/seoul-bike-trip-duration-prediction

> dataset · [Kaggle](https://www.kaggle.com/datasets/saurabhshahane/seoul-bike-trip-duration-prediction)

서울 자전거 대여 시스템의 대기 환경 요소를 고려한 자전거 여행 시간 예측 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Predict the Bike Trip Duration while considering atmospheric factors` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The Data used include trip duration, trip distance, pickup-dropoff latitude and longitude, temperature, precipitation, wind speed, humidity, solar radiation, sn` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `Predict the Bike Trip Duration while considering atmospheric factors` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Attribution 4.0 International (CC BY 4.0)` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — ner · readme = `Trip duration is the most fundamental measure in all modes of transportation.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `data mining techniques are employed in this paper to predict the trip duration of rental bikes in Seoul Bike sharing system.` · 신뢰도 low
