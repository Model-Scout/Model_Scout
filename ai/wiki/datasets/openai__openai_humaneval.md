---
type: "dataset"
id: "openai/openai_humaneval"
source: "huggingface"
url: "https://huggingface.co/datasets/openai/openai_humaneval"
downloads: 236808
summary: "OpenAI HumanEval은 164개의 파이썬 프로그래밍 문제와 단위 테스트를 포함한 코드 생성 평가용 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# openai/openai_humaneval

> dataset · [Hugging Face](https://huggingface.co/datasets/openai/openai_humaneval)

OpenAI HumanEval은 164개의 파이썬 프로그래밍 문제와 단위 테스트를 포함한 코드 생성 평가용 데이터셋입니다.

## 분류

- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `218` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `They were handwritten to ensure not to be included in the training set of code generation models.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `test` 열 p90 871자 ≈ 218 토큰 (viewer statistics, openai_humaneval/test)

## 이 데이터로 학습한 모델

- [[rico03__Qwopus-GLM-9B-DualReason-Distilled-GGUF|rico03/Qwopus-GLM-9B-DualReason-Distilled-GGUF]]
