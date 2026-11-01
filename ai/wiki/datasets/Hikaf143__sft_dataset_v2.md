---
type: "dataset"
id: "Hikaf143/sft_dataset_v2"
source: "huggingface"
url: "https://huggingface.co/datasets/Hikaf143/sft_dataset_v2"
downloads: 80
summary: "Keural을 위한 한국어-영어 대화형 지도학습 데이터셋으로, 총 151,500개 예제를 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
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
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Hikaf143/sft_dataset_v2

> dataset · [Hugging Face](https://huggingface.co/datasets/Hikaf143/sft_dataset_v2)

Keural을 위한 한국어-영어 대화형 지도학습 데이터셋으로, 총 151,500개 예제를 포함함.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `Schema: conversational messages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Every example ends with an assistant message` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean-English conversational language models` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is intended for supervised fine-tuning` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `mkd-minju/sft_dataset_v2`
