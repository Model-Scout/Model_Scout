---
type: "dataset"
id: "neurlang/phonetic"
source: "huggingface"
url: "https://huggingface.co/datasets/neurlang/phonetic"
downloads: 23
summary: "140개 이상의 언어에 대한 IPA 음성 데이터셋으로 음성 인식 및 음성 처리에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# neurlang/phonetic

> dataset · [Hugging Face](https://huggingface.co/datasets/neurlang/phonetic)

140개 이상의 언어에 대한 IPA 음성 데이터셋으로 음성 인식 및 음성 처리에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · task_categories = `token-classification` · 신뢰도 low
- **작업**: [[음성 인식]] — ner · readme = `Phonetic IPA Dataset for 140+ languages` · 신뢰도 low
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:information_extraction, task:translation = `Chinese/Mandarin-IPA language sentence pairs were generated` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition, task:translation = `Chinese/Mandarin-IPA language sentence pairs were generated` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `80 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `cc` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Phonetic IPA Dataset for 140+ languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Use our model trained on the dataset` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
