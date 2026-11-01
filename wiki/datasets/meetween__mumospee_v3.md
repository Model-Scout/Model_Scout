---
type: "dataset"
id: "meetween/mumospee_v3"
source: "huggingface"
url: "https://huggingface.co/datasets/meetween/mumospee_v3"
downloads: 230
summary: "Mumospee V3는 43개 언어의 유튜브 영상에서 추출한 6백만 개 이상의 문장 단위 음성 데이터셋으로, 자동 음성 인식 학습에 사용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# meetween/mumospee_v3

> dataset · [Hugging Face](https://huggingface.co/datasets/meetween/mumospee_v3)

Mumospee V3는 43개 언어의 유튜브 영상에서 추출한 6백만 개 이상의 문장 단위 음성 데이터셋으로, 자동 음성 인식 학습에 사용됩니다.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `the clip audio is the input` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `Whisper large-v3-turbo transcript of the clip (cased and punctuated) is the target` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `Whisper large-v3-turbo transcript of the clip (cased and punctuated) is the target (`text_output`).` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `43 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `114` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The videos come from the YouTube collection of Mumospee V2` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = ``split` | string | `train` | Data split in the speechLMM format: all rows are training data.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text_output` 열 p90 457자 ≈ 114 토큰 (viewer statistics, default/asr)
