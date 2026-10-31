---
type: "dataset"
id: "kyujinpy/KOpen-platypus"
source: "huggingface"
url: "https://huggingface.co/datasets/kyujinpy/KOpen-platypus"
downloads: 243
summary: "Open-Platypus 관련 데이터셋을 한국어로 번역한 데이터셋으로, LLM 논리 추론 능력 향상에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
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
# kyujinpy/KOpen-platypus

> dataset · [Hugging Face](https://huggingface.co/datasets/kyujinpy/KOpen-platypus)

Open-Platypus 관련 데이터셋을 한국어로 번역한 데이터셋으로, LLM 논리 추론 능력 향상에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This dataset is focused on improving LLM logical reasoning skills and was used to train the Platypus2 models.` · 신뢰도 medium
- **작업**: [[번역]] — ner · readme = `Korean Translation dataset about Open-Platypus` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `Korean Translation dataset about Open-Platypus` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `Korean Translation dataset about Open-Platypus` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `802` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset is focused on improving LLM logical reasoning skills and was used to train the Platypus2 models.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This dataset is focused on improving LLM logical reasoning skills and was used to train the Platypus2 models.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 1203자 ≈ 802 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[tensorblock__mncai_Mistral-7B-v0.1-orca_platy-1k-GGUF|tensorblock/mncai_Mistral-7B-v0.1-orca_platy-1k-GGUF]]
