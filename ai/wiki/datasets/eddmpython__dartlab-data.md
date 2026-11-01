---
type: "dataset"
id: "eddmpython/dartlab-data"
source: "huggingface"
url: "https://huggingface.co/datasets/eddmpython/dartlab-data"
downloads: 347396
summary: "한국 DART와 미국 SEC EDGAR 공시 데이터를 종목코드로 비교 가능한 표로 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
  - "[[표 질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
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
  - "[[대규모 데이터]]"
---
# eddmpython/dartlab-data

> dataset · [Hugging Face](https://huggingface.co/datasets/eddmpython/dartlab-data)

한국 DART와 미국 SEC EDGAR 공시 데이터를 종목코드로 비교 가능한 표로 제공하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `한국 전 상장사(약 2,700사)와 미국 주요 상장사(약 1,000사)의 재무제표, 사업보고서 본문, 정형 공시, 주가, 거시지표가 들어 있습니다.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `DartLab이 한국 DART 전자공시와 미국 SEC EDGAR 공시를 종목코드 하나로 비교 가능한 표로 가공해 Parquet으로 올려둔 데이터셋입니다.` · 신뢰도 low
- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:table_qa = `Structured Korean (DART) and US (SEC EDGAR) disclosure data, ready as Parquet.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:retrieval, task:table_qa = `사업보고서 본문을 항목 × 기간 격자로` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `DartLab이 한국 DART 전자공시와 미국 SEC EDGAR 공시를 종목코드 하나로 비교 가능한 표로 가공해 Parquet으로 올려둔 데이터셋입니다.` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:table_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `DartLab의 데이터 층입니다. dartlab.Company("005930")을 호출하면 라이브러리가 필요한 parquet을 여기서 자동으로 내려받습니다.` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `Fundmanager145/dartlab-data`
- `idleengine/dartlab-data`
- `withdev/dartlab-data`
