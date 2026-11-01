---
type: "dataset"
id: "peterkirby/mymirmdatasets"
source: "huggingface"
url: "https://huggingface.co/datasets/peterkirby/mymirmdatasets"
downloads: 708
summary: "MIRM 다국어 저자 데이터셋으로 3996만 개 문서와 294 구성 포함, 저자 식별 연구용"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# peterkirby/mymirmdatasets

> dataset · [Hugging Face](https://huggingface.co/datasets/peterkirby/mymirmdatasets)

MIRM 다국어 저자 데이터셋으로 3996만 개 문서와 294 구성 포함, 저자 식별 연구용

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `authorship publication` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `complete English abstract, with outer whitespace trimmed` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:information_extraction, task:language_modeling = `complete English abstract, with outer whitespace trimmed` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `authorship publication` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `47 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MIRM multilingual authorship datasets` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Validation` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
