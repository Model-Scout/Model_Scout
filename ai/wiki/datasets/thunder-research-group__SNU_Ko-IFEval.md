---
type: "dataset"
id: "thunder-research-group/SNU_Ko-IFEval"
source: "huggingface"
url: "https://huggingface.co/datasets/thunder-research-group/SNU_Ko-IFEval"
downloads: 90
summary: "Ko-IFEval은 한국어 자연어 지시 수행 능력을 평가하는 한국어 지시 수행 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
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
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# thunder-research-group/SNU_Ko-IFEval

> dataset · [Hugging Face](https://huggingface.co/datasets/thunder-research-group/SNU_Ko-IFEval)

Ko-IFEval은 한국어 자연어 지시 수행 능력을 평가하는 한국어 지시 수행 벤치마크입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `All prompts and constraints are written in Korean.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `All prompts and constraints are written in Korean.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Ko-IFEval is a Korean instruction-following benchmark designed to evaluate how well language models can follow natural language instructions in Korean.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Evaluation code and task configurations for this benchmark are available in the evaluation_code directory of the Korean Benchmark Suite GitHub repository.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
