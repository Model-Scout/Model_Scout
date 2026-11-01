---
type: "dataset"
id: "allenai/Dolci-Instruct-SFT"
source: "huggingface"
url: "https://huggingface.co/datasets/allenai/Dolci-Instruct-SFT"
downloads: 5012
summary: "Dolci Instruct SFT는 다양한 프롬프트를 모아 Olmo 3 7B Instruct SFT 학습에 사용된 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# allenai/Dolci-Instruct-SFT

> dataset · [Hugging Face](https://huggingface.co/datasets/allenai/Dolci-Instruct-SFT)

Dolci Instruct SFT는 다양한 프롬프트를 모아 Olmo 3 7B Instruct SFT 학습에 사용된 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `The Dolci Instruct SFT mixture was used to train Olmo 3 7B Instruct SFT.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `It contains 2,152,112 samples from the following sets: Sources include a mixture of existing prompts` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `It contains 2,152,112 samples from the following sets: Sources include a mixture of existing prompts` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `70 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Sources include a mixture of existing prompts` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The Dolci Instruct SFT mixture was used to train Olmo 3 7B Instruct SFT.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[ATH-MaaS__Marco-Mini-Instruct|ATH-MaaS/Marco-Mini-Instruct]]
- [[ATH-MaaS__Marco-Nano-Instruct|ATH-MaaS/Marco-Nano-Instruct]]
- [[Abu-Dju__Marco-Mini-Instruct|Abu-Dju/Marco-Mini-Instruct]]
