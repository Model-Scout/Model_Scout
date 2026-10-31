---
type: "dataset"
id: "IFM/MegaMath"
source: "huggingface"
url: "https://huggingface.co/datasets/IFM/MegaMath"
downloads: 67713
summary: "MegaMath는 3000억 토큰 규모의 수학 특화 오픈 프리트레이닝 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[코드 (입력 형식)|코드]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# IFM/MegaMath

> dataset · [Hugging Face](https://huggingface.co/datasets/IFM/MegaMath)

MegaMath는 3000억 토큰 규모의 수학 특화 오픈 프리트레이닝 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `MegaMath, an open math pretraining dataset` · 신뢰도 low
- **입력 형식**: [[코드 (입력 형식)|코드]] — ner · readme = `We identified high quality math-related code from large code training corpus` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `mathematical documents from Common Crawl with math-oriented HTML optimizations` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `We synthesized QA-style text, math-related code, and interleaved text-code blocks` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `MegaMath is the largest open math pre-training dataset to date` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[ATH-MaaS__Marco-Mini-Base|ATH-MaaS/Marco-Mini-Base]]
- [[ATH-MaaS__Marco-Mini-Global-Base|ATH-MaaS/Marco-Mini-Global-Base]]
- [[ATH-MaaS__Marco-Nano-Base|ATH-MaaS/Marco-Nano-Base]]
