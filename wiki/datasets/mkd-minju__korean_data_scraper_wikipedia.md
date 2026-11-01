---
type: "dataset"
id: "mkd-minju/korean_data_scraper_wikipedia"
source: "huggingface"
url: "https://huggingface.co/datasets/mkd-minju/korean_data_scraper_wikipedia"
downloads: 267
summary: "한국어 위키백과 문서 본문 텍스트를 추출한 코퍼스입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# mkd-minju/korean_data_scraper_wikipedia

> dataset · [Hugging Face](https://huggingface.co/datasets/mkd-minju/korean_data_scraper_wikipedia)

한국어 위키백과 문서 본문 텍스트를 추출한 코퍼스입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `한국어 위키백과(ko.wikipedia.org) 덤프를 파싱하여 문서 본문 텍스트를 추출한 결과입니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `문서 본문 텍스트를 추출한 결과입니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `문서 본문 텍스트를 추출한 결과입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Korean_data_scraper 프로젝트의 wikipedia_dump 소스가 생성한 코퍼스입니다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `Hikaf143/korean_data_scraper_wikipedia`
