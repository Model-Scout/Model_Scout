---
license: apache-2.0
tags:
  - uncensored
  - qwen3.6
  - gguf
  - vision
  - multimodal
  - agentic
  - coding
language:
  - en
  - zh
  - multilingual
pipeline_tag: image-text-to-text
base_model: Qwen/Qwen3.6-27B
---

# Qwen3.6-27B-Uncensored-HauhauCS-Balanced

> **[Join the Discord](https://discord.gg/SZ5vacTXYf)** for updates, roadmaps, projects, or just to chat.

Qwen3.6-27B uncensored by HauhauCS. **0/465 Refusals.** \*

> **HuggingFace's "Hardware Compatibility" widget doesn't recognize K_P quants** — it may show fewer files than actually exist. Click **"View +X variants"** or go to **Files and versions** to see all available downloads.

## About

No changes to datasets or capabilities. Fully functional, 100% of what the original authors intended — just without the refusals.

These are meant to be the best lossless uncensored models out there.

## Balanced Variant

Balanced is the **recommended default** — 99.9%+ of users will be happy here.

Same refusal-removal as Aggressive (**0/465 refusals** on the benchmark). The difference is *how* it complies on edgy prompts:

- **Balanced**: will reason through the request out loud, occasionally attach a short disclaimer or safety framing, then give the full answer. Output is complete, nothing held back but it can talk itself into it first. **Recommended for (Agentic) Coding, Tool use, Reasoning, Creative Writing/RP use cases.**
- **Aggressive** *(separate release)*: strips the self-reasoning. Delivers the raw answer directly, no preamble.

Balanced also has meaningfully more stable sampling across re-runs, which matters for long agentic loops due to no sporadic topic drift deep into a tool-call chain. Go Aggressive only if you're pushing really hardcore prompts (think things that make people's stomachs turn) and specifically want the model to skip its preamble.

## Downloads

