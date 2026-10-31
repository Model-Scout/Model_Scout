---
type: "dataset"
id: "NotoriousH2/countdown-rlvr"
source: "huggingface"
url: "https://huggingface.co/datasets/NotoriousH2/countdown-rlvr"
downloads: 31
summary: "Qwen3-4B 검증용으로 숫자 4개와 사칙연산으로 목표값 만드는 수식 생성 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[소규모 데이터]]"
---
# NotoriousH2/countdown-rlvr

> dataset · [Hugging Face](https://huggingface.co/datasets/NotoriousH2/countdown-rlvr)

Qwen3-4B 검증용으로 숫자 4개와 사칙연산으로 목표값 만드는 수식 생성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `모델에 전달하는 한국어 문제 문자열` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `목표값을 만드는 수식을 생성합니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Countdown 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `train, validation, test 분할` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[NotoriousH2__Qwen3-4B-Countdown-RLVR|NotoriousH2/Qwen3-4B-Countdown-RLVR]]
