---
type: "dataset"
id: "FINAL-Bench/Aether-7B-5Attn-checkpoints"
source: "huggingface"
url: "https://huggingface.co/datasets/FINAL-Bench/Aether-7B-5Attn-checkpoints"
downloads: 94
summary: "Aether-7B-5Attn 중간 사전학습 체크포인트로 재현성과 학습 동역학 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[코드 (출력 형식)|코드]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# FINAL-Bench/Aether-7B-5Attn-checkpoints

> dataset · [Hugging Face](https://huggingface.co/datasets/FINAL-Bench/Aether-7B-5Attn-checkpoints)

Aether-7B-5Attn 중간 사전학습 체크포인트로 재현성과 학습 동역학 연구용 데이터셋입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `Intermediate pretraining checkpoints of FINAL-Bench/Aether-7B-5Attn` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:language_modeling = `Intermediate pretraining checkpoints` · 신뢰도 medium
- **출력 형식**: [[코드 (출력 형식)|코드]] — ner · readme = `Each folder contains `model.safetensors` + `config.json` + tokenizer` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:language_modeling = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Intermediate pretraining checkpoints of FINAL-Bench/Aether-7B-5Attn, released for full reproducibility and training-dynamics research` · 신뢰도 medium
