---
type: "dataset"
id: "ai-music/ai-music-deduplicated"
source: "huggingface"
url: "https://huggingface.co/datasets/ai-music/ai-music-deduplicated"
downloads: 2694
summary: "Mureka, Riffusion, Sonauto, Suno, Udio 5개 플랫폼의 AI 생성 음악과 메타데이터 대규모 모음집입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ai-music/ai-music-deduplicated

> dataset · [Hugging Face](https://huggingface.co/datasets/ai-music/ai-music-deduplicated)

Mureka, Riffusion, Sonauto, Suno, Udio 5개 플랫폼의 AI 생성 음악과 메타데이터 대규모 모음집입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Each song includes the original audio file and its full platform metadata as a JSON sidecar.` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `A large-scale collection of AI-generated music from five platforms` · 신뢰도 low
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-audio` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification = `Each song includes the original audio file` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval, task:text_to_speech = `full platform metadata as a JSON sidecar` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `Each song includes the original audio file` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `full platform metadata as a JSON sidecar` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `9` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A large-scale collection of AI-generated music from five platforms` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A large-scale collection of AI-generated music from five platforms` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `webdataset` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `__key__` 열 p90 36자 ≈ 9 토큰 (viewer statistics, default/train)
