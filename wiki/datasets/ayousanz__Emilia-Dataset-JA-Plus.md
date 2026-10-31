---
type: "dataset"
id: "ayousanz/Emilia-Dataset-JA-Plus"
source: "huggingface"
url: "https://huggingface.co/datasets/ayousanz/Emilia-Dataset-JA-Plus"
downloads: 740
summary: "Emilia는 101k 시간 규모의 다국어 음성 데이터셋으로 대규모 음성 생성 연구에 활용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[음성 인식]]"
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# ayousanz/Emilia-Dataset-JA-Plus

> dataset · [Hugging Face](https://huggingface.co/datasets/ayousanz/Emilia-Dataset-JA-Plus)

Emilia는 101k 시간 규모의 다국어 음성 데이터셋으로 대규모 음성 생성 연구에 활용됩니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `An Extensive, Multilingual, and Diverse Speech Dataset for Large-Scale Speech Generation` · 신뢰도 medium
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `raw, in-the-wild speech data` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation, task:text_to_speech = `text` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `model-ready data` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `high-quality training data with annotations for speech generation` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
