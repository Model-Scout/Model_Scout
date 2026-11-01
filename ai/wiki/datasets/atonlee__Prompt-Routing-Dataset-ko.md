---
type: "dataset"
id: "atonlee/Prompt-Routing-Dataset-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/atonlee/Prompt-Routing-Dataset-ko"
downloads: 44
summary: "SupraLabs/Prompt-Routing-Dataset의 한국어 번역 데이터셋으로, 프롬프트 라우팅 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# atonlee/Prompt-Routing-Dataset-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/atonlee/Prompt-Routing-Dataset-ko)

SupraLabs/Prompt-Routing-Dataset의 한국어 번역 데이터셋으로, 프롬프트 라우팅 연구에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[번역]] — tag_match · tags = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:translation = `Only the prompt column was translated.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `routing_choice` | string | `big model` or `small model`` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `332` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `primary_domain` | string | free text, 338 distinct values` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Only the `prompt` column was translated. Every label was copied verbatim.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `prompt_en` 열 p90 498자 ≈ 332 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[atonlee__supra-ko-pii-router|atonlee/supra-ko-pii-router]]
