---
type: "dataset"
id: "allenai/tulu-v2-sft-mixture"
source: "huggingface"
url: "https://huggingface.co/datasets/allenai/tulu-v2-sft-mixture"
downloads: 1096
summary: "Tulu V2 Mix는 다양한 공개 데이터셋을 혼합한 언어 모델 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
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
# allenai/tulu-v2-sft-mixture

> dataset · [Hugging Face](https://huggingface.co/datasets/allenai/tulu-v2-sft-mixture)

Tulu V2 Mix는 다양한 공개 데이터셋을 혼합한 언어 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Tulu is a series of language models that are trained to act as helpful assistants.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Tulu is a series of language models that are trained to act as helpful assistants.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Tulu V2 is presented as a singular training split.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[bartowski__Tralalabs_Pythia-6.9B-Instruct-v1-Merged-GGUF|bartowski/Tralalabs_Pythia-6.9B-Instruct-v1-Merged-GGUF]]
