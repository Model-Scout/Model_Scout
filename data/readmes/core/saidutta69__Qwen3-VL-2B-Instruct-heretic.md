---
license: apache-2.0
library_name: transformers
pipeline_tag: image-text-to-text
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
- qwen3-vl
- vision-language
- vlm
- multimodal
- image-text-to-text
- video
- ocr
- grounding
- agent
- heretic
- uncensored
- decensored
- abliterated
- reproducible
- gguf
- roleplay
- local-llm
- consumer-gpu
base_model: Qwen/Qwen3-VL-2B-Instruct
---

# Qwen3-VL-2B-Instruct-heretic

<div align="center">
  <img src="https://photu.kashyalabanavli.site/racer-is-op.png" alt="RACER IS OP" width="100%">
</div>

<br>

A decensored variant of [Qwen/Qwen3-VL-2B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct), produced with [Heretic](https://github.com/p-e-w/heretic) v1.4.0 (directional ablation / "abliteration"). Qwen3-VL is the vision-language branch of the Qwen3 family — image, video, and OCR input with spatial grounding — and refusal behaviour is suppressed here via targeted weight edits to the attention output and MLP down-projections rather than fine-tuning, so the vision tower and grounding behaviour are left largely intact.

**Who this is for:** developers who want uncensored vision-language understanding on hardware they already own. At 2B this is the smallest model in the collection that still sees images, and it answers directly instead of declining — refusals drop from 97/100 to 5/100. Best for local OCR, screenshot and document Q&A, UI-to-code from a reference image, and vision agents on CPU or a low-VRAM GPU. If you need text-only at this size, [Qwen2.5-3B-Instruct-heretic](https://huggingface.co/saidutta69/Qwen2.5-3B-Instruct-heretic) is the denser sibling.

<!-- racer-gpu-matrix -->
## Runs on your gaming PC

Full GGUF ladder included - pick the quant that fits your card:

| Your GPU | Recommended quant | Weights |
| :--- | :--- | :--- |
| RTX 4090 / 5090 (24 GB) | Q8_0 | 1.71 GB |
| RTX 4080 / 5080 / 4060 Ti 16G (16 GB) | Q6_K | 1.32 GB |
| RTX 3060 / 4070 / 5070 (12 GB) | Q5_K_M | 1.17 GB |
| RTX 4060 / 3070 (8 GB) | Q4_K_M | 1.03 GB |
| GTX 1660 Super / 2060 / 3050 laptop (6 GB) | IQ4_XS | 0.95 GB |
| CPU-only / Apple Silicon | Q4_K_M | 1.03 GB |

Weights only, at this model's native 2B size; add ~1 GB per 32K of context. Multimodal context
carries image tokens too, so budget more KV cache than a text-only model of the same size.
OOM? Drop one quant level. Headroom to spare? Go one up.

## Abliteration parameters

Trial 74 of a 200-trial Heretic run (seed `1736045380`). `direction_index` was selected per layer.

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | per layer |
| **attn.o_proj.max_weight** | 1.25 |
| **attn.o_proj.max_weight_position** | 26.80 |
| **attn.o_proj.min_weight** | 0.97 |
| **attn.o_proj.min_weight_distance** | 14.91 |
| **mlp.down_proj.max_weight** | 1.25 |
| **mlp.down_proj.max_weight_position** | 22.23 |
| **mlp.down_proj.min_weight** | 0.90 |
| **mlp.down_proj.min_weight_distance** | 6.95 |

## Performance

| Metric | This model | Original model ([Qwen/Qwen3-VL-2B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0528 | 0 *(by definition)* |
| **Refusals** | 5/100 | 97/100 |

KL divergence of 0.0528 with refusals at 5/100 is one of the stronger trade-offs in this batch:
the harmful evaluation set drops from 97/100 to 5/100 while the vision tower and grounding
behaviour stay close to the original. Small models concentrate refusal behaviour into fewer
directions, which is why a 2B edit can land this cleanly.

## Why abliteration instead of fine-tuning

Fine-tuning a "helpful" persona on top of RLHF'd refusals fights the base model's training and tends to degrade coherence. Abliteration instead finds and edits the specific weight directions responsible for refusal, leaving the rest of the network (and its capabilities) untouched. See the [Heretic repo](https://github.com/p-e-w/heretic) and the [original abliteration writeup](https://huggingface.co/blog/mlabonne/abliteration) for the mechanism.

> Made with ❤️ by **RACER IS OP** — follow for more uncensored models

## Files

### Safetensors

| File | Size |
|---|---|
| `model.safetensors` | 3.96 GB |

BF16, ~2B. The `reproduce/` directory carries the full Heretic recipe -
`config.toml`, `requirements.txt`, the Optuna study journal, and SHA-256 sums - so this exact
model can be regenerated bit-for-bit. Reproduce it with `heretic --reproduce reproduce/reproduce.json`.

### GGUF quantizations
Full quantization set (14 quants + F16) produced with [llama.cpp](https://github.com/ggml-org/llama.cpp).

| File | Format | Size |
|---|---|---|
| `Qwen3-VL-2B-Instruct-heretic-F16.gguf` | GGUF F16 | 3.21 GB |
| `Qwen3-VL-2B-Instruct-heretic-Q2_K.gguf` | GGUF Q2_K | 0.72 GB |
| `Qwen3-VL-2B-Instruct-heretic-IQ3_S.gguf` | GGUF IQ3_S | 0.81 GB |
| `Qwen3-VL-2B-Instruct-heretic-Q3_K_S.gguf` | GGUF Q3_K_S | 0.81 GB |
| `Qwen3-VL-2B-Instruct-heretic-Q3_K_M.gguf` | GGUF Q3_K_M | 0.88 GB |
| `Qwen3-VL-2B-Instruct-heretic-Q3_K_L.gguf` | GGUF Q3_K_L | 0.93 GB |
| `Qwen3-VL-2B-Instruct-heretic-IQ4_XS.gguf` | GGUF IQ4_XS | 0.95 GB |
| `Qwen3-VL-2B-Instruct-heretic-Q4_K_S.gguf` | GGUF Q4_K_S | 0.99 GB |
| `Qwen3-VL-2B-Instruct-heretic-Q4_0.gguf` | GGUF Q4_0 | 0.98 GB |
| `Qwen3-VL-2B-Instruct-heretic-Q4_1.gguf` | GGUF Q4_1 | 1.06 GB |
| `Qwen3-VL-2B-Instruct-heretic-Q4_K_M.gguf` | GGUF Q4_K_M | 1.03 GB |
| `Qwen3-VL-2B-Instruct-heretic-Q5_K_S.gguf` | GGUF Q5_K_S | 1.15 GB |
| `Qwen3-VL-2B-Instruct-heretic-Q5_K_M.gguf` | GGUF Q5_K_M | 1.17 GB |
| `Qwen3-VL-2B-Instruct-heretic-Q6_K.gguf` | GGUF Q6_K | 1.32 GB |
| `Qwen3-VL-2B-Instruct-heretic-Q8_0.gguf` | GGUF Q8_0 | 1.71 GB |

Qwen3-VL architecture (`qwen3vl`) with its vision encoder - loads natively in llama.cpp / LM Studio / Jan.

Run `llama serve -hf saidutta69/Qwen3-VL-2B-Instruct-heretic` to pull the default quant.

## Quickstart

```bash
# llama.cpp - the vision projector ships with the GGUF
llama serve -hf saidutta69/Qwen3-VL-2B-Instruct-heretic
```

```python
# transformers
from transformers import AutoProcessor, AutoModelForImageTextToText

model_name = "saidutta69/Qwen3-VL-2B-Instruct-heretic"
model = AutoModelForImageTextToText.from_pretrained(model_name, dtype="auto", device_map="auto")
processor = AutoProcessor.from_pretrained(model_name)

messages = [{"role": "user", "content": [
    {"type": "image", "image": "https://example.com/screenshot.png"},
    {"type": "text", "text": "Transcribe all text in this image and describe the layout."},
]}]
inputs = processor.apply_chat_template(messages, add_generation_prompt=True, tokenize=True,
                                        return_dict=True, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=1024)
print(processor.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

### Grounding and OCR

Qwen3-VL emits bounding boxes in a normalised coordinate space, so you can ask for element
positions directly and get coordinates back rather than prose descriptions:

```python
messages = [{"role": "user", "content": [
    {"type": "image", "image": "https://example.com/page.jpg"},
    {"type": "text", "text": "Give the bounding box of the submit button."},
]}]
```

This is the practical path for UI automation and for building training data from screenshots.

## Model details

| | |
|---|---|
| **Architecture** | `Qwen3VLForConditionalGeneration` (vision-language decoder) |
| **Parameters** | ~2B |
| **Layers / heads** | 28 layers, 16 attention heads, 8 KV heads, head dim 128 |
| **Hidden / intermediate** | 2048 / 6144 |
| **Position embedding** | mRoPE (interleaved, sections 24/20/20), theta = 5,000,000 |
| **Context length** | 262,144 |
| **Vocab** | 151,936 |
| **Precision** | bfloat16 |
| **Modalities** | Text and image/video in, text out |
| **Base model** | [Qwen/Qwen3-VL-2B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct) |

## About Qwen3-VL

Qwen3-VL is the vision-language branch of the Qwen series, available in dense and MoE sizes with
Instruct and Thinking editions. This generation brings deeper visual perception and reasoning,
extended context, stronger spatial and video understanding, and improved agent interaction — OCR,
grounding, and video temporal reasoning are the headline capabilities over the earlier Qwen2.5-VL.

## Responsible use

Refusal suppression is deliberate and works as intended: this model will comply with requests the base model would refuse, including some it shouldn't. There is no safety filtering layered on top. You are responsible for how you deploy it — don't put this behind an unmoderated public-facing endpoint serving third parties. It inherits Qwen3-VL's factual limitations and biases; abliteration removes refusal directions, it doesn't add capability or judgment.

## License

Inherits the [`apache-2.0`](https://www.apache.org/licenses/LICENSE-2.0) license from the base model.

## Related

- [Qwen/Qwen3-VL-2B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct) — the base model
- [saidutta69/gemma-4-E4B-it-heretic](https://huggingface.co/saidutta69/gemma-4-E4B-it-heretic) — the larger multimodal sibling in this collection
- [RACER IS OP — Heretic Models — full collection](https://huggingface.co/collections/saidutta69/racer-is-op-heretic-models)

## Abliteration hardware

Recorded in `reproduce/reproduce.json`:

- **GPU:** NVIDIA GeForce RTX 4090 (23.51 GB VRAM)
- **CPU:** AMD Ryzen 9 5950X 16-Core Processor
- **OS:** `Linux-7.0.0-31-generic-x86_64-with-glibc2.35`
- **CUDA / driver:** CUDA 13.0, driver 595.84
- **Software:** PyTorch 2.14.1+cu130, Heretic 1.4.0

Heretic notes that KL-divergence and refusal numbers can vary slightly with hardware and library versions.
