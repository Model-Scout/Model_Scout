---
type: "dataset"
id: "deepghs/arknights_voices_kr"
source: "huggingface"
url: "https://huggingface.co/datasets/deepghs/arknights_voices_kr"
downloads: 102
summary: "Arknights 게임 캐릭터 음성-텍스트 한국어 데이터셋으로 ASR/ASV 모델 학습에 활용됨."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[음성 분류]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
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
  - "[[소규모 데이터]]"
---
# deepghs/arknights_voices_kr

> dataset · [Hugging Face](https://huggingface.co/datasets/deepghs/arknights_voices_kr)

Arknights 게임 캐릭터 음성-텍스트 한국어 데이터셋으로 ASR/ASV 모델 학습에 활용됨.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · readme, task_categories = `automatic-speech-recognition` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification, task:speech_recognition = `9996 records, 23.1 hours in total.` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `voice_text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `voice_text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `84` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KR Voice-Text Dataset for Arknights Waifus` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Very useful for fine-tuning or evaluating ASR/ASV models.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `voice_text` 열 p90 126자 ≈ 84 토큰 (viewer statistics, default/train)
