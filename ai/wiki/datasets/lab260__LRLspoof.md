---
type: "dataset"
id: "lab260/LRLspoof"
source: "huggingface"
url: "https://huggingface.co/datasets/lab260/LRLspoof"
downloads: 2768
summary: "66개 언어의 저자원 음성 합성 스푸핑 탐지 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
  - "[[음성 합성]]"
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
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# lab260/LRLspoof

> dataset · [Hugging Face](https://huggingface.co/datasets/lab260/LRLspoof)

66개 언어의 저자원 음성 합성 스푸핑 탐지 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[텍스트 분류]] — ner · readme = `Multilingual low-resource-language anti-spoofing benchmark: 1,304,455 TTS (spoof) utterances across 66 languages and many TTS systems.` · 신뢰도 low
- **작업**: [[음성 합성]] — tag_match · tags = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:audio_classification = `The audio ships as the multi-part tarball `lrl_spoof.tar.gz.part_*`; download + extract it into a ` / / .wav` tree.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:text_to_speech = `text` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = ``data/labels.parquet` (utterance_id + label, all spoof) exists only for arena re-verification.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `66 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual low-resource-language anti-spoofing benchmark: 1,304,455 TTS (spoof) utterances across 66 languages and many TTS systems.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `This repository hosts the benchmark, evaluation protocol, and baseline submissions released with the paper.` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
