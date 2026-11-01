---
type: "dataset"
id: "nmixx-fin/twice_kr_financial_bqa_cls"
source: "huggingface"
url: "https://huggingface.co/datasets/nmixx-fin/twice_kr_financial_bqa_cls"
downloads: 30
summary: "금융 분야 질문에 대해 Yes/No로 답하는 이진 분류 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nmixx-fin/twice_kr_financial_bqa_cls

> dataset · [Hugging Face](https://huggingface.co/datasets/nmixx-fin/twice_kr_financial_bqa_cls)

금융 분야 질문에 대해 Yes/No로 답하는 이진 분류 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `A binary classification task that answers a given question with Yes/No.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `A binary classification task that answers a given question with Yes/No.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `733` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Utilizing the open dataset FINNUMBER/QA_Instruction` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1100자 ≈ 733 토큰 (viewer statistics, default/train)
