---
type: "dataset"
id: "aims-foundations/safety-irt"
source: "huggingface"
url: "https://huggingface.co/datasets/aims-foundations/safety-irt"
downloads: 1082
summary: "10개 언어로 61개 모델의 190만 안전성 평가 응답을 포함한 안전성 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[bn]]"
  - "[[영어]]"
  - "[[it]]"
  - "[[jv]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[sw]]"
  - "[[th]]"
  - "[[vi]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# aims-foundations/safety-irt

> dataset · [Hugging Face](https://huggingface.co/datasets/aims-foundations/safety-irt)

10개 언어로 61개 모델의 190만 안전성 평가 응답을 포함한 안전성 연구용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Contains 1.9M graded responses from 61 model configurations across 10 languages` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Contains 1.9M graded responses from 61 model configurations across 10 languages, along with anchor selections, judge validation data, and native speaker transla` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:question_answering = `Contains 1.9M graded responses from 61 model configurations across 10 languages, along with anchor selections, judge validation data, and native speaker transla` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Contains 1.9M graded responses from 61 model configurations across 10 languages, along with anchor selections, judge validation data, and native speaker transla` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[bn]] — metadata · languages = `bn` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[jv]] — metadata · languages = `jv` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[sw]] — metadata · languages = `sw` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Data for "Why Do Safety Guardrails Degrade Across Languages?"` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Data for "Why Do Safety Guardrails Degrade Across Languages?" Contains 1.9M graded responses from 61 model configurations across 10 languages` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
