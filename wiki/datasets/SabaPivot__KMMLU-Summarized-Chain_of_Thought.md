---
type: "dataset"
id: "SabaPivot/KMMLU-Summarized-Chain_of_Thought"
source: "huggingface"
url: "https://huggingface.co/datasets/SabaPivot/KMMLU-Summarized-Chain_of_Thought"
downloads: 867
summary: "KMMLU 원본 데이터를 요약하고 추론 체인 추가한 한국어 다중선택 문제 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[교육]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# SabaPivot/KMMLU-Summarized-Chain_of_Thought

> dataset · [Hugging Face](https://huggingface.co/datasets/SabaPivot/KMMLU-Summarized-Chain_of_Thought)

KMMLU 원본 데이터를 요약하고 추론 체인 추가한 한국어 다중선택 문제 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `achieving higher KMMLU benchmark test scores for some models` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `multiple-choice options` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:embedding, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `171` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `KMMLU: Measuring Massive Multitask Language Understanding in Korean` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `The "test" dataset remains unchanged.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The "train" and "dev" splits have been modified.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 256자 ≈ 171 토큰 (viewer statistics, Korean-History/test)
