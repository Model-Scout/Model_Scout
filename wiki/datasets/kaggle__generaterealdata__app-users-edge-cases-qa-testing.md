---
type: "dataset"
id: "kaggle/generaterealdata/app-users-edge-cases-qa-testing"
source: "kaggle"
url: "https://www.kaggle.com/datasets/generaterealdata/app-users-edge-cases-qa-testing"
downloads: 12
summary: "다양한 언어와 특수문자를 포함한 사용자 데이터로 QA 테스트용 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/generaterealdata/app-users-edge-cases-qa-testing

> dataset · [Kaggle](https://www.kaggle.com/datasets/generaterealdata/app-users-edge-cases-qa-testing)

다양한 언어와 특수문자를 포함한 사용자 데이터로 QA 테스트용 합성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `QA of forms, search, sorting, exports and emails with awkward text` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `Security-testing input handling (the strings are harmless samples)` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `QA Testing` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Tables` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:information_extraction, task:question_answering = `names in Arabic, Hebrew, Chinese, Japanese, Korean, Cyrillic and Greek, emoji, one-character and 100-character names` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Tables` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Attribution 4.0 International (CC BY 4.0)` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Seed data for testing a multi-tenant web application` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Seed data for testing a multi-tenant web application` · 신뢰도 low
