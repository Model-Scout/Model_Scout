---
type: "dataset"
id: "xzuyn/manythings-translations-alpaca"
source: "huggingface"
url: "https://huggingface.co/datasets/xzuyn/manythings-translations-alpaca"
downloads: 25
summary: "영어와 84개 언어 간 번역 데이터 630만 건을 포함한 다국어 번역 데이터셋입니다."
readme_status: "thin"
readme_language: "en"
korean_focus: "not_ko"
task:
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
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# xzuyn/manythings-translations-alpaca

> dataset · [Hugging Face](https://huggingface.co/datasets/xzuyn/manythings-translations-alpaca)

영어와 84개 언어 간 번역 데이터 630만 건을 포함한 다국어 번역 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `3,164,972 translations from English to 84 other languages.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `3,164,972 translations from English to 84 other languages.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `16` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `instruction` 열 p90 66자 ≈ 16 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[QuantFactory__Llama-3.2-Taiwan-3B-Instruct-GGUF|QuantFactory/Llama-3.2-Taiwan-3B-Instruct-GGUF]]
