---
license: apache-2.0
license_link: https://www.apache.org/licenses/LICENSE-2.0
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
library_name: transformers
pipeline_tag: text-generation
base_model:
- ibm-granite/granite-4.2-3b
tags:
- granite
- granite-4.2
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
---

# granite-4.2-3b-heretic

<div align="center">
  <img src="https://photu.kashyalabanavli.site/racer-is-op.png" alt="RACER IS OP" width="100%">
</div>

<br>

A decensored variant of [ibm-granite/granite-4.2-3b](https://huggingface.co/ibm-granite/granite-4.2-3b), produced with [Heretic](https://github.com/p-e-w/heretic) v1.4.0 (directional ablation / "abliteration"). IBM's compact Granite 4.2 reasoning model keeps its native `<think>...</think>` chain-of-thought, tool calling, and 128K context; refusal behavior is suppressed via targeted weight edits to the attention output and MLP down-projections rather than fine-tuning, so the base model's reasoning and knowledge are left largely intact.

**Who this is for:** developers who want a small reasoning model that thinks out loud and answers directly instead of refusing - for local agents, tool-calling workflows, and multilingual reasoning on consumer hardware. At 3.66B it runs on CPU and low-VRAM GPUs via GGUF, and it is the only Granite 4.2 variant in this collection, so the full 128K context and thinking budget stay reachable without a datacenter GPU.

<!-- racer-gpu-matrix -->
## Runs on your gaming PC

Full GGUF ladder included - pick the quant that fits your card:

| Your GPU | Recommended quant | Weights |
| :--- | :--- | :--- |
| RTX 3090 / 4090 / 5090 (24 GB) | Q8_0 | 3.89 GB |
| RTX 4080 / 5080 / 4060 Ti 16G (16 GB) | Q6_K | 3.01 GB |
| RTX 3060 / 4070 / 5070 (12 GB) | Q5_K_M | 2.61 GB |
| RTX 4060 / 3070 (8 GB) | Q4_K_M | 2.24 GB |
| GTX 1660 Super / 2060 / 3050 laptop (6 GB) | IQ4_XS | 2.05 GB |
| CPU-only / Apple Silicon | Q4_K_M | fits in system RAM |

Weights only, at this model's 3.66B native size; add ~1 GB for context.
OOM? Drop one quant level. Headroom to spare? Go one up.

## Abliteration parameters

Trial 180 of a 200-trial Heretic run (seed `3959419965`).

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | 24.94 |
| **attn.o_proj.max_weight** | 1.46 |
| **attn.o_proj.max_weight_position** | 23.67 |
| **attn.o_proj.min_weight** | 0.44 |
| **attn.o_proj.min_weight_distance** | 22.08 |
| **mlp.down_proj.max_weight** | 1.48 |
| **mlp.down_proj.max_weight_position** | 24.04 |
| **mlp.down_proj.min_weight** | 0.77 |
| **mlp.down_proj.min_weight_distance** | 22.92 |

## Performance

| Metric | This model | Original model ([ibm-granite/granite-4.2-3b](https://huggingface.co/ibm-granite/granite-4.2-3b)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0095 | 0 *(by definition)* |
| **Refusals** | 3/100 | 62/100 |

KL divergence of 0.0095 is the tightest constraint Heretic optimizes against, so this is a
high-fidelity edit: refusal directions were removed with minimal collateral damage to the
model's other behaviour. Refusals on the harmful evaluation set drop from 62/100 to 3/100.

## Why abliteration instead of fine-tuning

Fine-tuning a "helpful" persona on top of RLHF'd refusals fights the base model's training and tends to degrade coherence. Abliteration instead finds and edits the specific weight directions responsible for refusal, leaving the rest of the network (and its capabilities) untouched. See the [Heretic repo](https://github.com/p-e-w/heretic) and the [original abliteration writeup](https://huggingface.co/blog/mlabonne/abliteration) for the mechanism.

> Made with ❤️ by **RACER IS OP (saidutta69)** — follow for more uncensored models

## Files

### Safetensors

| File | Size |
|---|---|
| `model-00001-of-00002.safetensors` | 4.96 GB |
| `model-00002-of-00002.safetensors` | 2.36 GB |

BF16, 3,659,737,600 parameters. The `reproduce/` directory carries the full Heretic recipe -
`config.toml`, `requirements.txt`, the Optuna study journal, and SHA-256 sums - so this exact
model can be regenerated bit-for-bit. Reproduce it with `heretic --reproduce reproduce/reproduce.json`.

### GGUF quantizations
Full quantization set (14 quants + F16) produced with [llama.cpp](https://github.com/ggml-org/llama.cpp).

| File | Format | Size |
|---|---|---|
| `granite-4.2-3b-heretic-F16.gguf` | GGUF F16 | 7.32 GB |
| `granite-4.2-3b-heretic-Q2_K.gguf` | GGUF Q2_K | 1.46 GB |
| `granite-4.2-3b-heretic-IQ3_S.gguf` | GGUF IQ3_S | 1.68 GB |
| `granite-4.2-3b-heretic-Q3_K_S.gguf` | GGUF Q3_K_S | 1.68 GB |
| `granite-4.2-3b-heretic-Q3_K_M.gguf` | GGUF Q3_K_M | 1.84 GB |
| `granite-4.2-3b-heretic-Q3_K_L.gguf` | GGUF Q3_K_L | 1.97 GB |
| `granite-4.2-3b-heretic-IQ4_XS.gguf` | GGUF IQ4_XS | 2.05 GB |
| `granite-4.2-3b-heretic-Q4_K_S.gguf` | GGUF Q4_K_S | 2.14 GB |
| `granite-4.2-3b-heretic-Q4_0.gguf` | GGUF Q4_0 | 2.13 GB |
| `granite-4.2-3b-heretic-Q4_1.gguf` | GGUF Q4_1 | 2.34 GB |
| `granite-4.2-3b-heretic-Q4_K_M.gguf` | GGUF Q4_K_M | 2.24 GB |
| `granite-4.2-3b-heretic-Q5_K_S.gguf` | GGUF Q5_K_S | 2.55 GB |
| `granite-4.2-3b-heretic-Q5_K_M.gguf` | GGUF Q5_K_M | 2.61 GB |
| `granite-4.2-3b-heretic-Q6_K.gguf` | GGUF Q6_K | 3.01 GB |
| `granite-4.2-3b-heretic-Q8_0.gguf` | GGUF Q8_0 | 3.89 GB |

Granite architecture (`granite`, 363 tensors) - loads natively in llama.cpp / Ollama / LM Studio / Jan.

Run `llama serve -hf saidutta69/granite-4.2-3b-heretic` to pull the default quant.

## Quickstart

```bash
# llama.cpp
llama serve -hf saidutta69/granite-4.2-3b-heretic
```

```python
# transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "saidutta69/granite-4.2-3b-heretic"
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
| **Parameters** | 3.66B |
| **Layers / heads** | 40 layers, 40 attention heads, 8 KV heads (GQA) |
| **Hidden / intermediate** | 2560 / 8192 (SwiGLU) |
| **Position embedding** | RoPE, theta = 10,000,000 |
| **Context length** | 131,072 native (512K via YaRN extension) |
| **Vocab** | 100,352 |
| **Precision** | bfloat16 |
| **Languages** | English, German, Spanish, French, Japanese, Portuguese, Arabic, Czech, Italian, Korean, Dutch, Chinese |
| **Base model** | [ibm-granite/granite-4.2-3b](https://huggingface.co/ibm-granite/granite-4.2-3b) (a fine-tune of [ibm-granite/granite-4.1-3b-base](https://huggingface.co/ibm-granite/granite-4.1-3b-base)) |

## FAQ

### What is granite-4.2-3b-heretic?

`granite-4.2-3b-heretic` is a decensored build of [`ibm-granite/granite-4.2-3b`](https://huggingface.co/ibm-granite/granite-4.2-3b) produced with Heretic 1.4.0 (directional ablation). It is the same weights with the refusal direction removed, not a new fine-tune, so its capabilities track the base model.

### Is granite-4.2-3b-heretic actually uncensored?

Yes. On Heretic's 100-prompt refusal harness it drops from 62/100 to 3/100 at KL divergence 0.0095 from the base model. These are measured values, not a claim; reproduction data is in [`reproduce/`](reproduce/).

### How do I run granite-4.2-3b-heretic locally?

`llama serve -hf saidutta69/granite-4.2-3b-heretic:Q4_K_M` pulls the default quant; the repo ships 15 GGUF quants (see Files).

## Responsible use

Refusal suppression is deliberate and works as intended: this model will comply with requests the base model would refuse, including some it shouldn't. There is no safety filtering layered on top. You are responsible for how you deploy it — don't put this behind an unmoderated public-facing endpoint serving third parties. It inherits Granite 4.2's factual limitations and biases; abliteration removes refusal directions, it doesn't add capability or judgment.

## License

Inherits the [`apache-2.0`](https://www.apache.org/licenses/LICENSE-2.0) license from the base model.

## Related

- [ibm-granite/granite-4.2-3b](https://huggingface.co/ibm-granite/granite-4.2-3b) — the base model
- [RACER IS OP — Heretic Models — full collection](https://huggingface.co/collections/saidutta69/racer-is-op-heretic-models)

## Abliteration hardware

Recorded in `reproduce/reproduce.json`:

- **GPU:** Tesla T4 (14.56 GB VRAM), Tesla T4 (14.56 GB VRAM)
- **CPU:** Intel(R) Xeon(R) CPU @ 2.00GHz
- **OS:** `Linux-6.18.48+-x86_64-with-glibc2.35`
- **CUDA / driver:** CUDA 13.0, driver 580.178.04
- **Software:** PyTorch 2.14.1+cu130, Heretic 1.4.0

Heretic notes that KL-divergence and refusal numbers can vary slightly with hardware and library versions.
