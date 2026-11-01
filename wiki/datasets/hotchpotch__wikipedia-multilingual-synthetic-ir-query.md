---
type: "dataset"
id: "hotchpotch/wikipedia-multilingual-synthetic-ir-query"
source: "huggingface"
url: "https://huggingface.co/datasets/hotchpotch/wikipedia-multilingual-synthetic-ir-query"
downloads: 1909
summary: "위키피디아 기반 다국어 합성 질의-문서 쌍 데이터로 정보 검색 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
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
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# hotchpotch/wikipedia-multilingual-synthetic-ir-query

> dataset · [Hugging Face](https://huggingface.co/datasets/hotchpotch/wikipedia-multilingual-synthetic-ir-query)

위키피디아 기반 다국어 합성 질의-문서 쌍 데이터로 정보 검색 학습용입니다.

## 분류

- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `pairs of (query, short document)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `pairs of (query, short document)` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1784` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `gfdl` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The source documents are Wikipedia-derived texts.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains multilingual Wikipedia-derived synthetic query-document pairs for information retrieval training.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `document` 열 p90 7135자 ≈ 1784 토큰 (viewer statistics, ko-long_doc/train)
