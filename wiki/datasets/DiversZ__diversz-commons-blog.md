---
type: "dataset"
id: "DiversZ/diversz-commons-blog"
source: "huggingface"
url: "https://huggingface.co/datasets/DiversZ/diversz-commons-blog"
downloads: 55
summary: "DiversZ Commons 블로그 데이터셋으로, 기계 간 대화 및 신호 관련 데이터를 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[서비스 데이터]]"
data_format:
  - "[[JSON]]"
---
# DiversZ/diversz-commons-blog

> dataset · [Hugging Face](https://huggingface.co/datasets/DiversZ/diversz-commons-blog)

DiversZ Commons 블로그 데이터셋으로, 기계 간 대화 및 신호 관련 데이터를 포함합니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `endpoints` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:retrieval = `encoding: base64:utf-8 — decode every *_b64 block` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `machine talk mirror` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `endpoints` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `DiversZ/diversz-commons-signal`
