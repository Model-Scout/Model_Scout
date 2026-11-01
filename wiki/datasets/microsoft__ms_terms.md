---
type: "dataset"
id: "microsoft/ms_terms"
source: "huggingface"
url: "https://huggingface.co/datasets/microsoft/ms_terms"
downloads: 198
summary: "Microsoft 제품과 연동되는 애플리케이션 현지화 및 IT 용어집 개발용 용어집 데이터입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[도구 호출]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[서비스 데이터]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# microsoft/ms_terms

> dataset · [Hugging Face](https://huggingface.co/datasets/microsoft/ms_terms)

Microsoft 제품과 연동되는 애플리케이션 현지화 및 IT 용어집 개발용 용어집 데이터입니다.

## 분류

- **작업**: [[도구 호출]] — ner · readme = `The Microsoft Terminology Collection can be used to develop localized versions of applications that integrate with Microsoft products.` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:translation = `Terminology is provided in .tbx format, an industry standard for terminology exchange.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Terminology is provided in .tbx format, an industry standard for terminology exchange.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `103 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `ms-pl` · 신뢰도 high
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `Terminology is provided in .tbx format, an industry standard for terminology exchange.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
