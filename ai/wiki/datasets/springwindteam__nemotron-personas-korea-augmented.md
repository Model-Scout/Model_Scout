---
type: "dataset"
id: "springwindteam/nemotron-personas-korea-augmented"
source: "huggingface"
url: "https://huggingface.co/datasets/springwindteam/nemotron-personas-korea-augmented"
downloads: 44
summary: "한국 정책·여론 시뮬레이션을 위한 100만명 합성 페르소나 증강 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# springwindteam/nemotron-personas-korea-augmented

> dataset · [Hugging Face](https://huggingface.co/datasets/springwindteam/nemotron-personas-korea-augmented)

한국 정책·여론 시뮬레이션을 위한 100만명 합성 페르소나 증강 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[질의응답]] — ner · readme = `정책·여론 멀티에이전트 시뮬레이션의 합성 시민 표본 (제작 목적)` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `한국어 페르소나 기반 생성·대화 모델 학습/평가` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `한국어 페르소나 기반 생성·대화 모델 학습/평가` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `한국어 페르소나 기반 생성·대화 모델 학습/평가` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
