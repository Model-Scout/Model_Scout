---
type: "dataset"
id: "eddmpython/cleangov-local-settlements"
source: "huggingface"
url: "https://huggingface.co/datasets/eddmpython/cleangov-local-settlements"
downloads: 309
summary: "지방재정365 결산 통계 Open API로 자치단체 재정 결산 데이터를 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# eddmpython/cleangov-local-settlements

> dataset · [Hugging Face](https://huggingface.co/datasets/eddmpython/cleangov-local-settlements)

지방재정365 결산 통계 Open API로 자치단체 재정 결산 데이터를 제공하는 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `지방재정365 결산 통계 Open API (세입·세출결산, 재무제표, 지방세, 지역통합재정통계, 공공시설·청사·채무)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `세출결산(기능별·성질별·회계별·구조별 단체별), 세입결산(재원별·성질별), 기금결산, 교육비특별회계 결산, 투자적경비 순계, 재무제표(재정상태표·통합재정운영표·순자산변동표·복식부기 수익·비용·자산·부채), 지방세(징수율·세목별 비중·세수신장률·체납 누계), 지역통합재정통계 (세입·세출·` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `지방재정365 결산 통계 Open API (세입·세출결산, 재무제표, 지방세, 지역통합재정통계, 공공시설·청사·채무)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `자치단체 재정의 결산 기준 정본이며` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `지방재정365 결산 통계 Open API` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
