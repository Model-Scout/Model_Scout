---
type: "dataset"
id: "upstage-isd-agent/scenarios"
source: "huggingface"
url: "https://huggingface.co/datasets/upstage-isd-agent/scenarios"
downloads: 473
summary: "교수설계 AI 에이전트 평가용 한국어 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# upstage-isd-agent/scenarios

> dataset · [Hugging Face](https://huggingface.co/datasets/upstage-isd-agent/scenarios)

교수설계 AI 에이전트 평가용 한국어 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `교수설계(Instructional Systems Design) AI 에이전트 평가용 한국어 벤치마크 데이터셋입니다.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation = `언어 한국어` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `교수설계(Instructional Systems Design) AI 에이전트 평가용 한국어 벤치마크 데이터셋입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · readme, tags = `education` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Test 1,202개 (4.7%)` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Train 24,593개 (95.3%)` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
