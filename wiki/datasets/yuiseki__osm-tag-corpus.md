---
type: "dataset"
id: "yuiseki/osm-tag-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/yuiseki/osm-tag-corpus"
downloads: 88
summary: "OpenStreetMap 태그와 다국어 설명, 관련 용어, 사용 빈도를 담은 임베딩용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[지리·위치]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# yuiseki/osm-tag-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/yuiseki/osm-tag-corpus)

OpenStreetMap 태그와 다국어 설명, 관련 용어, 사용 빈도를 담은 임베딩용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, tags, task_categories = `feature-extraction` · 신뢰도 high
- **작업**: [[문서 검색]] — tag_match · readme, tags = `retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `every tag the OSM wiki documents, with its description in each language it is documented in, its related terms` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The format in which a tag becomes a sentence changes how well it retrieves` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `20 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `29` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odbl` · 신뢰도 high
- **도메인**: [[지리·위치]] — ner · readme = `Frozen source material for embedding OpenStreetMap tags: every tag the OSM wiki documents` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Built from taginfo dumps of 2026-01-30.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `description` 열 p90 117자 ≈ 29 토큰 (viewer statistics, default/train)
