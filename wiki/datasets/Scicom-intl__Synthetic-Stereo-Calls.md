---
type: "dataset"
id: "Scicom-intl/Synthetic-Stereo-Calls"
source: "huggingface"
url: "https://huggingface.co/datasets/Scicom-intl/Synthetic-Stereo-Calls"
downloads: 320
summary: "두 채널로 구성된 깨끗한 스튜디오 음성 기반 2인 통화 데이터로, 통화 음성 향상 모델 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
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
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
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
# Scicom-intl/Synthetic-Stereo-Calls

> dataset · [Hugging Face](https://huggingface.co/datasets/Scicom-intl/Synthetic-Stereo-Calls)

두 채널로 구성된 깨끗한 스튜디오 음성 기반 2인 통화 데이터로, 통화 음성 향상 모델 학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `We built these calls to train CallEnhancer on recordings that hold both parties in one channel.` · 신뢰도 low
- **작업**: [[음성 인식]] — ner · readme = `Two-party calls made from clean studio speech. Each call has two channels at 48 kHz, one party per channel` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Each call has two channels at 48 kHz, one party per channel` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme = `We built these calls to train CallEnhancer on recordings that hold both parties in one channel.` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `34 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `4` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Two-party calls made from clean studio speech.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `We built these calls to train CallEnhancer on recordings that hold both parties in one channel.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `speaker_a` 열 p90 16자 ≈ 4 토큰 (viewer statistics, default/test)
