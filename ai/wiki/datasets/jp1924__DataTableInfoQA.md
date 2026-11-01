---
type: "dataset"
id: "jp1924/DataTableInfoQA"
source: "huggingface"
url: "https://huggingface.co/datasets/jp1924/DataTableInfoQA"
downloads: 11
summary: "테이블 기반 질의응답 데이터셋으로, 표에서 질문에 답하기 위한 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[표 질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jp1924/DataTableInfoQA

> dataset · [Hugging Face](https://huggingface.co/datasets/jp1924/DataTableInfoQA)

테이블 기반 질의응답 데이터셋으로, 표에서 질문에 답하기 위한 데이터입니다.

## 분류

- **작업**: [[표 질의응답]] — metadata · readme, task_categories = `table-question-answering` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:table_qa = `task_categories:
- table-question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:table_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:table_qa = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `- name: validation
num_bytes: 56060671
num_examples: 20000` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train
num_bytes: 444099171
num_examples: 160000` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
