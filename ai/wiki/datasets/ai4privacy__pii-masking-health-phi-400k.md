---
type: "dataset"
id: "ai4privacy/pii-masking-health-phi-400k"
source: "huggingface"
url: "https://huggingface.co/datasets/ai4privacy/pii-masking-health-phi-400k"
downloads: 140
summary: "아시아 태평양 지역을 포함한 개인 건강 및 의료 정보(PII) 마스킹 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[의료·보건]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ai4privacy/pii-masking-health-phi-400k

> dataset · [Hugging Face](https://huggingface.co/datasets/ai4privacy/pii-masking-health-phi-400k)

아시아 태평양 지역을 포함한 개인 건강 및 의료 정보(PII) 마스킹 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Control identified personal data through masking, pseudonymization, or k-anonymization` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories = `token-classification` · 신뢰도 medium
- **작업**: [[리랭킹]] — ner · readme = `evaluating de-anonymization risks through expert annotation and automated assessment` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:information_extraction, task:reranking = `Scan and markup private entities in unstructured text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `producing a structured privacy mask with entity types` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `30 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `Personal Health & Medical Information, Global PII Dataset` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
