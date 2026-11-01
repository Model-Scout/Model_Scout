---
type: "dataset"
id: "FronyAI/ko-multisource-retrieval-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/FronyAI/ko-multisource-retrieval-dataset"
downloads: 20
summary: "여러 공개 출처를 통합한 한국어 query–passage 페어 데이터셋으로 문서 검색에 활용됨."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
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
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# FronyAI/ko-multisource-retrieval-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/FronyAI/ko-multisource-retrieval-dataset)

여러 공개 출처를 통합한 한국어 query–passage 페어 데이터셋으로 문서 검색에 활용됨.

## 분류

- **작업**: [[임베딩]] — metadata · tags, task_categories = `sentence-similarity` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `query
질의문 (2~2,020자)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `passage
대응 문서 (10~2,050자)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `675` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `여러 공개 출처를 하나의 스키마로 통합한 한국어 query–passage 페어 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `stage1, stage2 두 subset. 각각 train 100,000 / valid 10,000행 (총 220,000행, parquet, 151MB)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `passage` 열 p90 1013자 ≈ 675 토큰 (viewer statistics, stage1/train)
