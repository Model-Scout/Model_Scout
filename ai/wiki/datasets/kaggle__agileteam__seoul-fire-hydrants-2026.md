---
type: "dataset"
id: "kaggle/agileteam/seoul-fire-hydrants-2026"
source: "kaggle"
url: "https://www.kaggle.com/datasets/agileteam/seoul-fire-hydrants-2026"
downloads: 3
summary: "서울시 소방용 소화전 및 급수시설 62,771개 위치와 속성 정보 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[지리·위치]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/agileteam/seoul-fire-hydrants-2026

> dataset · [Kaggle](https://www.kaggle.com/datasets/agileteam/seoul-fire-hydrants-2026)

서울시 소방용 소화전 및 급수시설 62,771개 위치와 속성 정보 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Look at infrastructure age by district using `install_year`.` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Find areas far from the nearest hydrant (nearest-neighbour distance).` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Map hydrant density per district or 500 m grid.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:retrieval = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[지리·위치]] — ner · readme = `62,771 geocoded fire hydrants and water facilities in Seoul, Korea` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Translation and cleaning by the uploader.` · 신뢰도 low
