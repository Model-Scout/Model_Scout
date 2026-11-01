---
type: "dataset"
id: "BCCard/gemma-4-26B-A4B-korean-on-policy-150k"
source: "huggingface"
url: "https://huggingface.co/datasets/BCCard/gemma-4-26B-A4B-korean-on-policy-150k"
downloads: 35
summary: "한국어 온-정책 질의응답 데이터로 EAGLE-3 모델 재학습 및 일반 명령어 튜닝에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
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
# BCCard/gemma-4-26B-A4B-korean-on-policy-150k

> dataset · [Hugging Face](https://huggingface.co/datasets/BCCard/gemma-4-26B-A4B-korean-on-policy-150k)

한국어 온-정책 질의응답 데이터로 EAGLE-3 모델 재학습 및 일반 명령어 튜닝에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `Korean On-Policy QA (Gemma 4 26B-A4B) — EAGLE-3 training data` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `Columns: instruction (str)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Built to retrain an EAGLE-3 speculator for Korean, but also usable for general instruction-tuning / distillation.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Split: train` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
