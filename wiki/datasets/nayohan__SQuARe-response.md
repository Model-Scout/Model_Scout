---
type: "dataset"
id: "nayohan/SQuARe-response"
source: "huggingface"
url: "https://huggingface.co/datasets/nayohan/SQuARe-response"
downloads: 43
summary: "SQuARe는 민감한 질문과 적절한 응답으로 구성된 대규모 한국어 안전성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nayohan/SQuARe-response

> dataset · [Hugging Face](https://huggingface.co/datasets/nayohan/SQuARe-response)

SQuARe는 민감한 질문과 적절한 응답으로 구성된 대규모 한국어 안전성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `SQuARe: A Large-Scale Dataset of Sensitive Questions and Acceptable Responses` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Sensitive Questions and Acceptable Responses` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Sensitive Questions and Acceptable Responses` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `136` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `SQuARe: A Large-Scale Dataset of Sensitive Questions and Acceptable Responses` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A Large-Scale Dataset of Sensitive Questions and Acceptable Responses Created Through Human-Machine Collaboration` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `response_en` 열 p90 204자 ≈ 136 토큰 (viewer statistics, default/test)

## 같은 데이터의 사본·중복 등록

- `nayohan/SQuARe-question`
