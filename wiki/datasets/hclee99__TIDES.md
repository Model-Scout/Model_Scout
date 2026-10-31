---
type: "dataset"
id: "hclee99/TIDES"
source: "huggingface"
url: "https://huggingface.co/datasets/hclee99/TIDES"
downloads: 217
summary: "한국 대학생 팀의 협업 대화와 역할, 팀 발전을 추적한 장기 이중언어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
---
# hclee99/TIDES

> dataset · [Hugging Face](https://huggingface.co/datasets/hclee99/TIDES)

한국 대학생 팀의 협업 대화와 역할, 팀 발전을 추적한 장기 이중언어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `includes transcripts and chat logs from meetings conducted by participants as they worked on real course projects throughout the semester` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:retrieval = `transcripts and chat logs from meetings` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `collected by tracking Korean university student teams over the course of a semester` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `TIDES includes transcripts and chat logs from meetings conducted by participants as they worked on real course projects throughout the semester` · 신뢰도 low
