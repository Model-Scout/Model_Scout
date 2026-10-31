---
type: "dataset"
id: "dynohyuck/K-FinancialSpeech"
source: "huggingface"
url: "https://huggingface.co/datasets/dynohyuck/K-FinancialSpeech"
downloads: 137
summary: "금융 서비스 상황에서 감정 발화를 수집한 한국어 금융 도메인 감정 음성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[금융·경제]]"
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# dynohyuck/K-FinancialSpeech

> dataset · [Hugging Face](https://huggingface.co/datasets/dynohyuck/K-FinancialSpeech)

금융 서비스 상황에서 감정 발화를 수집한 한국어 금융 도메인 감정 음성 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories, task_ids = `audio-classification` · 신뢰도 low
- **작업**: [[텍스트 분류]] — ner · readme = `FDS(이상거래탐지) 시스템의 감정 분류 모델 학습을 위해 제작되었습니다.` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification = `16kHz, mono, WAV (PCM 16-bit)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `감정 분류 모델 학습을 위해 제작되었습니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `financial` · 신뢰도 medium
- **도메인**: [[의료·보건]] — ner · readme = `감정 발화를 수집한 한국어 음성 데이터셋` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Speech Emotion Recognition (SER) model training/fine-tuning` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `audiofolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
