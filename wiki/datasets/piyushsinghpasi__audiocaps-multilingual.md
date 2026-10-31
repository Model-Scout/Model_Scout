---
type: "dataset"
id: "piyushsinghpasi/audiocaps-multilingual"
source: "huggingface"
url: "https://huggingface.co/datasets/piyushsinghpasi/audiocaps-multilingual"
downloads: 97
summary: "AudioCaps 오디오 클립에 33개 언어 다국어 캡션을 추가한 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# piyushsinghpasi/audiocaps-multilingual

> dataset · [Hugging Face](https://huggingface.co/datasets/piyushsinghpasi/audiocaps-multilingual)

AudioCaps 오디오 클립에 33개 언어 다국어 캡션을 추가한 평가용 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — metadata · task_categories = `audio-text-to-text` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — metadata · modality, task:speech_recognition = `audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `captions in multiple languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `captions in multiple languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `33 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `31` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual and cross-lingual audio–text models` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `The dataset is intended primarily for evaluation and analysis` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `audiofolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `mal_Mlym` 열 p90 126자 ≈ 31 토큰 (viewer statistics, default/test)
