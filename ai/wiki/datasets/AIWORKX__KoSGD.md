---
type: "dataset"
id: "AIWORKX/KoSGD"
source: "huggingface"
url: "https://huggingface.co/datasets/AIWORKX/KoSGD"
downloads: 63
summary: "KoSGD는 한국어로 번역 및 검수된 다중 도메인 목적 지향 대화 데이터셋으로, 한국어 LLM의 스키마 이해 및 태스크 수행 평가에 사용됩니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# AIWORKX/KoSGD

> dataset · [Hugging Face](https://huggingface.co/datasets/AIWORKX/KoSGD)

KoSGD는 한국어로 번역 및 검수된 다중 도메인 목적 지향 대화 데이터셋으로, 한국어 LLM의 스키마 이해 및 태스크 수행 평가에 사용됩니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · tags, task_categories = `token-classification` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, tags, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation, task:information_extraction, task:question_answering = `KoSGD는 한국어 LLM이 다중 도메인(21개 이상) 환경에서 얼마나 유연하게 대화 상태를 추적하고 적절한 응답을 생성하는지 종합적으로 평가하기 위해 설계되었습니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `KoSGD는 한국어 LLM이 다중 도메인(21개 이상) 환경에서 얼마나 유연하게 대화 상태를 추적하고 적절한 응답을 생성하는지 종합적으로 평가하기 위해 설계되었습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KoSGD는 Google Research의 Schema-Guided Dialogue(SGD) 데이터셋을 한국어로 변환한 대규모 Task-Oriented Dialogue(ToD) 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `본 벤치마크 평가는 실시간 응답이 가능한 Local 및 API 모델을 대상으로 수행하였습니다.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `chaeyeonn/KoSGD`
