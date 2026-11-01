---
type: "dataset"
id: "kaggle/hardbr0/tv-series-metadata-dataset-10k-shows"
source: "kaggle"
url: "https://www.kaggle.com/datasets/hardbr0/tv-series-metadata-dataset-10k-shows"
downloads: 22
summary: "10,000개 TV 시리즈의 메타데이터로 인기, 평점, 국가, 언어 분석 및 추천에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/hardbr0/tv-series-metadata-dataset-10k-shows

> dataset · [Kaggle](https://www.kaggle.com/datasets/hardbr0/tv-series-metadata-dataset-10k-shows)

10,000개 TV 시리즈의 메타데이터로 인기, 평점, 국가, 언어 분석 및 추천에 활용 가능

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The `overview` column contains descriptions of the TV series, making the dataset suitable for Natural Language Processing (NLP) applications such as text classi` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `Build TF-IDF or embedding-based recommendation systems.` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — ner · readme = `Perform text similarity using `overview`.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Recommend similar shows based on titles and descriptions.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:generation, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Before performing analysis or machine learning, users should consider` · 신뢰도 low
