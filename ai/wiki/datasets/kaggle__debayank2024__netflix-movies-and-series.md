---
type: "dataset"
id: "kaggle/debayank2024/netflix-movies-and-series"
source: "kaggle"
url: "https://www.kaggle.com/datasets/debayank2024/netflix-movies-and-series"
downloads: 13217
summary: "넷플릭스 영화 및 시리즈 8,800여 편의 장르, 평점, 국가별 정보를 담은 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/debayank2024/netflix-movies-and-series

> dataset · [Kaggle](https://www.kaggle.com/datasets/debayank2024/netflix-movies-and-series)

넷플릭스 영화 및 시리즈 8,800여 편의 장르, 평점, 국가별 정보를 담은 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `metadata like cast, director, country of production, genre tags, and a short synopsis` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Exploring 8,800+ Movies & Series: Genres, Ratings, and Global Reach on Netflix` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `Each row has one title (movie or series) available on Netflix, with metadata like cast, director, country of production, genre tags, and a short synopsis.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each row has one title (movie or series) available on Netflix, with metadata like cast, director, country of production, genre tags, and a short synopsis.` · 신뢰도 low
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `Movies & Series: Genres, Ratings, and Global Reach on Netflix` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Each row has one title (movie or series) available on Netflix, with metadata like cast, director, country of production, genre tags, and a short synopsis.` · 신뢰도 low
