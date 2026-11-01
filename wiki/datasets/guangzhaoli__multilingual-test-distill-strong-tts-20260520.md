---
type: "dataset"
id: "guangzhaoli/multilingual-test-distill-strong-tts-20260520"
source: "huggingface"
url: "https://huggingface.co/datasets/guangzhaoli/multilingual-test-distill-strong-tts-20260520"
downloads: 39
summary: "다국어 음성 합성 테스트용 음성 데이터셋으로, 여러 언어의 음성 및 메타데이터를 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# guangzhaoli/multilingual-test-distill-strong-tts-20260520

> dataset · [Hugging Face](https://huggingface.co/datasets/guangzhaoli/multilingual-test-distill-strong-tts-20260520)

다국어 음성 합성 테스트용 음성 데이터셋으로, 여러 언어의 음성 및 메타데이터를 포함함.

## 분류

- **작업**: [[음성 합성]] — metadata · readme, tags, task_categories = `text-to-speech` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — metadata · modality = `audio` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:text_to_speech = `Metadata format:
file_path|duration|dnsmos|text` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `data/zh/**/*.wav
data/en/**/*.wav
data/ja/**/*.wav
data/ko/**/*.wav` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `8` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This repository contains a distributable tar-sharded version of multilingual_test_distill_strong_tts_20260520.` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `webdataset` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `__key__` 열 p90 34자 ≈ 8 토큰 (viewer statistics, default/train)
