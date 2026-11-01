---
type: "dataset"
id: "wony98/healtheat-pill-synthetic-baseline"
source: "huggingface"
url: "https://huggingface.co/datasets/wony98/healtheat-pill-synthetic-baseline"
downloads: 9
summary: "HealthEat 프로젝트의 알약 검출 baseline 모델 학습용 합성 이미지 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# wony98/healtheat-pill-synthetic-baseline

> dataset · [Hugging Face](https://huggingface.co/datasets/wony98/healtheat-pill-synthetic-baseline)

HealthEat 프로젝트의 알약 검출 baseline 모델 학습용 합성 이미지 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `3팀 HealthEat 프로젝트의 알약 검출 baseline 모델 학습용 합성 데이터.` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · tags, task_categories = `object-detection` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:vision = `총 8,000장.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `클래스 인덱스는 0~117 (118 클래스).` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `healthcare` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `baseline 학습용` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
