---
type: "dataset"
id: "neulab/agent-data-collection"
source: "huggingface"
url: "https://huggingface.co/datasets/neulab/agent-data-collection"
downloads: 32347
summary: "다양한 환경에서 AI 에이전트 학습과 평가를 위한 에이전트 상호작용 데이터셋 모음입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# neulab/agent-data-collection

> dataset · [Hugging Face](https://huggingface.co/datasets/neulab/agent-data-collection)

다양한 환경에서 AI 에이전트 학습과 평가를 위한 에이전트 상호작용 데이터셋 모음입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `training and evaluating AI agents across diverse domains and tasks` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[도구 호출]] — tag_match · tags = `tool-use` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation = `agent trajectories from various environments including web browsing, code generation, household tasks, knowledge base querying, and software engineering` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `agent trajectories from various environments including web browsing, code generation, household tasks, knowledge base querying, and software engineering` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `AI agents across diverse domains and tasks` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `for training and evaluating AI agents` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `for training and evaluating AI agents` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[mradermacher__next-70b-GGUF|mradermacher/next-70b-GGUF]]
- [[mradermacher__next-70b-i1-GGUF|mradermacher/next-70b-i1-GGUF]]
- [[thelamapi__next-70b-GGUF|thelamapi/next-70b-GGUF]]
- [[thelamapi__next-70b-i1-GGUF|thelamapi/next-70b-i1-GGUF]]
