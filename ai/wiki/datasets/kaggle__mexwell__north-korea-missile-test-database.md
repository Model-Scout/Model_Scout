---
type: "dataset"
id: "kaggle/mexwell/north-korea-missile-test-database"
source: "kaggle"
url: "https://www.kaggle.com/datasets/mexwell/north-korea-missile-test-database"
downloads: 109
summary: "1984년부터 2023년까지 북한 미사일 시험 발사 기록과 메타데이터를 담은 데이터베이스입니다."
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
  - "[[조건부 이용]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/mexwell/north-korea-missile-test-database

> dataset · [Kaggle](https://www.kaggle.com/datasets/mexwell/north-korea-missile-test-database)

1984년부터 2023년까지 북한 미사일 시험 발사 기록과 메타데이터를 담은 데이터베이스입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `The database captures advancements in North Korea’s missile program by documenting all such tests since the first one occurred in April 1984` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `The James Martin Center for Nonproliferation Studies (CNS) North Korea Missile Test Database is the first database to record flight tests of all missiles launch` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Missile Tests from 1984 till 2023 with metadata` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Missile Tests from 1984 till 2023 with metadata` · 신뢰도 low
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[행정·민원]] — tag_match · readme, tags = `government` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The database captures advancements in North Korea’s missile program by documenting all such tests since the first one occurred in April 1984` · 신뢰도 low
