---
type: "dataset"
id: "joyfuljune/S16k"
source: "huggingface"
url: "https://huggingface.co/datasets/joyfuljune/S16k"
downloads: 117
summary: "NetEase Cloud Music에서 수집한 169,148곡의 다중 감정 라벨 음악 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 분류]]"
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
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
  - "[[비상업 전용]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# joyfuljune/S16k

> dataset · [Hugging Face](https://huggingface.co/datasets/joyfuljune/S16k)

NetEase Cloud Music에서 수집한 169,148곡의 다중 감정 라벨 음악 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `pre-extracted audio features` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:audio_classification = `pre-extracted audio features` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding = `metadata, 74 tag columns, emotion labels` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — metadata · modality = `timeseries` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `multi-label emotion annotations` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `61` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `NetEase Cloud Music (网易云音乐) carries editorial tags such as 流行, 治愈, 夜晚` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `169,148 songs with multi-label emotion annotations, the 46,613 user-curated playlists the annotations are derived from` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `description` 열 p90 244자 ≈ 61 토큰 (viewer statistics, playlists/train)
