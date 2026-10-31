---
type: "dataset"
id: "danish-foundation-models/multi-ifeval"
source: "huggingface"
url: "https://huggingface.co/datasets/danish-foundation-models/multi-ifeval"
downloads: 1095
summary: "300개 이상의 언어로 번역·현지화된 영어 IFEval 기반 명령어 수행 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
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
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# danish-foundation-models/multi-ifeval

> dataset · [Hugging Face](https://huggingface.co/datasets/danish-foundation-models/multi-ifeval)

300개 이상의 언어로 번역·현지화된 영어 IFEval 기반 명령어 수행 평가 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `This dataset is designed to be used for evaluating models on the instruction-following task.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `prompt containing all the instructions that is to be followed` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `instruction-following dataset` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `301 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `48` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `instruction-following dataset for 300+ languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `There's only a single split, the `test` split, which is intended to be for evaluation purposes.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 191자 ≈ 48 토큰 (viewer statistics, ko/test)
