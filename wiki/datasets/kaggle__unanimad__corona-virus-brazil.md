---
type: "dataset"
id: "kaggle/unanimad/corona-virus-brazil"
source: "kaggle"
url: "https://www.kaggle.com/datasets/unanimad/corona-virus-brazil"
downloads: 48816
summary: "브라질의 코로나19 누적 확진자 수 시계열 데이터를 제공하는 공개 데이터셋입니다."
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
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/unanimad/corona-virus-brazil

> dataset · [Kaggle](https://www.kaggle.com/datasets/unanimad/corona-virus-brazil)

브라질의 코로나19 누적 확진자 수 시계열 데이터를 제공하는 공개 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `This dataset has information on the number of cases in Brazil. Please note that this is a time series data and so the number of cases on any given day is a cumu` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme, task:forecasting = `Please note that this is a time series data` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme, task:forecasting = `the number of cases on any given day is a cumulative number.` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `health` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset has information on the number of cases in Brazil.` · 신뢰도 low
