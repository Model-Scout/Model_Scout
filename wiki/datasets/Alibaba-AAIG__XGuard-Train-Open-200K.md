---
type: "dataset"
id: "Alibaba-AAIG/XGuard-Train-Open-200K"
source: "huggingface"
url: "https://huggingface.co/datasets/Alibaba-AAIG/XGuard-Train-Open-200K"
downloads: 305
summary: "XGuard-Train-Open-200K은 대형 언어 모델 안전 가드레일 학습용 20만 개 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Alibaba-AAIG/XGuard-Train-Open-200K

> dataset · [Hugging Face](https://huggingface.co/datasets/Alibaba-AAIG/XGuard-Train-Open-200K)

XGuard-Train-Open-200K은 대형 언어 모델 안전 가드레일 학습용 20만 개 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `accommodating both general text content (user prompts or model responses) and interconnected query-response dialogue pairs.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `The definitive risk category label, represented by a single classification token.` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[musubilabs__policylm-1.7b|musubilabs/policylm-1.7b]]
