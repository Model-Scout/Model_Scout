---
type: "dataset"
id: "Scicom-intl/semantic-vad-eot"
source: "huggingface"
url: "https://huggingface.co/datasets/Scicom-intl/semantic-vad-eot"
downloads: 22339
summary: "다국어 음성 데이터와 침묵 구간 정보를 포함한 사용자 발화 단위의 음성 데이터셋으로, 음성 대화의 끝 지점 탐지에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 분류]]"
  - "[[텍스트 생성]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Scicom-intl/semantic-vad-eot

> dataset · [Hugging Face](https://huggingface.co/datasets/Scicom-intl/semantic-vad-eot)

다국어 음성 데이터와 침묵 구간 정보를 포함한 사용자 발화 단위의 음성 데이터셋으로, 음성 대화의 끝 지점 탐지에 활용됨.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `voice-activity-detection` · 신뢰도 low
- **작업**: [[텍스트 생성]] — tag_match · tags = `conversational` · 신뢰도 low
- **작업**: [[음성 인식]] — ner · readme = `Each row is one user turn: an audio clip (16 kHz mp3), its words, and ordered silence_spans.` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification, task:speech_recognition = `Each row is one user turn: an audio clip (16 kHz mp3)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:speech_recognition = `its words, and ordered silence_spans.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `15 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `End-of-turn (semantic VAD) turns, schema-compatible with livekit/eot-bench-data.` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
