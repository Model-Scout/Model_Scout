---
type: "dataset"
id: "aiqwe/FinShibainu"
source: "huggingface"
url: "https://huggingface.co/datasets/aiqwe/FinShibainu"
downloads: 95
summary: "KRX LLM 경진대회 우수상 수상 shibainu24 모델 학습용 금융 QA 및 MCQA 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[금융·경제]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# aiqwe/FinShibainu

> dataset · [Hugging Face](https://huggingface.co/datasets/aiqwe/FinShibainu)

KRX LLM 경진대회 우수상 수상 shibainu24 모델 학습용 금융 QA 및 MCQA 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Preference의 A는 answer_A, B는 answer_B 컬럼입니다.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `multiple-choice` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = ``question`` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = ``answer_A`` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `235` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = ``validation`: `shibainu24` 모델 Checkpoint 테스트시 사용한 Validation 데이터(MCQA 형태)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = ``mcqa`: `shibainu24` 모델의 MCQA 학습에 사용된 데이터` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `reasoning_process` 열 p90 352자 ≈ 235 토큰 (viewer statistics, mcqa/train)
