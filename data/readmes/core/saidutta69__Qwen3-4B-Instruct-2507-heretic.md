---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/LICENSE
library_name: transformers
pipeline_tag: text-generation
language:
- en
- zh
- ja
- ko
- de
- fr
- es
- pt
- ru
tags:
- qwen
- qwen3
- non-thinking
- instruct
- coding
- tool-use
- reasoning
- long-context
- heretic
- uncensored
- decensored
- abliterated
- reproducible
- gguf
- roleplay
- local-llm
- consumer-gpu
base_model: Qwen/Qwen3-4B-Instruct-2507
---

# Qwen3-4B-Instruct-2507-heretic

<div align="center">
  <img src="https://photu.kashyalabanavli.site/racer-is-op.png" alt="RACER IS OP" width="100%">
</div>

<br>

A decensored variant of [Qwen/Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507), produced with [Heretic](https://github.com/p-e-w/heretic) v1.4.0 (directional ablation / "abliteration"). The 2507 Instruct refresh of Qwen3-4B is the non-thinking edition — rebuilt for instruction following, tool use, and long-context work rather than reasoning traces — and refusal behaviour is suppressed here via targeted weight edits to the attention output and MLP down-projections rather than fine-tuning, so the 2507 tuning is left largely intact.

**Who this is for:** developers who want a fast 4B that just follows instructions, without the thinking overhead and without the refusals. Refusals drop from 100/100 to 3/100 — effectively total removal. Because it's the non-thinking edition it returns tokens directly, which makes it the better pick for tool-calling loops, structured extraction, and agent scaffolding where per-token latency matters. At 4B with 256K context it runs on CPU and low-VRAM GPUs via GGUF.

<!-- racer-gpu-matrix -->
## Runs on your gaming PC

Full GGUF ladder included - pick the quant that fits your card:

| Your GPU | Recommended quant | Weights |
| :--- | :--- | :--- |
| RTX 4090 / 5090 (24 GB) | Q8_0 | 3.99 GB |
| RTX 4080 / 5080 / 4060 Ti 16G (16 GB) | Q6_K | 3.08 GB |
| RTX 3060 / 4070 / 5070 (12 GB) | Q5_K_M | 2.69 GB |
| RTX 4060 / 3070 (8 GB) | Q4_K_M | 2.33 GB |
| GTX 1660 Super / 2060 / 3050 laptop (6 GB) | IQ4_XS | 2.16 GB |
| CPU-only / Apple Silicon | Q4_K_M | 2.33 GB |

Weights only, at this model's native 4.02B size; add ~1 GB per 32K of context.
OOM? Drop one quant level. Headroom to spare? Go one up.

## Abliteration parameters

Trial 172 of a 200-trial Heretic run (seed `2540954398`).

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | 19.46 |
| **attn.o_proj.max_weight** | 1.50 |
| **attn.o_proj.max_weight_position** | 29.11 |
| **attn.o_proj.min_weight** | 1.42 |
| **attn.o_proj.min_weight_distance** | 20.04 |
| **mlp.down_proj.max_weight** | 1.37 |
| **mlp.down_proj.max_weight_position** | 21.54 |
| **mlp.down_proj.min_weight** | 1.34 |
| **mlp.down_proj.min_weight_distance** | 10.08 |

## Performance

| Metric | This model | Original model ([Qwen/Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0958 | 0 *(by definition)* |
| **Refusals** | 3/100 | 100/100 |

Refusals on the harmful evaluation set drop from 100/100 to 3/100 — the base model refused
everything tested, and all but three of those are gone. KL divergence of 0.0958 is a
moderate-fidelity edit, so expect more drift in tone and formatting than a low-KL model in this
collection; the 2507 instruction-following and tool-use tuning survives intact. `direction_index`
is a single index (19.46) rather than per-layer, which is why the refusal removal lands this
completely without needing a wider edit.

## Why abliteration instead of fine-tuning

Fine-tuning a "helpful" persona on top of RLHF'd refusals fights the base model's training and tends to degrade coherence. Abliteration instead finds and edits the specific weight directions responsible for refusal, leaving the rest of the network (and its capabilities) untouched. See the [Heretic repo](https://github.com/p-e-w/heretic) and the [original abliteration writeup](https://huggingface.co/blog/mlabonne/abliteration) for the mechanism.

> Made with ❤️ by **RACER IS OP** — follow for more uncensored models

## Files

### Safetensors

| File | Size |
|---|---|
| `model-00001-of-00002.safetensors` | 4.65 GB |
| `model-00002-of-00002.safetensors` | 2.84 GB |

BF16, 4.02B parameters. The `reproduce/` directory carries the full Heretic recipe -
`config.toml`, `requirements.txt`, the Optuna study journal, and SHA-256 sums - so this exact
model can be regenerated bit-for-bit. Reproduce it with `heretic --reproduce reproduce/reproduce.json`.

### GGUF quantizations
Full quantization set (F16 + Q4_K_M, Q5_K_M, Q6_K, Q8_0) produced with [llama.cpp](https://github.com/ggml-org/llama.cpp).

| File | Format | Size |
|---|---|---|
| `Qwen3-4B-Instruct-2507-heretic-F16.gguf` | GGUF F16 | 7.50 GB |
| `Qwen3-4B-Instruct-2507-heretic-Q4_K_M.gguf` | GGUF Q4_K_M | 2.33 GB |
| `Qwen3-4B-Instruct-2507-heretic-Q5_K_M.gguf` | GGUF Q5_K_M | 2.69 GB |
| `Qwen3-4B-Instruct-2507-heretic-Q6_K.gguf` | GGUF Q6_K | 3.08 GB |
| `Qwen3-4B-Instruct-2507-heretic-Q8_0.gguf` | GGUF Q8_0 | 3.99 GB |

Qwen3 architecture (`qwen3`) - loads natively in llama.cpp / Ollama / LM Studio / Jan.

Run `llama serve -hf saidutta69/Qwen3-4B-Instruct-2507-heretic` to pull the default quant.

## Quickstart

```bash
# llama.cpp
llama serve -hf saidutta69/Qwen3-4B-Instruct-2507-heretic
```

```python
# transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "saidutta69/Qwen3-4B-Instruct-2507-heretic"
model = AutoModelForCausalLM.from_pretrained(model_name, dtype="auto", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)

messages = [{"role": "user", "content": "Write a Python function that parses an ISO-8601 duration string into seconds. Include type hints and three test cases."}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=True,
                                        return_dict=True, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=1024)
print(tokenizer.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

Also runnable via Ollama, LM Studio, Jan, vLLM, SGLang.

### Non-thinking by design

This is the Instruct edition, not the Thinking one — there is no `<think>` block to strip and no
reasoning mode to toggle. For hard problems that benefit from visible reasoning, use the
[Qwen3-4B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507) line instead; for
latency-sensitive agent loops, this one is the right pick.

### Tool use

Pass tool definitions straight through `apply_chat_template`. The 2507 refresh specifically
improved tool-usage accuracy, so the format is already well in-distribution.

## Model details

| | |
|---|---|
| **Architecture** | `Qwen3ForCausalLM` (decoder-only dense transformer) |
| **Parameters** | 4.02B |
| **Layers / heads** | 36 layers, 32 attention heads, 8 KV heads (GQA), head dim 128 |
| **Hidden / intermediate** | 2560 / 9728 (SwiGLU) |
| **Position embedding** | RoPE, theta = 5,000,000 |
| **Context length** | 262,144 |
| **Vocab** | 151,936 |
| **Precision** | bfloat16 |
| **Base model** | [Qwen/Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507) |

## What 2507 changed

The 2507 Instruct refresh rebuilt the non-thinking mode of Qwen3-4B: significant gains in
instruction following, logical reasoning, text comprehension, mathematics, science, coding and
tool usage; substantial long-tail multilingual coverage; better alignment to user preference on
subjective and open-ended tasks; and 256K long-context understanding.

## Responsible use

Refusal suppression is deliberate and works as intended: this model will comply with requests the base model would refuse, including some it shouldn't. There is no safety filtering layered on top. You are responsible for how you deploy it — don't put this behind an unmoderated public-facing endpoint serving third parties. It inherits Qwen3's factual limitations and biases; abliteration removes refusal directions, it doesn't add capability or judgment.

## License

Inherits the [`apache-2.0`](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/LICENSE) license from the base model.

## Related

- [Qwen/Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507) — the base model
- [saidutta69/Qwen3-VL-2B-Instruct-heretic](https://huggingface.co/saidutta69/Qwen3-VL-2B-Instruct-heretic) — the multimodal sibling at 2B
- [RACER IS OP — Heretic Models — full collection](https://huggingface.co/collections/saidutta69/racer-is-op-heretic-models)