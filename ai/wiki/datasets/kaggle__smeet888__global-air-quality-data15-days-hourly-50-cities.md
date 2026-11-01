---
type: "dataset"
id: "kaggle/smeet888/global-air-quality-data15-days-hourly-50-cities"
source: "kaggle"
url: "https://www.kaggle.com/datasets/smeet888/global-air-quality-data15-days-hourly-50-cities"
downloads: 16898
summary: "15일간 50개 도시의 시간별 대기질 및 기상 데이터로 환경 분석과 예측에 활용 가능"
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
  - "[[환경·기상]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/smeet888/global-air-quality-data15-days-hourly-50-cities

> dataset · [Kaggle](https://www.kaggle.com/datasets/smeet888/global-air-quality-data15-days-hourly-50-cities)

15일간 50개 도시의 시간별 대기질 및 기상 데이터로 환경 분석과 예측에 활용 가능

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `This dataset is ideal for time-series modeling, forecasting, environmental analytics, and machine-learning experimentation.` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `global_air_quality_50_cities.csv
Rows: 18,000+
Columns: 16
Format: UTF-8 CSV` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `global_air_quality_50_cities.csv
Rows: 18,000+
Columns: 16
Format: UTF-8 CSV` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[환경·기상]] — tag_match · readme, tags = `environment` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is ideal for time-series modeling, forecasting, environmental analytics, and machine-learning experimentation.` · 신뢰도 low
