---
type: "dataset"
id: "HelightDev/nvt-voice-pack2-clips"
source: "huggingface"
url: "https://huggingface.co/datasets/HelightDev/nvt-voice-pack2-clips"
downloads: 351
summary: "23개 언어의 음성 클립과 전사로 다국어 음성 인식 모델 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 인식]]"
  - "[[음성 합성]]"
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
---
# HelightDev/nvt-voice-pack2-clips

> dataset · [Hugging Face](https://huggingface.co/datasets/HelightDev/nvt-voice-pack2-clips)

23개 언어의 음성 클립과 전사로 다국어 음성 인식 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `audio/SET/SPLIT/SPEAKER/ID.EXT` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:text_to_speech = `Speech clips with transcripts in 23 languages` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `Speech clips with transcripts in 23 languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `23 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Speech clips with transcripts in 23 languages, selected from openly licensed corpora for training a small multilingual speech model` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `for training a small multilingual speech model` · 신뢰도 medium
