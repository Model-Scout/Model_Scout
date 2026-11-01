---
type: "dataset"
id: "unreadlogs/Spam-Ham-OpenShield"
source: "huggingface"
url: "https://huggingface.co/datasets/unreadlogs/Spam-Ham-OpenShield"
downloads: 38
summary: "21개 언어로 된 약 19만 샘플의 스팸/햄 분류용 다국어 텍스트 분류 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# unreadlogs/Spam-Ham-OpenShield

> dataset · [Hugging Face](https://huggingface.co/datasets/unreadlogs/Spam-Ham-OpenShield)

21개 언어로 된 약 19만 샘플의 스팸/햄 분류용 다국어 텍스트 분류 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · tags, task_categories = `text-classification` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Content of the message or communication` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Classification label (`0`: Ham, `1`: Spam)` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `21 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual text classification benchmark designed to evaluate and train spam detection filters, guardrails, and language models across diverse global language` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `designed to evaluate and train spam detection filters` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
