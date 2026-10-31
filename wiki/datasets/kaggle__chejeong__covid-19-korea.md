---
type: "dataset"
id: "kaggle/chejeong/covid-19-korea"
source: "kaggle"
url: "https://www.kaggle.com/datasets/chejeong/covid-19-korea"
downloads: 165
summary: "한국의 코로나19 확진자 및 검사 현황 데이터를 분석하는 데 사용되는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/chejeong/covid-19-korea

> dataset · [Kaggle](https://www.kaggle.com/datasets/chejeong/covid-19-korea)

한국의 코로나19 확진자 및 검사 현황 데이터를 분석하는 데 사용되는 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Analysis such as the trend of infections, vulnerable age groups, and many others can be conducted.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `analyzing the covid status data of South Korea may give insight into the trend of the pandemic` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The *covid_kr* file contains information such as number of: confirmed cases, released from quarantine, tests, deaths, patients being treated, negative cases, ag` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `The *covid_kr* file contains information such as number of: confirmed cases, released from quarantine, tests, deaths, patients being treated, negative cases, ag` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `health` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The *covid_kr* file contains information such as number of: confirmed cases, released from quarantine, tests, deaths, patients being treated, negative cases, ag` · 신뢰도 low
