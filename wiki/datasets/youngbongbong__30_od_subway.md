---
type: "dataset"
id: "youngbongbong/30_od_subway"
source: "huggingface"
url: "https://huggingface.co/datasets/youngbongbong/30_od_subway"
downloads: 203
summary: "서울 수도권 지하철역 30분 단위 승하차 통계로 모빌리티 수요 분석에 활용."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
  - "[[표 데이터 예측]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# youngbongbong/30_od_subway

> dataset · [Hugging Face](https://huggingface.co/datasets/youngbongbong/30_od_subway)

서울 수도권 지하철역 30분 단위 승하차 통계로 모빌리티 수요 분석에 활용.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `It is intended for mobility demand analysis, temporal flow pattern analysis, and comparison with other urban mobility datasets.` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-classification` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme, task:tabular_prediction = `Each file provides station-level subway usage statistics aggregated by 30-minute time windows.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Each file provides station-level subway usage statistics aggregated by 30-minute time windows.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — tag_match · readme, tags = `transportation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Each file provides station-level subway usage statistics aggregated by 30-minute time windows.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
