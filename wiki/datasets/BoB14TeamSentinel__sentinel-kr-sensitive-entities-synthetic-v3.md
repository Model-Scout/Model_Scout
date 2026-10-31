---
type: "dataset"
id: "BoB14TeamSentinel/sentinel-kr-sensitive-entities-synthetic-v3"
source: "huggingface"
url: "https://huggingface.co/datasets/BoB14TeamSentinel/sentinel-kr-sensitive-entities-synthetic-v3"
downloads: 106
summary: "Sentinel KR Sensitive Entities (Synthetic) v3는 한국어 합성 데이터로 민감정보 탐지용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# BoB14TeamSentinel/sentinel-kr-sensitive-entities-synthetic-v3

> dataset · [Hugging Face](https://huggingface.co/datasets/BoB14TeamSentinel/sentinel-kr-sensitive-entities-synthetic-v3)

Sentinel KR Sensitive Entities (Synthetic) v3는 한국어 합성 데이터로 민감정보 탐지용입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[정보 추출]] — metadata · readme, task_categories = `token-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction = `chat messages in SFT style, typically 3 turns` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Sentinel KR Sensitive Entities (Synthetic) v3 is a Korean synthetic (AI-generated) dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train / evaluate models that detect sensitive information before sending prompts or text payloads to external LLM services.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
