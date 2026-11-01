---
type: "dataset"
id: "kaggle/changsubchang/corona-and-korean-general-election"
source: "kaggle"
url: "https://www.kaggle.com/datasets/changsubchang/corona-and-korean-general-election"
downloads: 139
summary: "서울시 지역별 코로나와 20·21대 총선 선거 데이터를 포함한 상세 데이터셋입니다."
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
  - "[[뉴스·미디어]]"
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/changsubchang/corona-and-korean-general-election

> dataset · [Kaggle](https://www.kaggle.com/datasets/changsubchang/corona-and-korean-general-election)

서울시 지역별 코로나와 20·21대 총선 선거 데이터를 포함한 상세 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `to find the potential relations with Corona virus spread in Korea` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `to find the potential relations with Corona virus spread in Korea` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `The contents include: 1. General election data of 20th and 21st General Electtion 2. Corona data of the Seoul Metropolitan Area` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `The contents include: 1. General election data of 20th and 21st General Electtion 2. Corona data of the Seoul Metropolitan Area` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — tag_match · tags = `news` · 신뢰도 medium
- **도메인**: [[행정·민원]] — ner · readme = `Detailed dataset on Korean recent elections, to the municipal government level` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The Team collected, cleansed, and preprocessed election data of 20th and 21st General Election in Seoul metropolitan area` · 신뢰도 low
