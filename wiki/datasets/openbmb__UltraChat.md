---
type: "dataset"
id: "openbmb/UltraChat"
source: "huggingface"
url: "https://huggingface.co/datasets/openbmb/UltraChat"
downloads: 6485
summary: "Turbo API 기반의 대규모 다중 라운드 대화 데이터로, 다양한 주제의 질의응답과 창작 지원에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# openbmb/UltraChat

> dataset · [Hugging Face](https://huggingface.co/datasets/openbmb/UltraChat)

Turbo API 기반의 대규모 다중 라운드 대화 데이터로, 다양한 주제의 질의응답과 창작 지원에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `dialogue data in a list format` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `dialogue data in a list format` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The topics covered are extensive, spanning areas such as technology, art, and entrepreneurship.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The generated dialogues undergo further post-processing and filtering.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[llm-semantic-router__mmbert32k-modality-router-merged|llm-semantic-router/mmbert32k-modality-router-merged]]
- [[vllm-sr__mmbert32k-modality-router-merged|vllm-sr/mmbert32k-modality-router-merged]]
