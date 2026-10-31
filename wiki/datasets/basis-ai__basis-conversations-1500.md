---
type: "dataset"
id: "basis-ai/basis-conversations-1500"
source: "huggingface"
url: "https://huggingface.co/datasets/basis-ai/basis-conversations-1500"
downloads: 3420
summary: "Basis Conversations 1500은 최대 4명 동시 참여 다국어 대화 음성 데이터셋으로, 대화 분석용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 분류]]"
  - "[[텍스트 생성]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
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
  - "[[미디어 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# basis-ai/basis-conversations-1500

> dataset · [Hugging Face](https://huggingface.co/datasets/basis-ai/basis-conversations-1500)

Basis Conversations 1500은 최대 4명 동시 참여 다국어 대화 음성 데이터셋으로, 대화 분석용입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — tag_match · tags = `conversational` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification, task:speech_recognition = `Each conversation includes up to 4 simultaneous speakers, each with channel-separated, 48 kHz audio.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:speech_recognition = `transcripts, annotations and speaker metadata can be inspected without downloading audio` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `22 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Basis Conversations 1500 is a multi-party, multilingual, full duplex conversational speech dataset.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `about 100 hours of conversations are human annotated (113k human judgements from 7,362 labelers)` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `audiofolder` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
