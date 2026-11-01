---
type: "dataset"
id: "jp1924/KoBPO"
source: "huggingface"
url: "https://huggingface.co/datasets/jp1924/KoBPO"
downloads: 6
summary: "KoBPO는 한국어 대화 데이터로, 대화 모델 학습용 데이터셋입니다."
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
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jp1924/KoBPO

> dataset · [Hugging Face](https://huggingface.co/datasets/jp1924/KoBPO)

KoBPO는 한국어 대화 데이터로, 대화 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `conversations` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `- name: content
dtype: string` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `- name: content
dtype: string` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train
num_bytes: 122180963
num_examples: 40236` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
