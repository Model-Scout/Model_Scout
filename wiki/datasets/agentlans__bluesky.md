---
type: "dataset"
id: "agentlans/bluesky"
source: "huggingface"
url: "https://huggingface.co/datasets/agentlans/bluesky"
downloads: 535
summary: "약 900만 개의 Bluesky 공개 게시글을 정제하여 기계학습 연구용으로 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# agentlans/bluesky

> dataset · [Hugging Face](https://huggingface.co/datasets/agentlans/bluesky)

약 900만 개의 Bluesky 공개 게시글을 정제하여 기계학습 연구용으로 제공하는 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Approximately 9 million public Bluesky posts, processed and cleaned for machine learning research and experimentation.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `Each line in the JSON Lines files represents a single post with the following structure: - `text`: The processed text content of the post` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each line in the JSON Lines files represents a single post with the following structure: - `text`: The processed text content of the post` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `121 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `29` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Approximately 9 million public Bluesky posts` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Approximately 9 million public Bluesky posts, processed and cleaned for machine learning research and experimentation.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 118자 ≈ 29 토큰 (viewer statistics, ko/train)

## 같은 데이터의 사본·중복 등록

- `bobHe2099/bluesky`
