---
type: "dataset"
id: "lgris/CVSS-X"
source: "huggingface"
url: "https://huggingface.co/datasets/lgris/CVSS-X"
downloads: 1446
summary: "CVSS-X는 영어에서 28개 언어로 음성-음성 번역을 위한 대규모 다국어 합성 음성 번역 코퍼스입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
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
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# lgris/CVSS-X

> dataset · [Hugging Face](https://huggingface.co/datasets/lgris/CVSS-X)

CVSS-X는 영어에서 28개 언어로 음성-음성 번역을 위한 대규모 다국어 합성 음성 번역 코퍼스입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `speech-to-speech translation (S2ST) corpus` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme = `speech-to-speech translation (S2ST) corpus` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation, task:text_to_speech, task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `speech-to-speech translation (S2ST) corpus` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `29 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a massive synthetic speech-to-speech translation (S2ST) corpus` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `split: test` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `split: train` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
