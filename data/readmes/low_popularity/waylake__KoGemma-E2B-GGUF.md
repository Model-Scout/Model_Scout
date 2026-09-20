---
language:
- ko
license: gemma
library_name: gguf
pipeline_tag: text-generation
base_model: waylake/KoGemma-E2B
base_model_relation: quantized
tags:
- korean
- gguf
- llama.cpp
- ollama
- on-device
- tool-calling
- quantized
---

<div align="center">

# KoGemma-E2B-GGUF

**Laptop-runnable GGUF build of [KoGemma-E2B](https://huggingface.co/waylake/KoGemma-E2B) (v6) —
3.1 GB, Korean chat + tool-action JSON.**

[![GitHub](https://img.shields.io/badge/GitHub-kogemma--e2b-181717?logo=github)](https://github.com/waylake/kogemma-e2b)
[![Full weights](https://img.shields.io/badge/safetensors-KoGemma--E2B-4285F4)](https://huggingface.co/waylake/KoGemma-E2B)

</div>

## Files

| File | Size | Notes |
|---|---|---|
| `KoGemma-E2B-v6-Q4_K_M.gguf` | **3.4 GB** | recommended — runs on an 8 GB laptop |
| `KoGemma-E2B-v6-f16.gguf` | 9.3 GB | full precision, for re-quantizing |

Converted from the **v6** merged checkpoint (Mix Distillation + tool trajectories).

## Quick start

```bash
hf download waylake/KoGemma-E2B-GGUF KoGemma-E2B-v6-Q4_K_M.gguf --local-dir .

# chat (no tools)
llama-cli -m KoGemma-E2B-v6-Q4_K_M.gguf --jinja \
  --chat-template-kwargs '{"enable_thinking":false}' \
  -sys "너는 한국어로 정확하게 답하는 AI 비서다." \
  -p "한국 가을 음식 하나 소개해줘" \
  -n 300 --temp 0 --repeat-penalty 1.15
```

### Tool calling

Put the tool list in the **system** prompt; the model answers with a single-line JSON action.

```bash
llama-cli -m KoGemma-E2B-v6-Q4_K_M.gguf --jinja \
  --chat-template-kwargs '{"enable_thinking":false}' \
  -sys '너는 한국어로 정확하게 답하고, 필요하면 도구를 쓰는 AI 비서다. 도구가 필요하면 한 줄 JSON으로만 답한다: {"action": "web_search", "args": {"query": "..."}} 사용 가능 도구: web_search{query}, fetch_page{url}, calculator{expr}, now{}' \
  -p "지금 원달러 환율 얼마야?" -n 80 --temp 0
# -> {"action": "web_search", "args": {"query": "원달러 환율"}}
```

Feed the result back as a user turn prefixed with `[도구 결과]` + JSON, then generate again.

### LM Studio

```bash
# 모델 폴더에 바로 내려받기 (publisher/model/file 구조를 지켜야 인식됨)
hf download waylake/KoGemma-E2B-GGUF KoGemma-E2B-v6-Q4_K_M.gguf \
  --local-dir ~/.lmstudio/models/waylake/KoGemma-E2B-GGUF
```

Then load it in the GUI, or headless:

```bash
lms load kogemma-e2b --gpu max --context-length 4096
lms server start          # OpenAI-compatible on :1234
```

GGUF metadata carries `general.name = KoGemma-E2B`, so the GUI shows the proper name.
For plain chat keep the tool list out of the system prompt.

### Ollama

```
FROM ./KoGemma-E2B-v6-Q4_K_M.gguf
PARAMETER temperature 0
PARAMETER repeat_penalty 1.15
```

## ⚠️ Two settings that matter

| Setting | Value | Why (measured) |
|---|---|---|
| `--chat-template-kwargs '{"enable_thinking":false}'` | **required** | training used the non-thinking format. On the **llama.cpp path** leaving thinking on produced Russian-mixed gibberish inside the thinking block (the GGUF's baked template differs from the training format). On transformers the same setting merely wastes the token budget on an English reasoning block |
| `--repeat-penalty 1.15` | **required** | greedy decoding degenerates into repetition without it |
| `--temp` | 0 – 0.3 | ≥0.7 drifts into word salad |

**Tool prompts trigger tools aggressively.** Keep the tool list out of the system prompt when you
want plain chat — with a plain system prompt the model does not emit actions.

## Evaluation (same protocol as the parent repo)

| Metric | base `gemma-4-E2B-it` | **this build (v6)** |
|---|---|---|
| KMMLU 5-shot | 0.3000 | **0.3089** |
| HAE-RAE 5-shot | 0.4600 | 0.4350 |
| CoT format failures (600 q) | 8.0% | **4.5%** |
| `web_search` / `calculator` / `fetch_page` action accuracy | 0.53 / 0.00 / 0.00 | **1.00 / 0.75 / 1.00** |
| Tool restraint (no call when unnecessary) | **1.00** | 0.00 |

Knowledge is at parity with the base model; the gain is tool calling and format compliance, the
loss is tool restraint. Full analysis, including the data-composition bug that caused it:
[GitHub](https://github.com/waylake/kogemma-e2b).

## License

[Gemma Terms of Use](https://ai.google.dev/gemma/docs/gemma_4_license) · code MIT.
