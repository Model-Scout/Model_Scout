---
type: "dataset"
id: "hecatonai/Housing_Subscription_QA_Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/hecatonai/Housing_Subscription_QA_Dataset"
downloads: 10
summary: "2024 주택청약 FAQ를 기반으로 한 한국 주택청약 질의응답 데이터셋입니다."
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# hecatonai/Housing_Subscription_QA_Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/hecatonai/Housing_Subscription_QA_Dataset)

2024 주택청약 FAQ를 기반으로 한 한국 주택청약 질의응답 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `question : Question of korea's Housing…` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `answer : Answer for Question same blocks.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `205` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · tags = `finance` · 신뢰도 medium
- **도메인**: [[행정·민원]] — ner · readme = `2024 주택청약 FAQ` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset card aims to be a base template for new datasets.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 308자 ≈ 205 토큰 (viewer statistics, 2021/train)
