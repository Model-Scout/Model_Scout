---
type: "dataset"
id: "yena0rganization/global-llm-value-gap"
source: "huggingface"
url: "https://huggingface.co/datasets/yena0rganization/global-llm-value-gap"
downloads: 29
summary: "WVS 기반 66개국 윤리 문항 응답으로 LLM과 인간 가치관 괴리 측정 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# yena0rganization/global-llm-value-gap

> dataset · [Hugging Face](https://huggingface.co/datasets/yena0rganization/global-llm-value-gap)

WVS 기반 66개국 윤리 문항 응답으로 LLM과 인간 가치관 괴리 측정 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — tag_match · tags = `LLM` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `23개 윤리 문항에 대한 응답을 수집하고` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `23개 윤리 문항에 대한 응답을 수집하고` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `World Values Survey(WVS) Wave 7 기반 시뮬레이션 응답 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터셋은 대규모 언어 모델(LLM)과 인간 집단 간의 가치관 괴리를 측정하기 위해 구축된 World Values Survey(WVS) Wave 7 기반 시뮬레이션 응답 데이터셋입니다.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `ynchoi/global-llm-value-gap`
