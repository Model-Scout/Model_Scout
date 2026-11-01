---
type: "dataset"
id: "hell0ks/namuwiki-extracted-acg-filtered"
source: "huggingface"
url: "https://huggingface.co/datasets/hell0ks/namuwiki-extracted-acg-filtered"
downloads: 30
summary: "애니메이션, 만화, 게임 관련 나무위키 덤프 필터링 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[문화·관광]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# hell0ks/namuwiki-extracted-acg-filtered

> dataset · [Hugging Face](https://huggingface.co/datasets/hell0ks/namuwiki-extracted-acg-filtered)

애니메이션, 만화, 게임 관련 나무위키 덤프 필터링 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `LLM-as-Judge categorization using Qwen3-Next-80B-A3B` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `LLM-as-Judge categorization using Qwen3-Next-80B-A3B` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding = `Remove low effort entries: under 200 char or 3 sentences articles.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Add redirect column for synonym` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `32952` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-2.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `ACG(Anime, Comics and Games) filtered version` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `나무위키 덤프입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `애니메이션, 만화, 게임 필터링 된 나무위키 덤프입니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 49428자 ≈ 32952 토큰 (viewer statistics, default/train)
