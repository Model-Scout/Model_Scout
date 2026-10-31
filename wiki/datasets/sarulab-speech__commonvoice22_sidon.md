---
type: "dataset"
id: "sarulab-speech/commonvoice22_sidon"
source: "huggingface"
url: "https://huggingface.co/datasets/sarulab-speech/commonvoice22_sidon"
downloads: 3440
summary: "Mozilla Common Voice 22 데이터를 Sidon 음성 복원 모델로 복원한 음성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 인식]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# sarulab-speech/commonvoice22_sidon

> dataset · [Hugging Face](https://huggingface.co/datasets/sarulab-speech/commonvoice22_sidon)

Mozilla Common Voice 22 데이터를 Sidon 음성 복원 모델로 복원한 음성 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — ner · readme = `Sidon speech restoration model` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Sidon resamples chunks to 16 kHz internally and writes 48 kHz FLAC output.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:text_to_speech = `text` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `Sidon resamples chunks to 16 kHz internally and writes 48 kHz FLAC output.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `134 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Mozilla Common Voice 22` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Each language directory contains Sidon-processed shards for the Common Voice splits that exist for that language (`train`, `validation`, `test`, `other`, and `i` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Each language directory contains Sidon-processed shards for the Common Voice splits that exist for that language (`train`, `validation`, `test`, `other`, and `i` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `webdataset` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
