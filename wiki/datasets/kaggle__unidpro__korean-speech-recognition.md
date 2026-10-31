---
type: "dataset"
id: "kaggle/unidpro/korean-speech-recognition"
source: "kaggle"
url: "https://www.kaggle.com/datasets/unidpro/korean-speech-recognition"
downloads: 62
summary: "한국어 전화 대화 음성 데이터 10시간 이상으로 자동 음성 인식 모델 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[음성 분류]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
---
# kaggle/unidpro/korean-speech-recognition

> dataset · [Kaggle](https://www.kaggle.com/datasets/unidpro/korean-speech-recognition)

한국어 전화 대화 음성 데이터 10시간 이상으로 자동 음성 인식 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — tag_match · tags = `audio classification` · 신뢰도 low
- **작업**: [[음성 인식]] — tag_match · readme, tags = `automatic speech recognition` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:audio_classification, task:speech_recognition = `Audio of telephone dialogues in Korean` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `transcribing audio` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `native korean speakers` · 신뢰도 low
