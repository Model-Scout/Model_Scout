---
type: "dataset"
id: "kaggle/hongsean/covid19-in-korea-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/hongsean/covid19-in-korea-dataset"
downloads: 922
summary: "한국의 코로나19 일별 확진자 및 인구통계, 지리 정보 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/hongsean/covid19-in-korea-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/hongsean/covid19-in-korea-dataset)

한국의 코로나19 일별 확진자 및 인구통계, 지리 정보 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `daily confirmed case with demographic and geographic information` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `daily confirmed case with demographic and geographic information` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `3 files attached which are 1) COVID Korea Status 2) COVID Korea Demo 3) COVID Korea Geo` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `3 files attached which are 1) COVID Korea Status 2) COVID Korea Demo 3) COVID Korea Geo` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `covid19` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This datasets are prepared to cheer Korea up fighting against coronavirus` · 신뢰도 low
