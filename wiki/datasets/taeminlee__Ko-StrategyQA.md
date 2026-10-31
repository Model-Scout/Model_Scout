---
type: "dataset"
id: "taeminlee/Ko-StrategyQA"
source: "huggingface"
url: "https://huggingface.co/datasets/taeminlee/Ko-StrategyQA"
downloads: 1490
summary: "Ko-StrategyQA 데이터셋을 다중 홉 질의응답용으로 가공해 BeIR 포맷으로 변환한 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
  - "[[문서 검색]]"
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# taeminlee/Ko-StrategyQA

> dataset · [Hugging Face](https://huggingface.co/datasets/taeminlee/Ko-StrategyQA)

Ko-StrategyQA 데이터셋을 다중 홉 질의응답용으로 가공해 BeIR 포맷으로 변환한 데이터입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `The original dataset was designed for multi-hop QA` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · tags, task_categories, task_ids = `text-retrieval` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:retrieval = `grouped the evidence documents tagged by annotators into sets` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `multi-hop QA` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `15` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset represents a conversion of the Ko-StrategyQA dataset into the BeIR format` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `query-id` 열 p90 22자 ≈ 15 토큰 (viewer statistics, default/train)
