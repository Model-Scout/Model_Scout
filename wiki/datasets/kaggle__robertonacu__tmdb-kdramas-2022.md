---
type: "dataset"
id: "kaggle/robertonacu/tmdb-kdramas-2022"
source: "kaggle"
url: "https://www.kaggle.com/datasets/robertonacu/tmdb-kdramas-2022"
downloads: 454
summary: "TMDB 공식 API로 구축한 한국 TV 시리즈 데이터셋으로, 시리즈 정보와 관련 인물, 장르 등을 포함합니다."
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
  - "[[학습용]]"
---
# kaggle/robertonacu/tmdb-kdramas-2022

> dataset · [Kaggle](https://www.kaggle.com/datasets/robertonacu/tmdb-kdramas-2022)

TMDB 공식 API로 구축한 한국 TV 시리즈 데이터셋으로, 시리즈 정보와 관련 인물, 장르 등을 포함합니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `series.csv: file containing all the series, tried my best to scrape all non-translated series or data` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This dataset is focused on Korean TV series available on The Movie Database (TMDB)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `series.csv: file containing all the series, tried my best to scrape all non-translated series or data` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `series.csv: file containing all the series, tried my best to scrape all non-translated series or data` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `Korean TV Series listed on TMDB` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is focused on Korean TV series available on The Movie Database (TMDB) and has been built using TMDB's official API` · 신뢰도 low
