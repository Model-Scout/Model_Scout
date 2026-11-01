---
type: "dataset"
id: "bookcorpus/bookcorpus"
source: "huggingface"
url: "https://huggingface.co/datasets/bookcorpus/bookcorpus"
downloads: 13225
summary: "책과 영화의 시각적 내용을 설명하기 위해 책과 영화를 정렬한 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
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
  - "[[영어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# bookcorpus/bookcorpus

> dataset · [Hugging Face](https://huggingface.co/datasets/bookcorpus/bookcorpus)

책과 영화의 시각적 내용을 설명하기 위해 책과 영화를 정렬한 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Books are a rich source of both fine-grained information, how a character, an object or a scene looks like, as well as high-level semantics` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · task_categories, task_ids = `fill-mask` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `This work aims to align books to their movie releases` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation, task:language_modeling, task:retrieval = `Books are a rich source of both fine-grained information` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:language_modeling = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Books are a rich source of both fine-grained information, how a character, an object or a scene looks like, as well as high-level semantics` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[google__canine-c|google/canine-c]]
- [[google__canine-s|google/canine-s]]
