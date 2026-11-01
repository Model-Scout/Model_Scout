---
type: "dataset"
id: "kopens/aura-industrial-bench"
source: "huggingface"
url: "https://huggingface.co/datasets/kopens/aura-industrial-bench"
downloads: 52
summary: "산업 현장 LLM 평가용 한국어 데이터셋으로 설비 이상 탐지, 공학 계산, 안전 거절, 환각 능력을 측정함."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# kopens/aura-industrial-bench

> dataset · [Hugging Face](https://huggingface.co/datasets/kopens/aura-industrial-bench)

산업 현장 LLM 평가용 한국어 데이터셋으로 설비 이상 탐지, 공학 계산, 안전 거절, 환각 능력을 측정함.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `설비 이상 탐지 결과를 읽고 해석하는 능력, 공학 계산, 안전 거절, 측정값 환각을 봅니다.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = `설비 이상 탐지 결과를 읽고 해석하는 능력, 공학 계산, 안전 거절, 측정값 환각을 봅니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `고장=원인 일치 · 센서=센서 고장을 그 태그로 지목 · 정상=정상이라 하고 고장 단정 없음 · 경계=단정 없이 추세 감시 권고.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `41` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `산업 현장 LLM 을 재는 한국어 평가셋입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `평가 전용으로 만들었습니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 62자 ≈ 41 토큰 (viewer statistics, dib/train)
