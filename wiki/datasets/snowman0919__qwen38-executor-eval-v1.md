---
type: "dataset"
id: "snowman0919/qwen38-executor-eval-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/snowman0919/qwen38-executor-eval-v1"
downloads: 181
summary: "Qwen3.8 Executor 평가용 데이터셋으로 도구 사용 및 컴퓨터 작업 평가에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[도구 호출]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# snowman0919/qwen38-executor-eval-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/snowman0919/qwen38-executor-eval-v1)

Qwen3.8 Executor 평가용 데이터셋으로 도구 사용 및 컴퓨터 작업 평가에 활용됨.

## 분류

- **작업**: [[도구 호출]] — tag_match · readme, tags = `tool-calling` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `Images and executable artifacts are self-contained bytes where included.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `DO NOT USE FOR TRAINING. This repository contains evaluation-only tasks and model outputs.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
