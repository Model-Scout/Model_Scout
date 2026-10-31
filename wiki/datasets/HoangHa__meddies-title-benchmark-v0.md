---
type: "dataset"
id: "HoangHa/meddies-title-benchmark-v0"
source: "huggingface"
url: "https://huggingface.co/datasets/HoangHa/meddies-title-benchmark-v0"
downloads: 28
summary: "17개 언어별 200개씩 총 3,400개의 그룹 분리 쿼리로 구성된 Meddies Title 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# HoangHa/meddies-title-benchmark-v0

> dataset · [Hugging Face](https://huggingface.co/datasets/HoangHa/meddies-title-benchmark-v0)

17개 언어별 200개씩 총 3,400개의 그룹 분리 쿼리로 구성된 Meddies Title 평가용 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `3,400 group-isolated queries, exactly 200 per language across 17 languages` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `3,400 group-isolated queries` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Private frozen evaluation subset for Meddies Title v0` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
