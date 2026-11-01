---
type: "dataset"
id: "ENERZAiKR/huibeom_korean-if-verifiable-v1"
source: "huggingface"
url: "https://huggingface.co/datasets/ENERZAiKR/huibeom_korean-if-verifiable-v1"
downloads: 33
summary: "162,223개의 한국어 명령-응답 예제로, 결정론적 규칙으로 제약 조건을 검증하여 정확한 답변 생성을 위한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ENERZAiKR/huibeom_korean-if-verifiable-v1

> dataset · [Hugging Face](https://huggingface.co/datasets/ENERZAiKR/huibeom_korean-if-verifiable-v1)

162,223개의 한국어 명령-응답 예제로, 결정론적 규칙으로 제약 조건을 검증하여 정확한 답변 생성을 위한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Each example pairs a seed question with one or more verifiable Korean constraints, plus an assistant answer` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `The assistant answer carries reasoning_content (the plan) alongside content (the reply).` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `162,223 Korean instruction-following examples whose every constraint is checked by a deterministic rule, not by an LLM.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `162,223 Korean instruction-following examples whose every constraint is checked by a deterministic rule, not by an LLM.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
