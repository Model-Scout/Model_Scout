---
type: "dataset"
id: "kaggle/darkbarrierhub/anime-dataset-2026-nsfw"
source: "kaggle"
url: "https://www.kaggle.com/datasets/darkbarrierhub/anime-dataset-2026-nsfw"
downloads: 24
summary: "일본 애니메이션(NSFW) 정보와 평점, 인기 등을 분석하고 추천 시스템에 활용하는 데이터셋입니다."
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
# kaggle/darkbarrierhub/anime-dataset-2026-nsfw

> dataset · [Kaggle](https://www.kaggle.com/datasets/darkbarrierhub/anime-dataset-2026-nsfw)

일본 애니메이션(NSFW) 정보와 평점, 인기 등을 분석하고 추천 시스템에 활용하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Genres: The genres of the anime, separated by commas.` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Recommendation systems leverage user ratings, genres, and other factors to suggest anime series` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `recommendations play a crucial role in helping enthusiasts discover new shows` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:retrieval = `anime_id: Unique ID for each anime. Name: The name of the anime in its original language. English name: The English name of the anime.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Score: The score or rating given to the anime. Genres: The genres of the anime, separated by commas. Synopsis: A brief description or summary of the anime's plo` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Database: Open Database, Contents: Database Contents` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `Anime is a popular form of entertainment originating from Japan.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset offers valuable information for analyzing and comprehending the characteristics, ratings, popularity, and viewership of various anime shows.` · 신뢰도 low
