---
type: "dataset"
id: "neuralchemy/Prompt-injection-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/neuralchemy/Prompt-injection-dataset"
downloads: 2894
summary: "대형 언어 모델의 프롬프트 인젝션 및 탈옥 공격 탐지를 위한 이진 분류 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
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
# neuralchemy/Prompt-injection-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/neuralchemy/Prompt-injection-dataset)

대형 언어 모델의 프롬프트 인젝션 및 탈옥 공격 탐지를 위한 이진 분류 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Raw prompt text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Prompt Injection & Jailbreak Detection Dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Two configs — core for classical ML, full for transformers` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Horizon-Labs__prompt-injection-guard-base|Horizon-Labs/prompt-injection-guard-base]]
- [[Horizon-Labs__prompt-injection-guard-large|Horizon-Labs/prompt-injection-guard-large]]
- [[Horizon-Labs__prompt-injection-guard-small|Horizon-Labs/prompt-injection-guard-small]]
