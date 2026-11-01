---
type: "dataset"
id: "khursanirevo/multiturn_ks"
source: "huggingface"
url: "https://huggingface.co/datasets/khursanirevo/multiturn_ks"
downloads: 374
summary: "139개 유튜브 영상의 다중 언어 대화 및 스테레오 오디오 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 인식]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# khursanirevo/multiturn_ks

> dataset · [Hugging Face](https://huggingface.co/datasets/khursanirevo/multiturn_ks)

139개 유튜브 영상의 다중 언어 대화 및 스테레오 오디오 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Audio: Stereo audio with speaker separation (speaker 0 = left channel, speaker 1 = right channel)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `Multi-language: Transcripts in 9 languages (en, ms, zh-Hans, zh-Hant, ru, id, ar, ja, ko)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `Multi-language: Transcripts in 9 languages (en, ms, zh-Hans, zh-Hant, ru, id, ar, ja, ko)` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[id]] — metadata · languages = `id` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[ms]] — metadata · languages = `ms` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `8 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multiturn dialogue dataset with speaker-separated stereo audio and multi-language transcripts from 139 YouTube videos.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Created from YouTube videos with dialogue separation using DialogueSidon model.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
