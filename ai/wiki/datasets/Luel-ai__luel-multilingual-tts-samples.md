---
type: "dataset"
id: "Luel-ai/luel-multilingual-tts-samples"
source: "huggingface"
url: "https://huggingface.co/datasets/Luel-ai/luel-multilingual-tts-samples"
downloads: 41
summary: "7개 언어의 단문 음성 데이터로 TTS 학습 및 평가에 활용되는 다국어 음성 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
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
  - "[[ar]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[he]]"
  - "[[hi]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Luel-ai/luel-multilingual-tts-samples

> dataset · [Hugging Face](https://huggingface.co/datasets/Luel-ai/luel-multilingual-tts-samples)

7개 언어의 단문 음성 데이터로 TTS 학습 및 평가에 활용되는 다국어 음성 합성 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · readme, tags, task_categories = `text-to-speech` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Each sample is a single-speaker recording of a written prompt` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:text_to_speech = `Each sample is a single-speaker recording of a written prompt` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `A multilingual text-to-speech / read-speech dataset of short scripted utterances across 7 languages.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[he]] — metadata · languages = `he` · 신뢰도 high
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A multilingual text-to-speech / read-speech dataset of short scripted utterances across 7 languages.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Useful for TTS training and evaluation, ASR adaptation, dialect/accent studies, and read-speech benchmarking.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Useful for TTS training and evaluation, ASR adaptation, dialect/accent studies, and read-speech benchmarking.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
