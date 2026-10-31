---
type: "dataset"
id: "lemon-mint/korean-realqa-reasoning-v01-raw-conversational"
source: "huggingface"
url: "https://huggingface.co/datasets/lemon-mint/korean-realqa-reasoning-v01-raw-conversational"
downloads: 7
summary: "한국어 대화형 질의응답 추론 데이터셋으로 학습용 데이터입니다."
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lemon-mint/korean-realqa-reasoning-v01-raw-conversational

> dataset · [Hugging Face](https://huggingface.co/datasets/lemon-mint/korean-realqa-reasoning-v01-raw-conversational)

한국어 대화형 질의응답 추론 데이터셋으로 학습용 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `korean-realqa-reasoning-v01-raw-conversational` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `korean-realqa-reasoning-v01-raw-conversational` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `- name: content
dtype: string` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `- name: content
dtype: string` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
