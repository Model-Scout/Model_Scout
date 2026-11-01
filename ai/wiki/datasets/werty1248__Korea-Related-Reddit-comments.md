---
type: "dataset"
id: "werty1248/Korea-Related-Reddit-comments"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/Korea-Related-Reddit-comments"
downloads: 28
summary: "한국 관련 레딧 댓글과 게시글 데이터셋으로 한국어 및 관련 토론 분석에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# werty1248/Korea-Related-Reddit-comments

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/Korea-Related-Reddit-comments)

한국 관련 레딧 댓글과 게시글 데이터셋으로 한국어 및 관련 토론 분석에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `major_language: 본문의 주요 언어` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Korea/Korean related comments only` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:retrieval = `body: 내용` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `body: 내용` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `624` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Subreddit comments/submissions 2005-06 to 2024-12
Korea/Korean related comments only` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Posts
Contains at least one Korean character in the selftext (body).
Comments
Only comments that reply to Korean posts as defined above.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `body` 열 p90 935자 ≈ 624 토큰 (viewer statistics, default/train)
