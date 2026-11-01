---
type: "dataset"
id: "Seoyoung07/keypoint_dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/Seoyoung07/keypoint_dataset"
downloads: 15
summary: "한국 수어 영상에서 추출한 키포인트 데이터로 수어 단어 인식 모델 학습/평가용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Seoyoung07/keypoint_dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/Seoyoung07/keypoint_dataset)

한국 수어 영상에서 추출한 키포인트 데이터로 수어 단어 인식 모델 학습/평가용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Korean Sign Language isolated-word model training/evaluation experiments` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding = `text` · 신뢰도 medium
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme = `keypoint cache used for Korean Sign Language isolated-word model training/evaluation experiments` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme = `keypoint cache used for Korean Sign Language isolated-word model training/evaluation experiments` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean Sign Language Keypoint Dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `used for Korean Sign Language isolated-word model training/evaluation experiments` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
