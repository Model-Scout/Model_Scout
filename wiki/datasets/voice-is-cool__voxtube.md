---
type: "dataset"
id: "voice-is-cool/voxtube"
source: "huggingface"
url: "https://huggingface.co/datasets/voice-is-cool/voxtube"
downloads: 1197
summary: "VoxTube는 10개 이상 언어로 5,040명 화자의 음성 데이터를 포함한 다국어 화자 인식용 음성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# voice-is-cool/voxtube

> dataset · [Hugging Face](https://huggingface.co/datasets/voice-is-cool/voxtube)

VoxTube는 10개 이상 언어로 5,040명 화자의 음성 데이터를 포함한 다국어 화자 인식용 음성 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[텍스트 분류]] — ner · readme = `multilingual speaker recognition dataset` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification = `A typical data point comprises the audio signal iself` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual speaker recognition dataset collected from the CC BY 4.0 YouTube videos` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The VoxTube is a multilingual speaker recognition dataset collected from the CC BY 4.0 YouTube videos.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
