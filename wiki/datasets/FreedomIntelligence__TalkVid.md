---
type: "dataset"
id: "FreedomIntelligence/TalkVid"
source: "huggingface"
url: "https://huggingface.co/datasets/FreedomIntelligence/TalkVid"
downloads: 2324
summary: "TalkVid는 음성 기반 토킹헤드 합성을 위한 대규모 고품질 다국어 영상 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[영상 (출력 형식)|영상]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# FreedomIntelligence/TalkVid

> dataset · [Hugging Face](https://huggingface.co/datasets/FreedomIntelligence/TalkVid)

TalkVid는 음성 기반 토킹헤드 합성을 위한 대규모 고품질 다국어 영상 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `We argue that this generalization gap is a direct symptom of limitations in existing training data` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `Audio-driven talking head synthesis has achieved remarkable photorealism` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `Our experiments demonstrate that a model trained on TalkVid outperforms counterparts trained on previous datasets` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme = `Audio-driven talking head synthesis` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:generation, task:reranking = `text` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · modality, readme = `1244 hours of video from 7729 unique speakers` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[영상 (출력 형식)|영상]] — ner · readme = `Audio-driven talking head synthesis has achieved remarkable photorealism` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `14 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `18` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `audio-path` 열 p90 73자 ≈ 18 토큰 (viewer statistics, default/test)
