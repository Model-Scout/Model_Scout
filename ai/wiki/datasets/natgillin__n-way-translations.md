---
type: "dataset"
id: "natgillin/n-way-translations"
source: "huggingface"
url: "https://huggingface.co/datasets/natgillin/n-way-translations"
downloads: 28
summary: "다국어 N-way 병렬 말뭉치로 여러 언어의 문장을 포함하여 번역 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
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
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# natgillin/n-way-translations

> dataset · [Hugging Face](https://huggingface.co/datasets/natgillin/n-way-translations)

다국어 N-way 병렬 말뭉치로 여러 언어의 문장을 포함하여 번역 연구에 활용됨.

## 분류

- **작업**: [[번역]] — metadata · readme, tags, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `English text (also kept inside translations)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `English text (also kept inside translations)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `50 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual N-way parallel corpus` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Inherits per-corpus terms from the upstream sources. Tatoeba:` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
