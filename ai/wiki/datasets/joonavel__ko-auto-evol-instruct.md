---
type: "dataset"
id: "joonavel/ko-auto-evol-instruct"
source: "huggingface"
url: "https://huggingface.co/datasets/joonavel/ko-auto-evol-instruct"
downloads: 9
summary: "joonavel/ko-auto-evol-instruct는 Auto-Evol-instruct를 적용해 만든 데이터셋입니다."
readme_status: "thin"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# joonavel/ko-auto-evol-instruct

> dataset · [Hugging Face](https://huggingface.co/datasets/joonavel/ko-auto-evol-instruct)

joonavel/ko-auto-evol-instruct는 Auto-Evol-instruct를 적용해 만든 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Auto-Evol-instruct` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `Auto-Evol-instruct` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Auto-Evol-instruct` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `689` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This Dataset is created from https://huggingface.co/datasets/joonavel/seed_for_evolving by applying Auto-Evol-instruct` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 1033자 ≈ 689 토큰 (viewer statistics, default/train)
