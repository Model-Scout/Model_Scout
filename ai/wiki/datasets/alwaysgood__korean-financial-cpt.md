---
type: "dataset"
id: "alwaysgood/korean-financial-cpt"
source: "huggingface"
url: "https://huggingface.co/datasets/alwaysgood/korean-financial-cpt"
downloads: 63
summary: "한국어 금융 관련 원시 JSONL 데이터셋으로 금융 텍스트 분석에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# alwaysgood/korean-financial-cpt

> dataset · [Hugging Face](https://huggingface.co/datasets/alwaysgood/korean-financial-cpt)

한국어 금융 관련 원시 JSONL 데이터셋으로 금융 텍스트 분석에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Korean Financial CPT (Raw JSONL)` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `Korean Financial CPT (Raw JSONL)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation, task:language_modeling = `raw JSONL files (no instruction formatting)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `raw JSONL files (no instruction formatting)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This repository currently stores raw source files only.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
