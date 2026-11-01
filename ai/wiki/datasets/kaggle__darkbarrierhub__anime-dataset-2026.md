---
type: "dataset"
id: "kaggle/darkbarrierhub/anime-dataset-2026"
source: "kaggle"
url: "https://www.kaggle.com/datasets/darkbarrierhub/anime-dataset-2026"
downloads: 1031
summary: "일본 애니메이션 정보와 평점, 인기 등을 담은 데이터셋으로 분석과 추천에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/darkbarrierhub/anime-dataset-2026

> dataset · [Kaggle](https://www.kaggle.com/datasets/darkbarrierhub/anime-dataset-2026)

일본 애니메이션 정보와 평점, 인기 등을 담은 데이터셋으로 분석과 추천에 활용 가능

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The genres of the anime, separated by commas.` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `The dataset facilitates the creation of recommendation systems, time series analysis, and clustering` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Recommendation systems leverage user ratings, genres, and other factors to suggest anime series` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `"anime-dataset-2026.csv"` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `The dataset offers valuable information for analyzing and comprehending the characteristics, ratings, popularity, and viewership of various anime shows.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Database: Open Database, Contents: Database Contents` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `popular culture, arts and entertainment, movies and tv shows, japan, anime and manga` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `By utilizing this dataset, one can conduct a wide range of analyses, including identifying the highest-rated anime` · 신뢰도 low
