---
type: "dataset"
id: "saltlux/EthicsAI-B11-AugMT"
source: "huggingface"
url: "https://huggingface.co/datasets/saltlux/EthicsAI-B11-AugMT"
downloads: 40
summary: "EthicsAI-B11-AugMT는 LLM의 대화 맥락 내 사회적 편견 식별 및 윤리적 추론 평가용 멀티턴 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# saltlux/EthicsAI-B11-AugMT

> dataset · [Hugging Face](https://huggingface.co/datasets/saltlux/EthicsAI-B11-AugMT)

EthicsAI-B11-AugMT는 LLM의 대화 맥락 내 사회적 편견 식별 및 윤리적 추론 평가용 멀티턴 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `본 데이터셋은 단순히 편견의 유무를 판단하는 것을 넘어` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation = `두 명 이상의 화자가 참여하는 멀티턴 대화 내용` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `11가지 주요 민감 주제를 폭넓게 다룹니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `약 31,000개의 멀티턴(Multi-turn) 대화 시나리오로 확장했습니다.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
