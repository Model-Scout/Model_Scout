---
type: "dataset"
id: "wony98/healtheat-pill-yolo"
source: "huggingface"
url: "https://huggingface.co/datasets/wony98/healtheat-pill-yolo"
downloads: 50
summary: "HealthEat 프로젝트의 알약 검출 학습용 정제본 데이터셋으로 YOLO 포맷을 사용함."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# wony98/healtheat-pill-yolo

> dataset · [Hugging Face](https://huggingface.co/datasets/wony98/healtheat-pill-yolo)

HealthEat 프로젝트의 알약 검출 학습용 정제본 데이터셋으로 YOLO 포맷을 사용함.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `총 클래스 수: 118종 (한국 식약처 등재 의약품)` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · readme, tags, task_categories = `object-detection` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:vision = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `26` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `healthcare` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `3팀 HealthEat 프로젝트의 알약 검출 학습용 정제본 데이터셋` · 신뢰도 medium
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 39자 ≈ 26 토큰 (viewer statistics, default/validation)
