---
type: "dataset"
id: "neureps/warmly-nmt-data"
source: "huggingface"
url: "https://huggingface.co/datasets/neureps/warmly-nmt-data"
downloads: 6
summary: "Warmly 프로젝트의 영어→한국어 번역 학습 및 평가용 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[번역]]"
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
  - "[[평가용]]"
  - "[[학습용]]"
---
# neureps/warmly-nmt-data

> dataset · [Hugging Face](https://huggingface.co/datasets/neureps/warmly-nmt-data)

Warmly 프로젝트의 영어→한국어 번역 학습 및 평가용 합성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `페르소나 제어토큰` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `0.8B 영어 댓글 생성 + 소형 번역기` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:generation, task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Warmly(온기) B안 트랙("0.8B 영어 댓글 생성 + 소형 번역기")의 학습·평가 데이터셋` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `공용 평가셋 — testset40(+8B 참조·NLLB-ft 출력), 제로샷 선발전 bakeoff 전문` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Warmly(온기) B안 트랙("0.8B 영어 댓글 생성 + 소형 번역기")의 학습·평가 데이터셋` · 신뢰도 medium
