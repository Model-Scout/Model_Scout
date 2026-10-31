---
type: "dataset"
id: "graelo/wikipedia"
source: "huggingface"
url: "https://huggingface.co/datasets/graelo/wikipedia"
downloads: 936
summary: "다국어 위키피디아 문서 정제 데이터셋으로, 최신 덤프를 기반으로 구축됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# graelo/wikipedia

> dataset · [Hugging Face](https://huggingface.co/datasets/graelo/wikipedia)

다국어 위키피디아 문서 정제 데이터셋으로, 최신 덤프를 기반으로 구축됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Each example contains the content of one full Wikipedia article with cleaning to strip markdown and unwanted sections` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_categories, task_ids = `fill-mask` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `Wikipedia dataset containing cleaned articles of all languages.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation, task:language_modeling, task:retrieval = `Each example contains the content of one full Wikipedia article with cleaning to strip markdown and unwanted sections` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Each example contains the content of one full Wikipedia article with cleaning to strip markdown and unwanted sections` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `316 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `4143` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-3.0` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `gfdl` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Wikipedia dataset containing cleaned articles of all languages.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The datasets are built from the Wikipedia dump (https://dumps.wikimedia.org/) with one split per language.` · 신뢰도 low
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 16571자 ≈ 4143 토큰 (viewer statistics, 20230601.ko/train)
