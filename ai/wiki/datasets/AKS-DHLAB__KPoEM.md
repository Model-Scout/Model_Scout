---
type: "dataset"
id: "AKS-DHLAB/KPoEM"
source: "huggingface"
url: "https://huggingface.co/datasets/AKS-DHLAB/KPoEM"
downloads: 148
summary: "한국 근현대시 483편의 감정 주석 데이터로 시 감정 분류 및 생성 연구에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# AKS-DHLAB/KPoEM

> dataset · [Hugging Face](https://huggingface.co/datasets/AKS-DHLAB/KPoEM)

한국 근현대시 483편의 감정 주석 데이터로 시 감정 분류 및 생성 연구에 활용됨

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories = `text-classification` · 신뢰도 high
- **작업**: [[텍스트 생성]] — ner · readme = `RAG-based emotion-aware poetry generation framework` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation = `7,007 emotion-annotated line-level texts and 615 work-level entries` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `emotion classification model` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `modeling culturally grounded affective patterns in modern Korean literature` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
