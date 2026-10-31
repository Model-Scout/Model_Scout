---
type: "dataset"
id: "pykorai/pykorai-base"
source: "huggingface"
url: "https://huggingface.co/datasets/pykorai/pykorai-base"
downloads: 9
summary: "pykorai는 한국어 대화형 QA 데이터셋으로 LLM 미세조정에 활용됩니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
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
# pykorai/pykorai-base

> dataset · [Hugging Face](https://huggingface.co/datasets/pykorai/pykorai-base)

pykorai는 한국어 대화형 QA 데이터셋으로 LLM 미세조정에 활용됩니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `거대 언어 모델(LLM)의 미세 조정(Fine-tuning) 및 사전 학습(Pre-training)에 최적화된 고품질 한국어 대화 말뭉치` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `거대 언어 모델(LLM)의 미세 조정(Fine-tuning) 및 사전 학습(Pre-training)에 최적화된 고품질 한국어 대화 말뭉치` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `1B 규모의 QA 데이터셋` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling, task:question_answering = `한국어 대화 말뭉치` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:question_answering = `질문-답변(QA) 다목적 대화 데이터` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `84` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 대화형 데이터셋 구축 프로젝트` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `LLM 학습에 즉시 활용 가능한 표준 형식으로 LTHR을 이용해 패키징합니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 126자 ≈ 84 토큰 (viewer statistics, default/train)
