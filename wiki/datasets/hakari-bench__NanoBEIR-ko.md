---
type: "dataset"
id: "hakari-bench/NanoBEIR-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/hakari-bench/NanoBEIR-ko"
downloads: 249
summary: "NanoBEIR-ko는 한국어 문서 랭킹 평가를 위한 Nano 스타일 검색 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[리랭킹]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# hakari-bench/NanoBEIR-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/hakari-bench/NanoBEIR-ko)

NanoBEIR-ko는 한국어 문서 랭킹 평가를 위한 Nano 스타일 검색 데이터셋입니다.

## 분류

- **작업**: [[리랭킹]] — tag_match · tags = `reranking` · 신뢰도 low
- **작업**: [[문서 검색]] — tag_match · readme, tags = `retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:reranking, task:retrieval = `text` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `639` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `NanoBEIR-ko is the Korean language-specific component of MNanoBEIR. It groups compact BEIR-derived retrieval tasks` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `for efficient evaluation of document ranking in that language` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 959자 ≈ 639 토큰 (viewer statistics, queries/NanoArguAna)
