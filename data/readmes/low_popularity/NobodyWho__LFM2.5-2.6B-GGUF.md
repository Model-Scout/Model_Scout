---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: LiquidAI/LFM2.5-2.6B
library_name: gguf
pipeline_tag: text-generation
language:
  - ar
  - zh
  - en
  - fr
  - de
  - hi
  - id
  - it
  - ja
  - ko
  - pl
  - pt
  - ru
  - es
  - th
  - vi
tags:
  - gguf
  - nobodywho
  - liquid
  - lfm2.5
  - reasoning
  - tool-calling
---

# NobodyWho/LFM2.5-2.6B-GGUF

## Overview

GGUF build of LiquidAI's **LFM2.5-2.6B**, prepared for
[NobodyWho](https://github.com/nobodywho-ooo/nobodywho). The upstream GGUF cannot render a
single prompt in any llama.cpp-family runtime because of an invalid chat template; this repo
ships the same file with that template repaired. The **weight tensors are bit-identical** to
upstream — only three metadata keys differ.

LFM2.5 is a hybrid architecture built for on-device deployment, extending LFM2 with additional
pre-training and reinforcement learning. This checkpoint is a **reasoning model**: it emits a
`<think>` block before its answer.

## Model Capabilities

- **Text generation** — instruction-following chat
- **Reasoning** — the template always opens a `<think>` block on the generation prompt
- **Tool calling** — native LFM2 function-calling format
- **Long context** — 128k tokens
- **Multilingual** — 16 languages

## Getting Started

Install [NobodyWho](https://docs.nobodywho.ooo/):

```bash
pip install nobodywho
```

Run — the model is downloaded and cached automatically on first use:

```python
from nobodywho import Chat

chat = Chat("huggingface:NobodyWho/LFM2.5-2.6B-GGUF/LFM2.5-2.6B-Q4_K_M.gguf")
print(chat.ask("What is the capital of Denmark?").completed())
```

Because this is a reasoning model, the completion contains the model's `<think>` trace
followed by `</think>` and then the answer.

### Tool calling

```python
from nobodywho import Chat, tool

@tool(description="Gets the current weather for a city")
def get_weather(city: str) -> str:
    return f"It is sunny and 22°C in {city}."

chat = Chat(
    "huggingface:NobodyWho/LFM2.5-2.6B-GGUF/LFM2.5-2.6B-Q4_K_M.gguf",
    tools=[get_weather],
)
print(chat.ask("What is the weather in Paris?").completed())
```

The model reliably emits its native tool-call markup —
`<|tool_call_start|>[get_weather(city='Paris')]<|tool_call_end|>` — for both single and
follow-up turns.

> [!NOTE]
> Parsing that markup into executed tool calls ships in the upcoming `nobodywho` release
> ([PR #564](https://github.com/nobodywho-ooo/nobodywho/pull/564)). On `nobodywho` 1.1.0 the
> markup is returned as text.

## Why

The upstream template wraps the assistant branch of its message loop in
`{% generation %}` … `{% endgeneration %}`. Those tags are a Hugging Face *transformers*
extension used to mark assistant spans for `return_assistant_tokens_mask` during training.
They are not part of Jinja2, and no llama.cpp-family runtime implements them — so the template
fails to compile and **every prompt errors out**:

```
Could not render messages Template failed to render:
syntax error: unknown statement generation (in <string>:86)
```

The tags emit no output, so removing them is a no-op for the rendered prompt. The template in
this repo is byte-identical to upstream apart from those two lines.

Two related metadata problems were fixed at the same time:

- `tokenizer.ggml.add_bos_token` was **absent**, so runtimes fell back to their own default
  (NobodyWho logs `defaulting to true`) while the template already emits `{{- bos_token -}}`
  itself — putting two leading `<|startoftext|>` tokens on every prompt. Upstream's
  `tokenizer.json` uses a plain `ByteLevel` post-processor that adds no BOS, so `false` is the
  correct value.
- `general.name` held `Ab00687315Bc1298E9D54E9C4B611Dde9867Ccc2`, a build hash that leaked into
  the metadata during the vendor's GGUF conversion.

### Full metadata diff versus upstream

| Key | Upstream | Here |
|---|---|---|
| `tokenizer.chat_template` | `{% generation %}` tags present — fails to compile | tags removed, otherwise byte-identical |
| `tokenizer.ggml.add_bos_token` | *absent* | `false` |
| `general.name` | `Ab00687315Bc1298E9D54E9C4B611Dde9867Ccc2` | `LFM2.5 2.6B` |

Nothing else changed: 266 tensors, identical names, shapes and dtypes, and an identical
SHA-256 over the tensor payload (`9230ca69…4b978d6`).

## Files

| File | Fix recipe | Size |
|---|---|---|
| `LFM2.5-2.6B-Q4_K_M.gguf` | chat template + BOS + name | 1.6 GB |

## Verification

The patched template was checked against every branch it can take — plain user turn, system
prompt, multi-turn with thinking stripped from pre-last-user turns, `preserve_thinking=true`,
tools in the system prompt, assistant `tool_calls`, multipart (list) content,
`add_generation_prompt=false`, and the `CONTINUE_FINAL_MESSAGE_TAG` path — then exercised in
NobodyWho for multi-turn chat with a system prompt and for single and follow-up tool calls.

## Sampling notes

The file carries LiquidAI's recommended `general.sampling.*` metadata as upstream shipped it:
`temperature 0.1`, `top_k 50`. NobodyWho reads these and applies them by default.

The vendor additionally recommends `repetition_penalty 1.1` — both the upstream model card and
`leap/Q4_K_M.json` agree on it — but it is **not** embedded in the GGUF. Pass it yourself if
you want the vendor's full recipe:

```
llama-cli -m LFM2.5-2.6B-Q4_K_M.gguf --conversation \
    --temp 0.1 --top-k 50 --repeat-penalty 1.1
```

## Model Details

| Property | Value |
|---|---|
| Parameters | 2.6B |
| Quantization | Q4_K_M |
| Context length | 131,072 tokens |
| Architecture | `lfm2` (hybrid) |
| Vocabulary | 128,000 tokens |
| License | [LFM Open License v1.0](LICENSE) |
| Base model | [LiquidAI/LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B) |
| Upstream GGUF | [LiquidAI/LFM2.5-2.6B-GGUF](https://huggingface.co/LiquidAI/LFM2.5-2.6B-GGUF) |

These files also work in any other llama.cpp-based runtime; the original unmodified GGUFs live
in the upstream [LiquidAI/LFM2.5-2.6B-GGUF](https://huggingface.co/LiquidAI/LFM2.5-2.6B-GGUF)
repo.

## License

LFM Open License v1.0, unchanged from upstream — see [LICENSE](LICENSE).
All credit for the model goes to [Liquid AI](https://huggingface.co/LiquidAI).
