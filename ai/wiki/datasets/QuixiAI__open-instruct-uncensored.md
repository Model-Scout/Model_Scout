---
type: "dataset"
id: "QuixiAI/open-instruct-uncensored"
source: "huggingface"
url: "https://huggingface.co/datasets/QuixiAI/open-instruct-uncensored"
downloads: 159
summary: "Allen AI의 open-instruct 데이터셋으로 Tulu 모델 학습에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# QuixiAI/open-instruct-uncensored

> dataset · [Hugging Face](https://huggingface.co/datasets/QuixiAI/open-instruct-uncensored)

Allen AI의 open-instruct 데이터셋으로 Tulu 모델 학습에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `It is used to train the Tulu family of models.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Merged data/processed/**/*.jsonl into a single "open-instruct.jsonl"` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `It is used to train the Tulu family of models.` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `It is used to train the Tulu family of models.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Lamapi__next-8b-Q4_K_M-GGUF|Lamapi/next-8b-Q4_K_M-GGUF]]
- [[mradermacher__next-8b-GGUF|mradermacher/next-8b-GGUF]]
- [[mradermacher__next-8b-i1-GGUF|mradermacher/next-8b-i1-GGUF]]
