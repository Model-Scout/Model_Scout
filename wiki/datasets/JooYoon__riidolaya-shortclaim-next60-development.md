---
type: "dataset"
id: "JooYoon/riidolaya-shortclaim-next60-development"
source: "huggingface"
url: "https://huggingface.co/datasets/JooYoon/riidolaya-shortclaim-next60-development"
downloads: 2439
summary: "37개의 개발 요청과 108개의 후보 라벨로 검증 순서 제안을 위한 소규모 클레임/힌트 모델 개발 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# JooYoon/riidolaya-shortclaim-next60-development

> dataset · [Hugging Face](https://huggingface.co/datasets/JooYoon/riidolaya-shortclaim-next60-development)

37개의 개발 요청과 108개의 후보 라벨로 검증 순서 제안을 위한 소규모 클레임/힌트 모델 개발 데이터셋입니다.

## 분류

- **작업**: [[리랭킹]] — ner · readme = `This development dataset prepares a tiny claim/hint model to suggest a verification order.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:reranking = `Only request/candidate text enters features` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `labels, groups, sources and evidence stay separate.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This development dataset prepares a tiny claim/hint model to suggest a verification order.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
