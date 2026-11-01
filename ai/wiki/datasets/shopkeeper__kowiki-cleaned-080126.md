---
type: "dataset"
id: "shopkeeper/kowiki-cleaned-080126"
source: "huggingface"
url: "https://huggingface.co/datasets/shopkeeper/kowiki-cleaned-080126"
downloads: 49
summary: "2026년 8월 1일자 한국어 위키백과 문서의 정제된 평문 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# shopkeeper/kowiki-cleaned-080126

> dataset · [Hugging Face](https://huggingface.co/datasets/shopkeeper/kowiki-cleaned-080126)

2026년 8월 1일자 한국어 위키백과 문서의 정제된 평문 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `Plain-text articles from the Korean Wikipedia dump` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Plain-text articles from the Korean Wikipedia dump` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling, task:retrieval = `Plain-text articles from the Korean Wikipedia dump` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Plain-text articles from the Korean Wikipedia dump` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `11178` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean Wikipedia, cleaned (2026-08-01 dump)` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Plain-text articles from the Korean Wikipedia dump` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 16767자 ≈ 11178 토큰 (viewer statistics, default/train)
