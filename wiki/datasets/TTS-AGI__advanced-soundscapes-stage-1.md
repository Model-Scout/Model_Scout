---
type: "dataset"
id: "TTS-AGI/advanced-soundscapes-stage-1"
source: "huggingface"
url: "https://huggingface.co/datasets/TTS-AGI/advanced-soundscapes-stage-1"
downloads: 3690
summary: "LAION UAAP 파이프라인의 5백만 사운드스케이프 레시피와 원시 오디오 구성요소 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 분류]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
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
dataset_size:
  - "[[대규모 데이터]]"
---
# TTS-AGI/advanced-soundscapes-stage-1

> dataset · [Hugging Face](https://huggingface.co/datasets/TTS-AGI/advanced-soundscapes-stage-1)

LAION UAAP 파이프라인의 5백만 사운드스케이프 레시피와 원시 오디오 구성요소 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification, task:speech_recognition = `5,000,000 soundscape recipes with raw audio components` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme = `recipe.json — full recipe with timeline, events, loudness, speaker IDs, overlap/density settings` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `multilingual` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset contains Stage 1 output from the LAION Universal Audio Annotation Pipeline (UAAP) data generation plan.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains Stage 1 output from the LAION Universal Audio Annotation Pipeline (UAAP) data generation plan.` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
