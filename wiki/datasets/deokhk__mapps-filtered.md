---
type: "dataset"
id: "deokhk/mapps-filtered"
source: "huggingface"
url: "https://huggingface.co/datasets/deokhk/mapps-filtered"
downloads: 120
summary: "프로그래밍 문제를 다국어로 번역한 데이터셋으로 다국어 프로그램 합성 등에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[bn]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[sw]]"
  - "[[te]]"
  - "[[중국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# deokhk/mapps-filtered

> dataset · [Hugging Face](https://huggingface.co/datasets/deokhk/mapps-filtered)

프로그래밍 문제를 다국어로 번역한 데이터셋으로 다국어 프로그램 합성 등에 활용됨

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `questions formatted in Standard Input Format` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `programming tasks` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `translated from English into six target languages` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:translation = `questions formatted in Standard Input Format` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `expected standard input/output for the solution` · 신뢰도 medium
- **언어**: [[bn]] — metadata · languages = `bn` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[sw]] — metadata · languages = `sw` · 신뢰도 high
- **언어**: [[te]] — metadata · languages = `te` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `19988` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `programming tasks` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a multilingual extension of the "introductory" level problems from the codeparrot/apps dataset` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `solutions` 열 p90 79953자 ≈ 19988 토큰 (viewer statistics, default/en)
