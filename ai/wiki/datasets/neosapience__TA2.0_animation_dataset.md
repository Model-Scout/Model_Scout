---
type: "dataset"
id: "neosapience/TA2.0_animation_dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/neosapience/TA2.0_animation_dataset"
downloads: 10088
summary: "TA2.0 애니메이션 데이터셋은 9개 언어 음성 기반 AI 생성 애니메이션 영상 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[영상 (출력 형식)|영상]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[it]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[nl]]"
  - "[[pl]]"
  - "[[pt]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# neosapience/TA2.0_animation_dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/neosapience/TA2.0_animation_dataset)

TA2.0 애니메이션 데이터셋은 9개 언어 음성 기반 AI 생성 애니메이션 영상 데이터입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `clips sharing a `ref_id` were generated from the same reference character image (useful for identity-disjoint splits)` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `audio-driven avatar video generation model` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme = `driven by speech audio in 9 languages` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `conditioned on reference character images` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:generation = `text` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — metadata · modality = `video` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[영상 (출력 형식)|영상]] — ner · readme = `11,255 AI-generated anime-style talking avatar video clips (≈30.3 hours)` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[nl]] — metadata · languages = `nl` · 신뢰도 high
- **언어**: [[pl]] — metadata · languages = `pl` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `AI-generated anime-style talking avatar video clips` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Single `train` split` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
