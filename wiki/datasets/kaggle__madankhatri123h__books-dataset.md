---
type: "dataset"
id: "kaggle/madankhatri123h/books-dataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/madankhatri123h/books-dataset"
downloads: 3492
summary: "Google Books API 기반의 다양한 책 메타데이터를 포함한 도서 데이터셋으로 출판 및 독자 분석에 활용 가능"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/madankhatri123h/books-dataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/madankhatri123h/books-dataset)

Google Books API 기반의 다양한 책 메타데이터를 포함한 도서 데이터셋으로 출판 및 독자 분석에 활용 가능

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Genre Analysis: Explore genre distribution and their characteristics (e.g., page length, ratings).` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Explore genre distribution and their characteristics (e.g., page length, ratings).` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Book Recommendation Systems: Analyze titles, genres, and ratings to build recommendation algorithms.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Book Recommendation Systems: Analyze titles, genres, and ratings to build recommendation algorithms.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Apache 2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset, sourced from the Google Books API with some manually added entries, contains detailed information about a collection of books across various genre` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `It is designed for researchers, data analysts, and enthusiasts interested in exploring book metadata, publication trends, and reader engagement.` · 신뢰도 low
