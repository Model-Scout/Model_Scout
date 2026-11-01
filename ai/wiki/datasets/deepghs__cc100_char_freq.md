---
type: "dataset"
id: "deepghs/cc100_char_freq"
source: "huggingface"
url: "https://huggingface.co/datasets/deepghs/cc100_char_freq"
downloads: 166
summary: "CC-110 데이터셋 기반 116개 언어 문자 빈도 분석표로 언어 지원 확인에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
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
  - "[[서비스 데이터]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# deepghs/cc100_char_freq

> dataset · [Hugging Face](https://huggingface.co/datasets/deepghs/cc100_char_freq)

CC-110 데이터셋 기반 116개 언어 문자 빈도 분석표로 언어 지원 확인에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `letter frequency analysis table based on CC-110 dataset` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:information_extraction = `letter frequency analysis table` · 신뢰도 high
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `letter frequency analysis table` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `109 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is the letter frequency analysis table based on CC-110 dataset.` · 신뢰도 low
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `This dataset is useful for do some basic checking` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `char` 열 p90 1자 ≈ 0 토큰 (viewer statistics, default/train)
