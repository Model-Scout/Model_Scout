---
type: "dataset"
id: "sarulab-speech/yodas2_sidon"
source: "huggingface"
url: "https://huggingface.co/datasets/sarulab-speech/yodas2_sidon"
downloads: 11255
summary: "YODAS2-Sidon은 YODAS-2의 음성 복원 버전으로 음성 합성과 음성 언어 모델링에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[음성 인식]]"
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# sarulab-speech/yodas2_sidon

> dataset · [Hugging Face](https://huggingface.co/datasets/sarulab-speech/yodas2_sidon)

YODAS2-Sidon은 YODAS-2의 음성 복원 버전으로 음성 합성과 음성 언어 모델링에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Speech Synthesis and Spoken Language Modeling` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `Spoken Language Modeling` · 신뢰도 medium
- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `audio file (24 kHz, single channel, restored)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:language_modeling, task:text_to_speech = `text` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `audio file (24 kHz, single channel, restored)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:language_modeling, task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `149 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `YODAS-2 is a massive, multilingual YouTube-derived dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `for efficient large-scale training` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `webdataset` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
