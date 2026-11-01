---
type: "dataset"
id: "syshim/MuSSeD-EnKo"
source: "huggingface"
url: "https://huggingface.co/datasets/syshim/MuSSeD-EnKo"
downloads: 56
summary: "영어와 한국어 다중 화자 음성 분리용 합성 음성 데이터셋입니다."
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
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# syshim/MuSSeD-EnKo

> dataset · [Hugging Face](https://huggingface.co/datasets/syshim/MuSSeD-EnKo)

영어와 한국어 다중 화자 음성 분리용 합성 음성 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — ner · readme = `A bilingual speech-separation corpus of synthetic multi-speaker mixtures` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — metadata · modality, task:speech_recognition = `audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1959` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A bilingual speech-separation corpus of synthetic multi-speaker mixtures built from English (LibriTTS-R) and Korean read-speech sources` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `37,800 total — 30,000 train / 3,900 dev / 3,900 test` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `meta` 열 p90 2938자 ≈ 1959 토큰 (viewer statistics, 2spk/test)
