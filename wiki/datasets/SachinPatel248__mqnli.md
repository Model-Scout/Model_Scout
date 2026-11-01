---
type: "dataset"
id: "SachinPatel248/mqnli"
source: "huggingface"
url: "https://huggingface.co/datasets/SachinPatel248/mqnli"
downloads: 38
summary: "다국어 QNLI 데이터셋으로 문장 간 관계 분류를 위한 텍스트 분류 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# SachinPatel248/mqnli

> dataset · [Hugging Face](https://huggingface.co/datasets/SachinPatel248/mqnli)

다국어 QNLI 데이터셋으로 문장 간 관계 분류를 위한 텍스트 분류 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `214` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `language:
- en
- de
- es
- ar
- zh
- hi
- pt
- ru
- ja
- fr
- ur
- tr
- ko
- pl
- it
- sv` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `splits:
- name: train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `sentence` 열 p90 855자 ≈ 214 토큰 (viewer statistics, default/train)
