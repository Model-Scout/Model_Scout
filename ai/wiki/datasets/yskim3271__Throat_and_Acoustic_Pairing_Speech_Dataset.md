---
type: "dataset"
id: "yskim3271/Throat_and_Acoustic_Pairing_Speech_Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/yskim3271/Throat_and_Acoustic_Pairing_Speech_Dataset"
downloads: 410
summary: "60명의 한국어 원어민이 동시에 녹음한 목소리와 음향 마이크 음성 쌍 데이터셋으로 음성 향상 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# yskim3271/Throat_and_Acoustic_Pairing_Speech_Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/yskim3271/Throat_and_Acoustic_Pairing_Speech_Dataset)

60명의 한국어 원어민이 동시에 녹음한 목소리와 음향 마이크 음성 쌍 데이터셋으로 음성 향상 연구에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This dataset facilitates speech enhancement research by enabling the development of models that recover lost high-frequency components and improve intelligibili` · 신뢰도 low
- **작업**: [[음성 인식]] — ner · readme = `The Throat and Acoustic Paired Speech (TAPS) dataset is a standardized corpus designed for deep learning-based speech enhancement` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Each dataset entry consists of metadata and paired audio recordings.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `The dataset includes both `text` (orthographic transcript) and `normalized_text` (pronunciation-oriented transcript) fields` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme = `Each dataset entry consists of metadata and paired audio recordings.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:speech_recognition = `The dataset includes both `text` (orthographic transcript) and `normalized_text` (pronunciation-oriented transcript) fields` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `56` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dataset provides paired recordings from 60 native Korean speakers` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Development Set (10 speakers, 1,000 utterances, 2.5 hours)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Training Set (40 speakers, 4,000 utterances, 10.2 hours)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `normalized_text` 열 p90 85자 ≈ 56 토큰 (viewer statistics, default/test)
