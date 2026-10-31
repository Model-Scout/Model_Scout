---
type: "dataset"
id: "kaggle/kimjihoo/kpopdb"
source: "kaggle"
url: "https://www.kaggle.com/datasets/kimjihoo/kpopdb"
downloads: 4167
summary: "1992년부터 2020년까지 K-pop 아이돌, 그룹, 뮤직비디오 정보를 담은 데이터베이스입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[서비스 데이터]]"
---
# kaggle/kimjihoo/kpopdb

> dataset · [Kaggle](https://www.kaggle.com/datasets/kimjihoo/kpopdb)

1992년부터 2020년까지 K-pop 아이돌, 그룹, 뮤직비디오 정보를 담은 데이터베이스입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `K-Pop Database from dbkpop.com` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `K-Pop Database from dbkpop.com` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `- K-pop Idols
- K-pop Boy Groups
- K-pop Girl Groups
- K-pop Music Videos` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `- K-pop Idols
- K-pop Boy Groups
- K-pop Girl Groups
- K-pop Music Videos` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `K-pop (abbreviation of Korean pop) is a genre of popular music originating in South Korea.` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `Source of Data: [dbkpop](https://dbkpop.com/) (K-pop Database)` · 신뢰도 low
