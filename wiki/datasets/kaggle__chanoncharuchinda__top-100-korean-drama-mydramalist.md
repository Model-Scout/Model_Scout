---
type: "dataset"
id: "kaggle/chanoncharuchinda/top-100-korean-drama-mydramalist"
source: "kaggle"
url: "https://www.kaggle.com/datasets/chanoncharuchinda/top-100-korean-drama-mydramalist"
downloads: 7140
summary: "MyDramaList 웹사이트에서 수집한 한국 드라마 100편의 정보와 평점 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
  - "[[학습용]]"
---
# kaggle/chanoncharuchinda/top-100-korean-drama-mydramalist

> dataset · [Kaggle](https://www.kaggle.com/datasets/chanoncharuchinda/top-100-korean-drama-mydramalist)

MyDramaList 웹사이트에서 수집한 한국 드라마 100편의 정보와 평점 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `What is/are the popular Genres and Theme (Tags column) and does it leads to higher rating?` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Create a recommendation system for the Drama (and check with the recommendation by the website)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:retrieval = `* Name: Korean Drama name
* Year of release: Release year of the drama
* Aired Date: Aired Date (start) - (end)
* Aired On: Aired on what day(s) of the week
* N` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `* Rank: Ranking on the website
* Rating: Rating by the users on the website out of ten` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `태그: arts and entertainment, movies and tv shows, data visualization, recommender systems, korea` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `I have recently published another dataset with information about Korean Drama.` · 신뢰도 low
