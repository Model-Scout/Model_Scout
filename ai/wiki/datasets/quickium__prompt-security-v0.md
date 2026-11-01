---
type: "dataset"
id: "quickium/prompt-security-v0"
source: "huggingface"
url: "https://huggingface.co/datasets/quickium/prompt-security-v0"
downloads: 112
summary: "Quickium Prompt Security v0은 다국어 프롬프트 보안 분류용 데이터셋으로, 프롬프트 인젝션, 탈옥, PII 노출 탐지에 사용됩니다."
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
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# quickium/prompt-security-v0

> dataset · [Hugging Face](https://huggingface.co/datasets/quickium/prompt-security-v0)

Quickium Prompt Security v0은 다국어 프롬프트 보안 분류용 데이터셋으로, 프롬프트 인젝션, 탈옥, PII 노출 탐지에 사용됩니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `One row per prompt, both splits. Six columns:

| Column | Type | Meaning |
|---|---|---|
| `id` | string | Stable unique row id, prefixed by `source` (plus a su` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `| `label` | int8 | **Target.** `0` = safe, `1` = unsafe. Source-derived (see below). |` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `32 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A multilingual corpus for prompt-security classification — prompt injection, jailbreak, and PII exposure — curated and published by Quickium.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Split
Rows
Sources
License posture

train
71,117
10
Commercial-clean (permissive + one GPL-3.0 slice + one ODC-BY source)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
