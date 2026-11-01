---
license: other
license_name: lfm-license-1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking/blob/main/LICENSE
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
tags:
- liquid
- lfm2.5
- lfm2
- edge
- on-device
- reasoning
- thinking
- tool-calling
- heretic
- uncensored
- decensored
- abliterated
- reproducible
- gguf
- local-llm
base_model: LiquidAI/LFM2.5-1.2B-Thinking
---

# LFM2.5-1.2B-Thinking-heretic

<div align="center">
  <img src="https://photu.kashyalabanavli.site/racer-is-op.png" alt="RACER IS OP" width="100%">
</div>

<br>

A decensored variant of [LiquidAI/LFM2.5-1.2B-Thinking](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking), produced with [Heretic](https://github.com/p-e-w/heretic) v1.4.0 (directional ablation / "abliteration"). This is the reasoning sibling of the LFM2.5-1.2B line: it emits an explicit `<think>…</think>` trace before its answer. Liquid's hybrid conv+attention architecture keeps its native Pythonic tool-call format, instruction-following, and multilingual coverage; refusal behaviour is suppressed via targeted weight edits to the attention output and MLP down-projections rather than fine-tuning, so the base model's reasoning ability is left largely intact.

**Who this is for:** developers who want a genuine on-device reasoning model that still fits on a phone. LFM2.5-1.2B-Thinking scores 87.96 on MATH-500, 85.60 on GSM8K, 88.42 on IFEval and 56.97 on BFCLv3 — real chain-of-thought and tool-calling numbers — while decoding at 116 tok/s on an AMD Ryzen CPU (Q4_0) in under 1 GB. Use it for local agents, math and multi-step reasoning, RAG, and structured extraction where a cloud round-trip would be the bottleneck.

Refusals drop from **98/100 to 10/100**. See [Performance](#performance) for why the KL figure here needs reading together with that count.

## Runs anywhere

| Device | Recommended quant | Weights |
| :--- | :--- | :--- |
| Phone / browser (4 GB RAM) | Q4_K_M | ~0.68 GB |
| Raspberry Pi 5 (4 GB) | Q4_K_M | ~0.68 GB |
| Laptop (8 GB, Apple Silicon) | Q8_0 | ~1.16 GB |
| RTX 3060 / 4060 (8-12 GB) | Q6_K | ~0.90 GB |
| Server / multi-tenant | Q5_K_M | ~0.79 GB |

Weights only, at this model's 1.17B native size. The hybrid architecture spends 10 of its 16 layers in cheap
convolution blocks, so this model is decode-bandwidth-bound: fast RAM and memory bandwidth matter far more
than raw compute. Because it is a reasoning model, budget output tokens generously — the `<think>` trace can
dwarf the final answer on a hard question. OOM? Drop one quant level; the Q2_K tier (~0.45 GB) is there if
you truly need it.

## Abliteration parameters

Trial 83 of a 200-trial Heretic run (seed `2205080409`).

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | per layer |
| **attn.o_proj.max_weight** | 1.49 |
| **attn.o_proj.max_weight_position** | 11.43 |
| **attn.o_proj.min_weight** | 1.48 |
| **attn.o_proj.min_weight_distance** | 7.75 |
| **mlp.down_proj.max_weight** | 1.44 |
| **mlp.down_proj.max_weight_position** | 9.61 |
| **mlp.down_proj.min_weight** | 1.12 |
| **mlp.down_proj.min_weight_distance** | 8.36 |

## Performance

| Metric | This model | Original model ([LiquidAI/LFM2.5-1.2B-Thinking](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0005 | 0 *(by definition)* |
| **Refusals** | 10/100 | 98/100 |

Refusals on the harmful evaluation set drop from 98/100 to 10/100. The KL divergence of 0.0005 is the
lowest in this collection: the optimiser found a direction it applied conservatively, which is why so much
of the base model's behaviour and reasoning survives. It is not a free lunch — 10 refusals remain, more
than the near-fully-decensored edits in this collection. Read the KL figure and the refusal count together,
never the KL alone: a low KL only means the edit was careful, not that refusals fell.

## Why abliteration instead of fine-tuning

Fine-tuning a "helpful" persona on top of RLHF'd refusals fights the base model's training and tends to degrade coherence. Abliteration instead finds and edits the specific weight directions responsible for refusal, leaving the rest of the network (and its capabilities) untouched. See the [Heretic repo](https://github.com/p-e-w/heretic) and the [original abliteration writeup](https://huggingface.co/blog/mlabonne/abliteration) for the mechanism.

> Made with ❤️ by **RACER IS OP** — follow for more uncensored models

## Files

### Safetensors

| File | Size |
|---|---|
| `model.safetensors` | 2.18 GB |

BF16, 1.17B parameters. The `reproduce/` directory carries the full Heretic recipe — `config.toml`,
`requirements.txt`, the Optuna study journal, and SHA-256 sums — so this exact model can be regenerated
bit-for-bit. Reproduce it with `heretic --reproduce reproduce/reproduce.json`.

### GGUF quantizations

Full quantization set (14 quants + F16) produced with [llama.cpp](https://github.com/ggml-org/llama.cpp).

| File | Format | Size |
|---|---|---|
| `LFM2.5-1.2B-Thinking-heretic-F16.gguf` | GGUF F16 | 2.18 GB |
| `LFM2.5-1.2B-Thinking-heretic-Q2_K.gguf` | GGUF Q2_K | 0.45 GB |
| `LFM2.5-1.2B-Thinking-heretic-IQ3_S.gguf` | GGUF IQ3_S | 0.52 GB |
| `LFM2.5-1.2B-Thinking-heretic-Q3_K_S.gguf` | GGUF Q3_K_S | 0.52 GB |
| `LFM2.5-1.2B-Thinking-heretic-Q3_K_M.gguf` | GGUF Q3_K_M | 0.56 GB |
| `LFM2.5-1.2B-Thinking-heretic-Q3_K_L.gguf` | GGUF Q3_K_L | 0.59 GB |
| `LFM2.5-1.2B-Thinking-heretic-IQ4_XS.gguf` | GGUF IQ4_XS | 0.62 GB |
| `LFM2.5-1.2B-Thinking-heretic-Q4_K_S.gguf` | GGUF Q4_K_S | 0.65 GB |
| `LFM2.5-1.2B-Thinking-heretic-Q4_0.gguf` | GGUF Q4_0 | 0.65 GB |
| `LFM2.5-1.2B-Thinking-heretic-Q4_1.gguf` | GGUF Q4_1 | 0.71 GB |
| `LFM2.5-1.2B-Thinking-heretic-Q4_K_M.gguf` | GGUF Q4_K_M | 0.68 GB |
| `LFM2.5-1.2B-Thinking-heretic-Q5_K_S.gguf` | GGUF Q5_K_S | 0.77 GB |
| `LFM2.5-1.2B-Thinking-heretic-Q5_K_M.gguf` | GGUF Q5_K_M | 0.79 GB |
| `LFM2.5-1.2B-Thinking-heretic-Q6_K.gguf` | GGUF Q6_K | 0.90 GB |
| `LFM2.5-1.2B-Thinking-heretic-Q8_0.gguf` | GGUF Q8_0 | 1.16 GB |

LFM2 dense architecture (`lfm2`) - loads natively in llama.cpp / LM Studio / Jan. Day-one upstream support,
so this also works with MLX, vLLM, SGLang, and Nexa-optimized NPU builds.

Run `llama serve -hf saidutta69/LFM2.5-1.2B-Thinking-heretic` to pull the default quant.

## Quickstart

```bash
# llama.cpp
llama serve -hf saidutta69/LFM2.5-1.2B-Thinking-heretic
```

```python
# transformers (requires transformers>=5.0.0)
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "saidutta69/LFM2.5-1.2B-Thinking-heretic"
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", dtype="bfloat16")
tokenizer = AutoTokenizer.from_pretrained(model_name)

messages = [{"role": "user", "content": "A train leaves at 14:05 travelling 80 km/h. A car leaves at 14:15 travelling 120 km/h on the same track. When does the car catch the train? Show your work."}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
out = model.generate(**inputs, do_sample=True, temperature=0.05, top_k=50, max_new_tokens=4096)
text = tokenizer.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)

# The model emits a <think>...</think> trace, then the answer. Strip it for display,
# but keep it in the message history on multi-turn so the model stays consistent.
answer = text.split("</think>")[-1].strip() if "</think>" in text else text
print(answer)
```

Also runnable via Ollama, LM Studio, Jan, vLLM, SGLang, and OpenVINO.

### Reasoning format

This is a thinking model. It writes its chain of thought between `<think>` and `</think>` before the final
answer. The chat template keeps the trace for the most recent assistant turn by default; pass
`preserve_thinking=True` to `apply_chat_template` to keep it across turns. Note that output can contain a
closing `</think>` with the opening tag supplied by the template, so strip on `</think>` rather than
assuming both tags are present.

### Generation parameters

Liquid's recommended settings for this reasoning model - a very low temperature with a top-k cut:

```python
model.generate(**inputs, temperature=0.05, top_k=50)
```

### Chat template

LFM2.5 uses a ChatML-like format. See the [Chat Template documentation](https://docs.liquid.ai/lfm/key-concepts/chat-template) for details.

```
<|startoftext|><|im_start|>system
You are a helpful assistant trained by Liquid AI.<|im_end|>
<|im_start|>user
What is C. elegans?<|im_end|>
<|im_start|>assistant
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
| **Parameters** | 1.17B |
| **Layers / heads** | 16 layers (10 double-gated conv + 6 GQA), 32 attention heads, 8 KV heads |
| **Hidden / intermediate** | 2048 / 12288 |
| **Convolution cache** | L_cache = 3 |
| **Position embedding** | RoPE, theta = 1,000,000 |
| **Context length** | 32,768 tokens |
| **Vocab** | 65,536 |
| **Precision** | bfloat16 |
| **Languages** | English, Arabic, Chinese, French, German, Japanese, Korean, Spanish |
| **Base model** | [LiquidAI/LFM2.5-1.2B-Thinking](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking) |

## Responsible use

Refusal suppression is deliberate and works as intended: this model will comply with requests the base model would refuse, including some it shouldn't. There is no safety filtering layered on top. You are responsible for how you deploy it — don't put this behind an unmoderated public-facing endpoint serving third parties. It inherits LFM2.5's factual limitations; abliteration removes refusal directions, it doesn't add capability or judgment.

## License

Inherits the [LFM License 1.0](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking/blob/main/LICENSE) from the base model.

## Related

- [LiquidAI/LFM2.5-1.2B-Thinking](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking) — the base model
- [saidutta69/LFM2.5-1.2B-Instruct-heretic](https://huggingface.co/saidutta69/LFM2.5-1.2B-Instruct-heretic) — the non-reasoning sibling
- [LFM2.5 technical report](https://arxiv.org/abs/2511.23404) — architecture and benchmarks
- [RACER IS OP — Heretic Models — full collection](https://huggingface.co/collections/saidutta69/racer-is-op-heretic-models)

## Abliteration hardware

Recorded in `reproduce/reproduce.json`:

- **GPU:** NVIDIA GeForce RTX 4090 (23.52 GB VRAM)
- **CPU:** AMD EPYC 7402 24-Core Processor
- **OS:** `Linux-6.8.0-146-generic-x86_64-with-glibc2.35`
- **CUDA / driver:** CUDA 13.0, driver 595.99.02
- **Software:** PyTorch 2.14.1+cu130, Heretic 1.4.0

Heretic notes that KL-divergence and refusal numbers can vary slightly with hardware and library versions.
