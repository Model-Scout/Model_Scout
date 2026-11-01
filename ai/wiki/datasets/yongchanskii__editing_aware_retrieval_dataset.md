---
type: "dataset"
id: "yongchanskii/editing_aware_retrieval_dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/yongchanskii/editing_aware_retrieval_dataset"
downloads: 16
summary: "한국어 쿼리와 관련 문서 점수를 포함한 편집 인지 검색 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
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
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# yongchanskii/editing_aware_retrieval_dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/yongchanskii/editing_aware_retrieval_dataset)

한국어 쿼리와 관련 문서 점수를 포함한 편집 인지 검색 데이터셋입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `editing_aware_retrieval_dataset` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `- name: query
dtype: string` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `- name: pos
sequence: string` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `123` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `- name: train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `query` 열 p90 184자 ≈ 123 토큰 (viewer statistics, default/train)
