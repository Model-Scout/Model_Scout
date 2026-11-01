---
type: "dataset"
id: "anujpaude1/moodwave-music-tagging"
source: "huggingface"
url: "https://huggingface.co/datasets/anujpaude1/moodwave-music-tagging"
downloads: 67
summary: "힌디어, 네팔어 등 다국어 음악 장르 및 스타일 태깅용 메타데이터 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
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
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# anujpaude1/moodwave-music-tagging

> dataset · [Hugging Face](https://huggingface.co/datasets/anujpaude1/moodwave-music-tagging)

힌디어, 네팔어 등 다국어 음악 장르 및 스타일 태깅용 메타데이터 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[텍스트 분류]] — ner · readme = `Every song has a genre and a finer style` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:audio_classification = `audio` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `This repository contains metadata only, no audio` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Every song has a genre and a finer style` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `A multilingual music-genre dataset built for Hindi and Nepali repertoire` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `28,914 train / 3,640 validation / 3,669 test` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
