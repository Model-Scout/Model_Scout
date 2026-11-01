---
type: "dataset"
id: "MauroPello/reasoning-gym-verl-datasets"
source: "huggingface"
url: "https://huggingface.co/datasets/MauroPello/reasoning-gym-verl-datasets"
downloads: 65
summary: "Reasoning Gym 프레임워크 기반의 추론 과제 데이터로 veRL 모델 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# MauroPello/reasoning-gym-verl-datasets

> dataset · [Hugging Face](https://huggingface.co/datasets/MauroPello/reasoning-gym-verl-datasets)

Reasoning Gym 프레임워크 기반의 추론 과제 데이터로 veRL 모델 학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `These datasets were used to train MauroPello/Qwen3-1.7B-RL-final using GRPO` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:language_modeling = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:language_modeling = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `14 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `procedurally generated reasoning tasks from the Reasoning Gym (r-gym) framework` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Main validation dataset.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Raw training set containing randomly sampled tasks across English and translation languages.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
