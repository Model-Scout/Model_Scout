---
type: "dataset"
id: "kaggle/infobayai/audio-call-center-kannada"
source: "kaggle"
url: "https://www.kaggle.com/datasets/infobayai/audio-call-center-kannada"
downloads: 25
summary: "카나다어 콜센터 이중 채널 음성 데이터로 음성 인식 및 고객 지원 AI 모델 학습용"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# kaggle/infobayai/audio-call-center-kannada

> dataset · [Kaggle](https://www.kaggle.com/datasets/infobayai/audio-call-center-kannada)

카나다어 콜센터 이중 채널 음성 데이터로 음성 인식 및 고객 지원 AI 모델 학습용

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Sentiment analysis and emotion detection` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `Speech-to-Text (STT) for structured call transcription` · 신뢰도 low
- **작업**: [[음성 인식]] — ner · readme = `Training Automatic Speech Recognition (ASR) systems for call center environments` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:information_extraction = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `Speech-to-Text (STT) for structured call transcription` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `Attribution 4.0 International (CC BY 4.0)` · 신뢰도 high
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `High-quality Kannada Call-Center Audio data for training and evaluating AI model` · 신뢰도 medium
