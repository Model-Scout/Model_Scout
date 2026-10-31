---
type: "dataset"
id: "HuggingFaceTB/cosmopedia"
source: "huggingface"
url: "https://huggingface.co/datasets/HuggingFaceTB/cosmopedia"
downloads: 24123
summary: "Mixtral-8x7B-Instruct-v0.1 모델로 생성한 3천만 개 이상의 합성 교재, 블로그, 이야기 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# HuggingFaceTB/cosmopedia

> dataset · [Hugging Face](https://huggingface.co/datasets/HuggingFaceTB/cosmopedia)

Mixtral-8x7B-Instruct-v0.1 모델로 생성한 3천만 개 이상의 합성 교재, 블로그, 이야기 데이터셋입니다.

## 분류

- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `The prompts are all based on the concept of using a seed sample (for example an extract from a web page) and asking the model to generate new content` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1285` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 5140자 ≈ 1285 토큰 (viewer statistics, auto_math_text/train)

## 이 데이터로 학습한 모델

- [[pathcosmos__frankenstallm|pathcosmos/frankenstallm]]
