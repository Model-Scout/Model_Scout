---
type: "dataset"
id: "devngho/korean-instruction-mix"
source: "huggingface"
url: "https://huggingface.co/datasets/devngho/korean-instruction-mix"
downloads: 21
summary: "한국어 instruction 데이터셋들을 혼합한 데이터셋으로, 다양한 원본 데이터셋을 포함함."
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
# devngho/korean-instruction-mix

> dataset · [Hugging Face](https://huggingface.co/datasets/devngho/korean-instruction-mix)

한국어 instruction 데이터셋들을 혼합한 데이터셋으로, 다양한 원본 데이터셋을 포함함.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `한국어 instruction 데이터셋 mix` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `한국어 instruction 데이터셋 mix` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `한국어 instruction 데이터셋 mix` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 instruction 데이터셋 mix` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터셋을 사용해 학습된 모델은 아래 원본 데이터셋을 함께 인용해주세요.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
