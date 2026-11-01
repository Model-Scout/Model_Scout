---
type: "dataset"
id: "legacy-datasets/wikipedia"
source: "huggingface"
url: "https://huggingface.co/datasets/legacy-datasets/wikipedia"
downloads: 49130
summary: "위키피디아 덤프에서 언어별로 정제한 전체 문서 데이터를 담은 데이터셋입니다."
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
  - "[[상업 이용 가능]]"
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# legacy-datasets/wikipedia

> dataset · [Hugging Face](https://huggingface.co/datasets/legacy-datasets/wikipedia)

위키피디아 덤프에서 언어별로 정제한 전체 문서 데이터를 담은 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_categories, task_ids = `fill-mask` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Each example contains the content of one full Wikipedia article` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Each example contains the content of one full Wikipedia article` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `294 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `gfdl` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Wikipedia dataset containing cleaned articles of all languages.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The datasets are built from the Wikipedia dump` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Blaxzter__LaBSE-sentence-embeddings|Blaxzter/LaBSE-sentence-embeddings]]
- [[ai-forever__mGPT|ai-forever/mGPT]]
- [[google__canine-c|google/canine-c]]
- [[google__canine-s|google/canine-s]]
- [[michaelfeil__ct2fast-LaBSE|michaelfeil/ct2fast-LaBSE]]
- [[setu4993__LEALLA-base|setu4993/LEALLA-base]]
- [[setu4993__LEALLA-large|setu4993/LEALLA-large]]
- [[setu4993__LEALLA-small|setu4993/LEALLA-small]]
- [[setu4993__LaBSE|setu4993/LaBSE]]
- [[setu4993__smaller-LaBSE|setu4993/smaller-LaBSE]]
