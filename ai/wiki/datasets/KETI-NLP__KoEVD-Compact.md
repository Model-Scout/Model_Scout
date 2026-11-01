---
type: "dataset"
id: "KETI-NLP/KoEVD-Compact"
source: "huggingface"
url: "https://huggingface.co/datasets/KETI-NLP/KoEVD-Compact"
downloads: 337
summary: "KoEVD-Compact는 난이도별 평가용으로 기존 KoEVD에서 선정한 서브셋 데이터입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# KETI-NLP/KoEVD-Compact

> dataset · [Hugging Face](https://huggingface.co/datasets/KETI-NLP/KoEVD-Compact)

KoEVD-Compact는 난이도별 평가용으로 기존 KoEVD에서 선정한 서브셋 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `multiple-choice` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `task1 입력 위험 판단 (기본)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `task1 입력 위험 판단 (기본)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `유해·차별적·민감한 예시를 평가 목적으로 포함합니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `기존 응답으로 선정한 난이도별 평가 서브셋` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
