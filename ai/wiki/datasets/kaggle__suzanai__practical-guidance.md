---
type: "dataset"
id: "kaggle/suzanai/practical-guidance"
source: "kaggle"
url: "https://www.kaggle.com/datasets/suzanai/practical-guidance"
downloads: 16
summary: "PragmaEval은 의료, 공공서비스, 지역 비즈니스, 교육 분야의 실생활 질문에 대한 다국어 실용 안내 Q&A 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
  - "[[교육]]"
  - "[[의료·보건]]"
  - "[[행정·민원]]"
dataset_role:
  - "[[평가용]]"
---
# kaggle/suzanai/practical-guidance

> dataset · [Kaggle](https://www.kaggle.com/datasets/suzanai/practical-guidance)

PragmaEval은 의료, 공공서비스, 지역 비즈니스, 교육 분야의 실생활 질문에 대한 다국어 실용 안내 Q&A 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Cultural-specificity and localization-fidelity testing` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `Multilingual instruction-following and helpfulness evaluation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation = `The dataset pairs naturalistic prompts with structured "enhanced" variants` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Concise reference answer` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC0: Public Domain` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `local_business` · 신뢰도 low
- **도메인**: [[교육]] — ner · readme = `education` · 신뢰도 medium
- **도메인**: [[의료·보건]] — ner · readme = `healthcare_navigation` · 신뢰도 medium
- **도메인**: [[행정·민원]] — ner · readme = `public_services` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `This release is published to invite native speakers and evaluation experts to validate quality, accuracy, and cultural specificity before downstream benchmark u` · 신뢰도 medium
