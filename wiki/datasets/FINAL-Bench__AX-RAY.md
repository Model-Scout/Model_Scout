---
type: "dataset"
id: "FINAL-Bench/AX-RAY"
source: "huggingface"
url: "https://huggingface.co/datasets/FINAL-Bench/AX-RAY"
downloads: 200
summary: "AI 안전 진단 기준 117개를 정리한 AX-RAY 데이터셋으로, 모델 평가와 배포 준비에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# FINAL-Bench/AX-RAY

> dataset · [Hugging Face](https://huggingface.co/datasets/FINAL-Bench/AX-RAY)

AI 안전 진단 기준 117개를 정리한 AX-RAY 데이터셋으로, 모델 평가와 배포 준비에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `It organizes 117 AI/AX safety diagnostic criteria, including causal-leakage and causal-integrity review items` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `Every record has item-specific technical English for diagnostic focus, failure rationale, public detection guidance, and remediation guidance` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Build auditable AI-safety evaluation plans
- Map model and deployment risks to evidence requirements` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:information_extraction, task:question_answering, task:retrieval = `The catalog is English-primary and bilingual. Every record has item-specific technical English for diagnostic focus, failure rationale…` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Every record has item-specific technical English for diagnostic focus, failure rationale, public detection guidance, and remediation guidance.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `130` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The catalog is English-primary and bilingual.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = ``catalog` is used instead of `train`: these records define what to assess and what evidence to seek.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `evaluation_question_en` 열 p90 194자 ≈ 130 토큰 (viewer statistics, default/catalog)
