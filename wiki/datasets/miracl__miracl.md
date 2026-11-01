---
type: "dataset"
id: "miracl/miracl"
source: "huggingface"
url: "https://huggingface.co/datasets/miracl/miracl"
downloads: 13258
summary: "MIRACL은 18개 언어의 다국어 정보 검색을 위한 주제와 관련성 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[문서 검색]]"
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
dataset_role:
  - "[[학습용]]"
---
# miracl/miracl

> dataset · [Hugging Face](https://huggingface.co/datasets/miracl/miracl)

MIRACL은 18개 언어의 다국어 정보 검색을 위한 주제와 관련성 평가 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — metadata · task_categories, task_ids = `text-retrieval` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:retrieval = `the topics are saved in `.tsv` format` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `the topics are saved in `.tsv` format` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `18 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The structure is the same for `train`, `dev`, and `testA` set` · 신뢰도 medium

## 이 데이터로 학습한 모델

- [[opensearch-project__opensearch-neural-sparse-encoding-multilingual-v1|opensearch-project/opensearch-neural-sparse-encoding-multilingual-v1]]
