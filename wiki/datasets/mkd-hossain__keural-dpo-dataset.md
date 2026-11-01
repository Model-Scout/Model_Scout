---
type: "dataset"
id: "mkd-hossain/keural-dpo-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/mkd-hossain/keural-dpo-dataset"
downloads: 31
summary: "Keural 14.8B 언어모델의 DPO 학습을 위한 한영 이중언어 선호 데이터셋입니다."
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
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# mkd-hossain/keural-dpo-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/mkd-hossain/keural-dpo-dataset)

Keural 14.8B 언어모델의 DPO 학습을 위한 한영 이중언어 선호 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean, English` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `DPO alignment training` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
