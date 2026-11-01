---
type: "dataset"
id: "ReDUB/SoundHarvest"
source: "huggingface"
url: "https://huggingface.co/datasets/ReDUB/SoundHarvest"
downloads: 65
summary: "ReDUB/SoundHarvest는 다양한 언어의 오디오와 자막 데이터를 포함한 음성 인식 및 다국어 NLP용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[음성 인식]]"
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
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ReDUB/SoundHarvest

> dataset · [Hugging Face](https://huggingface.co/datasets/ReDUB/SoundHarvest)

ReDUB/SoundHarvest는 다양한 언어의 오디오와 자막 데이터를 포함한 음성 인식 및 다국어 NLP용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Use the dataset to develop and evaluate speech-to-speech translation models.` · 신뢰도 low
- **작업**: [[음성 인식]] — ner · readme = `Train ASR models to convert spoken language into text.` · 신뢰도 medium
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `487 hours 27 minutes 59 seconds of audio files.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:translation = `text` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme = `speech-to-speech translation models.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:speech_recognition, task:translation = `Train ASR models to convert spoken language into text.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual audio content` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Train ASR models to convert spoken language into text.` · 신뢰도 medium
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
