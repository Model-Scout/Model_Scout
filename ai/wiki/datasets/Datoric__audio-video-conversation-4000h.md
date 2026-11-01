---
type: "dataset"
id: "Datoric/audio-video-conversation-4000h"
source: "huggingface"
url: "https://huggingface.co/datasets/Datoric/audio-video-conversation-4000h"
downloads: 48
summary: "4,000시간 분량의 동기화된 음성 및 영상 대화 데이터로 음성-영상 모델 학습에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
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
  - "[[JSON]]"
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Datoric/audio-video-conversation-4000h

> dataset · [Hugging Face](https://huggingface.co/datasets/Datoric/audio-video-conversation-4000h)

4,000시간 분량의 동기화된 음성 및 영상 대화 데이터로 음성-영상 모델 학습에 활용됨.

## 분류

- **작업**: [[임베딩]] — ner · readme = `It is designed for multimodal voice agents, avatar systems, lip-sync models, emotion recognition, paralinguistic understanding, conversational video models, aud` · 신뢰도 low
- **작업**: [[텍스트 생성]] — tag_match · tags = `conversational` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `4,000 hours of synchronized speech and video of natural conversations` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:generation = `text` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `4,000 hours of synchronized speech and video of natural conversations` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:speech_recognition = `transcript segments, speaker turns, timestamps, face visibility, mouth visibility, gesture labels, emotion or tone labels, laughter events, interruption events,` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `21 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `natural conversations across diverse speakers, languages, accents, environments, and interaction styles.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The production dataset is rights-cleared and delivered directly to buyers.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `DatoricAI/audio-video-conversation-4000h`
