---
type: "dataset"
id: "NoeFlandre/landuse-sentence-relevance-golden-human-set"
source: "huggingface"
url: "https://huggingface.co/datasets/NoeFlandre/landuse-sentence-relevance-golden-human-set"
downloads: 81
summary: "85개 언어로 된 토지 이용 문장 관련성 골든 휴먼 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
input_modality:
  - "[[위치·좌표 (입력 형식)|위치·좌표]]"
  - "[[표 (입력 형식)|표]]"
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
  - "[[조건부 이용]]"
domain:
  - "[[지리·위치]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# NoeFlandre/landuse-sentence-relevance-golden-human-set

> dataset · [Hugging Face](https://huggingface.co/datasets/NoeFlandre/landuse-sentence-relevance-golden-human-set)

85개 언어로 된 토지 이용 문장 관련성 골든 휴먼 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `Land-use sentence relevance golden human set` · 신뢰도 low
- **입력 형식**: [[위치·좌표 (입력 형식)|위치·좌표]] — metadata · modality = `geospatial` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:retrieval = `sentence` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `label` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `85 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `22` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[지리·위치]] — ner · readme = `polygon_name, h3_cell, latitude, longitude` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Each subset has a single `train` split.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `sentence` 열 p90 88자 ≈ 22 토큰 (viewer statistics, ko/train)
