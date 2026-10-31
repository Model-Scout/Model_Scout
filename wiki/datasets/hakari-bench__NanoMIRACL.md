---
type: "dataset"
id: "hakari-bench/NanoMIRACL"
source: "huggingface"
url: "https://huggingface.co/datasets/hakari-bench/NanoMIRACL"
downloads: 2239
summary: "NanoMIRACL은 MIRACL에서 파생된 다국어 위키피디아 문서 검색 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[리랭킹]]"
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
# hakari-bench/NanoMIRACL

> dataset · [Hugging Face](https://huggingface.co/datasets/hakari-bench/NanoMIRACL)

NanoMIRACL은 MIRACL에서 파생된 다국어 위키피디아 문서 검색 평가용 데이터셋입니다.

## 분류

- **작업**: [[리랭킹]] — tag_match · tags = `reranking` · 신뢰도 low
- **작업**: [[문서 검색]] — tag_match · readme, tags = `retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:reranking, task:retrieval = `Each language split evaluates monolingual retrieval of Wikipedia passages for natural-language questions.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each language split evaluates monolingual retrieval of Wikipedia passages for natural-language questions.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `18 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `12` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Each language split evaluates monolingual retrieval of Wikipedia passages for natural-language questions.` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `NanoMIRACL is a compact multilingual benchmark derived from MIRACL.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 48자 ≈ 12 토큰 (viewer statistics, queries/ar)
