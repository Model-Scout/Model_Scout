---
type: "dataset"
id: "WueNLP/mHallucination_Evaluation"
source: "huggingface"
url: "https://huggingface.co/datasets/WueNLP/mHallucination_Evaluation"
downloads: 141
summary: "30개 언어 위키피디아 기반 LLM 환각 평가용 합성 쿼리-참조 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# WueNLP/mHallucination_Evaluation

> dataset · [Hugging Face](https://huggingface.co/datasets/WueNLP/mHallucination_Evaluation)

30개 언어 위키피디아 기반 LLM 환각 평가용 합성 쿼리-참조 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `multilingual hallucination detection dataset` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `estimating hallucinations` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = `synthetic query/prompt and wikipedia reference pair` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `estimating hallucinations` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `26 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `936` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `cc` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `wikipedia reference pair for estimating hallucinations` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset is a high quality synthetic query/prompt and wikipedia reference pair for estimating hallucinations` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `reference_1` 열 p90 3745자 ≈ 936 토큰 (viewer statistics, default/test)
