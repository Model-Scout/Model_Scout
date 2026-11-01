---
type: "dataset"
id: "BSC-LT/m-personas"
source: "huggingface"
url: "https://huggingface.co/datasets/BSC-LT/m-personas"
downloads: 192
summary: "mPersonas는 15개 언어의 페르소나 기반 대화 데이터셋으로 다양한 합성 대화 생성을 지원합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# BSC-LT/m-personas

> dataset · [Hugging Face](https://huggingface.co/datasets/BSC-LT/m-personas)

mPersonas는 15개 언어의 페르소나 기반 대화 데이터셋으로 다양한 합성 대화 생성을 지원합니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This dataset is a foundational resource designed to support the generation of diverse synthetic data.` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `persona descriptions synthetically generated` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `persona descriptions synthetically generated` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `15 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2213` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual open-source dataset with high-quality persona descriptions synthetically generated` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `While it can be used for LLM training or fine-tuning, the dataset was primarily designed to support diverse synthetic data generation` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `source_text` 열 p90 8851자 ≈ 2213 토큰 (viewer statistics, default/id)
