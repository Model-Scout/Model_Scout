---
type: "dataset"
id: "werty1248/Korea-Related-Reddit-posts"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/Korea-Related-Reddit-posts"
downloads: 26
summary: "한국 관련 레딧 게시글과 댓글 데이터셋으로 한국어 포함 게시글과 댓글을 수집함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# werty1248/Korea-Related-Reddit-posts

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/Korea-Related-Reddit-posts)

한국 관련 레딧 게시글과 댓글 데이터셋으로 한국어 포함 게시글과 댓글을 수집함.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `major_language: 본문의 주요 언어` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Contains at least one Korean character in the selftext (body).` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Subreddit comments/submissions 2005-06 to 2024-12 Korea/Korean related posts only` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:embedding, task:retrieval = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2609` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korea/Korean related posts only` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `selftext` 열 p90 3913자 ≈ 2609 토큰 (viewer statistics, default/train)
