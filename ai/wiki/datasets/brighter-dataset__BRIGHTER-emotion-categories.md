---
type: "dataset"
id: "brighter-dataset/BRIGHTER-emotion-categories"
source: "huggingface"
url: "https://huggingface.co/datasets/brighter-dataset/BRIGHTER-emotion-categories"
downloads: 3256
summary: "28개 언어의 다중 라벨 감정 분류를 위한 BRIGHTER 감정 범주 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[다국어]]"
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
# brighter-dataset/BRIGHTER-emotion-categories

> dataset · [Hugging Face](https://huggingface.co/datasets/brighter-dataset/BRIGHTER-emotion-categories)

28개 언어의 다중 라벨 감정 분류를 위한 BRIGHTER 감정 범주 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `multi-label emotion classification dataset` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Text content to classify` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Presence of emotion` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `26 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `human-annotated textual emotion recognition datasets for 28 Languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Zeolit__lettuce-thymos-26m-v1|Zeolit/lettuce-thymos-26m-v1]]
