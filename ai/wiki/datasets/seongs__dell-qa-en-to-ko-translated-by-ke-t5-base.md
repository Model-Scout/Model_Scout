---
type: "dataset"
id: "seongs/dell-qa-en-to-ko-translated-by-ke-t5-base"
source: "huggingface"
url: "https://huggingface.co/datasets/seongs/dell-qa-en-to-ko-translated-by-ke-t5-base"
downloads: 13
summary: "Dell 기술 관련 질문과 답변을 영어에서 한국어로 번역한 QA 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
  - "[[번역]]"
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
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# seongs/dell-qa-en-to-ko-translated-by-ke-t5-base

> dataset · [Hugging Face](https://huggingface.co/datasets/seongs/dell-qa-en-to-ko-translated-by-ke-t5-base)

Dell 기술 관련 질문과 답변을 영어에서 한국어로 번역한 QA 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:translation = `questions and answers` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:translation = `questions and answers` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `152` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `questions and answers related to Dell technologies` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `This dataset can be used for training and evaluating models on Korean question-answering tasks.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset can be used for training and evaluating models on Korean question-answering tasks.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `instruction` 열 p90 227자 ≈ 152 토큰 (viewer statistics, default/train)
