---
type: "dataset"
id: "CAMUS-LAB/data-road_network_eta"
source: "huggingface"
url: "https://huggingface.co/datasets/CAMUS-LAB/data-road_network_eta"
downloads: 932
summary: "16개 광역지자체 도로망 그래프와 시간대별 평균 통행속도 데이터로 ETA 산정에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[교통·모빌리티]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# CAMUS-LAB/data-road_network_eta

> dataset · [Hugging Face](https://huggingface.co/datasets/CAMUS-LAB/data-road_network_eta)

16개 광역지자체 도로망 그래프와 시간대별 평균 통행속도 데이터로 ETA 산정에 활용 가능

## 분류

- **작업**: [[문서 검색]] — ner · readme = `ETA(예상소요시간) 산정·라우팅·배차 시뮬레이션에 바로 사용 가능합니다.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · modality, readme = `{region}_osm_v3_nodes.parquet — 노드 (node_id, lat, lon)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `시간대별 평균 통행속도(p50)가 부착되어 있어 ETA(예상소요시간) 산정·라우팅·배차 시뮬레이션에 바로 사용 가능합니다.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — tag_match · readme, tags = `transportation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `프로젝트 코드(`phase_d_attach.py`) 참조.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
