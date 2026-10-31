---
type: "dataset"
id: "Thomcles/YodaLingua-Korean"
source: "huggingface"
url: "https://huggingface.co/datasets/Thomcles/YodaLingua-Korean"
downloads: 11
summary: "YodaLingua-Korean은 고품질 한국어 음성-텍스트 쌍 데이터로 TTS와 ASR 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[음성 분류]]"
  - "[[음성 인식]]"
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Thomcles/YodaLingua-Korean

> dataset · [Hugging Face](https://huggingface.co/datasets/Thomcles/YodaLingua-Korean)

YodaLingua-Korean은 고품질 한국어 음성-텍스트 쌍 데이터로 TTS와 ASR 학습용입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **작업**: [[음성 합성]] — metadata · tags, task_categories = `text-to-audio` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification, task:speech_recognition = `53,903 audio–transcription pairs` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:text_to_speech = `audio–text pairs` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `audio–text pairs` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This release contains the Korean portion of the multilingual YodaLingua collection.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `YodaLingua is a high-quality speech dataset designed for training text-to-speech (TTS) systems, ASR models` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
