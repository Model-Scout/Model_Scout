---
type: "dataset"
id: "SailAjou/S2ST-ko-hibiki"
source: "huggingface"
url: "https://huggingface.co/datasets/SailAjou/S2ST-ko-hibiki"
downloads: 33
summary: "한국어→영어 동시 음성-음성 번역을 위한 대규모 코퍼스, Hibiki 스타일 모델 미세조정용"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[음성 인식]]"
  - "[[음성 합성]]"
  - "[[번역]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# SailAjou/S2ST-ko-hibiki

> dataset · [Hugging Face](https://huggingface.co/datasets/SailAjou/S2ST-ko-hibiki)

한국어→영어 동시 음성-음성 번역을 위한 대규모 코퍼스, Hibiki 스타일 모델 미세조정용

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Korean → English simultaneous (streaming) speech-to-speech translation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `neural-codec speech modeling` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `real Korean source speech` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation, task:language_modeling, task:text_to_speech, task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `synthesized English speech` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:speech_recognition, task:translation = `English translation (text)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean → English simultaneous (streaming) speech-to-speech translation` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `built to fine-tune a Hibiki-style streaming model` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
