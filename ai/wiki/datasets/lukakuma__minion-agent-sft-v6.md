---
type: "dataset"
id: "lukakuma/minion-agent-sft-v6"
source: "huggingface"
url: "https://huggingface.co/datasets/lukakuma/minion-agent-sft-v6"
downloads: 43
summary: "한국어 웹 에이전트용 소형 모델 추가학습 데이터로 도구 호출 및 수학 문제 포함"
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
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lukakuma/minion-agent-sft-v6

> dataset · [Hugging Face](https://huggingface.co/datasets/lukakuma/minion-agent-sft-v6)

한국어 웹 에이전트용 소형 모델 추가학습 데이터로 도구 호출 및 수학 문제 포함

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[도구 호출]] — tag_match · tags = `function-calling` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = ``messages` | list of `{role, content}` | system / user / assistant 대화.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `마지막 assistant 의 `content` 가 학습 정답` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 웹 에이전트용 소형 모델(Minion GRPO)을 SFT/LoRA 로 추가학습하기 위한 데이터 v6 입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train
10,259` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
