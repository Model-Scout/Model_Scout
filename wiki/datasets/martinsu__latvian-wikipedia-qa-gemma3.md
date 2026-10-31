---
type: "dataset"
id: "martinsu/latvian-wikipedia-qa-gemma3"
source: "huggingface"
url: "https://huggingface.co/datasets/martinsu/latvian-wikipedia-qa-gemma3"
downloads: 35
summary: "라트비아어 위키백과 문서 기반의 다중턴 질의응답 합성 데이터셋으로, 라트비아어 QA 및 대화형 AI 학습에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[lv]]"
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
# martinsu/latvian-wikipedia-qa-gemma3

> dataset · [Hugging Face](https://huggingface.co/datasets/martinsu/latvian-wikipedia-qa-gemma3)

라트비아어 위키백과 문서 기반의 다중턴 질의응답 합성 데이터셋으로, 라트비아어 QA 및 대화형 AI 학습에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — tag_match · readme, tags = `conversational` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · readme, tags, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `Multi-turn conversations with user-assistant exchanges` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Multi-turn conversations with user-assistant exchanges` · 신뢰도 medium
- **언어**: [[lv]] — metadata · languages = `lv` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[martinsu__tildeopen-30b-mu-instruct|martinsu/tildeopen-30b-mu-instruct]]
