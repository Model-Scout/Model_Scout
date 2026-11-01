---
type: "dataset"
id: "werty1248/Korean-1930-Novel-Scene-Summarize"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/Korean-1930-Novel-Scene-Summarize"
downloads: 74
summary: "한국 저작권 만료 소설을 씬 단위로 분리하고 요약한 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
  - "[[문서 검색]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# werty1248/Korean-1930-Novel-Scene-Summarize

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/Korean-1930-Novel-Scene-Summarize)

한국 저작권 만료 소설을 씬 단위로 분리하고 요약한 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `각 Scene에서 인물, 주요 소품, 사건을 추출하고` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `씬 분리
사용 모델: Gemini-1.5-Flash
(띄어쓰기 포함) 100자 이상, 1200자 미만으로 적절한 문장에서 씬 단위로 분리하도록 지시` · 신뢰도 low
- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction, task:retrieval, task:summarization = `(띄어쓰기 포함) 100자 이상, 1200자 미만으로 적절한 문장에서 씬 단위로 분리하도록 지시` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:summarization = `각 Scene에서 인물, 주요 소품, 사건을 추출하고, 요약(scenario)을 생성하도록 함` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `659` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `한국 저작권 만료 소설에 대한 씬 분리 및 요약 데이터 셋` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `총 96개 소설 수집 및 전처리` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 988자 ≈ 659 토큰 (viewer statistics, default/train)
