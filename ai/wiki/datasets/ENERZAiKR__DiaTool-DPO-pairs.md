---
type: "dataset"
id: "ENERZAiKR/DiaTool-DPO-pairs"
source: "huggingface"
url: "https://huggingface.co/datasets/ENERZAiKR/DiaTool-DPO-pairs"
downloads: 14
summary: "DiaTool-DPO 방법론으로 구축한 멀티턴 tool-use 궤적 선호쌍 데이터셋으로, TA-LLM 대화흐름 제어 학습용입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ENERZAiKR/DiaTool-DPO-pairs

> dataset · [Hugging Face](https://huggingface.co/datasets/ENERZAiKR/DiaTool-DPO-pairs)

DiaTool-DPO 방법론으로 구축한 멀티턴 tool-use 궤적 선호쌍 데이터셋으로, TA-LLM 대화흐름 제어 학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · readme, tags = `tool-use` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `메시지는 OpenAI/Qwen3 chat 포맷(assistant `tool_calls`의 `arguments`는 JSON 문자열` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `메시지는 OpenAI/Qwen3 chat 포맷(assistant `tool_calls`의 `arguments`는 JSON 문자열` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = ``data_en/diatool_dpo_all.clean.jsonl`로 ternary QAT 1.7B(agentic SFT 후)에 반복 DPO` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
