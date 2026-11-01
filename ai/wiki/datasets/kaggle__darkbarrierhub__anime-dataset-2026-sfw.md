---
type: "dataset"
id: "kaggle/darkbarrierhub/anime-dataset-2026-sfw"
source: "kaggle"
url: "https://www.kaggle.com/datasets/darkbarrierhub/anime-dataset-2026-sfw"
downloads: 20
summary: "일본 애니메이션 정보와 평점, 인기 등을 포함한 데이터셋으로 추천 시스템 등에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[시계열 예측]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/darkbarrierhub/anime-dataset-2026-sfw

> dataset · [Kaggle](https://www.kaggle.com/datasets/darkbarrierhub/anime-dataset-2026-sfw)

일본 애니메이션 정보와 평점, 인기 등을 포함한 데이터셋으로 추천 시스템 등에 활용 가능

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Score: The score or rating given to the anime.` · 신뢰도 low
- **작업**: [[시계열 예측]] — ner · readme = `the dataset facilitates the creation of recommendation systems, time series analysis, and clustering to delve deeper into anime trends and user behavior.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Recommendation systems leverage user ratings, genres, and other factors to suggest anime series that users might enjoy based on their preferences.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:retrieval = `anime-dataset-2026-sfw.csv` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Score: The score or rating given to the anime.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Database: Open Database, Contents: Database Contents` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `popular culture, arts and entertainment, movies and tv shows, japan, anime and manga` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset offers valuable information for analyzing and comprehending the characteristics, ratings, popularity, and viewership of various anime shows.` · 신뢰도 low
