---
type: "dataset"
id: "golfoscar/povel-hearheart-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/golfoscar/povel-hearheart-dataset"
downloads: 38
summary: "Hearheart.com에서 수집한 한국어 성인 ASMR 음성 데이터셋으로 음성 합성 및 음성 분류에 활용."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[음성 분류]]"
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# golfoscar/povel-hearheart-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/golfoscar/povel-hearheart-dataset)

Hearheart.com에서 수집한 한국어 성인 ASMR 음성 데이터셋으로 음성 합성 및 음성 분류에 활용.

## 분류

- **작업**: [[음성 분류]] — metadata · readme, task_categories = `audio-classification` · 신뢰도 high
- **작업**: [[음성 합성]] — metadata · tags, task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification = `1,142개 오디오 파일` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:text_to_speech = `text` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `Demucs 보컬 분리 결과` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 성인 ASMR 음성 데이터셋` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `음성 합성 모델 학습 데이터` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `audiofolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
