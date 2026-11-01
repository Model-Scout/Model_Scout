---
type: "dataset"
id: "ktnet-research/subjects-not-authors-evidence"
source: "huggingface"
url: "https://huggingface.co/datasets/ktnet-research/subjects-not-authors-evidence"
downloads: 329
summary: "KTNET 연구진이 발표한 논문 'Subjects, Not Authors'의 증거 패키지로, 실험 기록과 분석 스크립트를 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ktnet-research/subjects-not-authors-evidence

> dataset · [Hugging Face](https://huggingface.co/datasets/ktnet-research/subjects-not-authors-evidence)

KTNET 연구진이 발표한 논문 'Subjects, Not Authors'의 증거 패키지로, 실험 기록과 분석 스크립트를 포함함.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `Raw outputs of the evaluated models are included.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:language_modeling = `All corpora and raw records use constructed values.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `Raw outputs of the evaluated models are included.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `The asset is a constructed certificate of origin with fields in sensitivity classes F0 (public trade facts), F1 (commercial quantities) and F2 (identities).` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This repository holds the preregistrations, corpora, raw trial records and analysis scripts behind Section 8 of the paper, and the preregistered clean-environme` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
