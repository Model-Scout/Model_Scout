---
type: "dataset"
id: "legesher/language-packs"
source: "huggingface"
url: "https://huggingface.co/datasets/legesher/language-packs"
downloads: 119
summary: "Legesher Language Packs는 프로그래밍 언어 예약어를 다양한 자연어로 번역한 코드 현지화 데이터입니다."
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
  - "[[상업 이용 가능]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# legesher/language-packs

> dataset · [Hugging Face](https://huggingface.co/datasets/legesher/language-packs)

Legesher Language Packs는 프로그래밍 언어 예약어를 다양한 자연어로 번역한 코드 현지화 데이터입니다.

## 분류

- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `Every reserved word within a programming language's grammar (keywords, builtins, exceptions, error messages) is compiled into a language pack` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `Every reserved word within a programming language's grammar (keywords, builtins, exceptions, error messages) is compiled into a language pack that, when utilize` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `56 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
