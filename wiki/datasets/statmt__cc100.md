---
type: "dataset"
id: "statmt/cc100"
source: "huggingface"
url: "https://huggingface.co/datasets/statmt/cc100"
downloads: 1008
summary: "100개 이상의 언어와 로마자 언어 데이터를 포함한 XLM-R 학습용 단일언어 말뭉치입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# statmt/cc100

> dataset · [Hugging Face](https://huggingface.co/datasets/statmt/cc100)

100개 이상의 언어와 로마자 언어 데이터를 포함한 XLM-R 학습용 단일언어 말뭉치입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_categories, task_ids = `fill-mask` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `This corpus comprises of monolingual data for 100+ languages and also includes data for romanized languages` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `This corpus comprises of monolingual data for 100+ languages and also includes data for romanized languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `109 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This corpus is an attempt to recreate the dataset used for training XLM-R.` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[pathcosmos__frankenstallm|pathcosmos/frankenstallm]]
