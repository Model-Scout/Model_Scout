---
type: "dataset"
id: "uonlp/CulturaX"
source: "huggingface"
url: "https://huggingface.co/datasets/uonlp/CulturaX"
downloads: 25647
readme_status: "ok"
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
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# uonlp/CulturaX

> dataset · [Hugging Face](https://huggingface.co/datasets/uonlp/CulturaX)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 high
- **작업**: [[언어 모델링]] — metadata · task_categories, task_ids = `fill-mask` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:language_modeling = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:language_modeling = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `167 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `9999999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[GuminiResearch__Gumini-1B-Base|GuminiResearch/Gumini-1B-Base]]
- [[dynamofl__dynamo-8B-v0.1|dynamofl/dynamo-8B-v0.1]]
- [[jjhsnail0822__danube-ko-1.8b-base|jjhsnail0822/danube-ko-1.8b-base]]
- [[mradermacher__Gumini-1B-Base-inherit-GGUF|mradermacher/Gumini-1B-Base-inherit-GGUF]]
- [[mradermacher__Gumini-1B-Base-inherit-i1-GGUF|mradermacher/Gumini-1B-Base-inherit-i1-GGUF]]
