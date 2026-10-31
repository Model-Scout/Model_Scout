---
type: "dataset"
id: "kaggle/adizz321/top-250-webtoons-and-manhwa-analytics-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/adizz321/top-250-webtoons-and-manhwa-analytics-dataset"
downloads: 60
summary: "한국 인기 웹툰 250편의 평점, 인기, 장르, 챕터, 줄거리 메타데이터를 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
# kaggle/adizz321/top-250-webtoons-and-manhwa-analytics-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/adizz321/top-250-webtoons-and-manhwa-analytics-dataset)

한국 인기 웹툰 250편의 평점, 인기, 장르, 챕터, 줄거리 메타데이터를 제공하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Identify top-performing genres and score distributions.` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Perform TF-IDF, sentiment analysis, or topic modeling on plot synopses.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Compare popularity rank versus average score to see if hyped webtoons match user ratings.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:retrieval = `plot synopses` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `average user scores, global rankings, popularity counts, chapter counts, status, genres, and cleaned plot synopses` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `top Korean comics` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset provides comprehensive metadata for the top-rated 250 Webtoons and Manhwa` · 신뢰도 low
