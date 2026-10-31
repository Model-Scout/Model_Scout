---
type: "dataset"
id: "PoSTMEDIA/rosetta-ko-math-synth-dpo"
source: "huggingface"
url: "https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-math-synth-dpo"
downloads: 22
summary: "한국어 수학 문제와 단계별 해답을 포함한 합성 데이터로, 수학 문제 해결 모델 학습에 사용됨."
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
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# PoSTMEDIA/rosetta-ko-math-synth-dpo

> dataset · [Hugging Face](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-math-synth-dpo)

한국어 수학 문제와 단계별 해답을 포함한 합성 데이터로, 수학 문제 해결 모델 학습에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation = `the Korean question` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `assistant responses; `chosen` is the verified-correct / better-grounded answer` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `Korean-native mathematics data` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Synthetic data generated with the Qwen3.6-27B teacher model` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
