---
type: "dataset"
id: "Baekpica/Solar-Open2-120B-A15B-REAM-148E-Healing-Mix"
source: "huggingface"
url: "https://huggingface.co/datasets/Baekpica/Solar-Open2-120B-A15B-REAM-148E-Healing-Mix"
downloads: 46
summary: "Solar-Open2-120B-A15B-REAM-148E 모델의 병합 손상 복구를 위한 결정론적 힐링 믹스 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[hi]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[금융·경제]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Baekpica/Solar-Open2-120B-A15B-REAM-148E-Healing-Mix

> dataset · [Hugging Face](https://huggingface.co/datasets/Baekpica/Solar-Open2-120B-A15B-REAM-148E-Healing-Mix)

Solar-Open2-120B-A15B-REAM-148E 모델의 병합 손상 복구를 위한 결정론적 힐링 믹스 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `instruction following · 포맷 · completeness` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `모든 시퀀스는 Solar Open 2 chat template로 사전 렌더·토크나이즈되어 있고` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `assistant 턴에만 loss 마스크가 열려 있습니다` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `표·수치·금융 분석 (장문)` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `한국어 응답에서 반복 붕괴` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `SFT 데이터만 사용했습니다` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Baekpica__Solar-Open2-120B-A15B-REAM-148E-BF16-v2|Baekpica/Solar-Open2-120B-A15B-REAM-148E-BF16-v2]]
- [[Baekpica__Solar-Open2-120B-A15B-REAM-148E-NVFP4-v2|Baekpica/Solar-Open2-120B-A15B-REAM-148E-NVFP4-v2]]
