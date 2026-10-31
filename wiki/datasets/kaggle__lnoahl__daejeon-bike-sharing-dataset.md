---
type: "dataset"
id: "kaggle/lnoahl/daejeon-bike-sharing-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/lnoahl/daejeon-bike-sharing-dataset"
downloads: 77
summary: "대전시 공공자전거 '타슈' 시간별 대여 데이터와 기상 정보를 포함한 시계열 예측용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/lnoahl/daejeon-bike-sharing-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/lnoahl/daejeon-bike-sharing-dataset)

대전시 공공자전거 '타슈' 시간별 대여 데이터와 기상 정보를 포함한 시계열 예측용 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `The data is ideal for time series forecasting, weather impact analysis, and mobility research.` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme, task:forecasting = `This dataset contains hourly aggregated bike rental data from the Tashu public bike-sharing system` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `count: number of bikes rented during the corresponding hour` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — ner · readme = `Daejeon Public Bicycle 'Tashu' rental dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `It has been aggregated, and reformed for research use.` · 신뢰도 low
