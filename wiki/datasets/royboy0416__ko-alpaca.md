---
type: "dataset"
id: "royboy0416/ko-alpaca"
source: "huggingface"
url: "https://huggingface.co/datasets/royboy0416/ko-alpaca"
downloads: 32
summary: "Ko-alpaca 데이터셋으로, 테스트 용도로 사용되는 한국어 Alpaca 데이터입니다."
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# royboy0416/ko-alpaca

> dataset · [Hugging Face](https://huggingface.co/datasets/royboy0416/ko-alpaca)

Ko-alpaca 데이터셋으로, 테스트 용도로 사용되는 한국어 Alpaca 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Ko_alpaca_data.json` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Ko_alpaca_data.json` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `253` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Testing purpose only` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 379자 ≈ 253 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[tensorblock__Mistral-7B-Instruct-v0.2-Ko-S-Core-GGUF|tensorblock/Mistral-7B-Instruct-v0.2-Ko-S-Core-GGUF]]
