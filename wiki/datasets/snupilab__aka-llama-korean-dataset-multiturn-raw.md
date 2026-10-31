---
type: "dataset"
id: "snupilab/aka-llama-korean-dataset-multiturn-raw"
source: "huggingface"
url: "https://huggingface.co/datasets/snupilab/aka-llama-korean-dataset-multiturn-raw"
downloads: 145
summary: "한국어 다중턴 대화 생성을 위한 원시 대화 데이터셋으로 연구 개발용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# snupilab/aka-llama-korean-dataset-multiturn-raw

> dataset · [Hugging Face](https://huggingface.co/datasets/snupilab/aka-llama-korean-dataset-multiturn-raw)

한국어 다중턴 대화 생성을 위한 원시 대화 데이터셋으로 연구 개발용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `multi-turn Korean conversation dataset` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `multi-turn dialogue generation` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean natural language processing (NLP)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a raw version of a multi-turn Korean conversation dataset` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
