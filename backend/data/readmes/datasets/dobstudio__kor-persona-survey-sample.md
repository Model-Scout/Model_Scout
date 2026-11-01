---
# 데이터셋 repo(dobstudio/kor-persona-survey-sample)의 README.md 초안
license: cc-by-4.0
language:
  - ko
task_categories:
  - text-generation
tags:
  - korean
  - persona
  - survey
  - synthetic
  - distillation
size_categories:
  - n<1K
---

# kor-persona-survey-sample

A **deliberately reduced demonstration sample** (800 triplets) of the synthetic training
data behind [dobstudio/kor-persona-survey-7b](https://huggingface.co/dobstudio/kor-persona-survey-7b):
Korean persona profiles answering survey / balance-game questions **in character**, labeled
by a Qwen2.5-72B-Instruct teacher.

**Shape: 16 questions × 50 distinct personas each.** The sample is intentionally
question-narrow and persona-wide so that its most visible property is the model's core
claim — *the same question, answered differently by different personas*.

## Fields

| field | description |
|---|---|
| `persona_uuid` | ID in nvidia/Nemotron-Personas-Korea |
| `persona_profile` | The exact profile text injected into the prompt (demographics + narrative) |
| `question` | Survey question (Korean, binary choice) |
| `options` | The two answer options |
| `category` | One of 8 non-sensitive topics (food, lifestyle, consumption, travel, leisure, work, values, digital) |
| `response` | Teacher label: `{choice, confidence, reason}` |

## How it was made

(persona sampled from Nemotron-Personas-Korea) + (question from a curated private question
bank) → Qwen2.5-72B-Instruct-AWQ generates the in-character response → quality filtering
(format validity, option match, confidence range, reason de-duplication; 95.2% pass rate).

**Not released**: the full 28k-triplet training set, the 515-question bank, evaluation
(held-out) questions and their labels, and the population-aggregation pipeline.
Politically/socially sensitive topics were excluded by design.

## 한국어 요약

[dobstudio/kor-persona-survey-7b](https://huggingface.co/dobstudio/kor-persona-survey-7b)
학습 데이터의 **의도적으로 축소된 시연용 샘플**(800건)입니다. 한국인 가상 인물 프로필이
설문/밸런스게임 문항에 인물의 입장에서 답한 (페르소나, 문항, 응답) 데이터로, 응답은
Qwen2.5-72B 교사 모델이 생성했습니다.

- **구성: 문항 16개 × 문항당 서로 다른 인물 50명** — "같은 질문에 인물마다 다른 답"
  이라는 모델의 핵심 성질이 그대로 보이도록 문항은 좁게, 인물은 넓게 설계했습니다.
- 비공개: 전체 학습 데이터(2.8만 건), 문항 뱅크 515개, 평가(held-out) 문항과 라벨,
  모집단 집계 파이프라인. 정치 등 민감 주제는 애초에 배제했습니다.
- 인물은 합성이며, 응답은 실제 사람의 의견이 아니라 LLM의 판단입니다.

## Attribution & license

- This dataset: **CC BY 4.0**.
- Persona profiles derive from [nvidia/Nemotron-Personas-Korea](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea) (CC BY 4.0, © NVIDIA).
- Responses were generated with Qwen2.5-72B-Instruct-AWQ (Qwen LICENSE, Alibaba Cloud) — **Built with Qwen.**
- Personas are **synthetic**; responses reflect LLM judgments, not real people's opinions.
