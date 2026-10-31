---
type: "dataset"
id: "ggh5454/legal-provence-ko-debug"
source: "huggingface"
url: "https://huggingface.co/datasets/ggh5454/legal-provence-ko-debug"
downloads: 37
summary: "legal-provence-ko의 소규모 디버그용 서브셋으로 파이프라인 개발과 실험에 사용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
  - "[[소규모 데이터]]"
---
# ggh5454/legal-provence-ko-debug

> dataset · [Hugging Face](https://huggingface.co/datasets/ggh5454/legal-provence-ko-debug)

legal-provence-ko의 소규모 디버그용 서브셋으로 파이프라인 개발과 실험에 사용됨

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[리랭킹]] — tag_match · readme, tags = `reranking` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `검색 쿼리` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:reranking, task:retrieval = `검색 쿼리` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `문서별 관련성 레이블` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `84` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `validation 소규모` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train 소규모` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `arrow` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `query` 열 p90 126자 ≈ 84 토큰 (viewer statistics, default/validation)
