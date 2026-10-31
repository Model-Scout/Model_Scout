---
type: "dataset"
id: "Cognitive-Lab/NayanaIR-CrossBench"
source: "huggingface"
url: "https://huggingface.co/datasets/Cognitive-Lab/NayanaIR-CrossBench"
downloads: 115
summary: "NayanaIR-CrossBench는 다국어 다중모달 문서 검색 벤치마크로, 교차언어 시각 검색 성능 평가용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
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
# Cognitive-Lab/NayanaIR-CrossBench

> dataset · [Hugging Face](https://huggingface.co/datasets/Cognitive-Lab/NayanaIR-CrossBench)

NayanaIR-CrossBench는 다국어 다중모달 문서 검색 벤치마크로, 교차언어 시각 검색 성능 평가용입니다.

## 분류

- **작업**: [[문서 검색]] — ner · readme = `designed to evaluate cross-lingual visual search capabilities` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `Images + Queries + Qrels` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:retrieval = `queries in any language` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Queries + Qrels` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `20 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `6` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual multimodal document retrieval benchmark` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `a comprehensive multilingual multimodal document retrieval benchmark designed to evaluate cross-lingual visual search capabilities` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `doc-id` 열 p90 26자 ≈ 6 토큰 (viewer statistics, corpus/test)
