---
type: "dataset"
id: "HaniMeni/KoPI-Bench"
source: "huggingface"
url: "https://huggingface.co/datasets/HaniMeni/KoPI-Bench"
downloads: 50
summary: "KoPI-Bench는 한국어로 된 직접 및 간접 프롬프트 인젝션 탐지용 이진 분류 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# HaniMeni/KoPI-Bench

> dataset · [Hugging Face](https://huggingface.co/datasets/HaniMeni/KoPI-Bench)

KoPI-Bench는 한국어로 된 직접 및 간접 프롬프트 인젝션 탐지용 이진 분류 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `- `text_ko`: Korean translated text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `- `label`: 0 (benign) / 1 (injection)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KoPI-Bench is a Korean benchmark for prompt injection detection that integrates both direct and indirect prompt injection attacks.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `| validation | 2,415 | 1,218 | 1,197 |` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `| train | 19,334 | 9,754 | 9,580 |` · 신뢰도 medium
