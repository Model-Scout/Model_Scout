---
type: "dataset"
id: "kaggle/balaaje/coronavirus-covid19-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/balaaje/coronavirus-covid19-dataset"
downloads: 1994
summary: "코로나19 확진자, 사망자, 회복자 수 정보를 담은 교육용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[교육]]"
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/balaaje/coronavirus-covid19-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/balaaje/coronavirus-covid19-dataset)

코로나19 확진자, 사망자, 회복자 수 정보를 담은 교육용 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `This dataset has information on the number of affected cases, deaths and recovery from 2019 novel coronavirus.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme = `This dataset has information on the number of affected cases, deaths and recovery from 2019 novel coronavirus.` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `This dataset has information on the number of affected cases, deaths and recovery from 2019 novel coronavirus.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `Data files © Original Authors` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · tags = `education` · 신뢰도 medium
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `health` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This data is solely for education purposes only.` · 신뢰도 low
