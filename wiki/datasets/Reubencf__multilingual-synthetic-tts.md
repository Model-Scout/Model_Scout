---
type: "dataset"
id: "Reubencf/multilingual-synthetic-tts"
source: "huggingface"
url: "https://huggingface.co/datasets/Reubencf/multilingual-synthetic-tts"
downloads: 129
summary: "Qwen3-TTS 기반 9개 언어 다국어 합성 음성 데이터셋으로 TTS, ASR, 음성 변환 연구용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
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
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
  - "[[ru]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Reubencf/multilingual-synthetic-tts

> dataset · [Hugging Face](https://huggingface.co/datasets/Reubencf/multilingual-synthetic-tts)

Qwen3-TTS 기반 9개 언어 다국어 합성 음성 데이터셋으로 TTS, ASR, 음성 변환 연구용입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `A large-scale synthetic multilingual speech dataset — 68,677 clips across 9 languages, generated with Qwen3-TTS-12Hz-1.7B-Base using zero-shot voice cloning fro` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **작업**: [[음성 합성]] — metadata · readme, tags, task_categories = `text-to-speech` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:speech_recognition = `A large-scale synthetic multilingual speech dataset — 68,677 clips across 9 languages` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:text_to_speech = `text` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:speech_recognition = `Each clip is paired with the ground-truth text and metadata (language, style, voice).` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `29` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A large-scale synthetic multilingual speech dataset — 68,677 clips across 9 languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Intended for training and evaluating TTS, ASR, voice conversion, and multilingual speech models.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Intended for training and evaluating TTS, ASR, voice conversion, and multilingual speech models.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 116자 ≈ 29 토큰 (viewer statistics, default/train)
