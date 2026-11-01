---
type: "dataset"
id: "KTH/hungarian-single-speaker-tts"
source: "huggingface"
url: "https://huggingface.co/datasets/KTH/hungarian-single-speaker-tts"
downloads: 206
summary: "CSS10 Hungarian 데이터셋은 단일 화자의 헝가리어 음성-텍스트 쌍으로 음성 합성에 사용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
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
  - "[[hu]]"
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
# KTH/hungarian-single-speaker-tts

> dataset · [Hugging Face](https://huggingface.co/datasets/KTH/hungarian-single-speaker-tts)

CSS10 Hungarian 데이터셋은 단일 화자의 헝가리어 음성-텍스트 쌍으로 음성 합성에 사용됩니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `single speaker speech datasets for 10 languages` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · readme, task_categories = `text-to-speech` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme = `audio files recorded by a single volunteer` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:text_to_speech = `their aligned text sourced from LibriVox` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `audio files recorded by a single volunteer` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[hu]] — metadata · languages = `hu` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `37` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `CSS10 is a collection of single speaker speech datasets for 10 languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `audio files recorded by a single volunteer and their aligned text sourced from LibriVox.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `original_text` 열 p90 147자 ≈ 37 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[Trendency__whisper-large-v3-hu|Trendency/whisper-large-v3-hu]]
