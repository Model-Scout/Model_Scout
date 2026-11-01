---
type: "dataset"
id: "ENERZAiKR/LGUplus_recommendation_candidates"
source: "huggingface"
url: "https://huggingface.co/datasets/ENERZAiKR/LGUplus_recommendation_candidates"
downloads: 15
summary: "LG U+ 페르소나 기반 TV 추천 파이프라인의 1차 후보 목록과 프로그램 테이블 데이터입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# ENERZAiKR/LGUplus_recommendation_candidates

> dataset · [Hugging Face](https://huggingface.co/datasets/ENERZAiKR/LGUplus_recommendation_candidates)

LG U+ 페르소나 기반 TV 추천 파이프라인의 1차 후보 목록과 프로그램 테이블 데이터입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `주간페르소나 프로필과 ko-sroberta 임베딩 유사도 + 시청장르 비례배분으로 뽑은 10개` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `LG U+ 페르소나 기반 TV 추천 파이프라인의 1차 후보 목록` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:generation, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `최종 top5 선정(교사 LLM)은 이 후보에서 5개를 고르는 다음 단계` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `LG U+ 페르소나 기반 TV 추천 파이프라인` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `test 후보` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train 후보 (persona×date×block)` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
