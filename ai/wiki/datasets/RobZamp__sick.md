---
type: "dataset"
id: "RobZamp/sick"
source: "huggingface"
url: "https://huggingface.co/datasets/RobZamp/sick"
downloads: 1974
summary: "SICK는 합성 의미론 모델 연구를 위한 약 1만 쌍의 영어 문장 유사도 및 함의 관계 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# RobZamp/sick

> dataset · [Hugging Face](https://huggingface.co/datasets/RobZamp/sick)

SICK는 합성 의미론 모델 연구를 위한 약 1만 쌍의 영어 문장 유사도 및 함의 관계 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories, task_ids = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `each pair was annotated for two crucial semantic tasks: relatedness in meaning (with a 5-point rating scale as gold score)` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding = `SICK consists of about 10,000 English sentence pairs` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `each pair was annotated for two crucial semantic tasks: relatedness in meaning (with a 5-point rating scale as gold score) and entailment relation between the t` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-3.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a large size English benchmark tailored for them` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The SICK data set was used in SemEval-2014 Task 1, and it freely available for research purposes.` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[BalaRajesh1__mmbert-small-nli|BalaRajesh1/mmbert-small-nli]]
