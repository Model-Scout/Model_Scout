---
type: "dataset"
id: "jg07/SpeechAmplitueEnvelope17Languages"
source: "huggingface"
url: "https://huggingface.co/datasets/jg07/SpeechAmplitueEnvelope17Languages"
downloads: 37
summary: "17개 언어의 음성 진폭 엔벨로프 데이터를 포함한 음성 신호 분석용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# jg07/SpeechAmplitueEnvelope17Languages

> dataset · [Hugging Face](https://huggingface.co/datasets/jg07/SpeechAmplitueEnvelope17Languages)

17개 언어의 음성 진폭 엔벨로프 데이터를 포함한 음성 신호 분석용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Speech Amplitude envelope computed on audio files` · 신뢰도 low
- **작업**: [[음성 인식]] — ner · readme = `Audiofiles were then transform to mono, downsampled to 16KHz and cut in pieces of 3 seconds.` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `Audiofiles were then transform to mono, downsampled to 16KHz and cut in pieces of 3 seconds.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme = `Speech Amplitude envelope data was downsampled to 512Hz.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Speech Amplitude envelope computed on audio files extracted from ‘www.faithcomesbyhearing.com'` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains Speech Amplitude envelope computed on audio files` · 신뢰도 low
