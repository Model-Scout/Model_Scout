---
type: "dataset"
id: "sinabis-group/sinabis-10k-synthetic-ediscovery-testset"
source: "huggingface"
url: "https://huggingface.co/datasets/sinabis-group/sinabis-10k-synthetic-ediscovery-testset"
downloads: 108
summary: "eDiscovery 및 포렌식 소프트웨어 테스트용 10,100개 문서의 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[표 (입력 형식)|표]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# sinabis-group/sinabis-10k-synthetic-ediscovery-testset

> dataset · [Hugging Face](https://huggingface.co/datasets/sinabis-group/sinabis-10k-synthetic-ediscovery-testset)

eDiscovery 및 포렌식 소프트웨어 테스트용 10,100개 문서의 합성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `testing eDiscovery and forensic software end to end: processing, de-duplication, e-mail threading, search, TAR / predictive coding, privilege screening, PII det` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · modality, readme = `the native files at `natives/ / . `` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:retrieval = `extracted text per document (`text/ / .txt`), empty where nothing can be extracted` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `scores a tool's output (CSV, Parquet or JSON Lines, one row per `doc_id`) for relevance per matter (incl. TAR ranking), privilege, hot documents, PII, de-duplic` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `26 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `16` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `All people, companies, agencies, events and data are fictional` · 신뢰도 low
- **도메인**: [[법률]] — tag_match · tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `A fully synthetic, 10,100-document collection for testing eDiscovery and forensic software end to end` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `sha256` 열 p90 64자 ≈ 16 토큰 (viewer statistics, manifest/train)
