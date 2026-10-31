---
type: "model"
id: "onnx-community/nemotron-3.5-asr-streaming-0.6b-onnx-int4"
source: "huggingface"
url: "https://huggingface.co/onnx-community/nemotron-3.5-asr-streaming-0.6b-onnx-int4"
downloads: 1706
context_length: 1024
task:
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
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
---
# onnx-community/nemotron-3.5-asr-streaming-0.6b-onnx-int4

> model · [Hugging Face](https://huggingface.co/onnx-community/nemotron-3.5-asr-streaming-0.6b-onnx-int4)

## 분류

- **작업**: [[음성 인식]] — metadata · task.matched = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `35 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — metadata · context_length = `1024` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]]

## 학습 데이터

- [[legacy-datasets__multilingual_librispeech|legacy-datasets/multilingual_librispeech]]
- [[nvidia__Granary|nvidia/Granary]]
