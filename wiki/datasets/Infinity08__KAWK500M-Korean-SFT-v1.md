---
type: "dataset"
id: "Infinity08/KAWK500M-Korean-SFT-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/Infinity08/KAWK500M-Korean-SFT-v1"
downloads: 15
summary: "한국어 전용 500M급 causal LM 학습용 assistant-only SFT 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
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
# Infinity08/KAWK500M-Korean-SFT-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/Infinity08/KAWK500M-Korean-SFT-v1)

한국어 전용 500M급 causal LM 학습용 assistant-only SFT 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `각 행에는 `input_ids`, `loss_mask`, `source`가 있습니다` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `답변 및 EOS만 `loss_mask=1`` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 전용 500M급 causal LM을 위한` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `train: 22,155 records` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Infinity08__KAWK-500M-Korean-Instruct-v1|Infinity08/KAWK-500M-Korean-Instruct-v1]]
