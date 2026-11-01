---
type: "dataset"
id: "Wi-Fi/korean-full-duplex-synthetic-dataset-preview"
source: "huggingface"
url: "https://huggingface.co/datasets/Wi-Fi/korean-full-duplex-synthetic-dataset-preview"
downloads: 75
summary: "한국어 풀듀플렉스 합성 음성 데이터셋으로 대화 음성 및 이벤트 정보를 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[음성 인식]]"
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Wi-Fi/korean-full-duplex-synthetic-dataset-preview

> dataset · [Hugging Face](https://huggingface.co/datasets/Wi-Fi/korean-full-duplex-synthetic-dataset-preview)

한국어 풀듀플렉스 합성 음성 데이터셋으로 대화 음성 및 이벤트 정보를 포함함.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `100 conversation WAV files` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:text_to_speech = ``events[].text`: utterance text` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `100 conversation WAV files` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = ``events[].text`: utterance text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `55` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean full-duplex synthetic speech dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Public preview of a Korean full-duplex synthetic speech dataset. This repository contains 100 conversations sampled from a corpus of 89,273 conversations (2,000` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `situation` 열 p90 83자 ≈ 55 토큰 (viewer statistics, representative/train)
