---
type: "dataset"
id: "basis-ai/basis-global-emotions"
source: "huggingface"
url: "https://huggingface.co/datasets/basis-ai/basis-global-emotions"
downloads: 2302
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
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# basis-ai/basis-global-emotions

> dataset · [Hugging Face](https://huggingface.co/datasets/basis-ai/basis-global-emotions)

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories, task_ids = `audio-classification` · 신뢰도 high
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — metadata · modality, task:audio_classification = `audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:text_to_speech = `text` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `83 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
