---
type: "dataset"
id: "yiseo0/GIS-Bench"
source: "huggingface"
url: "https://huggingface.co/datasets/yiseo0/GIS-Bench"
downloads: 43
summary: "GIS-Bench는 LLM 기반 GIS 자동화 에이전트의 공간 분석 작업 수행 능력을 평가하는 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[위치·좌표 (입력 형식)|위치·좌표]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[지리·위치]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# yiseo0/GIS-Bench

> dataset · [Hugging Face](https://huggingface.co/datasets/yiseo0/GIS-Bench)

GIS-Bench는 LLM 기반 GIS 자동화 에이전트의 공간 분석 작업 수행 능력을 평가하는 벤치마크입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `evaluate the capability of Large Language Model (LLM)-based agents in automating GIS (Geographic Information System) tasks` · 신뢰도 low
- **작업**: [[텍스트 생성]] — tag_match · tags = `LLM` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `targets real-world spatial analysis workflows executable in QGIS Desktop via Claude + MCP` · 신뢰도 low
- **입력 형식**: [[위치·좌표 (입력 형식)|위치·좌표]] — metadata · modality = `geospatial` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `Output Format | HTML (Leaflet.js map), PNG, JPG` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation, task:retrieval = `Natural language instruction (Korean)` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `Output Format | HTML (Leaflet.js map), PNG, JPG` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[지리·위치]] — ner · readme = `GIS (Geographic Information System) tasks` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `This benchmark was developed as part of a master's thesis research and targets real-world spatial analysis workflows` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Benchmark tasks, evaluation code, and results` · 신뢰도 low
