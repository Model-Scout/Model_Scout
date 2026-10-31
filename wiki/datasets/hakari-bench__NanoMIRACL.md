---
type: "dataset"
id: "hakari-bench/NanoMIRACL"
source: "huggingface"
url: "https://huggingface.co/datasets/hakari-bench/NanoMIRACL"
downloads: 2239
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[리랭킹]]"
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
  - "[[중규모 데이터]]"
---
# hakari-bench/NanoMIRACL

> dataset · [Hugging Face](https://huggingface.co/datasets/hakari-bench/NanoMIRACL)

## 분류

- **작업**: [[리랭킹]] — tag_match · tags = `reranking` · 신뢰도 medium
- **작업**: [[문서 검색]] — tag_match · tags = `retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:reranking, task:retrieval = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `18 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
