---
license: cc-by-4.0
task_categories:
  - text-generation
language:
  - ko
  - en
tags:
  - function-calling
  - tool-use
  - agent
  - reasoning
  - korean
  - synthetic
size_categories:
  - 100K<n<1M
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/*.jsonl"
---

# agentic-think-v2-react-hybrid-ko

**Korean localization** of [`HBKenerzai/agentic-think-v2-react-hybrid`](https://huggingface.co/datasets/HBKenerzai/agentic-think-v2-react-hybrid):
agentic tool-calling conversations where every natural-language surface — user messages, assistant
reasoning, assistant replies, and user-derived argument strings — is rendered in Korean, while the API
layer (function catalogs, parameter names, enum values, identifiers, tool observations) stays in
English, matching real deployments.

**181,894 rows** after a Korean-purity pass (2026-10-04) that removed rows containing Chinese characters,
translator/instruction leakage, single-turn register mixing, and emoji inside tool-call arguments. The
assistant text keeps its original **Markdown and emoji** (an earlier spoken/TTS-flattened variant has been
reverted at the maintainer's request). Same schema as the English corpus; the distractor-augmented tool
catalogs (9–16 entries per episode) are inherited unchanged.

## What is / isn't translated

| Korean | kept as-is (English) |
|---|---|
| user messages | tool catalogs (`tools`) |
| assistant `reasoning_content` | parameter names, enum values, ids, codes |
| assistant replies | tool observations (`role: tool`) |
| user-composed argument strings (message bodies, notes) | schema-constrained argument values |

**Argument language** follows how a Korean speaker actually talks: titles, brands and technical terms
stay English inside the Korean sentence ("Bohemian Rhapsody 가사 찾아줘"), user-composed free text
becomes Korean. Within a row, every occurrence of the same original value uses one consistent form.

## Korean purity (2026-10-04)

A deterministic pass (no LLM in the pass/fail decision) removed three defects a Korean training corpus
should not carry. Originals are preserved; only the cleaned rows ship here.

| defect | what / why | action |
|---|---|---|
| **Chinese characters** | the translator (Qwen3-30B-A3B) occasionally emitted Chinese (`听起来`, `归属되나요`) | drop the row |
| **instruction leak** | translator meta-text left in the utterance (`한국어로 번역된 사용자 메시지: …`) | drop the row |
| **register mixing** | 존댓말 and 반말 mixed in one speaker turn, judged by a Korean morphological analyzer (kiwi) | drop the row |
| **emoji in tool arguments** | emoji inside a function-call argument breaks consistency with the tool result | drop the row |

Net: 193,149 → 181,894. **Emoji and Markdown inside the natural-language text are kept** — a previous
variant that stripped emoji and flattened Markdown (for a text-to-speech use case) has been reverted;
use that variant's pipeline step (`tts_plain.py`) if you need spoken-plain output.

## Composition and upstream sources

| file | rows | upstream dataset | upstream license |
|---|---:|---|---|
| `glaive.jsonl` | 42,661 | [glaiveai/glaive-function-calling-v2](https://huggingface.co/datasets/glaiveai/glaive-function-calling-v2) | Apache-2.0 |
| `xlam.jsonl` | 37,946 | [Salesforce/xlam-function-calling-60k](https://huggingface.co/datasets/Salesforce/xlam-function-calling-60k) | CC-BY-4.0 |
| `nemotron_tc.jsonl` | 33,063 | [nvidia/Nemotron-SFT-Agentic-v2](https://huggingface.co/datasets/nvidia/Nemotron-SFT-Agentic-v2) (tool_calling) | CC-BY-4.0 |
| `synth_apigen.jsonl` | 28,512 | [argilla/Synth-APIGen-v0.1](https://huggingface.co/datasets/argilla/Synth-APIGen-v0.1) | CC-BY-4.0 |
| `nemotron_ia.jsonl` | 19,416 | [nvidia/Nemotron-SFT-Agentic-v2](https://huggingface.co/datasets/nvidia/Nemotron-SFT-Agentic-v2) (interactive_agent) | CC-BY-4.0 |
| `toolace.jsonl` | 8,559 | [Team-ACE/ToolACE](https://huggingface.co/datasets/Team-ACE/ToolACE) | Apache-2.0 |
| `robot.jsonl` | 5,667 | none — generated in-house with a deterministic robot-environment simulator | CC-BY-4.0 |
| `apigen_mt.jsonl` | 4,588 | [Salesforce/APIGen-MT-5k](https://huggingface.co/datasets/Salesforce/APIGen-MT-5k) | CC-BY-4.0 |
| `hermes.jsonl` | 1,482 | [NousResearch/hermes-function-calling-v1](https://huggingface.co/datasets/NousResearch/hermes-function-calling-v1) | Apache-2.0 |
| **total** | **181,894** | | |

## Schema

| field | type | description |
|---|---|---|
| `id` | str | same id as the English corpus — rows are joinable across the two |
| `source` | str | one of the 9 sources above |
| `tools` | str (JSON) | OpenAI-style function catalog, distractor-augmented, English |
| `messages` | str (JSON) | chat messages; assistant messages carry `reasoning_content` (Korean) alongside `content` and `tool_calls` |
| `think_source` | str | `v24_react` or `v23_annotate` — preserved from the English corpus |

```python
from datasets import load_dataset
ds = load_dataset("HBKenerzai/agentic-think-v2-react-hybrid-ko", split="train")
```

## Method

- Translator: Qwen3-30B-A3B-Instruct-2507-FP8, temperature 0, one call per **turn group**
  (user message + that turn's assistant rounds, round count enforced).
- Five hard gates per turn (fail = drop the whole row); schema-enum / code-token argument values are
  protected from translation; a per-row post-pass unifies argument spellings across turns.
- Korean-purity pass applied afterward (see above).
- Quality audit (pre-purity): 360 rows stratified 40-per-source, judged side-by-side against the
  English original by a **different** model (Qwen3.8-27B) on five axes: **94.2% score ≥4 on all five**.

## Known limitations

- The translation gate had already dropped ~9% of the English corpus before the purity pass
  (concentrated in the longest multi-turn rows).
- Person names inside arguments may appear in Hangul when the Korean utterance says them that way
  (노아 ↔ Noah). Remap if your target API expects Latin-only fields.
- Register-mixing removal is morphology-rule-based (≈96% precision on a 180-row check); a few clean
  rows may have been dropped and a few mixes may remain.
- Reasoning is machine-translated from teacher-generated English reasoning; not human-verified.

## Access

This dataset is gated: access is granted on request after manual review.

## Provenance

Direct base: [`HBKenerzai/agentic-think-v2-react-hybrid`](https://huggingface.co/datasets/HBKenerzai/agentic-think-v2-react-hybrid)
(ENERZAi). Localization and purity pipeline: agentic-datagen `data_gen/ko/`, `data_gen/purify_ko.py`,
`data_gen/mix_rule.py` (ENERZAi).

## 2026-10-29 품질 개선 (영어 원본 기준 규칙 복구 + 일부 메시지 재번역, 181,894 → 178,246행)
원본 ENERZAiKR/agentic-think-v2-react-hybrid 와 id·메시지 순서가 전부 일치하여 원본을 기준으로 고침 (`fix_think_v2*.py`):
- tool 메시지 원본 복원 2,197 · 식별자/조회 키 인자 원본 복원 32,564 · 언어 혼합 배열 복원 443 · 본문 속 ID 문자열 원복 1,032
- reasoning 이 따옴표로 인용한 인자 값을 실제 인자와 일치시킴
- 원문의 이메일·URL·식별자·숫자 손상, 영어 기능어 혼입, 영어 그대로 남은 답변 → 해당 메시지만 재번역 (약 1.2만 필드)
- 제외: 한자 2,980 · 재번역 실패 453 · 생성 단계 API 오류가 답변으로 들어간 행 242
- 알려진 잔여 문제: 원문 토큰이 보존된 의미 오역(일부 음차·고유명사 오역, 영어 일반어 미번역)은 규칙으로 검출되지 않아 남아 있음.
