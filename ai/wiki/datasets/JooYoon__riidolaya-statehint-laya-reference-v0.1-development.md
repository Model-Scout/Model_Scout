---
type: "dataset"
id: "JooYoon/riidolaya-statehint-laya-reference-v0.1-development"
source: "huggingface"
url: "https://huggingface.co/datasets/JooYoon/riidolaya-statehint-laya-reference-v0.1-development"
downloads: 73
summary: "한국어 및 영어 개발 코멘트에서 진행/완료 보고 및 질문 힌트를 위한 동결된 Laya 참조 개발 보고서 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
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
---
# JooYoon/riidolaya-statehint-laya-reference-v0.1-development

> dataset · [Hugging Face](https://huggingface.co/datasets/JooYoon/riidolaya-statehint-laya-reference-v0.1-development)

한국어 및 영어 개발 코멘트에서 진행/완료 보고 및 질문 힌트를 위한 동결된 Laya 참조 개발 보고서 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `The practical target is optional progress/completion-report/question hints in bounded Korean/English development comments.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The eight output columns match the existing intent IDs: question, blocker, reference, progress, completion_report, cancel_request, planned and unclear.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The practical target is optional progress/completion-report/question hints in bounded Korean/English development comments.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Report-only research release; source CI passed. No weights, new model, raw data, features or per-row predictions are included.` · 신뢰도 low
