---
type: "dataset"
id: "ENERZAiKR/LGUplus_epg_summary"
source: "huggingface"
url: "https://huggingface.co/datasets/ENERZAiKR/LGUplus_epg_summary"
downloads: 10
summary: "U+tv EPG 편성표에 방송 내용 한 문장 요약과 원본 시놉시스를 부여한 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
  - "[[요약]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ENERZAiKR/LGUplus_epg_summary

> dataset · [Hugging Face](https://huggingface.co/datasets/ENERZAiKR/LGUplus_epg_summary)

U+tv EPG 편성표에 방송 내용 한 문장 요약과 원본 시놉시스를 부여한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `방송 내용 한 문장 요약(교사 LLM 생성)` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · task_categories = `text-retrieval` · 신뢰도 low
- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:retrieval, task:summarization = `방송 내용 한 문장 요약(교사 LLM 생성)과 원본 EPG 시놉시스` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `방송 내용 한 문장 요약(교사 LLM 생성)과 원본 EPG 시놉시스` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `test는 train과 겹치지 않는 별도 주(6/14~20)로, 일반화 평가용` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `train / test 구성` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
