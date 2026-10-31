---
type: "dataset"
id: "useKled/conversations-in-korean"
source: "huggingface"
url: "https://huggingface.co/datasets/useKled/conversations-in-korean"
downloads: 24
summary: "Kled 앱으로 수집한 자연스러운 한국어 대화 음성 데이터로, 상업적 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[음성 분류]]"
  - "[[정보 추출]]"
  - "[[언어 모델링]]"
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
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# useKled/conversations-in-korean

> dataset · [Hugging Face](https://huggingface.co/datasets/useKled/conversations-in-korean)

Kled 앱으로 수집한 자연스러운 한국어 대화 음성 데이터로, 상업적 학습용입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `Diarization training with named speaker turns` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `Dialogue and turn-taking modeling` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification, task:speech_recognition = `Audio comes from a phone microphone in the room` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:information_extraction, task:language_modeling = `text` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme = `Audio comes from a phone microphone in the room` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:language_modeling, task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Natural Korean conversations` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `licensed for commercial training` · 신뢰도 medium
