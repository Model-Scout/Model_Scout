---
type: "dataset"
id: "superisaac1262/frontier-agentic-corpus-v10.3"
source: "huggingface"
url: "https://huggingface.co/datasets/superisaac1262/frontier-agentic-corpus-v10.3"
downloads: 317
summary: "최첨단 교사 모델로부터 생성된 다단계 에이전트 추론 및 코딩, 수학, 과학 데이터 분석 말뭉치입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
  - "[[도구 호출]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[학술·논문]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# superisaac1262/frontier-agentic-corpus-v10.3

> dataset · [Hugging Face](https://huggingface.co/datasets/superisaac1262/frontier-agentic-corpus-v10.3)

최첨단 교사 모델로부터 생성된 다단계 에이전트 추론 및 코딩, 수학, 과학 데이터 분석 말뭉치입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `coding, mathematical, scientific, and data-analysis reasoning` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `knowledge-distillation corpus of genuine multi-step agentic trajectories` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · task_categories = `text-retrieval` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · tags = `tool-use` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation, task:retrieval = `A multi-teacher knowledge-distillation corpus of genuine multi-step agentic trajectories, coding, mathematical, scientific, and data-analysis reasoning` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `training language models that behave agentically` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `34223` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `mathematical, scientific, and data-analysis reasoning` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `general-reasoning 1.31%` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `teacher-distilled/generated data for training language models` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 136892자 ≈ 34223 토큰 (viewer statistics, default/train)
