---
type: "dataset"
id: "gijs/speech-latents-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/gijs/speech-latents-v1"
downloads: 9
summary: "Emilia 음성 데이터셋에서 파생된 음성 잠재 표현과 감정 캡션, 점수 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# gijs/speech-latents-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/gijs/speech-latents-v1)

Emilia 음성 데이터셋에서 파생된 음성 잠재 표현과 감정 캡션, 점수 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Audio latents with transcripts, emotion captions and emotion/quality scores` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme = `Audio latents with transcripts, emotion captions and emotion/quality scores` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `text, language, speaker, duration, dnsmos, emotion_caption, emotion_annotation` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `derived from the Emilia speech dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `WebDataset tar shards in data/. Each sample has <key>.npy (float16 latents, [frames, 128])` · 신뢰도 low
