---
type: "dataset"
id: "youngbongbong/subway_od"
source: "huggingface"
url: "https://huggingface.co/datasets/youngbongbong/subway_od"
downloads: 24
summary: "서울 수도권 지하철의 역 간 이동 흐름과 공간 이동 구조 분석을 위한 지하철 출발-도착 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
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
# youngbongbong/subway_od

> dataset · [Hugging Face](https://huggingface.co/datasets/youngbongbong/subway_od)

서울 수도권 지하철의 역 간 이동 흐름과 공간 이동 구조 분석을 위한 지하철 출발-도착 데이터입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `The dataset can be used to construct OD matrices, analyze inter-station connectivity, and compare subway flows with cell-based population mobility data.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `It supports analysis of station-to-station movement flows and spatial mobility structures.` · 신뢰도 low
- **작업**: [[표 데이터 예측]] — metadata · task_categories = `tabular-classification` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme, task:tabular_prediction = `Main Columns
- origin_station_id: Origin subway station identifier
- destination_station_id: Destination subway station identifier
- origin_station_name: Origin` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Main Columns
- origin_station_id: Origin subway station identifier
- destination_station_id: Destination subway station identifier
- origin_station_name: Origin` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — tag_match · readme, tags = `transportation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is intended for OD matrix construction, subway flow analysis, and urban transportation demand modeling.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
