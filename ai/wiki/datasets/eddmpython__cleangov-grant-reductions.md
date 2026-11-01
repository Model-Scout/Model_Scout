---
type: "dataset"
id: "eddmpython/cleangov-grant-reductions"
source: "huggingface"
url: "https://huggingface.co/datasets/eddmpython/cleangov-grant-reductions"
downloads: 9
summary: "행정안전부의 지방교부세법 위반 감액 사건 데이터로, 위반 제재 분석에 활용됨"
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
---
# eddmpython/cleangov-grant-reductions

> dataset · [Hugging Face](https://huggingface.co/datasets/eddmpython/cleangov-grant-reductions)

행정안전부의 지방교부세법 위반 감액 사건 데이터로, 위반 제재 분석에 활용됨

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `행정안전부가 지방교부세법 위반(법령위반 과다지출·수입징수 태만·특별교부세 조건위반)으로 보통·특별교부세를 감액한 개별 사건.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `기관명·감액금액·사유유형·위반내용 자연어를 담는다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `기관명·감액금액·사유유형·위반내용 자연어를 담는다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `행정안전부가 지방교부세법 위반(법령위반 과다지출·수입징수 태만·특별교부세 조건위반)으로 보통·특별교부세를 감액한 개별 사건.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `실측 2020~2025 373건, 총 감액 851억` · 신뢰도 low
