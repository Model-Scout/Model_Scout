---
type: "dataset"
id: "PoSTMEDIA/rosetta-ko-law-synth-dpo"
source: "huggingface"
url: "https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-law-synth-dpo"
downloads: 9
summary: "국가법령정보센터 기반 한국어 법률 도메인 합성 데이터로 QA 및 선호도 학습에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
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
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# PoSTMEDIA/rosetta-ko-law-synth-dpo

> dataset · [Hugging Face](https://huggingface.co/datasets/PoSTMEDIA/rosetta-ko-law-synth-dpo)

국가법령정보센터 기반 한국어 법률 도메인 합성 데이터로 QA 및 선호도 학습에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `preference pairs (`chosen`/`rejected`)` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `source-grounded QA/preference/RLVR sets` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = ``prompt` (string) — the Korean question` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = ``chosen` / `rejected` — assistant responses` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `law` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Synthetic data generated with the Qwen3.6-27B teacher model — part of the Rosetta-KO suite` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
