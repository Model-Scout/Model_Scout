---
license: other
license_name: lfm-license-1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/main/LICENSE
library_name: transformers
pipeline_tag: text-generation
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
- pt
- it
tags:
- liquid
- lfm2.5
- lfm2
- moe
- edge
- on-device
- reasoning
- tool-calling
- heretic
- uncensored
- decensored
- abliterated
- reproducible
- gguf
- roleplay
- local-llm
- consumer-gpu
base_model: LiquidAI/LFM2.5-8B-A1B
---

# LFM2.5-8B-A1B-heretic

<div align="center">
  <img src="https://photu.kashyalabanavli.site/racer-is-op.png" alt="RACER IS OP" width="100%">
</div>

<br>

A decensored variant of [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B), produced with [Heretic](https://github.com/p-e-w/heretic) v1.4.0 (directional ablation / "abliteration"). Liquid's hybrid conv+attention MoE keeps its native reasoning traces, Pythonic tool-call format, and 128K context; refusal behaviour is suppressed via targeted weight edits to the attention output and MLP down-projections rather than fine-tuning, so the base model's agentic ability and multilingual coverage are left largely intact.

**Who this is for:** developers who want a fast, uncensored on-device assistant that actually calls tools - the 8.3B-total / 1.5B-active MoE decodes faster than dense models several times its size, so this runs at interactive speed on CPU-only laptops, Apple Silicon, and low-VRAM GPUs while still fitting a 128K context. Pair it with `LFM2.5-8B-A1B-DSpark` for ~2.5x faster speculative decoding.

<!-- racer-gpu-matrix -->
## Runs on your gaming PC

Full GGUF ladder included - pick the quant that fits your card:

| Your GPU | Recommended quant | Weights |
| :--- | :--- | :--- |
| RTX 4090 / 5090 (24 GB) | Q8_0 | 8.39 GB |
| RTX 4080 / 5080 (16 GB) | Q6_K | 6.48 GB |
| RTX 4070 / 5070 (12 GB) | Q5_K_M | 5.62 GB |
| RTX 4060 Ti / 3070 (8 GB) | Q4_K_M | 4.80 GB |
| GTX 1660 Super / 2060 (6 GB) | IQ4_XS | 4.49 GB |
| CPU-only / Apple Silicon | Q4_K_M | 4.80 GB |

Weights only, at this model's 8.3B total native size; add ~1 GB per 32K of context. Because this is a
mixture-of-experts model, memory *bandwidth* matters far more than raw VRAM - a CPU with fast RAM
often outruns a slow GPU. OOM? Drop one quant level. Headroom to spare? Go one up.

## Abliteration parameters

Trial 167 of a 200-trial Heretic run (seed `4217170727`). `direction_index` was selected per layer.

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | per layer |
| **attn.o_proj.max_weight** | 1.44 |
| **attn.o_proj.max_weight_position** | 13.92 |
| **attn.o_proj.min_weight** | 1.15 |
| **attn.o_proj.min_weight_distance** | 9.52 |
| **mlp.down_proj.max_weight** | 1.32 |
| **mlp.down_proj.max_weight_position** | 18.50 |
| **mlp.down_proj.min_weight** | 0.12 |
| **mlp.down_proj.min_weight_distance** | 11.61 |

## Performance

| Metric | This model | Original model ([LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.1649 | 0 *(by definition)* |
| **Refusals** | 28/100 | 90/100 |

Refusals on the harmful evaluation set drop from 90/100 to 28/100. KL divergence of 0.1649 is the
loosest of this batch - the refusal directions in this hybrid conv+attention MoE overlap more with
its instruction-following behaviour, so Heretic had to move further to hit the same refusal target.
Expect a small amount more drift in style and formatting than a low-KL sibling; the reasoning traces
and tool-call format survive intact.

## Why abliteration instead of fine-tuning

Fine-tuning a "helpful" persona on top of RLHF'd refusals fights the base model's training and tends to degrade coherence. Abliteration instead finds and edits the specific weight directions responsible for refusal, leaving the rest of the network (and its capabilities) untouched. See the [Heretic repo](https://github.com/p-e-w/heretic) and the [original abliteration writeup](https://huggingface.co/blog/mlabonne/abliteration) for the mechanism.

> Made with ❤️ by **RACER IS OP (saidutta69)** — follow for more uncensored models

## Files

### Safetensors

| File | Size |
|---|---|
| `model-00001-of-00004.safetensors` | 4.60 GB |
| `model-00002-of-00004.safetensors` | 4.55 GB |
| `model-00003-of-00004.safetensors` | 4.57 GB |
| `model-00004-of-00004.safetensors` | 2.05 GB |

BF16, ~8.3B total parameters (~1.5B active per token). The `reproduce/` directory carries the full Heretic recipe -
`config.toml`, `requirements.txt`, the Optuna study journal, and SHA-256 sums - so this exact
model can be regenerated bit-for-bit. Reproduce it with `heretic --reproduce reproduce/reproduce.json`.

### GGUF quantizations
Full quantization set (F16 + Q4_K_M, Q5_K_M, Q6_K, Q8_0) produced with [llama.cpp](https://github.com/ggml-org/llama.cpp).

| File | Format | Size |
|---|---|---|
| `LFM2.5-8B-A1B-heretic-F16.gguf` | GGUF F16 | 15.78 GB |
| `LFM2.5-8B-A1B-heretic-Q4_K_M.gguf` | GGUF Q4_K_M | 4.80 GB |
| `LFM2.5-8B-A1B-heretic-Q5_K_M.gguf` | GGUF Q5_K_M | 5.62 GB |
| `LFM2.5-8B-A1B-heretic-Q6_K.gguf` | GGUF Q6_K | 6.48 GB |
| `LFM2.5-8B-A1B-heretic-Q8_0.gguf` | GGUF Q8_0 | 8.39 GB |

LFM2 MoE architecture (`lfm2moe`) - loads natively in llama.cpp / LM Studio / Jan.

Run `llama serve -hf saidutta69/LFM2.5-8B-A1B-heretic` to pull the default quant.

## Quickstart

```bash
# llama.cpp
llama serve -hf saidutta69/LFM2.5-8B-A1B-heretic
```

```python
# transformers (requires transformers>=5.0.0)
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "saidutta69/LFM2.5-8B-A1B-heretic"
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", dtype="bfloat16")
tokenizer = AutoTokenizer.from_pretrained(model_name)

messages = [{"role": "user", "content": "A train leaves at 14:05 travelling 80 km/h. A car leaves at 14:15 travelling 120 km/h on the same track. When does the car catch the train? Show your work."}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
out = model.generate(**inputs, do_sample=True, temperature=0.2, top_k=80, repetition_penalty=1.05, max_new_tokens=8192)
print(tokenizer.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

Also runnable via Ollama, LM Studio, Jan, vLLM, SGLang.

### Generation parameters

Liquid's recommended settings - low temperature with a top-k cut:

```python
model.generate(**inputs, temperature=0.2, top_k=80, repetition_penalty=1.05)
```

### Tool use

LFM2.5 writes Pythonic calls: a Python list between `<|tool_call_start|>` and `<|tool_call_end|>`.
Pass tool definitions as a JSON list in the system prompt, or hand them to
`tokenizer.apply_chat_template(..., tools=tools)`, then feed the result back under a `tool` role.
To get JSON instead, just ask for it in the system prompt.

### Speculative decoding

Attach [LFM2.5-8B-A1B-DSpark](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B-DSpark) (a 328M drafter)
for roughly 2.5x faster decoding with identical outputs.

## Model details

| | |
|---|---|
| **Architecture** | `Lfm2MoeForCausalLM` (hybrid conv + attention MoE) |
| **Parameters** | 8.3B total / 1.5B active |
| **Layers / heads** | 24 layers (18 double-gated conv + 6 GQA), 32 attention heads, 8 KV heads |
| **Hidden / intermediate** | 2048 / 7168 dense, 1792 per expert |
| **Experts** | 32 experts, 4 routed per token |
| **Position embedding** | RoPE, theta = 5,000,000 |
| **Context length** | 128,000 |
| **Vocab** | 128,000 |
| **Precision** | bfloat16 |
| **Languages** | English, Arabic, Chinese, French, German, Italian, Japanese, Korean, Portuguese, Spanish |
| **Base model** | [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B) |

## FAQ

### What is LFM2.5-8B-A1B-heretic?

`LFM2.5-8B-A1B-heretic` is a decensored build of [`LiquidAI/LFM2.5-8B-A1B`](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B) produced with Heretic 1.4.0 (directional ablation). It is the same weights with the refusal direction removed, not a new fine-tune, so its capabilities track the base model.

### Is LFM2.5-8B-A1B-heretic actually uncensored?

Yes. On Heretic's 100-prompt refusal harness it drops from 90/100 to 28/100 at KL divergence 0.1649 from the base model. These are measured values, not a claim; reproduction data is in [`reproduce/`](reproduce/). This edit is conservative: only 62 of 90 refusals cleared, so read KL and refusal count together. KL is high for this checkpoint (0.1649); weights moved further than the low-KL siblings and capability impact is not benchmarked here.

### How do I run LFM2.5-8B-A1B-heretic locally?

`llama serve -hf saidutta69/LFM2.5-8B-A1B-heretic:Q4_K_M` pulls the default quant; the repo ships 5 GGUF quants (see Files).

## Responsible use

Refusal suppression is deliberate and works as intended: this model will comply with requests the base model would refuse, including some it shouldn't. There is no safety filtering layered on top. You are responsible for how you deploy it — don't put this behind an unmoderated public-facing endpoint serving third parties. It inherits LFM2.5's factual limitations and biases; abliteration removes refusal directions, it doesn't add capability or judgment.

## License

Inherits the [LFM License 1.0](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/main/LICENSE) from the base model.

## Related

- [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B) — the base model
- [LFM2.5 technical report](https://www.liquid.ai/blog/lfm2-5-8b-a1b) — architecture and benchmarks
- [RACER IS OP — Heretic Models — full collection](https://huggingface.co/collections/saidutta69/racer-is-op-heretic-models)

## Abliteration hardware

Recorded in `reproduce/reproduce.json`:

- **GPU:** NVIDIA GeForce RTX 5090 (31.36 GB VRAM)
- **CPU:** AMD Ryzen 7 9700X 8-Core Processor
- **OS:** `Linux-6.8.0-142-generic-x86_64-with-glibc2.35`
- **CUDA / driver:** CUDA 13.0, driver 595.84
- **Software:** PyTorch 2.14.1+cu130, Heretic 1.4.0

Heretic notes that KL-divergence and refusal numbers can vary slightly with hardware and library versions.
