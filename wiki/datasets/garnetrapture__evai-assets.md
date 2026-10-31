---
type: "dataset"
id: "garnetrapture/evai-assets"
source: "huggingface"
url: "https://huggingface.co/datasets/garnetrapture/evai-assets"
downloads: 318
summary: "서브컬처 스타일 AI 학습과 캐릭터 채팅용 캐릭터, 스토리, 음성 자산 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[영상 (출력 형식)|영상]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# garnetrapture/evai-assets

> dataset · [Hugging Face](https://huggingface.co/datasets/garnetrapture/evai-assets)

서브컬처 스타일 AI 학습과 캐릭터 채팅용 캐릭터, 스토리, 음성 자산 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme = `Korean and Japanese voice lines (OGG Vorbis, mono 24 kHz)` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `Character portraits and skins, talk backgrounds, story UI frames (PNG)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:text_to_speech = `Per-character persona profiles, localized dialogue sets and intimacy patterns (JSON / JSONL)` · 신뢰도 medium
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `Story cutscenes (MP4)` · 신뢰도 low
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `Korean and Japanese voice lines (OGG Vorbis, mono 24 kHz)` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `Character portraits and skins, talk backgrounds, story UI frames (PNG)` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Per-character persona profiles, localized dialogue sets and intimacy patterns (JSON / JSONL)` · 신뢰도 medium
- **출력 형식**: [[영상 (출력 형식)|영상]] — ner · readme = `Story cutscenes (MP4)` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Character, story and voice assets for subculture-style AI training and local character-chat applications.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Character, story and voice assets for subculture-style AI training and local character-chat applications.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
