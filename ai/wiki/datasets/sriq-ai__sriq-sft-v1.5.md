---
type: "dataset"
id: "sriq-ai/sriq-sft-v1.5"
source: "huggingface"
url: "https://huggingface.co/datasets/sriq-ai/sriq-sft-v1.5"
downloads: 64
summary: "다국어 질문과 중국어 추론을 포함한 ShareGPT 호환 감독 학습 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# sriq-ai/sriq-sft-v1.5

> dataset · [Hugging Face](https://huggingface.co/datasets/sriq-ai/sriq-sft-v1.5)

다국어 질문과 중국어 추론을 포함한 ShareGPT 호환 감독 학습 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[도구 호출]] — tag_match · tags = `tool-use` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `ShareGPT-compatible supervised fine-tuning conversations.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Assistant targets contain compressed Simplified Chinese reasoning and the original final answer.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `multilingual` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Questions are generated in many languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `ShareGPT-compatible supervised fine-tuning conversations.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[sriq-ai__sriq-MiniCPM5-2B-v1.5|sriq-ai/sriq-MiniCPM5-2B-v1.5]]
