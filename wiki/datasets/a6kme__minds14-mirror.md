---
type: "dataset"
id: "a6kme/minds14-mirror"
source: "huggingface"
url: "https://huggingface.co/datasets/a6kme/minds14-mirror"
downloads: 62
summary: "MINDS-14은 전자은행 도메인의 14개 의도 인식용 음성 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
  - "[[음성 인식]]"
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
  - "[[금융·경제]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# a6kme/minds14-mirror

> dataset · [Hugging Face](https://huggingface.co/datasets/a6kme/minds14-mirror)

MINDS-14은 전자은행 도메인의 14개 의도 인식용 음성 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_ids = `keyword-spotting` · 신뢰도 low
- **작업**: [[텍스트 분류]] — ner · readme = `MINDS-14 is training and evaluation resource for intent detection task` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:audio_classification, task:speech_recognition = `with spoken data` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `intent detection task` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `extracted from a commercial system in the e-banking domain` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `MINDS-14 is training and evaluation resource` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `MINDS-14 is training and evaluation resource` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
