---
type: "dataset"
id: "Meddies/meddies-embedding-data"
source: "huggingface"
url: "https://huggingface.co/datasets/Meddies/meddies-embedding-data"
downloads: 44
summary: "다국어 검색 임베딩 학습용 쿼리-본문 쌍 데이터셋으로, 합성 크로스링구얼 쿼리를 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Meddies/meddies-embedding-data

> dataset · [Hugging Face](https://huggingface.co/datasets/Meddies/meddies-embedding-data)

다국어 검색 임베딩 학습용 쿼리-본문 쌍 데이터셋으로, 합성 크로스링구얼 쿼리를 포함함.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Query/passage pairs for training multilingual retrieval embeddings` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `Query/passage pairs for training multilingual retrieval embeddings` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `Query/passage pairs for training multilingual retrieval embeddings` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each row is one generated query paired with the source passage it was grounded in` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Wikipedia across 17 languages, via `Meddies/wiki`` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Query/passage pairs for training multilingual retrieval embeddings` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
