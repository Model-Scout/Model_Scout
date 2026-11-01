---
type: "dataset"
id: "khursanirevo/dialogue-episodes"
source: "huggingface"
url: "https://huggingface.co/datasets/khursanirevo/dialogue-episodes"
downloads: 7596
summary: "다국어 대화 에피소드와 분리된 화자 오디오를 포함한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[문서 검색]]"
  - "[[음성 인식]]"
  - "[[번역]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[영어]]"
  - "[[id]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[ms]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[중국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# khursanirevo/dialogue-episodes

> dataset · [Hugging Face](https://huggingface.co/datasets/khursanirevo/dialogue-episodes)

다국어 대화 에피소드와 분리된 화자 오디오를 포함한 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `Multi-language transcripts in 9 languages` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Separated speakers - 2-channel audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:retrieval, task:translation = `Multi-language transcripts in 9 languages` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition, task:translation = `Multi-language transcripts in 9 languages` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[id]] — metadata · languages = `id` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[ms]] — metadata · languages = `ms` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `8 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multi-Language Dialogue Episodes Dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains dialogue episodes` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `audiofolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `DABAOSs/dialogue-episodes`
