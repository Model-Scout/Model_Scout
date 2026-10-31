---
type: "dataset"
id: "jp1924-laion-1/KoDocumentTableStruct"
source: "huggingface"
url: "https://huggingface.co/datasets/jp1924-laion-1/KoDocumentTableStruct"
downloads: 11
summary: "한국어 문서 내 표 구조 인식 및 표-텍스트 변환을 위한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[표 질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
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
# jp1924-laion-1/KoDocumentTableStruct

> dataset · [Hugging Face](https://huggingface.co/datasets/jp1924-laion-1/KoDocumentTableStruct)

한국어 문서 내 표 구조 인식 및 표-텍스트 변환을 위한 데이터셋입니다.

## 분류

- **작업**: [[표 질의응답]] — metadata · readme, task_categories = `table-question-answering` · 신뢰도 high
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `- name: image
  dtype: image` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme, task:table_qa = `- name: row_num
  dtype: int32
- name: col_num
  dtype: int32` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:table_qa, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:table_qa, task:visual_qa = `task_categories:
- table-question-answering
- table-to-text
- image-to-text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `splits:
- name: train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
