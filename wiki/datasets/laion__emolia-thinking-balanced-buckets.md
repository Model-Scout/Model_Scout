---
type: "dataset"
id: "laion/emolia-thinking-balanced-buckets"
source: "huggingface"
url: "https://huggingface.co/datasets/laion/emolia-thinking-balanced-buckets"
downloads: 606
summary: "VoiceNet/emolia-thinking 데이터셋의 음성 차원별 균형 잡힌 버킷 샘플로 음성 특성 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 분류]]"
  - "[[임베딩]]"
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# laion/emolia-thinking-balanced-buckets

> dataset · [Hugging Face](https://huggingface.co/datasets/laion/emolia-thinking-balanced-buckets)

VoiceNet/emolia-thinking 데이터셋의 음성 차원별 균형 잡힌 버킷 샘플로 음성 특성 학습용 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `derived from that dataset's zero-shot VoiceNet-dimension labels` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification = `clips from each ordinal bucket (0–6)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:text_to_speech = `text` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `VoiceNet voice/prosody/timbre/style dimension` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `downstream training / probing sees a balanced distribution` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
