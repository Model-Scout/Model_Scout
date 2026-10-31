---
type: "dataset"
id: "peterkirby/mymirmdatasets"
source: "huggingface"
url: "https://huggingface.co/datasets/peterkirby/mymirmdatasets"
downloads: 553
summary: "MIRM 다국어 저자 데이터셋으로 3,871만 문서와 277개 구성 포함, 저자 인식 연구용"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
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

MIRM 다국어 저자 데이터셋으로 3,871만 문서와 277개 구성 포함, 저자 인식 연구용

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `sparse fingerprints, representative posting samples, ranked candidates and bounded alignment` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding = `Each row contains one unchanged contiguous AO3 source excerpt of 500–21,000 Unicode code points` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Language and account labels come from AO3 metadata` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `47 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MIRM multilingual authorship datasets` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Validation` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
