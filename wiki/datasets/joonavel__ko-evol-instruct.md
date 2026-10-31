---
type: "dataset"
id: "joonavel/ko-evol-instruct"
source: "huggingface"
url: "https://huggingface.co/datasets/joonavel/ko-evol-instruct"
downloads: 9
summary: "evol-instruct 기법을 참고해 만든 한국어 상업용 오픈소스 모델 기반 데이터셋입니다."
readme_status: "ok"
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
# joonavel/ko-evol-instruct

> dataset · [Hugging Face](https://huggingface.co/datasets/joonavel/ko-evol-instruct)

evol-instruct 기법을 참고해 만든 한국어 상업용 오픈소스 모델 기반 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `한국어 데이터셋 입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `한국어 데이터셋 입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `622` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `다른 evol-instruct 데이터셋과 달리 opensource 모델(deepseek-v3)을 사용하여 상업적으로 사용 가능한 데이터셋입니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 933자 ≈ 622 토큰 (viewer statistics, default/train)
