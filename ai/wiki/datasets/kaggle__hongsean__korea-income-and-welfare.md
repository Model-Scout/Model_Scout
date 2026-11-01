---
type: "dataset"
id: "kaggle/hongsean/korea-income-and-welfare"
source: "kaggle"
url: "https://www.kaggle.com/datasets/hongsean/korea-income-and-welfare"
downloads: 6066
summary: "한국 정부가 2005년부터 14년간 조사한 한국 가계 소득 및 복지 관련 패널 데이터입니다."
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
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/hongsean/korea-income-and-welfare

> dataset · [Kaggle](https://www.kaggle.com/datasets/hongsean/korea-income-and-welfare)

한국 정부가 2005년부터 14년간 조사한 한국 가계 소득 및 복지 관련 패널 데이터입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `The Korea Welfare Panel still continue to study various statistical issues including quality improvement every year.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This studied several household characteristics related to panel attrition` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `There are 14 columns in data;` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `There are 14 columns in data;` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · tags = `education` · 신뢰도 medium
- **도메인**: [[행정·민원]] — ner · readme = `funded by Korea Government.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The data attached has been conducted from 2005 for 14 years funded by Korea Government.` · 신뢰도 low
