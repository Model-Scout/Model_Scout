---
type: "dataset"
id: "mlinmg/translation_dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/mlinmg/translation_dataset"
downloads: 3704
summary: "영어 참조 음성을 복제하는 다국어 합성 음성 데이터셋으로 크로스링구얼 더빙 연구용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 인식]]"
  - "[[음성 합성]]"
  - "[[번역]]"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# mlinmg/translation_dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/mlinmg/translation_dataset)

영어 참조 음성을 복제하는 다국어 합성 음성 데이터셋으로 크로스링구얼 더빙 연구용입니다.

## 분류

- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `Synthetic, expressive, multilingual speech for cross-lingual dubbing research.` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:text_to_speech, task:translation = `Each example pairs a style-annotated text with generated audio that clones an English reference voice` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `Each example pairs a style-annotated text with generated audio that clones an English reference voice` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Synthetic, expressive, multilingual speech for cross-lingual dubbing research.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `All nine subsets below are registered as loadable configurations with a `train` split.` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
