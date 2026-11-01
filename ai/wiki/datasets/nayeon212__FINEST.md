---
type: "dataset"
id: "nayeon212/FINEST"
source: "huggingface"
url: "https://huggingface.co/datasets/nayeon212/FINEST"
downloads: 29
summary: "FINEST는 민감한 주제에 대한 LLM 응답을 미세 평가하기 위한 한국어 중심 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nayeon212/FINEST

> dataset · [Hugging Face](https://huggingface.co/datasets/nayeon212/FINEST)

FINEST는 민감한 주제에 대한 LLM 응답을 미세 평가하기 위한 한국어 중심 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `fine-grained evaluation of LLM responses to sensitive topics` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `model-generated responses used as inputs to our evaluation framework` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = `The raw_responses configuration contains the full set of questions and model-generated responses` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `model-generated response` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `723` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `We release the FINEST dataset in two complementary configurations to support both reproducibility and further research` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `full_scores` 열 p90 1084자 ≈ 723 토큰 (viewer statistics, evaluation/evaluation)
