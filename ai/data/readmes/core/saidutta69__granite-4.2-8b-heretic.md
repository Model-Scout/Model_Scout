---
license: apache-2.0
license_link: https://www.apache.org/licenses/LICENSE-2.0
library_name: transformers
pipeline_tag: text-generation
language:
- en
- de
- es
- fr
- ja
- pt
- ar
- cs
- it
- ko
- nl
- zh
tags:
- granite
- granite-4.2
- granite-4
- reasoning
- thinking
- tool-calling
- ibm
- heretic
- uncensored
- decensored
- abliterated
- reproducible
- conversational
- gguf
- roleplay
- local-llm
- consumer-gpu
base_model: ibm-granite/granite-4.2-8b
---

# granite-4.2-8b-heretic

<div align="center">
  <img src="https://photu.kashyalabanavli.site/racer-is-op.png" alt="RACER IS OP" width="100%">
</div>

<br>

A decensored variant of [ibm-granite/granite-4.2-8b](https://huggingface.co/ibm-granite/granite-4.2-8b), produced with [Heretic](https://github.com/p-e-w/heretic) v1.4.0 (directional ablation / "abliteration"). IBM's Granite 4.2 reasoning model keeps its native `<think>...</think>` chain-of-thought, tool calling, and 131K context; refusal behaviour is suppressed via targeted weight edits to the attention output and MLP down-projections rather than fine-tuning, so the base model's reasoning and knowledge are left largely intact.

**Who this is for:** developers who want the full-size Granite 4.2 8B - the flagship of the 4.2 line, with 32 attention heads and 12,800 intermediate width - uncensored, for local agents, tool-calling workflows, and multilingual reasoning on consumer GPUs. It is the 8B counterpart to the [3B variant](https://huggingface.co/saidutta69/granite-4.2-3b-heretic) already in this collection: same family, same thinking modes, same tool-call format, roughly double the capacity.

<!-- racer-gpu-matrix -->
## Runs on your gaming PC

Full GGUF ladder included - pick the quant that fits your card:

| Your GPU | Recommended quant | Weights |
| :--- | :--- | :--- |
| RTX 4090 / 5090 (24 GB) | Q8_0 | 8.70 GB |
| RTX 4080 / 5080 / 4060 Ti 16G (16 GB) | Q6_K | 6.72 GB |
| RTX 3060 / 4070 / 5070 (12 GB) | Q5_K_M | 5.82 GB |
| RTX 4060 / 3070 (8 GB) | Q4_K_M | 4.98 GB |
| GTX 1660 Super / 2060 / 3050 laptop (6 GB) | IQ4_XS | 4.55 GB |
| CPU-only / Apple Silicon | Q4_K_M | 4.98 GB |

Weights only, at this model's native 8B size; add ~1 GB per 32K of context.
OOM? Drop one quant level. Headroom to spare? Go one up.

## Abliteration parameters

Trial 240 of a 250-trial Heretic run (seed `471411927`). `direction_index` was selected per layer.

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | per layer |
| **attn.o_proj.max_weight** | 1.43 |
| **attn.o_proj.max_weight_position** | 31.47 |
| **attn.o_proj.min_weight** | 0.16 |
| **attn.o_proj.min_weight_distance** | 14.62 |
| **mlp.down_proj.max_weight** | 1.48 |
| **mlp.down_proj.max_weight_position** | 32.12 |
| **mlp.down_proj.min_weight** | 1.45 |
| **mlp.down_proj.min_weight_distance** | 14.44 |

## Performance

| Metric | This model | Original model ([ibm-granite/granite-4.2-8b](https://huggingface.co/ibm-granite/granite-4.2-8b)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0662 | 0 *(by definition)* |
| **Refusals** | 28/100 | 95/100 |

KL divergence of 0.0662 is a moderate-fidelity edit - noticeably looser than the 0.0095 achieved on
the 3B sibling, which means slightly more drift in style than a low-KL Granite 4.2. Refusals on the
harmful evaluation set drop from 95/100 to 28/100, and the `<think>` reasoning traces and tool-call
format come through unchanged.

## Why abliteration instead of fine-tuning

Fine-tuning a "helpful" persona on top of RLHF'd refusals fights the base model's training and tends to degrade coherence. Abliteration instead finds and edits the specific weight directions responsible for refusal, leaving the rest of the network (and its capabilities) untouched. See the [Heretic repo](https://github.com/p-e-w/heretic) and the [original abliteration writeup](https://huggingface.co/blog/mlabonne/abliteration) for the mechanism.

> Made with ❤️ by **RACER IS OP (saidutta69)** — follow for more uncensored models

## Files

### Safetensors

| File | Size |
|---|---|
| `model-00001-of-00004.safetensors` | 4.60 GB |
| `model-00002-of-00004.safetensors` | 4.66 GB |
| `model-00003-of-00004.safetensors` | 4.62 GB |
| `model-00004-of-00004.safetensors` | 2.50 GB |

BF16. The `reproduce/` directory carries the full Heretic recipe -
`config.toml`, `requirements.txt`, the Optuna study journal, and SHA-256 sums - so this exact
model can be regenerated bit-for-bit. Reproduce it with `heretic --reproduce reproduce/reproduce.json`.

### GGUF quantizations
Full quantization set (F16 + Q4_K_M, Q5_K_M, Q6_K, Q8_0) produced with [llama.cpp](https://github.com/ggml-org/llama.cpp).

| File | Format | Size |
|---|---|---|
| `granite-4.2-8b-heretic-F16.gguf` | GGUF F16 | 16.38 GB |
| `granite-4.2-8b-heretic-Q4_K_M.gguf` | GGUF Q4_K_M | 4.98 GB |
| `granite-4.2-8b-heretic-Q5_K_M.gguf` | GGUF Q5_K_M | 5.82 GB |
| `granite-4.2-8b-heretic-Q6_K.gguf` | GGUF Q6_K | 6.72 GB |
| `granite-4.2-8b-heretic-Q8_0.gguf` | GGUF Q8_0 | 8.70 GB |

Granite architecture (`granite`) - loads natively in llama.cpp / Ollama / LM Studio / Jan.

Run `llama serve -hf saidutta69/granite-4.2-8b-heretic` to pull the default quant.

## Quickstart

```bash
# llama.cpp
llama serve -hf saidutta69/granite-4.2-8b-heretic
```

```python
# transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "saidutta69/granite-4.2-8b-heretic"
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)

messages = [{"role": "user", "content": "A train leaves at 14:05 travelling 80 km/h. A car leaves at 14:15 travelling 120 km/h on the same track. When does the car catch the train? Show your work."}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=True,
                                        return_dict=True, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=1024)
print(tokenizer.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

Also runnable via Ollama, LM Studio, Jan, vLLM, SGLang.

### Thinking modes

Granite 4.2 ships a `<think>...</think>` reasoning block and exposes three modes through the chat
template. Pick per query - full thinking for hard problems, non-thinking for latency, low effort
for a shallow pass:

```python
# full thinking (default)
tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)

# skip the reasoning block entirely - fastest, best for chat/classification/tool dispatch
tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False,
                              enable_thinking=False)

# shallow reasoning pass - appends a {reasoning effort: low} hint to the last user turn
tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False,
                              enable_thinking=True, reasoning_effort="low")
```

Strip the `<think>...</think>` block from the output before displaying to users if you enabled thinking.

### Tool calling

The base chat template implements OpenAI-style `tools` with Granite's `<tool_call>` /
`<function=...>` / `<parameter=...>` format, plus `<think>` reasoning about the call. Pass tools
straight through `apply_chat_template`; do not hand-roll the format.

## Model details

| | |
|---|---|
| **Architecture** | `GraniteForCausalLM` (decoder-only dense transformer) |
| **Parameters** | ~8B |
| **Layers / heads** | 40 layers, 32 attention heads, 8 KV heads (GQA) |
| **Hidden / intermediate** | 4096 / 12800 (SwiGLU) |
| **Position embedding** | RoPE, theta = 10,000,000 |
| **Context length** | 131,072 native (512K via YaRN extension) |
| **Vocab** | 100,352 |
| **Precision** | bfloat16 |
| **Languages** | English, German, Spanish, French, Japanese, Portuguese, Arabic, Czech, Italian, Korean, Dutch, Chinese |
| **Base model** | [ibm-granite/granite-4.2-8b](https://huggingface.co/ibm-granite/granite-4.2-8b) |

## FAQ

### What is granite-4.2-8b-heretic?

`granite-4.2-8b-heretic` is a decensored build of [`ibm-granite/granite-4.2-8b`](https://huggingface.co/ibm-granite/granite-4.2-8b) produced with Heretic 1.4.0 (directional ablation). It is the same weights with the refusal direction removed, not a new fine-tune, so its capabilities track the base model.

### Is granite-4.2-8b-heretic actually uncensored?

Yes. On Heretic's 100-prompt refusal harness it drops from 95/100 to 28/100 at KL divergence 0.0662 from the base model. These are measured values, not a claim; reproduction data is in [`reproduce/`](reproduce/). This edit is conservative: only 67 of 95 refusals cleared, so read KL and refusal count together.

### How do I run granite-4.2-8b-heretic locally?

`llama serve -hf saidutta69/granite-4.2-8b-heretic:Q4_K_M` pulls the default quant; the repo ships 5 GGUF quants (see Files).

## Responsible use

Refusal suppression is deliberate and works as intended: this model will comply with requests the base model would refuse, including some it shouldn't. There is no safety filtering layered on top. You are responsible for how you deploy it — don't put this behind an unmoderated public-facing endpoint serving third parties. It inherits Granite 4.2's factual limitations and biases; abliteration removes refusal directions, it doesn't add capability or judgment.

## License

Inherits the [`apache-2.0`](https://www.apache.org/licenses/LICENSE-2.0) license from the base model. The base repo ships no LICENSE file, so the link points at the Apache text directly.

## Related

- [ibm-granite/granite-4.2-8b](https://huggingface.co/ibm-granite/granite-4.2-8b) — the base model
- [saidutta69/granite-4.2-3b-heretic](https://huggingface.co/saidutta69/granite-4.2-3b-heretic) — the 3B sibling, tighter KL
- [Granite 4.2 technical blog](https://huggingface.co/blog/ibm-granite/granite-4-2) — architecture and benchmarks
- [RACER IS OP — Heretic Models — full collection](https://huggingface.co/collections/saidutta69/racer-is-op-heretic-models)

## Abliteration hardware

Recorded in `reproduce/reproduce.json`:

- **GPU:** NVIDIA GeForce RTX 5090 (31.36 GB VRAM)
- **CPU:** AMD Ryzen 9 9950X 16-Core Processor
- **OS:** `Linux-6.6.0-hiveos-x86_64-with-glibc2.35`
- **CUDA / driver:** CUDA 13.0, driver 580.173.02
- **Software:** PyTorch 2.14.1+cu130, Heretic 1.4.0

Heretic notes that KL-divergence and refusal numbers can vary slightly with hardware and library versions.
