---
type: "dataset"
id: "lukakuma/web-trajectories-sft"
source: "huggingface"
url: "https://huggingface.co/datasets/lukakuma/web-trajectories-sft"
downloads: 56
summary: "DOM 기반 웹 에이전트의 성공 세션으로부터 생성된 지도학습용 LLM 호출 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lukakuma/web-trajectories-sft

> dataset · [Hugging Face](https://huggingface.co/datasets/lukakuma/web-trajectories-sft)

DOM 기반 웹 에이전트의 성공 세션으로부터 생성된 지도학습용 LLM 호출 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[도구 호출]] — tag_match · tags = `tool-calling` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `One row = one LLM call: the exact input (messages, with the full tools definitions restored from the agent's source code — see the raw repo's Tool definitions)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `and the exact output (response)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `DOM-based, tool-calling web agent` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Supervised fine-tuning selections built from lukakuma/web-trajectories (judged-successful, completed sessions of a DOM-based, tool-calling web agent)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
