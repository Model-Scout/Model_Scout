---
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-2.6B/blob/main/LICENSE
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
- vi
- th
- id
- hi
- ru
- pl
tags:
- liquid
- lfm2
- lfm2.5
- edge
- on-device
- agentic
- tool-calling
- heretic
- uncensored
- decensored
- abliterated
- ara
- reproducible
- gguf
- local-llm
base_model: LiquidAI/LFM2.5-2.6B
---

# LFM2.5-2.6B-heretic

<div align="center">
  <img src="https://photu.kashyalabanavli.site/racer-is-op.png" alt="RACER IS OP" width="100%">
</div>

<br>

A decensored variant of [LiquidAI/LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B), produced with
[Heretic](https://github.com/p-e-w/heretic) **2.0.0.dev0** using **Arbitrary-Rank Ablation (ARA)**.
LFM2.5-2.6B is Liquid's on-device agentic model: 30 layers laid out as 22 double-gated short
convolution blocks plus 8 GQA layers, a 131K context, and a native tool-call format. ARA edits the
language model over layers 1-21; everything else is unchanged.

**Who this is for:** local agents, tool use, RAG and structured extraction where a 2.7B model
should run on a phone or a small laptop. Liquid's published numbers include BFCLv4 56.88,
ToolSandbox 77.83, IFBench 59.17 and IFStruct 85.49, and it is not recommended for agentic coding
or knowledge-heavy work at this size. This checkpoint is not the Fable5 coding-agent fine-tune
([`lfm2.5-2.6b-fable5-coding-agent-heretic`](https://huggingface.co/saidutta69/lfm2.5-2.6b-fable5-coding-agent-heretic));
it is the base 2.6B instruct model with refusals removed.

Refusals drop from **96/100 to 8/100** at a **KL divergence of 0.0059** - a tight edit.

## Arbitrary-Rank Ablation parameters

Trial 190 of a 250-trial Heretic 2.0 ARA run (seed `712709786`).

| Parameter | Value |
| :-------- | :---: |
| **start_layer_index** | 1 |
| **end_layer_index** | 21 |
| **preserve_good_behavior_weight** | 0.9588 |
| **steer_bad_behavior_weight** | 0.0009 |
| **overcorrect_relative_weight** | 0.0151 |
| **neighbor_count** | 6 |

## Performance

| Metric | This model | Original model ([LiquidAI/LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)) |
| :----- | :--------: | :---------------------------: |
| **Refusals** | 8/100 | 96/100 |
| **KL divergence** | 0.0059 | 0 *(by definition)* |

88 of the 96 refusals clear. KL 0.0059 is a tight edit, so expect little drift in phrasing, tool
format or multilingual behaviour.

### Base model benchmarks

Liquid's published numbers for LFM2.5-2.6B, not re-run here:

| Benchmark | LFM2.5-2.6B |
| :-------- | :--------: |
| BFCLv4 | 56.88 |
| ToolSandbox | 77.83 |
| IFBench | 59.17 |
| IFStruct | 85.49 |
| Multi-IF | 80.07 |
| AIME25 | 51.87 |
| LiveCodeBench v6 | 59.41 |
| Claw-Eval average (EN) | 62.85 |
| BrowseComp+ (OpenClaw) | 26.89 |

Abliteration removes refusal directions; it does not add capability. Treat these as the base
model's numbers, not a re-measurement of this checkpoint.

## Why ARA instead of directional ablation

Directional ablation finds one refusal direction and orthogonalizes attention/MLP outputs against
it. ARA learns a low-rank subspace over a layer range and blends a "preserve good behaviour" and
"steer bad behaviour" objective. Here it kept 96% of the preserve objective over layers 1-21 and
still removed 88 of 96 refusals. See the [Heretic repo](https://github.com/p-e-w/heretic).

## Files

### Safetensors

| File | Size |
|---|---|
| `model-00001-of-00002.safetensors` | 2.70 GB |
| `model-00002-of-00002.safetensors` | 2.70 GB |

BF16, 2,697,198,592 parameters (2.69B). The `reproduce/` directory carries the full Heretic 2.0
recipe - `config.toml`, `requirements.txt`, the Optuna study journal, and SHA-256 sums.

### GGUF quantizations

Full quantization set (F16 + 14 quants, 28.94 GB total), produced with
[llama.cpp](https://github.com/ggml-org/llama.cpp) master on 2026-10-28.

| File | Format | Size |
|---|---|---|
| `LFM2.5-2.6B-heretic-F16.gguf` | GGUF F16 | 5.40 GB |
| `LFM2.5-2.6B-heretic-Q2_K.gguf` | GGUF Q2_K | 1.09 GB |
| `LFM2.5-2.6B-heretic-IQ3_S.gguf` | GGUF IQ3_S | 1.27 GB |
| `LFM2.5-2.6B-heretic-Q3_K_S.gguf` | GGUF Q3_K_S | 1.27 GB |
| `LFM2.5-2.6B-heretic-Q3_K_M.gguf` | GGUF Q3_K_M | 1.37 GB |
| `LFM2.5-2.6B-heretic-Q3_K_L.gguf` | GGUF Q3_K_L | 1.45 GB |
| `LFM2.5-2.6B-heretic-IQ4_XS.gguf` | GGUF IQ4_XS | 1.53 GB |
| `LFM2.5-2.6B-heretic-Q4_K_S.gguf` | GGUF Q4_K_S | 1.60 GB |
| `LFM2.5-2.6B-heretic-Q4_0.gguf` | GGUF Q4_0 | 1.59 GB |
| `LFM2.5-2.6B-heretic-Q4_1.gguf` | GGUF Q4_1 | 1.75 GB |
| `LFM2.5-2.6B-heretic-Q4_K_M.gguf` | GGUF Q4_K_M | 1.67 GB |
| `LFM2.5-2.6B-heretic-Q5_K_S.gguf` | GGUF Q5_K_S | 1.90 GB |
| `LFM2.5-2.6B-heretic-Q5_K_M.gguf` | GGUF Q5_K_M | 1.94 GB |
| `LFM2.5-2.6B-heretic-Q6_K.gguf` | GGUF Q6_K | 2.22 GB |
| `LFM2.5-2.6B-heretic-Q8_0.gguf` | GGUF Q8_0 | 2.87 GB |

Text GGUF: arch `lfm2`, 266 tensors, 30 blocks (22 convolution + 8 full attention), 131,072
context, 128,000 vocab, tied embeddings, conv cache `L_cache=3`, rope theta 1e6.

## Quickstart

```bash
# llama.cpp
llama serve -hf saidutta69/LFM2.5-2.6B-heretic
```

```python
# transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "saidutta69/LFM2.5-2.6B-heretic"
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", dtype="bfloat16")
tokenizer = AutoTokenizer.from_pretrained(model_name)

messages = [{"role": "user", "content": "Explain how a heat pump works."}]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)
out = model.generate(**inputs, do_sample=True, temperature=0.1, top_k=50,
                     repetition_penalty=1.1, max_new_tokens=1024)
print(tokenizer.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

### Generation parameters

Liquid's recommended settings: `temperature=0.1, top_k=50, repetition_penalty=1.1`.

### Chat template and tools

LFM2.5 uses ChatML-style tags and Liquid's native tool-call format. Pass tool schemas with
`tools=...` to `apply_chat_template()` and feed results back under a `tool` role; see the
[base card](https://huggingface.co/LiquidAI/LFM2.5-2.6B) for the exact format.

## Runs anywhere

| Device | Recommended quant | Weights |
| :--- | :--- | :--- |
| Phone / browser (4 GB RAM) | Q4_K_M | 1.67 GB |
| Raspberry Pi 5 (8 GB) | Q4_K_M | 1.67 GB |
| Laptop (8 GB, Apple Silicon) | Q8_0 | 2.87 GB |
| RTX 3060 / 4060 (8-12 GB) | Q6_K | 2.22 GB |
| Server / multi-tenant | Q5_K_M | 1.94 GB |

Weights only. Liquid measures about 30 tok/s on a phone with the 2.6B model, and the hybrid stack
spends 22 of its 30 layers in cheap convolution blocks, so decode is bandwidth-bound.

## Model details

| | |
|---|---|
| **Architecture** | `Lfm2ForCausalLM` (hybrid conv + GQA) |
| **Parameters** | 2.69B |
| **Layers** | 30: 22 double-gated short convolution + 8 GQA |
| **Attention** | 32 heads / 8 KV heads, head dim 64 |
| **Hidden / intermediate** | 2048 / 10752 |
| **Convolution cache** | L_cache = 3 |
| **Position embedding** | RoPE, theta 10,000,000 |
| **Context length** | 131,072 |
| **Vocab** | 128,000 |
| **Precision** | bfloat16 |
| **Languages** | English, Arabic, Chinese, French, German, Italian, Japanese, Korean, Portuguese, Spanish, Vietnamese, Thai, Indonesian, Hindi, Russian, Polish |
| **Base model** | [LiquidAI/LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B) |

## FAQ

### What is LFM2.5-2.6B-heretic?

`LFM2.5-2.6B-heretic` is a decensored build of [`LiquidAI/LFM2.5-2.6B`](https://huggingface.co/LiquidAI/LFM2.5-2.6B) produced with Heretic 2.0.0.dev0 (Arbitrary-Rank Ablation). It is the same weights with the refusal direction removed, not a new fine-tune, so its capabilities track the base model.

### Is LFM2.5-2.6B-heretic actually uncensored?

Yes. On Heretic's 100-prompt refusal harness it drops from 96/100 to 8/100 at KL divergence 0.0059 from the base model. These are measured values, not a claim; reproduction data is in [`reproduce/`](reproduce/).

### How do I run LFM2.5-2.6B-heretic locally?

`llama serve -hf saidutta69/LFM2.5-2.6B-heretic:Q4_K_M` pulls the default quant; the repo ships 15 GGUF quants (see Files).

## Responsible use

Refusal suppression is deliberate and works as intended: this model will comply with requests the
base model would refuse, including some it should not. There is no safety filtering layered on top.
You are responsible for how you deploy it - don't put this behind an unmoderated public-facing
endpoint serving third parties. It inherits LFM2.5-2.6B's factual limitations; abliteration removes
refusal directions, it does not add capability or judgment.

> Made with ❤️ by **RACER IS OP (saidutta69)** - follow for more uncensored models

## License

Inherits the [LFM Open License v1.0](https://huggingface.co/LiquidAI/LFM2.5-2.6B/blob/main/LICENSE) from the base
model. This is **not** Apache-2.0; review the LFM terms before commercial use.

## Related

- [LiquidAI/LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B) - the base agentic model
- [LFM2.5 collection](https://huggingface.co/collections/LiquidAI/lfm25)
- [lfm2.5-2.6b-fable5-coding-agent-heretic](https://huggingface.co/saidutta69/lfm2.5-2.6b-fable5-coding-agent-heretic) - the separate Fable5 coding-agent fine-tune
- [RACER IS OP - Heretic Models - full collection](https://huggingface.co/collections/saidutta69/racer-is-op-heretic-models)

## Abliteration hardware

Recorded in `reproduce/reproduce.json`:

- **GPU:** NVIDIA RTX PRO 6000 Blackwell Server Edition (94.97 GB VRAM)
- **OS:** `Linux-4.19.0-gvisor-x86_64-with-glibc2.41`
- **CUDA / driver:** CUDA 13.0, driver 595.71.05
- **Software:** PyTorch 2.14.1+cu130, Heretic 2.0.0.dev0

Heretic notes that KL-divergence and refusal numbers can vary slightly with hardware and library versions.
