---
type: "dataset"
id: "sionic-ai/NanoBEIR-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/sionic-ai/NanoBEIR-ko"
downloads: 150
summary: "한국어 NanoBEIR 벤치마크 데이터셋으로 문서 검색 및 질의응답에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
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
domain:
  - "[[환경·기상]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# sionic-ai/NanoBEIR-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/sionic-ai/NanoBEIR-ko)

한국어 NanoBEIR 벤치마크 데이터셋으로 문서 검색 및 질의응답에 활용됨

## 분류

- **작업**: [[질의응답]] — ner · readme = `STATEMENT → QUESTION 변환` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:retrieval = `전처리된 쿼리 포함` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `STATEMENT → QUESTION 변환` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `66` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[환경·기상]] — ner · readme = `NanoClimateFEVER` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `NanoBEIR-ko (Preprocessed)` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 99자 ≈ 66 토큰 (viewer statistics, queries/NanoClimateFEVER)
