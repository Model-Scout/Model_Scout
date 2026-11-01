---
type: "dataset"
id: "nvidia/Granary-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/Granary-v2"
downloads: 1074
summary: "Granary-v2는 48개 언어의 다국어 음성 인식, 번역, 지시문 데이터를 제공하는 NVIDIA의 음성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[음성 인식]]"
  - "[[번역]]"
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
dataset_role:
  - "[[학습용]]"
---
# nvidia/Granary-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/Granary-v2)

Granary-v2는 48개 언어의 다국어 음성 인식, 번역, 지시문 데이터를 제공하는 NVIDIA의 음성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `ready-to-train instruction pairs.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `audio-text-to-text` · 신뢰도 medium
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation, task:question_answering, task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering, task:speech_recognition, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `48 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Granary-v2 is NVIDIA's second release of generated labels and instruction pairs for multilingual speech.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This repository contains label manifests only.` · 신뢰도 medium
