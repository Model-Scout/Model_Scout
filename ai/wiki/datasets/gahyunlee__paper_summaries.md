---
type: "dataset"
id: "gahyunlee/paper_summaries"
source: "huggingface"
url: "https://huggingface.co/datasets/gahyunlee/paper_summaries"
downloads: 14
summary: "12,777개 arXiv 논문 기반 학술 연구 분석 및 추천 시스템 구축용 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# gahyunlee/paper_summaries

> dataset · [Hugging Face](https://huggingface.co/datasets/gahyunlee/paper_summaries)

12,777개 arXiv 논문 기반 학술 연구 분석 및 추천 시스템 구축용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `학술 논문 추천 시스템` · 신뢰도 low
- **작업**: [[요약]] — metadata · readme, tags, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:retrieval, task:summarization = `arXiv 논문의 메타데이터` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:summarization = `LLM 기반 다중 요약 실험` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `학술 연구 분석 및 추천 시스템 구축을 위해 설계된12,777개의 arXiv 논문 기반 연구 데이터셋입니다.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `본 데이터셋은 다음과 같은 연구 및 서비스 개발을 위해 설계되었습니다` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
