---
type: "dataset"
id: "psdn-ai/CROWS-multilingual"
source: "huggingface"
url: "https://huggingface.co/datasets/psdn-ai/CROWS-multilingual"
downloads: 6171
summary: "Poseidon AI가 수집한 16개 언어의 82만 개 스크립트 음성 데이터셋으로 다국어 음성 인식과 딥페이크 탐지에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 분류]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# psdn-ai/CROWS-multilingual

> dataset · [Hugging Face](https://huggingface.co/datasets/psdn-ai/CROWS-multilingual)

Poseidon AI가 수집한 16개 언어의 82만 개 스크립트 음성 데이터셋으로 다국어 음성 인식과 딥페이크 탐지에 활용됨.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, tags, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification, task:speech_recognition = `821,361 scripted read-speech recordings` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `an automatic transcript, an English translation` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `122` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Crowdsourced Open World Speech (CROWS) Multilingual is a speech corpus collected by Poseidon AI, Inc.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `You can use the data for multilingual ASR and for synthetic-speech (deepfake) detection research` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `english_translated_hypothesis_transcript` 열 p90 487자 ≈ 122 토큰 (viewer statistics, breadth_gt_6_ko/full)
