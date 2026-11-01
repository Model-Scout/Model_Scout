---
license: other
license_name: mrl
license_link: https://mistral.ai/licenses/MRL-0.1.md
library_name: transformers
pipeline_tag: text-generation
language:
- en
- fr
- de
- es
- it
- pt
- zh
- ja
- ru
- ko
tags:
- mistral
- ministral
- text-generation
- function-calling
- multilingual
- uncensored
- decensored
- heretic
- abliterated
- reproducible
- gguf
- roleplay
- local-llm
- consumer-gpu
- research-only
base_model: mistralai/Ministral-8B-Instruct-2410
---

# Ministral-8B-Instruct-heretic

<div align="center">
  <img src="https://photu.kashyalabanavli.site/racer-is-op.png" alt="RACER IS OP" width="100%">
</div>

<br>

A decensored variant of [mistralai/Ministral-8B-Instruct-2410](https://huggingface.co/mistralai/Ministral-8B-Instruct-2410), produced with [Heretic](https://github.com/p-e-w/heretic) v1.4.0 (directional ablation / "abliteration"). Refusal behaviour is suppressed via targeted weight edits to the attention output and MLP down-projections rather than fine-tuning, so the multilingual ability, the code and math scores, and function calling are left intact.

> [!CAUTION]
> **Research use only.** The base model is released under the
> [Mistral AI Research License](https://mistral.ai/licenses/MRL-0.1.md), **not Apache-2.0**. Section 3.2 restricts use of the
> model, any derivative, and any output to "Research Purposes", which the license defines as
> personal, scientific or academic research **and** non-profit, non-commercial work. It
> explicitly excludes use by company employees in the course of their daily tasks, anything
> intended to generate revenue, and distribution by a commercial entity including free hosted
> or managed services. Section 2.3 does permit redistributing derivatives under other terms, but
> only if you carry the modification notice reproduced in the [License](#license) section below.
> If you need this commercially, go to [mistral.ai/contact](https://mistral.ai/contact/) first.

> [!NOTE]
> **The GGUF is 32K context, not the 128K the base card advertises, and it runs every layer as
> full attention.** No weights are lost - the F16 GGUF holds all 8,019,808,256 parameters, an exact
> match to the checkpoint - but two things do not survive the conversion. First,
> `max_position_embeddings` in the config is 32,768, so that is what llama.cpp gets. Second,
> Ministral's ragged interleaved sliding-window pattern (128k, 32k, 32k, 32k across 9 full and 27
> sliding layers) is not written into the GGUF, because llama.cpp's `LlamaModel` converter emits
> no sliding-window key at all. The practical effect: correct output, but a larger KV cache per
> token than Mistral's design intends. At 32K that is a non-issue; if you were planning to run
> this at 128K in llama.cpp on a 24 GB card, it will not fit the way the base card implies.
> The HF safetensors plus `mistral_common` remain the path for the full 128K window.

**Who this is for:** people who want a strong multilingual 8B that answers instead of declining, on hardware they already own. This is the best abliteration result recorded in this collection: refusals drop from 91/100 to **3/100** while KL divergence stays at **0.0149**, so the edit removed almost all of the refusal behaviour without meaningfully moving the model. Ministral 8B Instruct is genuinely good at code and function calling for its size (HumanEval 76.8, Math maj@1 54.5, internal function-calling bench 31.6) and covers ten languages. Best for local coding assistants, multilingual chat, and tool-calling agents on a single 24 GB card or on CPU at reduced quant.

<!-- racer-gpu-matrix -->
## Runs on your gaming PC

Full default quant set included - pick the quant that fits your card:

| Your GPU | Recommended quant | Weights |
| :--- | :--- | :--- |
| RTX 4090 / 5090 (24 GB) | Q8_0 | 8.53 GB |
| RTX 4080 / 5080 / 4060 Ti 16G (16 GB) | Q6_K | 6.59 GB |
| RTX 3060 / 4070 / 5070 (12 GB) | Q5_K_M | 5.72 GB |
| RTX 4060 / 3070 (8 GB) | Q4_K_M | 4.91 GB |
| GTX 1660 Super / 3060 8G / Apple Silicon | Q4_K_M | 4.91 GB |
| CPU-only | Q4_K_M | 4.91 GB |

Weights only, at this model's native 8B size; add ~1 GB per 8K of context at 32K context length.
OOM? Drop to Q4_K_M, or Q4_0 if you still do not fit. Headroom to spare? Go one up. Every layer
runs full attention here (see the note above), so the KV cache is a little heavier than Mistral's
own sliding-window design would imply - budget for that at long context.

## Abliteration parameters

Trial `trial_id` 181 of a 200-trial Heretic run (seed `3207215569`). Like MiniCPM-V 4.7 1B and
unlike most models in this collection, this run used a single refusal direction for the whole
network, so `direction_index` is a single value rather than one per layer.

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | 17.18 |
| **attn.o_proj.max_weight** | 1.12 |
| **attn.o_proj.max_weight_position** | 23.49 |
| **attn.o_proj.min_weight** | 1.00 |
| **attn.o_proj.min_weight_distance** | 19.24 |
| **mlp.down_proj.max_weight** | 1.16 |
| **mlp.down_proj.max_weight_position** | 23.41 |
| **mlp.down_proj.min_weight** | 1.01 |
| **mlp.down_proj.min_weight_distance** | 18.58 |

## Performance

| Metric | This model | Original model ([mistralai/Ministral-8B-Instruct-2410](https://huggingface.co/mistralai/Ministral-8B-Instruct-2410)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0149 | 0 *(by definition)* |
| **Refusals** | 3/100 | 91/100 |

These two numbers only mean anything read together, and this is a strong pairing. KL 0.0149 puts
it in the tight group in this collection - tighter than
[granite-4.1-3b-heretic](https://huggingface.co/saidutta69/granite-4.1-3b-heretic) (0.0852),
[Qwen3-VL-2B-Instruct-heretic](https://huggingface.co/saidutta69/Qwen3-VL-2B-Instruct-heretic)
(0.0528) and [Qwen2.5-VL-3B-Instruct-heretic](https://huggingface.co/saidutta69/Qwen2.5-VL-3B-Instruct-heretic)
(0.0178), looser than [granite-4.2-3b-heretic](https://huggingface.co/saidutta69/granite-4.2-3b-heretic)
(0.0095) - and it is on an 8B, which is a larger model to keep faithful than any of those.
Refusals at 3/100 is essentially the floor; a handful of models here reach 2/100.

For contrast, [FrogNano-4B-heretic](https://huggingface.co/saidutta69/FrogNano-4B-heretic) from the
same day posted a tighter KL of 0.0046 and only got refusals down to 71/100 - a timid edit that
preserved behaviour and preserved most refusals with it. Low KL is not a quality signal on its
own, and these two are the counter-examples in opposite directions.

The base starts at 91/100, so this edit is working against a heavily aligned model and still
clears 88 of them. That combination - the highest starting refusal count in the collection, a
near-floor result, and a tight KL on an 8B - is why this card does not need the "be faithful to
the base" hedge that weaker ablations get.

## Base model benchmarks

These are the base model's own numbers, measured by Mistral, on the un-abliterated checkpoint.
Abliteration is a weight edit, not a retrain, so expect these to hold approximately - but the
refusal behaviour below them is gone.

**Instruct models** (gpt-4o judge for the chat column)

| Model | MTBench | Arena Hard | WildBench | MBPP pass@1 | HumanEval pass@1 | Math maj@1 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Ministral 8B Instruct** | **8.3** | **70.9** | 41.3 | **70.0** | **76.8** | **54.5** |
| Mistral 7B Instruct v0.3 | 6.7 | 44.3 | 33.1 | 50.2 | 38.4 | 13.2 |
| Llama 3.1 8B Instruct | 7.5 | 62.4 | 37.0 | 69.7 | 67.1 | 49.3 |

**Function calling**, Mistral's internal bench: Ministral 8B Instruct **31.6**, Ministral 3B
Instruct 28.4, Mistral 7B Instruct v0.3 6.9. Llama 3.1 8B and Gemma 2 9B were not evaluated.
This is the standout number in the whole card - it is roughly four times the previous Mistral 7B
generation on tool use, which is the main reason to pick this checkpoint over a bigger general
model.

**Base (non-instruct) models**, for reference on the underlying knowledge

| Model | MMLU | AGIEval | Winogrande | Arc-c | TriviaQA | GSM8K maj@8 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Ministral 8B Base** | **65.0** | **48.3** | **75.3** | **71.9** | **65.5** | **64.5** |
| Llama 3.1 8B Base | 64.7 | 44.4 | 74.6 | 46.0 | 60.2 | 42.2 |
| Mistral 7B Base | 62.5 | 42.5 | 74.2 | 67.9 | 62.5 | 32.0 |

Multilingual MMLU for Ministral 8B Base: French 57.5, German 57.4, Spanish 59.6 - all well
ahead of the Llama 3.1 8B and Mistral 7B baselines.

## Why abliteration instead of fine-tuning

Fine-tuning a "helpful" persona on top of RLHF'd refusals fights the base model's training and tends to degrade coherence. Abliteration instead finds and edits the specific weight directions responsible for refusal, leaving the rest of the network (and its capabilities) untouched. See the [Heretic repo](https://github.com/p-e-w/heretic) and the [original abliteration writeup](https://huggingface.co/blog/mlabonne/abliteration) for the mechanism.

> Made with ❤️ by **RACER IS OP** — follow for more uncensored models

## Files

### Safetensors

| File | Size |
|---|---|
| `model-00001-of-00004.safetensors` … `model-00004-of-00004.safetensors` | 16.04 GB total |

BF16, 8.02B across 4 shards, 327 tensors. The `reproduce/` directory carries the full
Heretic recipe - `config.toml`, `requirements.txt`, the Optuna study journal, and SHA-256 sums -
so this exact model can be regenerated bit-for-bit with
`heretic --reproduce reproduce/reproduce.json`.

### GGUF quantizations
Default quant set (4 quants + F16) produced with [llama.cpp](https://github.com/ggml-org/llama.cpp).

| File | Format | Size |
|---|---|---|
| `Ministral-8B-Instruct-heretic-F16.gguf` | GGUF F16 | 16.05 GB |
| `Ministral-8B-Instruct-heretic-Q4_K_M.gguf` | GGUF Q4_K_M | 4.91 GB |
| `Ministral-8B-Instruct-heretic-Q5_K_M.gguf` | GGUF Q5_K_M | 5.72 GB |
| `Ministral-8B-Instruct-heretic-Q6_K.gguf` | GGUF Q6_K | 6.59 GB |
| `Ministral-8B-Instruct-heretic-Q8_0.gguf` | GGUF Q8_0 | 8.53 GB |

Total GGUF payload: 41.80 GB across 5 files.

Arch `llama`, 327 tensors, 36 blocks - an exact match to the
safetensors, so nothing is dropped in conversion. Note that `config.json` declares
`architectures: ["MinistralForCausalLM"]`, which llama.cpp does not register; the F16 was built
after rewriting that one field to `MistralForCausalLM` in a local copy of the config. The
checkpoint is a plain llama-architecture dense model underneath, so the rewrite is a rename and
nothing else - and this repo's own `config.json` on the Hub is untouched.

Run `llama-cli -hf saidutta69/Ministral-8B-Instruct-heretic` to pull the default quant.

## Quickstart

```bash
llama-cli -hf saidutta69/Ministral-8B-Instruct-heretic:Q5_K_M -ngl 99 -c 32768
```

```python
# transformers
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "saidutta69/Ministral-8B-Instruct-heretic"
tok = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, dtype="auto", device_map="auto")

messages = [{"role": "user", "content": "Write a Rust function that parses TOML."}]
inputs = tok.apply_chat_template(messages, add_generation_prompt=True,
                                 return_tensors="pt", return_dict=True).to(model.device)
out = model.generate(**inputs, max_new_tokens=512, do_sample=True,
                     temperature=0.6, top_p=0.95, repetition_penalty=1.0)
print(tok.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

```python
# function calling - the template emits [TOOL_CALLS] and expects [TOOL_RESULTS] back
messages = [{"role": "user", "content": "What is the weather in Paris?"}, {"role": "assistant",
    "content": "", "tool_calls": [{"tool_name": "get_weather",
        "tool_arguments": {"location": "Paris"}, "tool_call_id": "abc123456"}]}]
```

Two details if you wire tools up yourself: the chat template raises unless `tool_call_id` is an
alphanumeric string of **exactly 9 characters**, and there is no thinking mode in this template -
it is a plain instruct model, so there is no `enable_thinking` parameter and no `<think>` block
to strip.

## Model details

| | |
|---|---|
| **Architecture** | `MinistralForCausalLM` - dense transformer, GGUF arch `llama` |
| **Parameters** | 8,019,808,256 (8.02B) |
| **Layers** | 36 |
| **Attention pattern** | Ragged interleaved sliding-window, 9 full + 27 sliding (128k / 32k / 32k / 32k). **Not expressed in the GGUF** - see the note at the top. |
| **Heads** | 32 attention heads, 8 KV heads (GQA), head dim 128 |
| **Hidden / intermediate** | 4096 / 12288 |
| **Position embedding** | RoPE, theta = 100,000,000, 128 dims |
| **Context length** | 32,768 in GGUF. The base model was trained with a 128k window; see the note at the top. |
| **Vocab** | 131,072 |
| **Embeddings** | untied |
| **Precision** | bfloat16 |
| **Modalities** | Text in, text out |
| **Languages** | en, fr, de, es, it, pt, zh, ja, ru, ko |
| **Base model** | [mistralai/Ministral-8B-Instruct-2410](https://huggingface.co/mistralai/Ministral-8B-Instruct-2410) (commit `2f494a19`) |

## About Ministral 8B

Ministral is Mistral AI's "les Ministraux" line, released October 2024 as an on-device and
edge-focused pair (3B and 8B). The 8B is a dense transformer deliberately designed for the
performance-per-watt envelope: interleaved sliding-window attention gives long effective context
at a fraction of the KV cache cost, and it was trained on a large proportion of multilingual and
code data. It ships as `mistral-common` format upstream (V3-Tekken tokenizer); this repo carries
the equivalent HF `tokenizer.json` and `chat_template.jinja`, which is what llama.cpp and
transformers consume. Mistral's own recommendation for serving it is
[vLLM](https://github.com/vllm-project/vllm), capped at 32k context there until paged-attention
kernels for interleaved attention land.

## Responsible use

Refusal suppression is deliberate and works as intended: this model will comply with requests the base model would refuse, including some it shouldn't. There is no safety filtering layered on top. You are responsible for how you deploy it — don't put this behind an unmoderated public-facing endpoint serving third parties, and note that doing so commercially would also breach the base model's license. It inherits Ministral 8B's factual limitations and biases; abliteration removes refusal directions, it doesn't add capability or judgment.

## License

**This is not Apache-2.0.** The base model [mistralai/Ministral-8B-Instruct-2410](https://huggingface.co/mistralai/Ministral-8B-Instruct-2410) is released
under the [Mistral AI Research License, version 0.1](https://mistral.ai/licenses/MRL-0.1.md), and so is this derivative.

**Required notice, from MRL §2.3:**

> This model was modified from `mistralai/Ministral-8B-Instruct-2410`. It has been modified by
> RACER IS OP using abliteration (directional ablation) to remove refusal behaviour. It is not an
> official Mistral AI product and is not endorsed, approved or validated by Mistral AI.

What the license actually allows, in short:

- **§2.3** - you may distribute derivatives under additional or different terms, provided you
  include the notice above and state that you modified the model. The MRL still governs use and
  modification.
- **§3.1** - you may not imply the model is an official Mistral AI product or is endorsed by them.
- **§3.2** - use is limited to **Research Purposes**: personal, scientific or academic research,
  and non-profit and non-commercial. That definition explicitly rules out use by employees of a
  company in the course of their daily tasks, any activity intended to generate revenue, and
  distribution by a commercial entity, paid or free, including hosted or managed services.
- **§8** - governed by French law, courts of Paris have exclusive jurisdiction.

Mistral sells a commercial license; see [mistral.ai/contact](https://mistral.ai/contact/).

## Related

- [mistralai/Ministral-8B-Instruct-2410](https://huggingface.co/mistralai/Ministral-8B-Instruct-2410) — the base model
- [saidutta69/FrogNano-4B-heretic](https://huggingface.co/saidutta69/FrogNano-4B-heretic) — the same-day contrast case: tighter KL, far worse refusal suppression
- [saidutta69/Qwen3-4B-Thinking-heretic](https://huggingface.co/saidutta69/Qwen3-4B-Thinking-heretic) — the tightest-KL edit in the collection, Apache-2.0, 4B

## Abliteration hardware

Recorded in `reproduce/reproduce.json`:

- **GPU:** NVIDIA RTX A6000 (44.42 GB VRAM)
- **CPU:** 11th Gen Intel(R) Core(TM) i7-11700K @ 3.60GHz
- **OS:** `Linux-6.8.0-85-generic-x86_64-with-glibc2.35`
- **CUDA / driver:** CUDA 13.0, driver 580.178.04
- **Software:** PyTorch 2.14.1+cu130, Heretic 1.4.0

Heretic notes that KL-divergence and refusal numbers can vary slightly with hardware and library versions.
