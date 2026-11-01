---
type: "dataset"
id: "Salesforce/wikitext"
source: "huggingface"
url: "https://huggingface.co/datasets/Salesforce/wikitext"
downloads: 2025231
summary: "위키피디아의 검증된 문서에서 추출한 1억 개 이상의 토큰으로 구성된 언어 모델링 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Salesforce/wikitext

> dataset · [Hugging Face](https://huggingface.co/datasets/Salesforce/wikitext)

위키피디아의 검증된 문서에서 추출한 1억 개 이상의 토큰으로 구성된 언어 모델링 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_categories, task_ids = `fill-mask` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `The WikiText language modeling dataset is a collection of over 100 million tokens` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `The WikiText language modeling dataset is a collection of over 100 million tokens` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `235` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `gfdl` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `extracted from the set of verified Good and Featured articles on Wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The WikiText language modeling dataset is a collection of over 100 million tokens` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 942자 ≈ 235 토큰 (viewer statistics, wikitext-103-raw-v1/validation)

## 이 데이터로 학습한 모델

- [[MESHIVEAI__Qwen-3.8-27B-Q4_K_M-Imatrix|MESHIVEAI/Qwen-3.8-27B-Q4_K_M-Imatrix]]
- [[mp-juuuns__qwen3.5-4l-vocab40k-en-ko-headless|mp-juuuns/qwen3.5-4l-vocab40k-en-ko-headless]]
