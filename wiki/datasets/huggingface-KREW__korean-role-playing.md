---
type: "dataset"
id: "huggingface-KREW/korean-role-playing"
source: "huggingface"
url: "https://huggingface.co/datasets/huggingface-KREW/korean-role-playing"
downloads: 268
summary: "한국어 기반 다양한 상황과 관계를 반영한 롤플레잉 대화 데이터셋으로 캐릭터 AI 등에 활용 가능"
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
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# huggingface-KREW/korean-role-playing

> dataset · [Hugging Face](https://huggingface.co/datasets/huggingface-KREW/korean-role-playing)

한국어 기반 다양한 상황과 관계를 반영한 롤플레잉 대화 데이터셋으로 캐릭터 AI 등에 활용 가능

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `다양한 캐릭터와 상황에 맞춘 대화를 생성하거나 이해하는 태스크에 사용됩니다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = ``assistant`: 어시스턴트(여자로 가정), 현재 역할극에 맞는 자연스러운 응답` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 기반 롤플레잉 대화 데이터셋` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `모든 서브셋은 현재 `train` split만 제공됩니다.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 같은 데이터의 사본·중복 등록

- `namjanghee/korean-role-playing`

## 이 데이터로 학습한 모델

- [[lunar1020__EXAONE-ExaDialogue-DPO-2.4B|lunar1020/EXAONE-ExaDialogue-DPO-2.4B]]
