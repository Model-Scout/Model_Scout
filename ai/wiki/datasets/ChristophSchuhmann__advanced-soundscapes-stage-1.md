---
type: "dataset"
id: "ChristophSchuhmann/advanced-soundscapes-stage-1"
source: "huggingface"
url: "https://huggingface.co/datasets/ChristophSchuhmann/advanced-soundscapes-stage-1"
downloads: 51
summary: "LAION UAAP의 Stage 1 음향 데이터셋으로, 원시 오디오 구성요소와 메타데이터를 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
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
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ChristophSchuhmann/advanced-soundscapes-stage-1

> dataset · [Hugging Face](https://huggingface.co/datasets/ChristophSchuhmann/advanced-soundscapes-stage-1)

LAION UAAP의 Stage 1 음향 데이터셋으로, 원시 오디오 구성요소와 메타데이터를 포함함.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[텍스트 분류]] — ner · readme = `Recipe Archetypes | Archetype | Weight | Speech% | Music% | SFX% |` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Stage 1 output from the LAION Universal Audio Annotation Pipeline (UAAP) data generation plan` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `Stage 1 is CPU-only. It: 1. Samples a recipe (archetype, duration, density, overlap, speaker config) 2. Draws raw audio pieces from source datasets` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification, task:speech_recognition = `raw audio components` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation = `recipe.json — full recipe with timeline, events, loudness, speaker IDs, overlap/density settings` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme = `raw audio components` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:speech_recognition = `recipe.json — full recipe with timeline, events, loudness, speaker IDs, overlap/density settings` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `multilingual` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `LAION Universal Audio Annotation Pipeline (UAAP) data generation plan` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Stage 1 output from the LAION Universal Audio Annotation Pipeline (UAAP) data generation plan` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
