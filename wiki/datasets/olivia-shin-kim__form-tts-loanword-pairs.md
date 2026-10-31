---
type: "dataset"
id: "olivia-shin-kim/form-tts-loanword-pairs"
source: "huggingface"
url: "https://huggingface.co/datasets/olivia-shin-kim/form-tts-loanword-pairs"
downloads: 21
summary: "한국어 합성 음성 데이터로, 대출어와 고유어 쌍의 인식 비교 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# olivia-shin-kim/form-tts-loanword-pairs

> dataset · [Hugging Face](https://huggingface.co/datasets/olivia-shin-kim/form-tts-loanword-pairs)

한국어 합성 음성 데이터로, 대출어와 고유어 쌍의 인식 비교 연구용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `For controlled tests of how speech recognizers handle loanwords against native words.` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Synthetic speech for a controlled comparison` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `synthesized from Hangul input` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `For controlled tests of how speech recognizers handle loanwords against native words.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Synthetic speech for a controlled comparison in the thesis FORM: Form-tolerant Outcomes of Recognition for Multi-form Items` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `One split, `test`, with 1624 clips.` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `audiofolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
