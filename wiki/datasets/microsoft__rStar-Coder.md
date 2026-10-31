---
type: "dataset"
id: "microsoft/rStar-Coder"
source: "huggingface"
url: "https://huggingface.co/datasets/microsoft/rStar-Coder"
downloads: 7960
summary: "rStar-Coder는 대규모 경쟁 프로그래밍 문제와 장기 추론 솔루션, 다양한 난이도의 테스트 케이스를 포함한 코드 추론 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
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
# microsoft/rStar-Coder

> dataset · [Hugging Face](https://huggingface.co/datasets/microsoft/rStar-Coder)

rStar-Coder는 대규모 경쟁 프로그래밍 문제와 장기 추론 솔루션, 다양한 난이도의 테스트 케이스를 포함한 코드 추론 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `This dataset aims to enhance code reasoning capabilities in large language models, particularly in handling competitive code problems.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `long-reasoning solutions, and rich test cases` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `rStar-Coder is a large-scale competitive code problem dataset containing 418K programming problems, 580K long-reasoning solutions, and rich test cases of varyin` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The dataset comprises five distinct subsets, categorized by data origin (human-seeded or synthetic) and training paradigm (SFT or RL).` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[FoolDev__Janus-35B-HERETIC|FoolDev/Janus-35B-HERETIC]]
- [[FoolDev__Thanatos-27B-HERETIC|FoolDev/Thanatos-27B-HERETIC]]
