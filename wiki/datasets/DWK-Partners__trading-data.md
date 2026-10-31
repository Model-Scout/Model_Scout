---
type: "dataset"
id: "DWK-Partners/trading-data"
source: "huggingface"
url: "https://huggingface.co/datasets/DWK-Partners/trading-data"
downloads: 17731
summary: "한국 DART와 미국 EDGAR 전자공시 데이터를 구조화하여 기업 공시 정보를 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[문서 검색]]"
  - "[[표 질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# DWK-Partners/trading-data

> dataset · [Hugging Face](https://huggingface.co/datasets/DWK-Partners/trading-data)

한국 DART와 미국 EDGAR 전자공시 데이터를 구조화하여 기업 공시 정보를 제공하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `Full-text sections from annual/quarterly reports, parsed into structured blocks.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Structured company data from DART & EDGAR disclosure filings` · 신뢰도 low
- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:information_extraction, task:retrieval, task:table_qa = `Full-text sections from annual/quarterly reports, parsed into structured blocks.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:table_qa = `Full-text sections from annual/quarterly reports, parsed into structured blocks.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Pre-collected Parquet files from DartLab — a Python library that turns DART (Korea) and EDGAR (US) disclosure filings into one structured company map.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `DWKPartners/dartlab-data`
- `DWKPartners/trading-data`
- `DaffyDevESP/trading-data`
- `Snowfall0601/dartlab-data`
