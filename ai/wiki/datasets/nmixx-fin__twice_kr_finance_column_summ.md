---
type: "dataset"
id: "nmixx-fin/twice_kr_finance_column_summ"
source: "huggingface"
url: "https://huggingface.co/datasets/nmixx-fin/twice_kr_finance_column_summ"
downloads: 11
summary: "한국 경제 칼럼 요약의 정확성을 검증하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
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
# nmixx-fin/twice_kr_finance_column_summ

> dataset · [Hugging Face](https://huggingface.co/datasets/nmixx-fin/twice_kr_finance_column_summ)

한국 경제 칼럼 요약의 정확성을 검증하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `A task to verify whether the summary of a Korean economic column is correct.` · 신뢰도 low
- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:summarization = `summary of a Korean economic column` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:summarization = `Labeled as 1 if correct, otherwise 0.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `207` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Labeled as 1 if correct, otherwise 0.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 310자 ≈ 207 토큰 (viewer statistics, default/train)
