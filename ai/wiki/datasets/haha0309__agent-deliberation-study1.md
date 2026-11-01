---
type: "dataset"
id: "haha0309/agent-deliberation-study1"
source: "huggingface"
url: "https://huggingface.co/datasets/haha0309/agent-deliberation-study1"
downloads: 69
summary: "Agent deliberation Study 1의 재현 데이터로, 분석용 수치 입력과 코딩 대상 등을 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# haha0309/agent-deliberation-study1

> dataset · [Hugging Face](https://huggingface.co/datasets/haha0309/agent-deliberation-study1)

Agent deliberation Study 1의 재현 데이터로, 분석용 수치 입력과 코딩 대상 등을 포함함.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Evidence coding includes the full original 120 discussion inputs in `evidence-discussions.jsonl` and 600 final explanations in `evidence-reasons.jsonl`` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `analysis-level numerical inputs for 18,209 completed runs` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `exact analyzed coding targets and context, paired position-change targets` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:information_extraction = `Evidence coding includes the full original 120 discussion inputs in `evidence-discussions.jsonl` and 600 final explanations in `evidence-reasons.jsonl`` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `exact analyzed coding targets and context, paired position-change targets` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It is not the complete raw discussion corpus.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This repository contains analysis-level numerical inputs for 18,209 completed runs` · 신뢰도 low
