---
type: "dataset"
id: "kaggle/ramontanoeiro/air-quality-seoul"
source: "kaggle"
url: "https://www.kaggle.com/datasets/ramontanoeiro/air-quality-seoul"
downloads: 605
summary: "서울의 2017-2020년 대기질 데이터를 모아 예측 연구에 활용하는 데이터셋입니다."
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
  - "[[환경·기상]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/ramontanoeiro/air-quality-seoul

> dataset · [Kaggle](https://www.kaggle.com/datasets/ramontanoeiro/air-quality-seoul)

서울의 2017-2020년 대기질 데이터를 모아 예측 연구에 활용하는 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `I had the idea to create this dataset to try to make predictions for the 2020 year using the 2017-2019 data.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `태그: arts and entertainment, global, environment, tabular, pandas, plotly` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `I had the idea to create this dataset to try to make predictions for the 2020 year using the 2017-2019 data.` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC BY-SA 4.0` · 신뢰도 high
- **도메인**: [[환경·기상]] — tag_match · readme, tags = `environment` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `I had the idea to create this dataset to try to make predictions for the 2020 year using the 2017-2019 data.` · 신뢰도 low
