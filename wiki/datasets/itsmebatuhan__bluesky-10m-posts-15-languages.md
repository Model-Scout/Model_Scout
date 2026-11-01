---
type: "dataset"
id: "itsmebatuhan/bluesky-10m-posts-15-languages"
source: "huggingface"
url: "https://huggingface.co/datasets/itsmebatuhan/bluesky-10m-posts-15-languages"
downloads: 85
summary: "15개 언어로 된 Bluesky 10M 소셜 미디어 게시글 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# itsmebatuhan/bluesky-10m-posts-15-languages

> dataset · [Hugging Face](https://huggingface.co/datasets/itsmebatuhan/bluesky-10m-posts-15-languages)

15개 언어로 된 Bluesky 10M 소셜 미디어 게시글 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `Post content` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · tags, task_categories = `fill-mask` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Bluesky Jetstream API (public firehose)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:language_modeling, task:retrieval = `Post content` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Post content` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `15 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `63` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Bluesky 10M Multilingual Posts (15 Languages)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Load dataset
ds = load_dataset("itsmebatuhan/bluesky-10m-posts-15-languages", split="train")` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 252자 ≈ 63 토큰 (viewer statistics, default/train)
