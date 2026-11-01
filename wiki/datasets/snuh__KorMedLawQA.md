---
type: "dataset"
id: "snuh/KorMedLawQA"
source: "huggingface"
url: "https://huggingface.co/datasets/snuh/KorMedLawQA"
downloads: 49
summary: "한국 의료법 관련 객관식 질문 데이터셋으로, 의료법 LLM 개발과 KMLE 준비에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
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
  - "[[의료·보건]]"
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# snuh/KorMedLawQA

> dataset · [Hugging Face](https://huggingface.co/datasets/snuh/KorMedLawQA)

한국 의료법 관련 객관식 질문 데이터셋으로, 의료법 LLM 개발과 KMLE 준비에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `multiple-choice questions` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `was used to generate questions, options, answers, and detailed reasoning` · 신뢰도 low
- **작업**: [[질의응답]] — tag_match · readme, tags = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation, task:question_answering = `English translations of official South Korean medical laws were used as the foundational texts` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `multiple-choice question` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `healthcare` · 신뢰도 medium
- **도메인**: [[법률]] — ner · readme = `medical-legal domain` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Designed to support the development and evaluation of Large Language Models (LLMs)` · 신뢰도 low
