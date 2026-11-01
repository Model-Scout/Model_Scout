---
type: "dataset"
id: "jungsanghyun/subtitle-summary-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/jungsanghyun/subtitle-summary-dataset"
downloads: 5
summary: "국내 방송사 유튜브 자막 기반 스트리밍 누적 요약 및 검색 키워드 생성 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
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
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jungsanghyun/subtitle-summary-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/jungsanghyun/subtitle-summary-dataset)

국내 방송사 유튜브 자막 기반 스트리밍 누적 요약 및 검색 키워드 생성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:summarization = ``program_name, last_summary, 5min_script`(입력)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = ``current_summary, current_5min_keyword`(출력)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `도메인(유튜브 카테고리): Entertainment 2982 · Travel & Events 2081 · News & Politics 1667 · Education 613 · Film & Animation 249 · Music 212 · Howto & Style 124 · Autos &` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `validation 294 971` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train 2,641 10,159` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
