---
type: "dataset"
id: "nvidia/Granary"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Granary"
downloads: 6117
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[음성 인식]]"
  - "[[번역]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# nvidia/Granary

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Granary)

## 분류

- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 high
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:translation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `25 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Aliados__nemotron-3.5-asr-streaming-0.6b|Aliados/nemotron-3.5-asr-streaming-0.6b]]
- [[framadhita__INT8-nemotron-3.5-asr-streaming-0.6b|framadhita/INT8-nemotron-3.5-asr-streaming-0.6b]]
- [[nvidia__nemotron-3.5-asr-streaming-0.6b|nvidia/nemotron-3.5-asr-streaming-0.6b]]
- [[onnx-community__nemotron-3.5-asr-streaming-0.6b-onnx-int4|onnx-community/nemotron-3.5-asr-streaming-0.6b-onnx-int4]]
