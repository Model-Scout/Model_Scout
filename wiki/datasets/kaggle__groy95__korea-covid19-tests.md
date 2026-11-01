---
type: "dataset"
id: "kaggle/groy95/korea-covid19-tests"
source: "kaggle"
url: "https://www.kaggle.com/datasets/groy95/korea-covid19-tests"
downloads: 118
summary: "한국과 여러 국가의 코로나19 검사량과 결과를 나타내는 데이터셋입니다."
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
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/groy95/korea-covid19-tests

> dataset · [Kaggle](https://www.kaggle.com/datasets/groy95/korea-covid19-tests)

한국과 여러 국가의 코로나19 검사량과 결과를 나타내는 데이터셋입니다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `daily amount of tests performed by different countries` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `the data was collected from different sources to represent amout of tests and resolts for COVID-19 in each country` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `the data was collected from different sources to represent amout of tests and resolts for COVID-19 in each country` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `health` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset was collected in the effort of studying from South Korea and implementing insights from their actions in other countries.` · 신뢰도 low
