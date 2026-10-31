---
type: "dataset"
id: "kyujinpy/KoCoT_2000"
source: "huggingface"
url: "https://huggingface.co/datasets/kyujinpy/KoCoT_2000"
downloads: 28
summary: "kaist-CoT 관련 번역 데이터셋으로, DeepL 데이터셋을 활용함."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# kyujinpy/KoCoT_2000

> dataset · [Hugging Face](https://huggingface.co/datasets/kyujinpy/KoCoT_2000)

kaist-CoT 관련 번역 데이터셋으로, DeepL 데이터셋을 활용함.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `Using DeepL dataset, translation about kaist-CoT.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:translation = `Using DeepL dataset, translation about kaist-CoT.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `Using DeepL dataset, translation about kaist-CoT.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `224` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `|CoT-Collection|1837928|` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `source` 열 p90 895자 ≈ 224 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[tensorblock__KoT-platypus2-13B-GGUF|tensorblock/KoT-platypus2-13B-GGUF]]
