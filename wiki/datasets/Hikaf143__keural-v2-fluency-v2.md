---
type: "dataset"
id: "Hikaf143/keural-v2-fluency-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/Hikaf143/keural-v2-fluency-v2"
downloads: 54
summary: "Keural-v2 Fluency (v2)는 한국어-영어 대화 말뭉치로 LLM 미세조정용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Hikaf143/keural-v2-fluency-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/Hikaf143/keural-v2-fluency-v2)

Keural-v2 Fluency (v2)는 한국어-영어 대화 말뭉치로 LLM 미세조정용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `pre-encoded into DeepSeek-V4-Flash-0731's native training text format` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `pre-encoded into DeepSeek-V4-Flash-0731's native training text format` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `987` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A Curated Korean–English Conversational Corpus for LLM Fine-Tuning` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train/val/test split` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1481자 ≈ 987 토큰 (viewer statistics, default/validation)

## 같은 데이터의 사본·중복 등록

- `mkd-minju/keural-v2-fluency-v2`
