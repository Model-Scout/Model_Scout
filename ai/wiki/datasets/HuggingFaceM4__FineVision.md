---
type: "dataset"
id: "HuggingFaceM4/FineVision"
source: "huggingface"
url: "https://huggingface.co/datasets/HuggingFaceM4/FineVision"
downloads: 139578
summary: "FineVision은 1,730만 이미지와 9.5B 답변 토큰으로 구성된 비전-언어 모델 학습용 대규모 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# HuggingFaceM4/FineVision

> dataset · [Hugging Face](https://huggingface.co/datasets/HuggingFaceM4/FineVision)

FineVision은 1,730만 이미지와 9.5B 답변 토큰으로 구성된 비전-언어 모델 학습용 대규모 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `designed for training state-of-the-art open Vision-Language-Models` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `17.3M images` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `88.9M turns, and 9.5B answer tokens` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `9.5B answer tokens` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `FineVision is a massive collection of datasets with 17.3M images, 24.3M samples, 88.9M turns, and 9.5B answer tokens` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `designed for training state-of-the-art open Vision-Language-Models` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[nc-ai-consortium__VAETKI-VL-7B-A1B|nc-ai-consortium/VAETKI-VL-7B-A1B]]
