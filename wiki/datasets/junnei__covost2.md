---
type: "dataset"
id: "junnei/covost2"
source: "huggingface"
url: "https://huggingface.co/datasets/junnei/covost2"
downloads: 26
summary: "CoVoST 2는 21개 언어에서 영어로, 영어에서 15개 언어로 번역된 대규모 다국어 음성 번역 코퍼스입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 인식]]"
  - "[[번역]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# junnei/covost2

> dataset · [Hugging Face](https://huggingface.co/datasets/junnei/covost2)

CoVoST 2는 21개 언어에서 영어로, 영어에서 15개 언어로 번역된 대규모 다국어 음성 번역 코퍼스입니다.

## 분류

- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `The dataset can be used for Speech-to-text translation (ST). The model is presented with an audio file in one language and asked to transcribe the audio file to` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `The dataset contains the audio, transcriptions, and translations in the following languages` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition, task:translation = `asked to transcribe the audio file to written text in another language.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `22 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dataset is created using Mozilla’s open source Common Voice database of crowdsourced voice recordings.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `| config | train | validation | test |` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
