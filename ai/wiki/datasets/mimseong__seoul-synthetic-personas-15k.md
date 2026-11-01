---
type: "dataset"
id: "mimseong/seoul-synthetic-personas-15k"
source: "huggingface"
url: "https://huggingface.co/datasets/mimseong/seoul-synthetic-personas-15k"
downloads: 47
summary: "서울시 거주자 15,000명을 합성한 페르소나 데이터셋으로 정책·상권 시뮬레이션에 활용됨"
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# mimseong/seoul-synthetic-personas-15k

> dataset · [Hugging Face](https://huggingface.co/datasets/mimseong/seoul-synthetic-personas-15k)

서울시 거주자 15,000명을 합성한 페르소나 데이터셋으로 정책·상권 시뮬레이션에 활용됨

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `페르소나 데이터셋` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `5줄 생활 요약 (LLM 생성)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `서울 지역 정책이나 상권 변화에 대한 에이전트 기반 시뮬레이션(agent-based simulation)의 초기 인구로 쓰기 위해 제작되었습니다.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `서울 지역 정책·상권 시뮬레이션의 에이전트 초기화` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
