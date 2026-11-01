---
type: "dataset"
id: "kaggle/joebeachcapital/seoul-bike-sharing"
source: "kaggle"
url: "https://www.kaggle.com/datasets/joebeachcapital/seoul-bike-sharing"
downloads: 4918
summary: "서울 공유 자전거 수요 예측을 위한 환경 요인 기반 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[환경·기상]]"
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/joebeachcapital/seoul-bike-sharing

> dataset · [Kaggle](https://www.kaggle.com/datasets/joebeachcapital/seoul-bike-sharing)

서울 공유 자전거 수요 예측을 위한 환경 요인 기반 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Predict demand for shared bikes in Seoul based on various environmental factors` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme, task:forecasting = `The dataset contains weather information (Temperature, Humidity, Windspeed, Visibility, Dewpoint, Solar radiation, Snowfall, Rainfall), the number of bikes rent` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `Rented Bike count - Count of bikes rented at each hour` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Database: Open Database, Contents: Database Contents` · 신뢰도 high
- **도메인**: [[환경·기상]] — ner · readme = `The dataset contains weather information (Temperature, Humidity, Windspeed, Visibility, Dewpoint, Solar radiation, Snowfall, Rainfall)` · 신뢰도 medium
- **도메인**: [[교통·모빌리티]] — tag_match · readme, tags = `transportation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset contains weather information (Temperature, Humidity, Windspeed, Visibility, Dewpoint, Solar radiation, Snowfall, Rainfall), the number of bikes rent` · 신뢰도 low
