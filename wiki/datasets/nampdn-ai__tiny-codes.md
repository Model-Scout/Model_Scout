---
type: "dataset"
id: "nampdn-ai/tiny-codes"
source: "huggingface"
url: "https://huggingface.co/datasets/nampdn-ai/tiny-codes"
downloads: 726
summary: "1.6백만 개의 명확한 코드 스니펫으로 LLM 모델의 언어 및 코드 추론 능력 향상용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
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
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# nampdn-ai/tiny-codes

> dataset · [Hugging Face](https://huggingface.co/datasets/nampdn-ai/tiny-codes)

1.6백만 개의 명확한 코드 스니펫으로 LLM 모델의 언어 및 코드 추론 능력 향상용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `help LLM models learn how to reason with both natural and programming languages` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `LLM models can achieve state-of-the-art results on code-related tasks by training on high-quality data` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:language_modeling = `code snippets are carefully written and commented to ensure maximum readability and understandability` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `help LLM models learn how to reason with both natural and programming languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This synthetic dataset is a collection of 1.6 millions short and clear code snippets` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This synthetic dataset is a collection of 1.6 millions short and clear code snippets that can help LLM models learn` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[daekeun-ml__phi-2-ko-v0.1|daekeun-ml/phi-2-ko-v0.1]]
