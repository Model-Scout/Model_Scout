---
type: "dataset"
id: "ggh5454/legal-provence-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/ggh5454/legal-provence-ko"
downloads: 62
summary: "한국 법률 문서로 구성된 OpenProvence 형식의 쿼리-문서 관련성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ggh5454/legal-provence-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/ggh5454/legal-provence-ko)

한국 법률 문서로 구성된 OpenProvence 형식의 쿼리-문서 관련성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `쿼리-문서 쌍에 대해 관련 span의 character offset을 레이블로 포함합니다.` · 신뢰도 low
- **작업**: [[리랭킹]] — tag_match · readme, tags = `reranking` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `검색 쿼리` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction, task:reranking, task:retrieval = `검색 쿼리` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `문서별 관련성 레이블 (1=관련, 0=비관련)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `99` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `validation 1,000` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train 50,000` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `arrow` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `query` 열 p90 149자 ≈ 99 토큰 (viewer statistics, default/validation)
