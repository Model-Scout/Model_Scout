---
type: "dataset"
id: "jungsanghyun/subtitle-summary-lgu"
source: "huggingface"
url: "https://huggingface.co/datasets/jungsanghyun/subtitle-summary-lgu"
downloads: 7
summary: "LGUplus 방송 자막을 5분 단위 누적 요약과 검색 키워드로 재구성한 데이터셋입니다."
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
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jungsanghyun/subtitle-summary-lgu

> dataset · [Hugging Face](https://huggingface.co/datasets/jungsanghyun/subtitle-summary-lgu)

LGUplus 방송 자막을 5분 단위 누적 요약과 검색 키워드로 재구성한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:summarization = `프롬프트에는 자막만 사용(제목·메타 미사용).` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `current_summary, current_5min_keyword` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `도메인: 생활정보 9528 · 정보/토크 9458 · 퀴즈/게임 8123 · 푸드/요리 7221 · 토론/대담…` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `validation 1,846 13,177` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train 16,609 118,608` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
