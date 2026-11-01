---
type: "dataset"
id: "anon-researcher-ua/ua-codeforces-cots-open-r1-for-training"
source: "huggingface"
url: "https://huggingface.co/datasets/anon-researcher-ua/ua-codeforces-cots-open-r1-for-training"
downloads: 13
readme_status: "thin"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[요약]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[uk]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# anon-researcher-ua/ua-codeforces-cots-open-r1-for-training

> dataset · [Hugging Face](https://huggingface.co/datasets/anon-researcher-ua/ua-codeforces-cots-open-r1-for-training)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 high
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 high
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:summarization, task:translation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:summarization, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[uk]] — metadata · languages = `uk` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `13059` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `analysis` 열 p90 52237자 ≈ 13059 토큰 (viewer statistics, default/validation)

## 이 데이터로 학습한 모델

- [[anon-researcher-ua__codegpt-oss-20b-GGUF|anon-researcher-ua/codegpt-oss-20b-GGUF]]
