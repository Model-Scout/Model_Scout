---
type: "dataset"
id: "ENERZAiKR/LGUplus_summary_keyword"
source: "huggingface"
url: "https://huggingface.co/datasets/ENERZAiKR/LGUplus_summary_keyword"
downloads: 8
summary: "한국어 방송 자막 기반 스트리밍 누적 요약과 핵심 키워드 추출 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
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
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ENERZAiKR/LGUplus_summary_keyword

> dataset · [Hugging Face](https://huggingface.co/datasets/ENERZAiKR/LGUplus_summary_keyword)

한국어 방송 자막 기반 스트리밍 누적 요약과 핵심 키워드 추출 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `해당 5분의 핵심 키워드 1개를 뽑는 태스크를 위해 구축되었습니다` · 신뢰도 low
- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:information_extraction, task:summarization = `last_summary 직전 시점까지의 누적 요약 (첫 청크는 "") — 입력` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `current_summary 갱신된 방송 전체 대표 요약 (한 문장) — 출력` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 방송 자막 기반 스트리밍(누적) 요약 + 키워드 추출 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `validation | 2,129 | 13,236` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train | 16,326 | 104,010` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
