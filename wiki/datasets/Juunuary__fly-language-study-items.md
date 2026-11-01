---
type: "dataset"
id: "Juunuary/fly-language-study-items"
source: "huggingface"
url: "https://huggingface.co/datasets/Juunuary/fly-language-study-items"
downloads: 63
summary: "영어, 독일어, 한국어 문장 쌍으로 의미 동일성 판단을 위한 이항 분류 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Juunuary/fly-language-study-items

> dataset · [Hugging Face](https://huggingface.co/datasets/Juunuary/fly-language-study-items)

영어, 독일어, 한국어 문장 쌍으로 의미 동일성 판단을 위한 이항 분류 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `Template-generated sentence pairs in English, German and Korean` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `label 1) or not (label 0)?` · 신뢰도 low
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Template-generated sentence pairs in English, German and Korean` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train | 60,000 | 5,000 | 2,500 / 2,500 | declarative (`assertion`)` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
