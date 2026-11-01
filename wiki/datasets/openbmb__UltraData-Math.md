---
type: "dataset"
id: "openbmb/UltraData-Math"
source: "huggingface"
url: "https://huggingface.co/datasets/openbmb/UltraData-Math"
downloads: 24908
summary: "UltraData-Math는 수학적 추론 능력 향상을 위한 대규모 고품질 수학 사전학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[중국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[학술·논문]]"
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# openbmb/UltraData-Math

> dataset · [Hugging Face](https://huggingface.co/datasets/openbmb/UltraData-Math)

UltraData-Math는 수학적 추론 능력 향상을 위한 대규모 고품질 수학 사전학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, tags, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `mathematical pre-training dataset` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `mathematical pre-training dataset totaling 290B+ tokens` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `multi-format refined data (Q&A, multi-turn dialogues, knowledge textbooks, etc.)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `22440` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `mathematical pre-training dataset` · 신뢰도 low
- **도메인**: [[교육]] — ner · readme = `mathematical discussions and application scenarios in real web pages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `mathematical pre-training dataset` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `content` 열 p90 89762자 ≈ 22440 토큰 (viewer statistics, UltraData-Math-L1/train)

## 이 데이터로 학습한 모델

- [[FoolDev__Janus-35B-HERETIC|FoolDev/Janus-35B-HERETIC]]
- [[FoolDev__Thanatos-27B-HERETIC|FoolDev/Thanatos-27B-HERETIC]]
