---
type: "dataset"
id: "maitrix-org/Voila-million-voice"
source: "huggingface"
url: "https://huggingface.co/datasets/maitrix-org/Voila-million-voice"
downloads: 548
summary: "Voila는 실시간 음성-언어 통합 모델로 음성 인식, 음성 합성, 음성 번역 등에 활용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
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
  - "[[de]]"
  - "[[영어]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# maitrix-org/Voila-million-voice

> dataset · [Hugging Face](https://huggingface.co/datasets/maitrix-org/Voila-million-voice)

Voila는 실시간 음성-언어 통합 모델로 음성 인식, 음성 합성, 음성 번역 등에 활용됩니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Voila employs an innovative end-to-end model design and a novel hierarchical Transformer architecture.` · 신뢰도 low
- **작업**: [[음성 인식]] — ner · readme = `Voila supports multiple tasks, including Automatic Speech Recognition (ASR)` · 신뢰도 medium
- **작업**: [[번역]] — ner · readme = `speech translation across six languages` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `real-time streaming audio processing` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `speech evaluation benchmark, while Voila Voice Library provides millions of pre-built and customizable voices.` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme = `Text-to-Speech(TTS)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:speech_recognition, task:translation = `Automatic Speech Recognition (ASR)` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Voila is a new family of large voice-language foundation models aiming to lift human-AI interaction experiences` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `We publish the following two datasets: Voila Benchmark and Voila Voice Library.` · 신뢰도 low
