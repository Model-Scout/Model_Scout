---
type: "dataset"
id: "jp1924-laion-1/VisualQuestionAnswering"
source: "huggingface"
url: "https://huggingface.co/datasets/jp1924-laion-1/VisualQuestionAnswering"
downloads: 58
summary: "이미지와 질문-답변 쌍으로 구성된 시각 질의응답 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
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
  - "[[대규모 데이터]]"
---
# jp1924-laion-1/VisualQuestionAnswering

> dataset · [Hugging Face](https://huggingface.co/datasets/jp1924-laion-1/VisualQuestionAnswering)

이미지와 질문-답변 쌍으로 구성된 시각 질의응답 데이터셋입니다.

## 분류

- **작업**: [[이미지 이해]] — metadata · readme, task_categories = `visual-question-answering` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `- name: image
dtype: image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:visual_qa = `- name: question
  dtype: string` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `- name: answer
dtype: string` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `- name: validation
num_bytes: 26704475053.875
num_examples: 318553` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train
num_bytes: 66241679332.25
num_examples: 715406` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
