---
type: "dataset"
id: "kaggle/soundslikedata/movies-rating-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/soundslikedata/movies-rating-dataset"
downloads: 182
summary: "영화 평점 데이터셋으로 영화 장르, 언어, 평점 등의 정보를 포함합니다."
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
  - "[[조건부 이용]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/soundslikedata/movies-rating-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/soundslikedata/movies-rating-dataset)

영화 평점 데이터셋으로 영화 장르, 언어, 평점 등의 정보를 포함합니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `The average rating given to the movie, typically on a scale from 1 to 10.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `A measure of how popular the movie is, usually based on user ratings or views` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:retrieval = `| Column Name | Description |` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `| Column Name | Description |` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Other (specified in description)` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `movies and tv shows` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `출처: Kaggle (soundslikedata/movies-rating-dataset)` · 신뢰도 low
