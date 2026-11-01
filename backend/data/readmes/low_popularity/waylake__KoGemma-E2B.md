---
language:
- ko
license: gemma
library_name: transformers
pipeline_tag: text-generation
base_model: google/gemma-4-E2B-it
base_model_relation: finetune
tags:
- korean
- on-device
- tool-calling
- agentic
- lora
- self-distillation
- mix-distillation
- gemma
datasets:
- waylake/ko-agentic-sft
- waylake/ko-verified-cot
model-index:
- name: KoGemma-E2B
  results:
  - task:
      type: text-generation
      name: Korean Multiple Choice QA
    dataset:
      name: KMMLU
      type: HAERAE-HUB/KMMLU
    metrics:
    - name: acc (5-shot, lm-eval-harness)
      type: acc
      value: 0.3089
  - task:
      type: text-generation
      name: Korean Knowledge
    dataset:
      name: HAE-RAE Bench 1.1
      type: HAERAE-HUB/HAE_RAE_BENCH_1.1
    metrics:
    - name: acc (5-shot, lm-eval-harness)
      type: acc
      value: 0.4350
  - task:
      type: text-generation
      name: Tool Calling (held-out, rule-scored)
    dataset:
      name: kogemma-agentic-holdout
      type: custom
    metrics:
    - name: web_search action accuracy
      type: accuracy
      value: 1.0
    - name: calculator action accuracy
      type: accuracy
      value: 0.75
    - name: fetch_page action accuracy
      type: accuracy
      value: 1.0
---

<div align="center">

<img src="https://huggingface.co/waylake/KoGemma-E2B/resolve/main/banner.png" alt="KoGemma-E2B" width="100%"/>

# KoGemma-E2B

**Korean on-device SLM that actually calls tools — built on `gemma-4-E2B-it`, trained on
100% self-generated data (zero public datasets).**

