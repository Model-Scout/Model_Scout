---
type: "dataset"
id: "Meddies/meddies-pii-v3-filled"
source: "huggingface"
url: "https://huggingface.co/datasets/Meddies/meddies-pii-v3-filled"
downloads: 38
summary: "20개 언어로 의료 및 일상 텍스트에서 PII 탐지를 위한 합성 문서 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[정보 추출]]"
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
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Meddies/meddies-pii-v3-filled

> dataset · [Hugging Face](https://huggingface.co/datasets/Meddies/meddies-pii-v3-filled)

20개 언어로 의료 및 일상 텍스트에서 PII 탐지를 위한 합성 문서 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories = `token-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction = `Synthetic, span-labelled documents` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Synthetic, span-labelled documents` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `20 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `healthcare` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Synthetic, span-labelled documents for training and evaluating PII detection` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
