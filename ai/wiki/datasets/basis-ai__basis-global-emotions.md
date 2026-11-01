---
type: "dataset"
id: "basis-ai/basis-global-emotions"
source: "huggingface"
url: "https://huggingface.co/datasets/basis-ai/basis-global-emotions"
downloads: 2431
summary: "Basis Global Emotions는 다양한 언어와 감정 표현을 포함한 음성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 분류]]"
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
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# basis-ai/basis-global-emotions

> dataset · [Hugging Face](https://huggingface.co/datasets/basis-ai/basis-global-emotions)

Basis Global Emotions는 다양한 언어와 감정 표현을 포함한 음성 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · readme, task_categories, task_ids = `audio-classification` · 신뢰도 medium
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification = `Each recording is one native speaker performing a line in a described situation according to a steer, which is an emotion (e.g. happy, frustrated) or a directio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:text_to_speech = `text` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each recording is one native speaker performing a line in a described situation according to a steer, which is an emotion (e.g. happy, frustrated) or a directio` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `83 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Each recording is one native speaker performing a line in a described situation according to a steer, which is an emotion (e.g. happy, frustrated) or a directio` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Each recording is one native speaker performing a line in a described situation according to a steer, which is an emotion (e.g. happy, frustrated) or a directio` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
