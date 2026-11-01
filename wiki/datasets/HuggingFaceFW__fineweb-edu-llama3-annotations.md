---
type: "dataset"
id: "HuggingFaceFW/fineweb-edu-llama3-annotations"
source: "huggingface"
url: "https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu-llama3-annotations"
downloads: 749
summary: "FineWeb 웹페이지의 교육적 가치를 평가하기 위한 FineWeb-Edu 분류기 학습용 주석 데이터입니다."
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
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# HuggingFaceFW/fineweb-edu-llama3-annotations

> dataset · [Hugging Face](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu-llama3-annotations)

FineWeb 웹페이지의 교육적 가치를 평가하기 위한 FineWeb-Edu 분류기 학습용 주석 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `We prompt Llama-3-70B-Instruct to score web pages` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `FineWeb text sample, the prompt (using the first 1000 characters of the text sample)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `the scores` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1009` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `FineWeb-Edu educational quality classifier` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 4036자 ≈ 1009 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[tartuNLP__mmBERT-small-m-edu-classifier|tartuNLP/mmBERT-small-m-edu-classifier]]
