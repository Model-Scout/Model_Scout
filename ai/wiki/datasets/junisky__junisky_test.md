---
type: "dataset"
id: "junisky/junisky_test"
source: "huggingface"
url: "https://huggingface.co/datasets/junisky/junisky_test"
downloads: 36
summary: "Junisky의 테스트용 데이터로 텍스트 분류, 토큰 분류, 번역 작업에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[aa]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[xx]]"
commercial_use:
  - "[[조건부 이용]]"
---
# junisky/junisky_test

> dataset · [Hugging Face](https://huggingface.co/datasets/junisky/junisky_test)

Junisky의 테스트용 데이터로 텍스트 분류, 토큰 분류, 번역 작업에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **작업**: [[정보 추출]] — metadata · readme, task_categories = `token-classification` · 신뢰도 high
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:information_extraction, task:translation = `- text-classification
- token-classification
- translation` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `- text-classification
- token-classification
- translation` · 신뢰도 medium
- **언어**: [[aa]] — metadata · languages = `aa` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **언어**: [[xx]] — metadata · languages = `xx` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
