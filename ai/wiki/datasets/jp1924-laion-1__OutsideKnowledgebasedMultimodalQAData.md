---
type: "dataset"
id: "jp1924-laion-1/OutsideKnowledgebasedMultimodalQAData"
source: "huggingface"
url: "https://huggingface.co/datasets/jp1924-laion-1/OutsideKnowledgebasedMultimodalQAData"
downloads: 28
summary: "이미지와 질문-답변 쌍을 포함한 시각적 질문응답 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jp1924-laion-1/OutsideKnowledgebasedMultimodalQAData

> dataset · [Hugging Face](https://huggingface.co/datasets/jp1924-laion-1/OutsideKnowledgebasedMultimodalQAData)

이미지와 질문-답변 쌍을 포함한 시각적 질문응답 데이터셋입니다.

## 분류

- **작업**: [[이미지 이해]] — metadata · readme, task_categories = `visual-question-answering` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `- name: image
dtype: image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:visual_qa = `- name: caption
dtype: string` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `- name: answer
dtype: string` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `language:
- ko
- en` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `splits:
- name: train
num_bytes: 11169890399.625
num_examples: 47203` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
