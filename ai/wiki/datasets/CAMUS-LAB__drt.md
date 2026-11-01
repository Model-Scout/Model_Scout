---
type: "dataset"
id: "CAMUS-LAB/drt"
source: "huggingface"
url: "https://huggingface.co/datasets/CAMUS-LAB/drt"
downloads: 24
summary: "다도시 DRT 시뮬레이션 벤치마킹용 통합 입력 데이터셋으로 NYC, Chicago, 성남시 데이터를 포함한다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[시계열 예측]]"
  - "[[문서 검색]]"
input_modality:
  - "[[위치·좌표 (입력 형식)|위치·좌표]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# CAMUS-LAB/drt

> dataset · [Hugging Face](https://huggingface.co/datasets/CAMUS-LAB/drt)

다도시 DRT 시뮬레이션 벤치마킹용 통합 입력 데이터셋으로 NYC, Chicago, 성남시 데이터를 포함한다.

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `다도시 DRT 알고리즘 벤치마킹, 배차/리밸런싱 비교, 차량대수 산정 검증, 도시 카테고리 일반화 연구` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `다도시 DRT 알고리즘 벤치마킹, 배차/리밸런싱 비교, 차량대수 산정 검증, 도시 카테고리 일반화 연구` · 신뢰도 low
- **입력 형식**: [[위치·좌표 (입력 형식)|위치·좌표]] — metadata · modality = `geospatial` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `수요·도로 네트워크·차량 데이터를 공통 스키마로 정제하여 제공한다` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:retrieval = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `수요·도로 네트워크·차량 데이터를 공통 스키마로 정제하여 제공한다` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — ner · readme = `다도시 DRT(Demand-Responsive Transport) 시뮬레이션 벤치마킹을 위한 통합 입력 데이터셋` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `초기 공개판: NYC / Chicago / Seongnam 3개 도시 raw 입력 데이터, Dataset Card 및 통합 스키마 명세 추가` · 신뢰도 low
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high
