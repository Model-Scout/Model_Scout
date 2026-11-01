---
type: "dataset"
id: "PeterGraebner/LDNOOBW_V2"
source: "huggingface"
url: "https://huggingface.co/datasets/PeterGraebner/LDNOOBW_V2"
downloads: 43
summary: "다양한 언어의 욕설 및 부적절 단어 목록으로, 필터링 및 머신러닝에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# PeterGraebner/LDNOOBW_V2

> dataset · [Hugging Face](https://huggingface.co/datasets/PeterGraebner/LDNOOBW_V2)

다양한 언어의 욕설 및 부적절 단어 목록으로, 필터링 및 머신러닝에 활용 가능

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The best way to use these hard-coded word lists is to use them as an additional quality criterion for filtering texts` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `use them for ML building profanity filters` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:information_extraction = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `62 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `As the opinion on which words should be in such lists varies between culture, language, and geographies` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `use them for ML building profanity filters` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
