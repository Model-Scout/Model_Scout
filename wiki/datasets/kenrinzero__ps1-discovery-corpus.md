---
type: "dataset"
id: "kenrinzero/ps1-discovery-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/kenrinzero/ps1-discovery-corpus"
downloads: 42
summary: "7,995개 플레이스테이션1 게임 메타데이터로 감성 기반 검색용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# kenrinzero/ps1-discovery-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/kenrinzero/ps1-discovery-corpus)

7,995개 플레이스테이션1 게임 메타데이터로 감성 기반 검색용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `sentence-similarity` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:retrieval = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `292` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A multilingual metadata corpus of 7,995 PlayStation 1 games` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `frwiki_categories` 열 p90 1169자 ≈ 292 토큰 (viewer statistics, default/train)
