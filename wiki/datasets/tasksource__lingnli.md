---
type: "dataset"
id: "tasksource/lingnli"
source: "huggingface"
url: "https://huggingface.co/datasets/tasksource/lingnli"
downloads: 2340
summary: "ling_in_loop 데이터셋은 NLU 데이터 수집 개선을 위한 언어학자 개입 연구용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# tasksource/lingnli

> dataset · [Hugging Face](https://huggingface.co/datasets/tasksource/lingnli)

ling_in_loop 데이터셋은 NLU 데이터 수집 개선을 위한 언어학자 개입 연구용입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Does Putting a Linguist in the Loop Improve {NLU} Data Collection?` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Does Putting a Linguist in the Loop Improve {NLU} Data Collection?` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `23` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Does Putting a Linguist in the Loop Improve {NLU} Data Collection?` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `https://huggingface.co/datasets/tasksource/lingnli` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `hypothesis` 열 p90 92자 ≈ 23 토큰 (viewer statistics, default/validation)

## 이 데이터로 학습한 모델

- [[BalaRajesh1__mmbert-small-nli|BalaRajesh1/mmbert-small-nli]]
