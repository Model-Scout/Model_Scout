---
type: "dataset"
id: "laion/emolia-3k-speaker-clusters"
source: "huggingface"
url: "https://huggingface.co/datasets/laion/emolia-3k-speaker-clusters"
downloads: 84
summary: "TTS-AGI/emolia-hq 음성 데이터에서 3,000개 화자 클러스터를 추출한 음성 클러스터 데이터셋입니다."
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
  - "[[표 (출력 형식)|표]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[fr]]"
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
# laion/emolia-3k-speaker-clusters

> dataset · [Hugging Face](https://huggingface.co/datasets/laion/emolia-3k-speaker-clusters)

TTS-AGI/emolia-hq 음성 데이터에서 3,000개 화자 클러스터를 추출한 음성 클러스터 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · readme, task_categories = `audio-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `128-dimensional WavLM speaker timbre embeddings` · 신뢰도 medium
- **작업**: [[음성 합성]] — metadata · tags, task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme, task:audio_classification = `up to 20 representative audio samples per cluster` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:text_to_speech = `text` · 신뢰도 high
- **출력 형식**: [[음성 (출력 형식)|음성]] — ner · readme, task:text_to_speech = `up to 20 representative audio samples per cluster` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Each cluster is represented by its medoid` · 신뢰도 low
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `11` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The original emolia-hq dataset contains hundreds of thousands of speech samples` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A curated set of 3,000 diverse speaker clusters derived from the TTS-AGI/emolia-hq dataset` · 신뢰도 low
- **데이터 형식**: [[미디어 파일]] — metadata · format = `webdataset` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `__key__` 열 p90 45자 ≈ 11 토큰 (viewer statistics, default/train)
