---
type: "dataset"
id: "syvai/multi-bfcl"
source: "huggingface"
url: "https://huggingface.co/datasets/syvai/multi-bfcl"
downloads: 74
summary: "MultiBFCL은 BFCL-v2 함수 호출 벤치마크의 다국어 기계 번역 데이터셋으로, 다국어 함수 호출 평가에 사용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# syvai/multi-bfcl

> dataset · [Hugging Face](https://huggingface.co/datasets/syvai/multi-bfcl)

MultiBFCL은 BFCL-v2 함수 호출 벤치마크의 다국어 기계 번역 데이터셋으로, 다국어 함수 호출 평가에 사용됩니다.

## 분류

- **작업**: [[도구 호출]] — ner · readme = `Intended for evaluation of multilingual tool/function calling.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `The dataset contains tool-calling prompts, function definitions, and possible answers.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The dataset contains tool-calling prompts, function definitions, and possible answers.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `301 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `Intended for evaluation of multilingual tool/function calling.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
