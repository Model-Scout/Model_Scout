---
type: "dataset"
id: "ung30/UrbanReplayBench"
source: "huggingface"
url: "https://huggingface.co/datasets/ung30/UrbanReplayBench"
downloads: 24
summary: "서울시 실시간 도시 데이터 기반의 이벤트 및 컷오프 재현 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ung30/UrbanReplayBench

> dataset · [Hugging Face](https://huggingface.co/datasets/ung30/UrbanReplayBench)

서울시 실시간 도시 데이터 기반의 이벤트 및 컷오프 재현 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `The benchmark therefore evaluates availability to the collection system at a replay cutoff under this declared normalization rule.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `De-identified relational replay tables in `data/replay/*.parquet`.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:question_answering, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `De-identified relational replay tables in `data/replay/*.parquet`.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Public release containing the event/cutoff subset used in the IEEE BigData 2026 manuscript.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
