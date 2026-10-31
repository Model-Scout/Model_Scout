---
type: "dataset"
id: "legacy-datasets/multilingual_librispeech"
source: "huggingface"
url: "https://huggingface.co/datasets/legacy-datasets/multilingual_librispeech"
downloads: 172
summary: "Multilingual LibriSpeech는 8개 언어의 음성 인식 연구용 대규모 다국어 음성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[음성 분류]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[it]]"
  - "[[다국어]]"
  - "[[nl]]"
  - "[[pl]]"
  - "[[pt]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# legacy-datasets/multilingual_librispeech

> dataset · [Hugging Face](https://huggingface.co/datasets/legacy-datasets/multilingual_librispeech)

Multilingual LibriSpeech는 8개 언어의 음성 인식 연구용 대규모 다국어 음성 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:audio_classification, task:speech_recognition = `The dataset can be used to train a model for Automatic Speech Recognition (ASR). The model is presented with an audio file` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `The model is presented with an audio file and asked to transcribe the audio file to written text.` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[nl]] — metadata · languages = `nl` · 신뢰도 high
- **언어**: [[pl]] — metadata · languages = `pl` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual LibriSpeech (MLS) dataset is a large multilingual corpus suitable for speech research.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The dataset can be used to train a model for Automatic Speech Recognition (ASR).` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Aliados__nemotron-3.5-asr-streaming-0.6b|Aliados/nemotron-3.5-asr-streaming-0.6b]]
- [[framadhita__INT8-nemotron-3.5-asr-streaming-0.6b|framadhita/INT8-nemotron-3.5-asr-streaming-0.6b]]
- [[nvidia__nemotron-3.5-asr-streaming-0.6b|nvidia/nemotron-3.5-asr-streaming-0.6b]]
- [[onnx-community__nemotron-3.5-asr-streaming-0.6b-onnx-int4|onnx-community/nemotron-3.5-asr-streaming-0.6b-onnx-int4]]
