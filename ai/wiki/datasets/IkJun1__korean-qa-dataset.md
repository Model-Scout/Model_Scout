---
type: "dataset"
id: "IkJun1/korean-qa-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/IkJun1/korean-qa-dataset"
downloads: 60
summary: "한국어 일반 목적 인스트럭션 튜닝용 QA 데이터셋으로, LLM이 생성한 단일 턴 질문-응답 쌍을 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
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
# IkJun1/korean-qa-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/IkJun1/korean-qa-dataset)

한국어 일반 목적 인스트럭션 튜닝용 QA 데이터셋으로, LLM이 생성한 단일 턴 질문-응답 쌍을 포함함.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `The dataset is intended for general-purpose instruction tuning in Korean.` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `General-purpose Q/A style tasks` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `Each sample is a single-turn pair in the format: prompt: Human: ...` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `5148` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dataset is intended for general-purpose instruction tuning in Korean.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Instruction tuning for Korean-language models` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 7722자 ≈ 5148 토큰 (viewer statistics, default/train)