| File | Quant | BPW | Size |
|------|-------|-----|------|
| [Qwen3.6-27B-Uncensored-HauhauCS-Balanced-Q8_K_P.gguf](https://huggingface.co/HauhauCS/Qwen3.6-27B-Uncensored-HauhauCS-Balanced/resolve/main/Qwen3.6-27B-Uncensored-HauhauCS-Balanced-Q8_K_P.gguf) | Q8_K_P | 10.06 | 32 GB |
| — | Q8_0 | 8.5 | — |
| [Qwen3.6-27B-Uncensored-HauhauCS-Balanced-Q6_K_P.gguf](https://huggingface.co/HauhauCS/Qwen3.6-27B-Uncensored-HauhauCS-Balanced/resolve/main/Qwen3.6-27B-Uncensored-HauhauCS-Balanced-Q6_K_P.gguf) | Q6_K_P | 7.07 | 23 GB |
| — | Q6_K | 6.6 | — |
| [Qwen3.6-27B-Uncensored-HauhauCS-Balanced-Q5_K_P.gguf](https://huggingface.co/HauhauCS/Qwen3.6-27B-Uncensored-HauhauCS-Balanced/resolve/main/Qwen3.6-27B-Uncensored-HauhauCS-Balanced-Q5_K_P.gguf) | Q5_K_P | 6.47 | 21 GB |
| — | Q5_K_M | 5.7 | — |
| [Qwen3.6-27B-Uncensored-HauhauCS-Balanced-Q4_K_P.gguf](https://huggingface.co/HauhauCS/Qwen3.6-27B-Uncensored-HauhauCS-Balanced/resolve/main/Qwen3.6-27B-Uncensored-HauhauCS-Balanced-Q4_K_P.gguf) | Q4_K_P | 5.4 | 18 GB |
| — | Q4_K_M | 4.88 | — |
| [Qwen3.6-27B-Uncensored-HauhauCS-Balanced-IQ4_XS.gguf](https://huggingface.co/HauhauCS/Qwen3.6-27B-Uncensored-HauhauCS-Balanced/resolve/main/Qwen3.6-27B-Uncensored-HauhauCS-Balanced-IQ4_XS.gguf) | IQ4_XS | 4.32 | 15 GB |
| [Qwen3.6-27B-Uncensored-HauhauCS-Balanced-Q3_K_P.gguf](https://huggingface.co/HauhauCS/Qwen3.6-27B-Uncensored-HauhauCS-Balanced/resolve/main/Qwen3.6-27B-Uncensored-HauhauCS-Balanced-Q3_K_P.gguf) | Q3_K_P | 4.39 | 14 GB |
| — | Q3_K_M | 3.9 | — |
| [Qwen3.6-27B-Uncensored-HauhauCS-Balanced-IQ3_M.gguf](https://huggingface.co/HauhauCS/Qwen3.6-27B-Uncensored-HauhauCS-Balanced/resolve/main/Qwen3.6-27B-Uncensored-HauhauCS-Balanced-IQ3_M.gguf) | IQ3_M | 3.56 | 13 GB |
| [Qwen3.6-27B-Uncensored-HauhauCS-Balanced-IQ3_XS.gguf](https://huggingface.co/HauhauCS/Qwen3.6-27B-Uncensored-HauhauCS-Balanced/resolve/main/Qwen3.6-27B-Uncensored-HauhauCS-Balanced-IQ3_XS.gguf) | IQ3_XS | 3.3 | 12 GB |
| [Qwen3.6-27B-Uncensored-HauhauCS-Balanced-Q2_K_P.gguf](https://huggingface.co/HauhauCS/Qwen3.6-27B-Uncensored-HauhauCS-Balanced/resolve/main/Qwen3.6-27B-Uncensored-HauhauCS-Balanced-Q2_K_P.gguf) | Q2_K_P | 3.19 | 12 GB |
| [Qwen3.6-27B-Uncensored-HauhauCS-Balanced-IQ2_M.gguf](https://huggingface.co/HauhauCS/Qwen3.6-27B-Uncensored-HauhauCS-Balanced/resolve/main/Qwen3.6-27B-Uncensored-HauhauCS-Balanced-IQ2_M.gguf) | IQ2_M | 2.69 | 10 GB |
| [mmproj-Qwen3.6-27B-Uncensored-HauhauCS-Balanced-f16.gguf](https://huggingface.co/HauhauCS/Qwen3.6-27B-Uncensored-HauhauCS-Balanced/resolve/main/mmproj-Qwen3.6-27B-Uncensored-HauhauCS-Balanced-f16.gguf) | mmproj (f16) | — | 928 MB |

All quants generated with importance matrix (imatrix) for optimal quality preservation on abliterated weights.

## What are K_P quants?

K_P ("Perfect") quants are HauhauCS custom quantizations that use model-specific analysis to selectively preserve quality where it matters most. Each model gets its own optimized quantization profile.

A K_P quant effectively bumps quality up by 1-2 quant levels at only ~5-15% larger file size than the base quant. Fully compatible with llama.cpp, LM Studio, and any GGUF-compatible runtime — no special builds needed.

**Note:** K_P quants may show as "?" in LM Studio's quant column. This is a display issue only — the model loads and runs fine.

## Why Balanced for agentic coding

Agentic workflows hit the model with long tool-call chains, structured JSON outputs, deep reasoning chains, and back-to-back prompts in the same session. They need the model to stay **deterministic and on-task** — not occasionally drift on an edge prompt three tool calls deep into a plan.

Balanced is calibrated for that. It especially removes refusals on security/ops/research-adjacent topics that block legitimate coding work, without bending the sampling geometry that keeps long chains coherent.

Recommended quant for most coding work: **Q4_K_P** (18 GB, fits in 24 GB VRAM with room for context) or **Q8_K_P** (32 GB) if you have more VRAM and want 75-99% of BF16 performance (depending on use-case) at 55%'ish of the VRAM cost.

## Specs

- 27B dense parameters
- 64 layers, layout: `16 × (3 × (Gated DeltaNet → FFN) → 1 × (Gated Attention → FFN))`
- 48 linear attention layers + 16 full gated-attention layers
- Gated DeltaNet: 48 V heads / 16 QK heads, head dim 128
- Gated Attention: 24 Q heads / 4 KV heads, head dim 256, rope dim 64
- Hidden dim 5120, FFN dim 17408, vocab 248320
- 262K native context, extensible to ~1M with YaRN
- Natively multimodal (text, image, video) — ships with mmproj
- Based on [Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)

## Recommended Settings

From the official Qwen authors:

**Thinking mode (default) — general tasks:**
- `temperature=1.0, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0`

**Thinking mode — precise coding / WebDev:**
- `temperature=0.6, top_p=0.95, top_k=20, min_p=0.0, presence_penalty=0.0, repetition_penalty=1.0`

**Non-thinking (Instruct) mode:**
- `temperature=0.7, top_p=0.80, top_k=20, min_p=0.0, presence_penalty=1.5, repetition_penalty=1.0`

**My personal preference for coding:** `temperature=0.6` with `presence_penalty=1.5`. Slightly lower temp keeps tool-call formatting tight; presence 1.5 keeps thinking from spiraling in long agent loops.

**Important:**
- Keep at least 128K context to preserve thinking capabilities
- Recommended output length: 32,768 tokens for most queries, up to 81,920 for competition-tier math/code
- Use `--jinja` with llama.cpp for proper chat template handling
- Vision support requires the `mmproj` file alongside the main GGUF
- YaRN rope scaling is **static** in llama.cpp and can hurt short-context performance — only modify `rope_parameters` if you actually need >262K context

**Prompting tip:** this model is a bit more sensitive to prompt clarity than Qwen3.5-35B-A3B. For agentic flows, spell out format, constraints, and scope in the system prompt — it'll stay on rails much better than with vague instructions.

## Turning Thinking On/Off

Qwen3.6 ships with thinking **on by default**. Turn it off when you want faster, shorter replies and don't need chain-of-thought.

> **Heads up:** Qwen3.6 **does not support** the `/think` and `/no_think` soft switches that Qwen3 had. You must use the chat-template kwarg below.

### LM Studio

1. Load the model
2. Right-side settings panel → **Model Settings** → **Prompt Template** (or **Chat Template Options**)
3. Set `enable_thinking` to `false` in the template kwargs
4. Some LM Studio versions expose this as a direct **"Reasoning"** / **"Thinking"** toggle — same effect

### llama.cpp

**llama-server — set as default for all requests:**
```bash
llama-server -m Qwen3.6-27B-Uncensored-HauhauCS-Balanced-Q4_K_P.gguf \
  --mmproj mmproj-Qwen3.6-27B-Uncensored-HauhauCS-Balanced-f16.gguf \
  --jinja -c 131072 -ngl 99 \
  --chat-template-kwargs '{"enable_thinking": false}'
```

**Per-request via the OpenAI-compatible API:**
```json
{
  "model": "qwen3.6-27b",
  "messages": [{"role": "user", "content": "..."}],
  "chat_template_kwargs": {"enable_thinking": false}
}
```

Python `openai` SDK:
```python
client.chat.completions.create(
    model="qwen3.6-27b",
    messages=[{"role": "user", "content": "..."}],
    extra_body={"chat_template_kwargs": {"enable_thinking": False}},
)
```

**Agent scenarios — keep reasoning in context across turns (this one's important):**
```json
{"chat_template_kwargs": {"preserve_thinking": true}}
```

This retains the reasoning block in chat history. Useful for agents where reasoning consistency across tool-call loops matters.

## Usage

Works with llama.cpp, LM Studio, Jan, koboldcpp, and other GGUF-compatible runtimes.

```bash
llama-cli -m Qwen3.6-27B-Uncensored-HauhauCS-Balanced-Q4_K_P.gguf \
  --mmproj mmproj-Qwen3.6-27B-Uncensored-HauhauCS-Balanced-f16.gguf \
  --jinja -c 131072 -ngl 99
```

## Other Models

- [HauhauCS on HuggingFace](https://huggingface.co/HauhauCS/models)

---

\* _Tested with both automated and manual refusal benchmarks and none have been found. If you hit one that's actually obstructive to your use case, [join the Discord](https://discord.gg/SZ5vacTXYf) and flag it so I can work on it in a future revision._
