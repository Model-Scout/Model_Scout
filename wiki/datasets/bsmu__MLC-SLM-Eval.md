---
type: "dataset"
id: "bsmu/MLC-SLM-Eval"
source: "huggingface"
url: "https://huggingface.co/datasets/bsmu/MLC-SLM-Eval"
downloads: 410
summary: "MLC-SLM 평가용 다국어 대화 음성 언어 모델 데이터셋의 오라클 분할, 화자 라벨, 전사 제공"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[정보 추출]]"
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
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# bsmu/MLC-SLM-Eval

> dataset · [Hugging Face](https://huggingface.co/datasets/bsmu/MLC-SLM-Eval)

MLC-SLM 평가용 다국어 대화 음성 언어 모델 데이터셋의 오라클 분할, 화자 라벨, 전사 제공

## 분류

- **작업**: [[정보 추출]] — ner · readme = `we release the oracle segmentation, speaker labels, and transcriptions of the Eval sets` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `we only provided the participants with the audio files of the Eval sets` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:information_extraction = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `oracle segmentation, speaker labels, and transcriptions of the Eval sets` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual Conversational Speech Language Model` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `audio files of the Eval sets` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
