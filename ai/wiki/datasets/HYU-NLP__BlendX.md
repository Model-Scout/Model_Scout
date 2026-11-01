---
type: "dataset"
id: "HYU-NLP/BlendX"
source: "huggingface"
url: "https://huggingface.co/datasets/HYU-NLP/BlendX"
downloads: 134
summary: "BlendX는 다중 의도 탐지를 위한 영어 및 한국어 혼합 패턴 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
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
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# HYU-NLP/BlendX

> dataset · [Hugging Face](https://huggingface.co/datasets/HYU-NLP/BlendX)

BlendX는 다중 의도 탐지를 위한 영어 및 한국어 혼합 패턴 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `created by concatenating these single-intent utterance data sources` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `multi-intent detection datasets` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `94` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `gpl-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `existing domain-specific corpora such as ATIS, Banking77, CLINC150, and SNIPS` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `You can easily load the dataset using HF `datasets` library` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `utterance` 열 p90 141자 ≈ 94 토큰 (viewer statistics, default/validation)
