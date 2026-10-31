---
type: "dataset"
id: "dabsdamoon/emilia-yodas-ko-ready"
source: "huggingface"
url: "https://huggingface.co/datasets/dabsdamoon/emilia-yodas-ko-ready"
downloads: 34
summary: "Emilia-YODAS 한국어 음성 데이터로 TTS 및 정렬기 학습용 고품질 음성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# dabsdamoon/emilia-yodas-ko-ready

> dataset · [Hugging Face](https://huggingface.co/datasets/dabsdamoon/emilia-yodas-ko-ready)

Emilia-YODAS 한국어 음성 데이터로 TTS 및 정렬기 학습용 고품질 음성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `quality-filtered and repackaged as 24 kHz FLAC-in-parquet shards for TTS and aligner training` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · tags, task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme = `24 kHz mono FLAC bytes in `audio`` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation, task:text_to_speech = `text` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `24 kHz mono FLAC bytes in `audio`` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean speech selected from Emilia-YODAS` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = ``split` is a per-utterance train/val assignment used by our training code` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
