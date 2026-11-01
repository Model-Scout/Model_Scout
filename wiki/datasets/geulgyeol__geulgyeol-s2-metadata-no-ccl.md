---
type: "dataset"
id: "geulgyeol/geulgyeol-s2-metadata-no-ccl"
source: "huggingface"
url: "https://huggingface.co/datasets/geulgyeol/geulgyeol-s2-metadata-no-ccl"
downloads: 24
summary: "geulgyeol-s2-metadata-no-ccl 데이터셋은 메타데이터와 메타데이터-노-CCL 게시물로 구성된 실험용 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# geulgyeol/geulgyeol-s2-metadata-no-ccl

> dataset · [Hugging Face](https://huggingface.co/datasets/geulgyeol/geulgyeol-s2-metadata-no-ccl)

geulgyeol-s2-metadata-no-ccl 데이터셋은 메타데이터와 메타데이터-노-CCL 게시물로 구성된 실험용 데이터입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `The dataset contains only metadata-no-ccl posts and/or metadata.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `The dataset contains only metadata-no-ccl posts and/or metadata.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The dataset contains only metadata-no-ccl posts and/or metadata.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This is an experimental preview and still WIP.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
