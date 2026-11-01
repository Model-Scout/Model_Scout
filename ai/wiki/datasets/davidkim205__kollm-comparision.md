---
type: "dataset"
id: "davidkim205/kollm-comparision"
source: "huggingface"
url: "https://huggingface.co/datasets/davidkim205/kollm-comparision"
downloads: 19
summary: "nox-solar-10.7b-v4에 사용된 dpo 데이터셋으로 공개 데이터와 twodigit 제작 데이터로 구성됨."
readme_status: "ok"
readme_language: "en"
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
  - "[[교육]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# davidkim205/kollm-comparision

> dataset · [Hugging Face](https://huggingface.co/datasets/davidkim205/kollm-comparision)

nox-solar-10.7b-v4에 사용된 dpo 데이터셋으로 공개 데이터와 twodigit 제작 데이터로 구성됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `kobest_boolq
한국어 벤치마크 KoBEST` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `kollm_belebele | 다국어 MRC 벤치마크 Belebele의 한국어 subset` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = `한국어 벤치마크 KoBEST` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `한국어 벤치마크 KoBEST` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `234` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `한국어 대학수학능력시험 질답 데이터셋` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `한국어 벤치마크 KoBEST` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `nox-solar-10.7b-v4에 사용된 dpo 데이터셋` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `instruction` 열 p90 351자 ≈ 234 토큰 (viewer statistics, default/train)