[![GitHub](https://img.shields.io/badge/GitHub-kogemma--e2b-181717?logo=github)](https://github.com/waylake/kogemma-e2b)
[![GGUF](https://img.shields.io/badge/GGUF-Q4__K__M%203.4GB-F2A93B)](https://huggingface.co/waylake/KoGemma-E2B-GGUF)
[![Adapter](https://img.shields.io/badge/LoRA-47MB%20adapter-5EE0C0)](https://huggingface.co/waylake/KoGemma-E2B-tools-v6)
[![Base](https://img.shields.io/badge/base-gemma--4--E2B--it-4285F4)](https://huggingface.co/google/gemma-4-E2B-it)

</div>

## What you get

| | |
|---|---|
| **Model** | 2.3B effective params (5.1B total), merged LoRA — this repo is the **v6** checkpoint |
| **New capability** | reliable single-line tool-action JSON: `web_search` **1.00**, `fetch_page` **1.00**, `calculator` **0.75** (base: 0.53 / 0.00 / 0.00) |
| **Knowledge** | unchanged vs base — KMMLU 0.3089 (base 0.3000), HAE-RAE 0.4350 (base 0.4600) |
| **Format** | CoT format failures **halved**: 8.0% → 4.5% (600 questions) |
| **Data** | 6,895 records / 25,957 turns · **0 public datasets** · generation cost **$0** |
| **Training** | LoRA r=16 · 1 epoch · lr 5e-5 · 44 min on one RTX 3090 |

## ⚠️ Read this before using

This checkpoint was trained so that **a tool-bearing system prompt means "tools are in play"**.
Consequence, measured on held-out cases:

| System prompt | Behaviour |
|---|---|
| **Plain** (`너는 한국어로 정확하게 답하는 AI 비서다.`) | normal chat — no tool calls, clean Korean answers |
| **With tool list** | calls a tool almost always, including when unnecessary (tool restraint 0/14) |

**So: only put the tool list in the system prompt when you want tool calls.** For plain chat use a
plain system prompt. Root cause and the fix are documented in
[the GitHub repo](https://github.com/waylake/kogemma-e2b) and the corrected dataset
([`ko-agentic-sft`](https://huggingface.co/datasets/waylake/ko-agentic-sft) ships 1,583 action
vs 786 no-action trajectories for retraining).

## Usage

### Chat (no tools)

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

mid = "waylake/KoGemma-E2B"
tok = AutoTokenizer.from_pretrained(mid)
model = AutoModelForCausalLM.from_pretrained(mid, dtype=torch.bfloat16, device_map="auto")

msgs = [{"role": "system", "content": "너는 한국어로 정확하게 답하는 AI 비서다."},
        {"role": "user", "content": "전세와 월세 차이를 세 문장으로 알려줘"}]
text = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True,
                               enable_thinking=False)
ids = tok(text, return_tensors="pt", add_special_tokens=False).to(model.device)
out = model.generate(**ids, max_new_tokens=320, do_sample=False, repetition_penalty=1.15)
print(tok.decode(out[0][ids["input_ids"].shape[1]:], skip_special_tokens=True))
```

### Tool calling

```python
SYS = ('너는 한국어로 정확하게 답하고, 필요하면 도구를 쓰는 AI 비서다. '
       '도구가 필요하면 한 줄 JSON으로만 답한다: '
       '{"action": "web_search", "args": {"query": "..."}} '
       '사용 가능 도구: web_search{query}, fetch_page{url}, calculator{expr}, now{}')

msgs = [{"role": "system", "content": SYS},
        {"role": "user", "content": "지금 원달러 환율 얼마야?"}]
# -> {"action": "web_search", "args": {"query": "원달러 환율"}}

# feed the observation back as a user turn:
msgs += [{"role": "assistant", "content": '{"action": "web_search", "args": {"query": "원달러 환율"}}'},
         {"role": "user", "content": '[도구 결과] {"results": [{"title": "환율", "url": "https://example.kr/fx", "text": "1,387.4원"}]}'}]
# -> 현재 원/달러 환율은 1,387.4원입니다. (출처: https://example.kr/fx)
```

### On a laptop (GGUF)

See [waylake/KoGemma-E2B-GGUF](https://huggingface.co/waylake/KoGemma-E2B-GGUF) — 3.4 GB Q4_K_M.

## Recommended settings

| Setting | Value | Why (measured) |
|---|---|---|
| `enable_thinking` | **false** | with thinking on, the model writes an **English** reasoning block that eats the whole token budget; no accuracy gain at 2.3B. It does not break — you would just need `max_new_tokens ≳ 1000` |
| temperature | **0 – 0.3** | at ≥0.7 output drifts off-manifold (word salad) |
| `repetition_penalty` | **1.15** | greedy decoding loops without it |

## Evaluation

Identical protocol for base and this model. `lm-evaluation-harness` 5-shot (`--limit 40`);
CoT accuracy = generate + extract on 600 held-out KMMLU test questions; agentic = 52 hand-written
held-out cases scored by rule (no LLM judge).

| Metric | `gemma-4-E2B-it` | **KoGemma-E2B (v6)** |
|---|---|---|
| KMMLU 5-shot | 0.3000 | **0.3089** |
| HAE-RAE 5-shot | 0.4600 | 0.4350 |
| CoT accuracy (600 q) | 0.3200 | **0.3250** |
| CoT format failures | 48 (8.0%) | **27 (4.5%)** |
| `web_search` action | 0.533 | **1.000** |
| `calculator` action | 0.000 | **0.750** |
| `fetch_page` action | 0.000 | **1.000** |
| Tool restraint | **1.000** | 0.000 |
| Private-info refusal | **1.000** | 0.333 |
| Agentic overall | 0.596 | **0.615** |

**Honest summary: knowledge is unchanged, format and tool use improved, tool restraint regressed.**
Benchmark parity is expected — see the method below for why.

## Method (why knowledge does not move)

1. **Self-distillation (SDFT) prevents forgetting but caps quality at the base.** Answers for plain
   chat are generated by the base model itself, so the output distribution never shifts
   (eval loss 1.57 → 0.44 vs a teacher-answer baseline that degraded the model).
2. **Verified teacher CoT + the model's own CoT, mixed 1:1** (Mix Distillation,
   [arXiv 2502.12143](https://arxiv.org/abs/2502.12143)). Teacher traces are capped at 3–4
   sentences because models ≤3B get *worse* from long chains. Teacher accuracy on those questions
   was 80–85%; the base scored 32% on the test split. Even so, student accuracy did not move —
   the bottleneck at 2.3B is capacity, not data.
3. **Tool calling is structure, not knowledge**, so distillation works immediately there
   (0% → 75–100%).

## Training data

| Component | Records | Source |
|---|---|---|
| Verified teacher CoT (KMMLU train, gold-checked) | 1,612 | `ox-alpha-free` |
| Base self-CoT (verified) | 1,074 | base model |
| Self-distilled chat replay | 3,501 | base model |
| Tool trajectories | 708 | `ox-alpha-free` |
| **Public datasets** | **0** | — |

Released as [`ko-agentic-sft`](https://huggingface.co/datasets/waylake/ko-agentic-sft) and
[`ko-verified-cot`](https://huggingface.co/datasets/waylake/ko-verified-cot).

## Limitations

- 2.3B ceiling — not a substitute for 30B-class Korean models.
- **Tool over-triggering** with a tool-bearing system prompt (see warning above).
- Private-info refusal regressed (0.333); do not rely on it as a safety layer.
- Tool schema is the action-JSON format documented here, not OpenAI function calling.
- Medical / legal / financial answers are general information only.

## Reproduce

Full pipeline — restart-safe generation queue, teacher distillation with gold verification, mixing,
training, and all evaluators — is at
[github.com/waylake/kogemma-e2b](https://github.com/waylake/kogemma-e2b), including the failed
rounds and the measurement traps that produced fake gains.

## License

Weights follow the [Gemma Terms of Use](https://ai.google.dev/gemma/docs/gemma_4_license); code MIT.
Credits: Google DeepMind (gemma-4), HAERAE-HUB (KMMLU · HAE-RAE), `lm-evaluation-harness`.
Synthetic-data teacher: `ox-alpha-free`.
