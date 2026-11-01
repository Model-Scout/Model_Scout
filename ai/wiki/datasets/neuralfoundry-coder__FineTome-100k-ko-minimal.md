---
type: "dataset"
id: "neuralfoundry-coder/FineTome-100k-ko-minimal"
source: "huggingface"
url: "https://huggingface.co/datasets/neuralfoundry-coder/FineTome-100k-ko-minimal"
downloads: 33
summary: "FineTome-100k-ko-minimal은 대규모 언어 모델의 한국어 지시 튜닝 및 대화 능력 향상을 위한 한국어 번역 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
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
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# neuralfoundry-coder/FineTome-100k-ko-minimal

> dataset · [Hugging Face](https://huggingface.co/datasets/neuralfoundry-coder/FineTome-100k-ko-minimal)

FineTome-100k-ko-minimal은 대규모 언어 모델의 한국어 지시 튜닝 및 대화 능력 향상을 위한 한국어 번역 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `이 데이터셋은 대규모 언어 모델(LLM)의 한국어 지시 튜닝 및 대화 능력 향상을 목표로 합니다.` · 신뢰도 medium
- **작업**: [[번역]] — tag_match · tags = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:translation = `conversations 컬럼을 한국어로 번역한 버전입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `conversations 컬럼을 한국어로 번역한 버전입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `FineTome-100k-ko-minimal는 mlabonne/FineTome-100k 데이터셋의 conversations 컬럼을 한국어로 번역한 버전입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터셋은 대규모 언어 모델(LLM)의 한국어 지시 튜닝 및 대화 능력 향상을 목표로 합니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
