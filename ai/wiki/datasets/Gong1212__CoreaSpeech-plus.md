---
type: "dataset"
id: "Gong1212/CoreaSpeech-plus"
source: "huggingface"
url: "https://huggingface.co/datasets/Gong1212/CoreaSpeech-plus"
downloads: 15
summary: "CoreaSpeech+는 한국어 음성 합성 연구를 위한 700시간 및 2000시간 규모의 음성 데이터셋 모음입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[음성 합성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Gong1212/CoreaSpeech-plus

> dataset · [Hugging Face](https://huggingface.co/datasets/Gong1212/CoreaSpeech-plus)

CoreaSpeech+는 한국어 음성 합성 연구를 위한 700시간 및 2000시간 규모의 음성 데이터셋 모음입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Validation split for Korean TTS training and model selection` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `CoreaSpeech+ is a unified Korean speech dataset repository for text-to-speech research, speech synthesis` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:generation, task:text_to_speech = `text` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `CoreaSpeech+ is a unified Korean speech dataset repository for text-to-speech research` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Korean Universal Testset is organized into three evaluation subsets` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
