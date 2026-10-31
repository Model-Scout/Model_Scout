---
type: "dataset"
id: "Bizspring/som-5domain-4llm-2026-05"
source: "huggingface"
url: "https://huggingface.co/datasets/Bizspring/som-5domain-4llm-2026-05"
downloads: 36
summary: "비즈스프링 5개 도메인에 대해 4대 LLM의 AI 답변 인용률을 측정한 GEO 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
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
# Bizspring/som-5domain-4llm-2026-05

> dataset · [Hugging Face](https://huggingface.co/datasets/Bizspring/som-5domain-4llm-2026-05)

비즈스프링 5개 도메인에 대해 4대 LLM의 AI 답변 인용률을 측정한 GEO 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `자사 5개 도메인을 4대 LLM에 동시 측정한 GEO(Generative Engine Optimization) 1차 데이터.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:retrieval = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `비즈스프링이 자사 GEO 측정 도구 GEOcare로 자사 도메인의 AI 답변 인용률을 직접 측정한 도그푸딩 데이터.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Bizspring SoM 5-Domain × 4-LLM Citation Matrix (2026-05)` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
