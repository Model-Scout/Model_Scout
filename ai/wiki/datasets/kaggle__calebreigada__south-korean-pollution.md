---
type: "dataset"
id: "kaggle/calebreigada/south-korean-pollution"
source: "kaggle"
url: "https://www.kaggle.com/datasets/calebreigada/south-korean-pollution"
downloads: 2606
summary: "한국의 대기오염 수치와 기상 데이터를 포함한 시계열 예측용 데이터셋입니다."
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
  - "[[상업 이용 가능]]"
domain:
  - "[[환경·기상]]"
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/calebreigada/south-korean-pollution

> dataset · [Kaggle](https://www.kaggle.com/datasets/calebreigada/south-korean-pollution)

한국의 대기오염 수치와 기상 데이터를 포함한 시계열 예측용 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Being able to accurately forecast the level of pollution would allow South Koreans to plan ahead and avoid exposing themselves to the harsh pollutants.` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme, task:forecasting = `Pollution data

date - date of measurement
pm25 - fine particulate matter (PM2.5) (µg/m3)
pm10 - fine particulate matter (PM10) (µg/m3)
o3 - Ozone (O3) (µg/m3)
` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `Being able to accurately forecast the level of pollution would allow South Koreans to plan ahead and avoid exposing themselves to the harsh pollutants.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[환경·기상]] — tag_match · readme, tags = `environment` · 신뢰도 medium
- **도메인**: [[뉴스·미디어]] — tag_match · tags = `news` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Pollution data

date - date of measurement
pm25 - fine particulate matter (PM2.5) (µg/m3)
pm10 - fine particulate matter (PM10) (µg/m3)
o3 - Ozone (O3) (µg/m3)
` · 신뢰도 low
