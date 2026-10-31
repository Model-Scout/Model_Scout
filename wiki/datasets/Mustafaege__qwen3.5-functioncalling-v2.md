---
type: "dataset"
id: "Mustafaege/qwen3.5-functioncalling-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/Mustafaege/qwen3.5-functioncalling-v2"
downloads: 66
summary: "Qwen3.5 Function Calling Dataset v2는 영어와 한국어 함수 호출 예제로 Qwen3.5 모델 미세조정용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
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
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Mustafaege/qwen3.5-functioncalling-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/Mustafaege/qwen3.5-functioncalling-v2)

Qwen3.5 Function Calling Dataset v2는 영어와 한국어 함수 호출 예제로 Qwen3.5 모델 미세조정용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · tags, task_categories = `text-generation` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · readme, tags = `function-calling` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Qwen3 messages format` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Function call JSON or natural language reply` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Built for Qwen3.5 fine-tuning` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
