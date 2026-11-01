---
type: "dataset"
id: "Ash-Hun/Welfare-QA"
source: "huggingface"
url: "https://huggingface.co/datasets/Ash-Hun/Welfare-QA"
downloads: 23
summary: "대한민국 보건복지부 안내책자 기반 복지제도 질의응답 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Ash-Hun/Welfare-QA

> dataset · [Hugging Face](https://huggingface.co/datasets/Ash-Hun/Welfare-QA)

대한민국 보건복지부 안내책자 기반 복지제도 질의응답 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `Question-Answering-Documents 데이터셋입니다` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Question-Answering-Documents 데이터셋입니다` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `79` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `대한민국 보건복지부에서 발간하였으며` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `dataset = load_dataset("Ash-Hun/Welfare-QA", split='train')` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `Answer` 열 p90 119자 ≈ 79 토큰 (viewer statistics, default/train)
