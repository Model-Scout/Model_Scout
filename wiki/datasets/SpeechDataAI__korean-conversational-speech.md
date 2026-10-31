---
type: "dataset"
id: "SpeechDataAI/korean-conversational-speech"
source: "huggingface"
url: "https://huggingface.co/datasets/SpeechDataAI/korean-conversational-speech"
downloads: 92
summary: "한국어 2인 대화 음성 500시간, 상업용 음성 인식·음성 합성 학습용 데이터셋"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[음성 인식]]"
  - "[[음성 합성]]"
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
  - "[[평가용]]"
  - "[[학습용]]"
---
# SpeechDataAI/korean-conversational-speech

> dataset · [Hugging Face](https://huggingface.co/datasets/SpeechDataAI/korean-conversational-speech)

한국어 2인 대화 음성 500시간, 상업용 음성 인식·음성 합성 학습용 데이터셋

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Speech LLM and audio-understanding fine-tuning` · 신뢰도 medium
- **작업**: [[음성 인식]] — metadata · readme, tags, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **작업**: [[음성 합성]] — metadata · readme, tags, task_categories = `text-to-speech` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Dual-channel audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:text_to_speech = `time-aligned human-verified transcripts` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:speech_recognition = `time-aligned human-verified transcripts` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean Conversational Speech Dataset` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `licensed for commercial ASR, TTS and voice AI training` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `licensed for commercial ASR, TTS and voice AI training` · 신뢰도 medium
