---
type: "dataset"
id: "FINGU-AI/synthetic_audio_conversations_v2"
source: "huggingface"
url: "https://huggingface.co/datasets/FINGU-AI/synthetic_audio_conversations_v2"
downloads: 29
summary: "한국어 합성 음성 대화 데이터셋으로 음성 인식 등에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[음성 인식]]"
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# FINGU-AI/synthetic_audio_conversations_v2

> dataset · [Hugging Face](https://huggingface.co/datasets/FINGU-AI/synthetic_audio_conversations_v2)

한국어 합성 음성 대화 데이터셋으로 음성 인식 등에 활용 가능

## 분류

- **작업**: [[음성 인식]] — ner · readme = `audio` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `- name: content` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `- name: content` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
