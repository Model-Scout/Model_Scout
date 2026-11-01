---
type: "dataset"
id: "jungsanghyun/lgu-rolling-persona"
source: "huggingface"
url: "https://huggingface.co/datasets/jungsanghyun/lgu-rolling-persona"
downloads: 11
summary: "LGUplus 시청 이력 기반 일일 롤링 페르소나 갱신 학습용 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jungsanghyun/lgu-rolling-persona

> dataset · [Hugging Face](https://huggingface.co/datasets/jungsanghyun/lgu-rolling-persona)

LGUplus 시청 이력 기반 일일 롤링 페르소나 갱신 학습용 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `TRL `SFTConfig(assistant_only_loss=True)` + `{% generation %}` 포함 ChatML 템플릿으로 assistant 구간만 loss` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = ``messages`가 문자열 content 표준형이라 `apply_chat_template`로 바로 사용` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `assistant 구간만 loss` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `LGUplus 롤링 시청 페르소나 (Task 1)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = ``train`: 9,900 persona (199,238 step)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
