---
type: "dataset"
id: "anchpop/yap-movie-clips"
source: "huggingface"
url: "https://huggingface.co/datasets/anchpop/yap-movie-clips"
downloads: 52
summary: "411개 영화의 12개 언어 대사 영상 클립과 자막, 음성 인식 데이터로 발음 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 분류]]"
  - "[[정보 추출]]"
  - "[[문서 검색]]"
  - "[[음성 인식]]"
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
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
  - "[[교육]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# anchpop/yap-movie-clips

> dataset · [Hugging Face](https://huggingface.co/datasets/anchpop/yap-movie-clips)

411개 영화의 12개 언어 대사 영상 클립과 자막, 음성 인식 데이터로 발음 연구에 활용됨.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `word-level timings, the surrounding subtitle cues, an independent speech-to-text transcript` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `fetch a single clip without a shard` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:audio_classification, task:speech_recognition = `phoneme recogniser actually heard` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction, task:retrieval, task:text_to_speech = `sentence as written in the film's official subtitles, word-level timings, the surrounding subtitle cues, an independent speech-to-text transcript` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `187,721 short video clips of film dialogue` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `the sentence as written in the film's official subtitles` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `a language-learning app` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `language-learning app` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `published so that the same material can be used for research` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
