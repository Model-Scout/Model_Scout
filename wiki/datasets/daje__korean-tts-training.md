---
type: "dataset"
id: "daje/korean-tts-training"
source: "huggingface"
url: "https://huggingface.co/datasets/daje/korean-tts-training"
downloads: 139
summary: "Google Gemini TTS 모델로 생성한 한국어 음성 데이터셋으로 TTS 학습에 사용됨."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[음성 인식]]"
  - "[[음성 합성]]"
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
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# daje/korean-tts-training

> dataset · [Hugging Face](https://huggingface.co/datasets/daje/korean-tts-training)

Google Gemini TTS 모델로 생성한 한국어 음성 데이터셋으로 TTS 학습에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Google Gemini gemini-2.5-pro-preview-tts 모델 (Voice: Zephyr)로 생성한 한국어 음성 데이터셋입니다.` · 신뢰도 low
- **작업**: [[음성 인식]] — ner · readme = `한국어 TTS 학습용 음성 데이터셋 (120문장)` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · tags, task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `Format: WAV (PCM)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:text_to_speech = `한국어 문장` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `Format: WAV (PCM)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `91` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 TTS 학습용 음성 데이터셋 (120문장)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `한국어 TTS 학습용 음성 데이터셋 (120문장)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `instruct` 열 p90 136자 ≈ 91 토큰 (viewer statistics, default/train)
