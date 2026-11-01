---
type: "dataset"
id: "cyankiwi/calibration-medium"
source: "huggingface"
url: "https://huggingface.co/datasets/cyankiwi/calibration-medium"
downloads: 59
summary: "16개 언어, 6개 도메인 대화 데이터셋으로 에이전트 및 도구 사용 추적에 중점."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# cyankiwi/calibration-medium

> dataset · [Hugging Face](https://huggingface.co/datasets/cyankiwi/calibration-medium)

16개 언어, 6개 도메인 대화 데이터셋으로 에이전트 및 도구 사용 추적에 중점.

## 분류

- **작업**: [[임베딩]] — ner · readme = `A 16-language, 6-domain calibration dataset: 12,800 conversations` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · tags = `tool-use` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation = `the chat transcript, one struct per message` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `the chat transcript, one struct per message` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A 16-language, 6-domain calibration dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `12,800 conversations ≈ 268.7M tokens` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
