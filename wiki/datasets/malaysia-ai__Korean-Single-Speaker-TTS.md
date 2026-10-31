---
type: "dataset"
id: "malaysia-ai/Korean-Single-Speaker-TTS"
source: "huggingface"
url: "https://huggingface.co/datasets/malaysia-ai/Korean-Single-Speaker-TTS"
downloads: 56
summary: "한국어 단일 화자 음성 데이터셋으로 음성 합성(TTS) 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# malaysia-ai/Korean-Single-Speaker-TTS

> dataset · [Hugging Face](https://huggingface.co/datasets/malaysia-ai/Korean-Single-Speaker-TTS)

한국어 단일 화자 음성 데이터셋으로 음성 합성(TTS) 연구에 활용됨.

## 분류

- **작업**: [[음성 합성]] — ner · readme = `Korean-Single-Speaker-TTS` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme = `kss_audio.zip` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:text_to_speech = `text` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `kss_audio.zip` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `19` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Originally from https://www.kaggle.com/datasets/bryanpark/korean-single-speaker-speech-dataset, we mirror it to HuggingFace.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `audio_filename` 열 p90 29자 ≈ 19 토큰 (viewer statistics, default/train)
