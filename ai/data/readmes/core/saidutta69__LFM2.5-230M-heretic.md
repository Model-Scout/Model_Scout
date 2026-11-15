---
license: other
license_name: lfm-license-1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-230M/blob/main/LICENSE
library_name: transformers
pipeline_tag: text-generation
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
tags:
- liquid
- lfm2.5
- lfm2
- edge
- on-device
- tool-calling
- heretic
- uncensored
- decensored
- abliterated
- reproducible
- gguf
- roleplay
- local-llm
base_model: LiquidAI/LFM2.5-230M
---

# LFM2.5-230M-heretic

<div align="center">
  <img src="https://photu.kashyalabanavli.site/racer-is-op.png" alt="RACER IS OP" width="100%">
</div>

<br>

A decensored variant of [LiquidAI/LFM2.5-230M](https://huggingface.co/LiquidAI/LFM2.5-230M), produced with [Heretic](https://github.com/p-e-w/heretic) v1.4.0 (directional ablation / "abliteration"). Liquid's hybrid conv+attention architecture keeps its native Pythonic tool-call format and ten-language coverage; refusal behaviour is suppressed via targeted weight edits to the attention output and MLP down-projections rather than fine-tuning, so the base model's agentic ability is left largely intact.

**Who this is for:** the smallest uncensored model in the collection — 230M parameters that run at 213 tok/s on a Galaxy S25 Ultra and 42 tok/s on a Raspberry Pi 5, in well under 1 GB. Reach for it for data extraction, structured output, tool routing, and RAG on hardware where nothing larger will fit. It scores 71.71 on IFEval and 43.26 on BFCLv3 — real instruction-following and tool-call numbers for the size — but Liquid does not recommend this tier for reasoning-heavy work, so treat it as an extraction and routing engine, not a chatbot.

Refusals drop from **95/100 to 10/100** across ten languages.

## Runs anywhere

At 230M there is no VRAM ladder — pick a quant by how much RAM and how much bandwidth your device has:

| Device | Recommended quant | Weights |
| :--- | :--- | :--- |
| Phone / browser (4 GB RAM) | Q4_K_M | ~0.14 GB |
| Raspberry Pi 5 (4 GB) | Q4_K_M | ~0.14 GB |
| Laptop (8 GB, Apple Silicon) | Q8_0 | ~0.23 GB |
| Server / multi-tenant | Q6_K | ~0.18 GB |

Weights only, at this model's 230M native size. The whole model — weights **and** KV cache — sits in
well under 1 GB at Q4_0, with roughly 32K of usable context. Because the hybrid architecture spends most
of its 14 layers in cheap convolution blocks, this model is far more decode-bandwidth-sensitive than its
parameter count suggests: fast RAM matters more than a fast GPU.

## Abliteration parameters

Trial 82 of a 200-trial Heretic run (seed `3544511175`).

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | 10.25 |
| **attn.o_proj.max_weight** | 1.41 |
| **attn.o_proj.max_weight_position** | 12.31 |
| **attn.o_proj.min_weight** | 0.94 |
| **attn.o_proj.min_weight_distance** | 6.61 |
| **mlp.down_proj.max_weight** | 0.81 |
| **mlp.down_proj.max_weight_position** | 9.59 |
| **mlp.down_proj.min_weight** | 0.59 |
| **mlp.down_proj.min_weight_distance** | 4.15 |

## Performance

| Metric | This model | Original model ([LiquidAI/LFM2.5-230M](https://huggingface.co/LiquidAI/LFM2.5-230M)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0548 | 0 *(by definition)* |
| **Refusals** | 10/100 | 95/100 |

Refusals on the harmful evaluation set drop from 95/100 to 10/100 at KL 0.0548. Ten remaining refusals
is on the higher side for this collection — small refusal-tuned models concentrate refusal behaviour into
fewer directions, so the edit both moves further and leaves more behind than on the larger siblings.
Read the KL figure and the refusal count together, never the KL alone.

## Why abliteration instead of fine-tuning

Fine-tuning a "helpful" persona on top of RLHF'd refusals fights the base model's training and tends to degrade coherence. Abliteration instead finds and edits the specific weight directions responsible for refusal, leaving the rest of the network (and its capabilities) untouched. See the [Heretic repo](https://github.com/p-e-w/heretic) and the [original abliteration writeup](https://huggingface.co/blog/mlabonne/abliteration) for the mechanism.

> Made with ❤️ by **RACER IS OP (saidutta69)** — follow for more uncensored models

## Files

### Safetensors

| File | Size |
|---|---|
| `model.safetensors` | 0.43 GB |

BF16, 230M parameters. The `reproduce/` directory carries the full Heretic recipe — `config.toml`,
`requirements.txt`, the Optuna study journal, and SHA-256 sums — so this exact model can be regenerated
bit-for-bit. Reproduce it with `heretic --reproduce reproduce/reproduce.json`.

### GGUF quantizations

Full quantization set (14 quants + F16) produced with [llama.cpp](https://github.com/ggml-org/llama.cpp).

| File | Format | Size |
|---|---|---|
| `LFM2.5-230M-heretic-F16.gguf` | GGUF F16 | 0.43 GB |
| `LFM2.5-230M-heretic-Q2_K.gguf` | GGUF Q2_K | 0.11 GB |
| `LFM2.5-230M-heretic-IQ3_S.gguf` | GGUF IQ3_S | 0.12 GB |
| `LFM2.5-230M-heretic-Q3_K_S.gguf` | GGUF Q3_K_S | 0.12 GB |
| `LFM2.5-230M-heretic-Q3_K_M.gguf` | GGUF Q3_K_M | 0.13 GB |
| `LFM2.5-230M-heretic-Q3_K_L.gguf` | GGUF Q3_K_L | 0.13 GB |
| `LFM2.5-230M-heretic-IQ4_XS.gguf` | GGUF IQ4_XS | 0.13 GB |
| `LFM2.5-230M-heretic-Q4_K_S.gguf` | GGUF Q4_K_S | 0.14 GB |
| `LFM2.5-230M-heretic-Q4_0.gguf` | GGUF Q4_0 | 0.14 GB |
| `LFM2.5-230M-heretic-Q4_1.gguf` | GGUF Q4_1 | 0.15 GB |
| `LFM2.5-230M-heretic-Q4_K_M.gguf` | GGUF Q4_K_M | 0.14 GB |
| `LFM2.5-230M-heretic-Q5_K_S.gguf` | GGUF Q5_K_S | 0.16 GB |
| `LFM2.5-230M-heretic-Q5_K_M.gguf` | GGUF Q5_K_M | 0.16 GB |
| `LFM2.5-230M-heretic-Q6_K.gguf` | GGUF Q6_K | 0.18 GB |
| `LFM2.5-230M-heretic-Q8_0.gguf` | GGUF Q8_0 | 0.23 GB |

LFM2 dense architecture (`lfm2`) - loads natively in llama.cpp / LM Studio / Jan. Day-one upstream support,
so this also works with MLX, vLLM, and Nexa-optimized NPU builds.

Run `llama serve -hf saidutta69/LFM2.5-230M-heretic` to pull the default quant.

## Quickstart

```bash
# llama.cpp
llama serve -hf saidutta69/LFM2.5-230M-heretic
```

```python
# transformers (requires transformers>=5.0.0)
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "saidutta69/LFM2.5-230M-heretic"
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", dtype="bfloat16")
tokenizer = AutoTokenizer.from_pretrained(model_name)

messages = [{"role": "user", "content": "Extract the invoice number and total from: 'Invoice INV-4471, total 231.50 USD, due 30 Nov.'"}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
out = model.generate(**inputs, do_sample=True, temperature=0.1, top_k=50, repetition_penalty=1.05, max_new_tokens=512)
print(tokenizer.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

Also runnable via Ollama, LM Studio, Jan, vLLM, SGLang, and OpenVINO.

### Generation parameters

Liquid's recommended settings - low temperature with a top-k cut:

```python
model.generate(**inputs, temperature=0.1, top_k=50, repetition_penalty=1.05)
```

### Chat template

LFM2.5 uses a ChatML-like format. See the [Chat Template documentation](https://docs.liquid.ai/lfm/key-concepts/chat-template) for details.

```
<|startoftext|>system
You are a helpful assistant trained by Liquid AI.
user
What is C. elegans?
assistant
```

### Tool use

LFM2.5 writes Pythonic calls: a Python list between `<|tool_call_start|>` and `<|tool_call_end|>`.
Pass tool definitions as a JSON list in the system prompt, or hand them to
`tokenizer.apply_chat_template(..., tools=tools)`, then feed the result back under a `tool` role.
To get JSON instead, just ask for it in the system prompt.

## Model details

| | |
|---|---|
| **Architecture** | `Lfm2ForCausalLM` (hybrid conv + attention) |
| **Parameters** | 230M |
| **Layers / heads** | 14 layers (8 double-gated conv + 6 GQA), 16 attention heads, 8 KV heads |
| **Hidden / intermediate** | 1024 / 2560 |
| **Convolution cache** | L_cache = 3 |
| **Position embedding** | RoPE, theta = 1,000,000 |
| **Context length** | 128,000 (config `max_position_embeddings`); Liquid's tuned default is 32,768 |
| **Vocab** | 65,536 |
| **Precision** | bfloat16 |
| **Languages** | English, Arabic, Chinese, French, German, Italian, Japanese, Korean, Portuguese, Spanish |
| **Base model** | [LiquidAI/LFM2.5-230M](https://huggingface.co/LiquidAI/LFM2.5-230M) |

## FAQ

### What is LFM2.5-230M-heretic?

`LFM2.5-230M-heretic` is a decensored build of [`LiquidAI/LFM2.5-230M`](https://huggingface.co/LiquidAI/LFM2.5-230M) produced with Heretic 1.4.0 (directional ablation). It is the same weights with the refusal direction removed, not a new fine-tune, so its capabilities track the base model.

### Is LFM2.5-230M-heretic actually uncensored?

Yes. On Heretic's 100-prompt refusal harness it drops from 95/100 to 10/100 at KL divergence 0.0548 from the base model. These are measured values, not a claim; reproduction data is in [`reproduce/`](reproduce/).

### How do I run LFM2.5-230M-heretic locally?

`llama serve -hf saidutta69/LFM2.5-230M-heretic:Q4_K_M` pulls the default quant; the repo ships 15 GGUF quants (see Files).

## Responsible use

Refusal suppression is deliberate and works as intended: this model will comply with requests the base model would refuse, including some it shouldn't. There is no safety filtering layered on top. You are responsible for how you deploy it — don't put this behind an unmoderated public-facing endpoint serving third parties. Liquid explicitly does not recommend LFM2.5-230M for reasoning-heavy work such as advanced math, code generation, or creative writing; it is built for extraction, structured output, and tool use.

## License

Inherits the [LFM License 1.0](https://huggingface.co/LiquidAI/LFM2.5-230M/blob/main/LICENSE) from the base model.

## Related

- [LiquidAI/LFM2.5-230M](https://huggingface.co/LiquidAI/LFM2.5-230M) — the base model
- [saidutta69/LFM2.5-350M-heretic](https://huggingface.co/saidutta69/LFM2.5-350M-heretic) — the next size up
- [saidutta69/LFM2.5-1.2B-Instruct-heretic](https://huggingface.co/saidutta69/LFM2.5-1.2B-Instruct-heretic) — the 1.2B sibling
- [RACER IS OP — Heretic Models — full collection](https://huggingface.co/collections/saidutta69/racer-is-op-heretic-models)

## Abliteration hardware

Recorded in `reproduce/reproduce.json`:

- **GPU:** NVIDIA GeForce RTX 4090 (23.52 GB VRAM)
- **CPU:** AMD EPYC 7402 24-Core Processor
- **OS:** `Linux-6.8.0-146-generic-x86_64-with-glibc2.35`
- **CUDA / driver:** CUDA 13.0, driver 595.99.02
- **Software:** PyTorch 2.14.1+cu130, Heretic 1.4.0

Heretic notes that KL-divergence and refusal numbers can vary slightly with hardware and library versions.
