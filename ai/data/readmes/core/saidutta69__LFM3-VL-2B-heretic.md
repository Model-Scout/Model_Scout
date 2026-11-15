---
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM3-VL-2B/blob/main/LICENSE
library_name: transformers
pipeline_tag: image-text-to-text
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
- lfm3
- lfm3-vl
- vision-language
- vlm
- multimodal
- image-text-to-text
- edge
- on-device
- ocr
- document
- video
- heretic
- uncensored
- decensored
- abliterated
- reproducible
- gguf
- local-llm
base_model: LiquidAI/LFM3-VL-2B
---

# LFM3-VL-2B-heretic

<div align="center">
  <img src="https://photu.kashyalabanavli.site/racer-is-op.png" alt="RACER IS OP" width="100%">
</div>

<br>

A decensored variant of [LiquidAI/LFM3-VL-2B](https://huggingface.co/LiquidAI/LFM3-VL-2B), produced with
[Heretic](https://github.com/p-e-w/heretic) v1.4.0 (directional ablation / "abliteration").
Only the **language model** is edited: refusal directions are removed from the text tower's
attention output projections (including the convolution operator's `out_proj` on conv layers) and
MLP down-projections. The 164M vision encoder and 25M projector are copied into the GGUF unchanged,
so image understanding survives quantization.

> [!IMPORTANT]
> **The GGUF is fully multimodal - text *and* vision.** The vision tower ships separately as
> `LFM3-VL-2B-heretic-mmproj-F16.gguf` (0.38 GB); the two files together are the model. For image input you **must**
> load both - see [Quickstart](#quickstart). Text-only use needs only the main GGUF. Nothing is
> dropped from the text path: the text GGUF carries the full language tower (287 tensors, 24
> blocks), and the mmproj carries 189,380,352 vision+projector parameters.
>
> llama.cpp video input for LFM3-VL is not supported upstream yet; image input is tested and works.
> Video works through the transformers checkpoint.

**Who this is for:** on-device document, chart, screenshot and video work that should not need a
data centre. LFM3-VL-2B is Liquid's post-trained 1.92B vision model, and its published numbers
include DocVQA 96.7, TextVQA 87.9, OCRBench v1 86.3, RealWorldQA 79.3 and MMMU 55.7. It is not
recommended for coding, multi-turn conversations, or complex reasoning; abliteration removes
refusals, not those limits.

Refusals drop from **98/100 to 3/100** at a **KL divergence of 0.0014** - a very tight text edit.

## Abliteration parameters

Trial 94 of a 200-trial Heretic run (seed `1424362134`).

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | 14.32 |
| **attn.o_proj.max_weight** | 1.41 |
| **attn.o_proj.max_weight_position** | 13.92 |
| **attn.o_proj.min_weight** | 0.95 |
| **attn.o_proj.min_weight_distance** | 10.15 |
| **mlp.down_proj.max_weight** | 1.48 |
| **mlp.down_proj.max_weight_position** | 21.08 |
| **mlp.down_proj.min_weight** | 1.41 |
| **mlp.down_proj.min_weight_distance** | 10.47 |

## Performance

| Metric | This model | Original model ([LiquidAI/LFM3-VL-2B](https://huggingface.co/LiquidAI/LFM3-VL-2B)) |
| :----- | :--------: | :---------------------------: |
| **KL divergence** | 0.0014 | 0 *(by definition)* |
| **Refusals** | 3/100 | 98/100 |

95 of the 98 refusals clear, and the edit is tight (KL 0.0014). The base was almost fully
refusal-tuned on Heretic's harmful evaluation set.

### MMLU (text only)

Measured on this checkpoint and on the original model in the same environment
(`lm-eval` 0.4.13, 14,042 questions):

| Metric | This model | Original model |
| :----- | :--------: | :------------: |
| **MMLU (acc)** | 34.44% | 34.37% |
| **stderr** | 0.40 pp | 0.40 pp |

The +0.07 pp difference is far inside one standard error. MMLU exercises the text path only; it
does **not** measure the vision encoder. Vision weights are unchanged from the base model, and the
image smoke test in the pipeline checks that the projector still pairs correctly.

## Why abliteration instead of fine-tuning

Fine-tuning a "helpful" persona on top of RLHF'd refusals fights the base model's training and
tends to degrade coherence. Abliteration instead finds and edits the specific weight directions
responsible for refusal, leaving the rest of the network (and its capabilities) untouched. See the
[Heretic repo](https://github.com/p-e-w/heretic) and the
[original abliteration writeup](https://huggingface.co/blog/mlabonne/abliteration) for the mechanism.

## Files

### Safetensors

| File | Size |
|---|---|
| `model.safetensors` | 3.84 GB |

BF16, 1,918,181,888 parameters (1.92B): 1,728,801,536 language model + 164,206,336
vision encoder + 25,174,016 projector. The `reproduce/` directory carries the full Heretic
recipe - `config.toml`, `requirements.txt`, the Optuna study journal, and SHA-256 sums.

### GGUF quantizations

Full quantization set (F16 + 14 quants, 19.31 GB including the projector) produced with
[llama.cpp](https://github.com/ggml-org/llama.cpp) master on 2026-10-28.

> [!IMPORTANT]
> The text files use the new `lfm3` GGUF architecture and the projector uses `clip`. You need an
> **LFM3-VL-capable llama.cpp build** (support landed in late October 2026); older builds will fail
> to load them. The upstream [LiquidAI/LFM3-VL-2B-GGUF](https://huggingface.co/LiquidAI/LFM3-VL-2B-GGUF)
> uses the same pair.

| File | Format | Size |
|---|---|---|
| `LFM3-VL-2B-heretic-F16.gguf` | GGUF F16 | 3.47 GB |
| `LFM3-VL-2B-heretic-Q2_K.gguf` | GGUF Q2_K | 0.75 GB |
| `LFM3-VL-2B-heretic-IQ3_S.gguf` | GGUF IQ3_S | 0.85 GB |
| `LFM3-VL-2B-heretic-Q3_K_S.gguf` | GGUF Q3_K_S | 0.85 GB |
| `LFM3-VL-2B-heretic-Q3_K_M.gguf` | GGUF Q3_K_M | 0.91 GB |
| `LFM3-VL-2B-heretic-Q3_K_L.gguf` | GGUF Q3_K_L | 0.97 GB |
| `LFM3-VL-2B-heretic-IQ4_XS.gguf` | GGUF IQ4_XS | 1.01 GB |
| `LFM3-VL-2B-heretic-Q4_K_S.gguf` | GGUF Q4_K_S | 1.06 GB |
| `LFM3-VL-2B-heretic-Q4_0.gguf` | GGUF Q4_0 | 1.05 GB |
| `LFM3-VL-2B-heretic-Q4_1.gguf` | GGUF Q4_1 | 1.14 GB |
| `LFM3-VL-2B-heretic-Q4_K_M.gguf` | GGUF Q4_K_M | 1.10 GB |
| `LFM3-VL-2B-heretic-Q5_K_S.gguf` | GGUF Q5_K_S | 1.23 GB |
| `LFM3-VL-2B-heretic-Q5_K_M.gguf` | GGUF Q5_K_M | 1.26 GB |
| `LFM3-VL-2B-heretic-Q6_K.gguf` | GGUF Q6_K | 1.43 GB |
| `LFM3-VL-2B-heretic-Q8_0.gguf` | GGUF Q8_0 | 1.85 GB |
| `LFM3-VL-2B-heretic-mmproj-F16.gguf` | GGUF F16 projector | 0.38 GB |

Text + vision needs both the chosen text quant and the projector. For reference:
Q4_K_M 1.48 GB, Q5_K_M 1.64 GB, Q6_K 1.81 GB,
Q8_0 2.23 GB. The projector is not quantized.

## Quickstart

```bash
# llama.cpp - -hf auto-fetches the matching mmproj (LFM3-VL-capable build)
llama-mtmd-cli -hf saidutta69/LFM3-VL-2B-heretic:Q4_K_M \
  --image photo.jpg -p "Describe this image."
```

```bash
# explicit two-file form
llama-mtmd-cli \
  -m LFM3-VL-2B-heretic-Q4_K_M.gguf \
  --mmproj LFM3-VL-2B-heretic-mmproj-F16.gguf \
  --image photo.jpg -p "Describe this image."
```

```python
# transformers (the checkpoint ships custom code; needs transformers>=5.21.0)
import torch
from transformers import AutoModelForImageTextToText, AutoProcessor

model_id = "saidutta69/LFM3-VL-2B-heretic"
model = AutoModelForImageTextToText.from_pretrained(
    model_id, dtype=torch.bfloat16, device_map="auto", trust_remote_code=True
)
processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)

messages = [{
    "role": "user",
    "content": [
        {"type": "image", "url": "https://placecats.com/300/200"},
        {"type": "text", "text": "Describe this image."},
    ],
}]
inputs = processor.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt", return_dict=True
).to(model.device)
out = model.generate(**inputs, do_sample=True, temperature=0.1, top_p=1.0, top_k=50,
                     repetition_penalty=1.1, max_new_tokens=512)
print(processor.tokenizer.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

### Generation parameters

Liquid's recommended settings: `temperature=0.1, top_p=1.0, top_k=50, min_p=0.0,
repetition_penalty=1.1`. For image and video preprocessing use the values in
`processor_config.json`.

### Chat template and thinking

LFM3 uses ChatML with `<|startoftext|>` at the front. Reasoning is enabled by default and arrives
in a ` thinking` block; pass `enable_thinking=False` to disable it (Liquid notes this can be
inconsistent on reasoning-heavy tasks). Prior-turn reasoning is dropped unless
`preserve_thinking=True`. Tool calls use the same XML format as LFM3-1.7B; pass schemas with
`tools=...` to `apply_chat_template()` and feed results back under a `tool` role.

## Runs anywhere

| Device | Recommended quant | Text weights | + vision projector |
| :--- | :--- | :--- | :--- |
| Phone / browser (6 GB RAM) | Q4_K_M | 1.10 GB | 1.48 GB |
| Raspberry Pi 5 (8 GB) | Q4_K_M | 1.10 GB | 1.48 GB |
| Laptop (8 GB, Apple Silicon) | Q6_K | 1.43 GB | 1.81 GB |
| RTX 3060 / 4060 (12 GB) | Q8_0 | 1.85 GB | 2.23 GB |
| Server / multi-tenant | Q5_K_M | 1.26 GB | 1.64 GB |

Weights only; the KV cache grows with context. The projector is fixed at 0.38 GB
regardless of the text quant.

## Model details

| | |
|---|---|
| **Architecture** | `Lfm3VlForConditionalGeneration` (LFM3 language tower + LFM3-VL vision) |
| **Parameters** | 1.92B: 1.73B language + 164M vision encoder + 25M projector |
| **Language tower** | 24 layers: 13 gated short convolutions, 5 sliding-window attention, 6 global attention |
| **Vision encoder** | 14 layers: 8 gated depthwise 2D convolutions, 6 bidirectional attention, 16x16 patches with 2D RoPE |
| **Attention (text)** | 16 heads / 4 KV heads on attention layers, head dim 128 |
| **Hidden / intermediate (text)** | 2048 / 7680 |
| **Convolution cache** | L_cache = 7 |
| **Sliding window** | 256 |
| **Context length** | 128,000 (base card and GGUF header `lfm3.context_length`) |
| **Vocab** | 128,000 |
| **Inputs** | Text, images, and video at native resolution; video at 2 fps; each 2x2 patch block is one language token |
| **Precision** | bfloat16 |
| **Languages** | English, Arabic, Chinese, French, German, Italian, Japanese, Korean, Portuguese, Spanish, Vietnamese, Thai, Indonesian, Hindi, Russian, Polish |
| **Base model** | [LiquidAI/LFM3-VL-2B](https://huggingface.co/LiquidAI/LFM3-VL-2B) |

Text GGUF: `arch=lfm3`, 287 tensors, 24 blocks, 128,000 context, tied embeddings (no `lm_head`
tensor). The projector GGUF carries the complete 164,206,336-parameter vision encoder +
25,174,016-parameter projector.

**Base-model note:** the heretic repo's original YAML tag said `LiquidAI/LFM3-1.7B-Base`, but the
ablation was run on `LiquidAI/LFM3-VL-2B` (commit `f83d2b0a...`) - see `reproduce/config.toml`.
This card uses the correct base.

## FAQ

### What is LFM3-VL-2B-heretic?

`LFM3-VL-2B-heretic` is a decensored build of [`LiquidAI/LFM3-VL-2B`](https://huggingface.co/LiquidAI/LFM3-VL-2B) produced with Heretic 1.4.0 (directional ablation). It is the same weights with the refusal direction removed, not a new fine-tune, so its capabilities track the base model.

### Is LFM3-VL-2B-heretic actually uncensored?

Yes. On Heretic's 100-prompt refusal harness it drops from 98/100 to 3/100 at KL divergence 0.0014 from the base model. These are measured values, not a claim; reproduction data is in [`reproduce/`](reproduce/).

### How do I run LFM3-VL-2B-heretic locally?

Text: `llama serve -hf saidutta69/LFM3-VL-2B-heretic:Q4_K_M`. Images: `llama-mtmd-cli -hf saidutta69/LFM3-VL-2B-heretic:Q4_K_M --mmproj LFM3-VL-2B-heretic-mmproj-F16.gguf`. The repo ships 15 GGUF quants plus the projector, so vision survives quantization.

## Responsible use

Refusal suppression is deliberate and works as intended: this model will comply with requests the
base model would refuse, including some it should not. There is no safety filtering layered on top.
You are responsible for how you deploy it - don't put this behind an unmoderated public-facing
endpoint serving third parties. It inherits LFM3-VL-2B's factual and visual limitations;
abliteration removes refusal directions, it does not add capability or judgment.

> Made with ❤️ by **RACER IS OP (saidutta69)** - follow for more uncensored models

## License

Inherits the [LFM Open License v1.0](https://huggingface.co/LiquidAI/LFM3-VL-2B/blob/main/LICENSE) from the base
model. This is **not** Apache-2.0; review the LFM terms before commercial use.

## Related

- [LiquidAI/LFM3-VL-2B](https://huggingface.co/LiquidAI/LFM3-VL-2B) - the post-trained vision-language base model
- [LiquidAI/LFM3-VL-2B-GGUF](https://huggingface.co/LiquidAI/LFM3-VL-2B-GGUF) - the upstream GGUF + mmproj
- [LFM3-1.7B-heretic](https://huggingface.co/saidutta69/LFM3-1.7B-heretic) - the text-only sibling
- [LFM3 family collection](https://huggingface.co/collections/LiquidAI/lfm3)
- [RACER IS OP - Heretic Models - full collection](https://huggingface.co/collections/saidutta69/racer-is-op-heretic-models)

## Abliteration hardware

Recorded in `reproduce/reproduce.json`:

- **GPU:** NVIDIA RTX PRO 6000 Blackwell Server Edition (94.97 GB VRAM)
- **OS:** `Linux-4.19.0-gvisor-x86_64-with-glibc2.41`
- **CUDA / driver:** CUDA 13.0, driver 595.71.05
- **Software:** PyTorch 2.14.1+cu130, Heretic 1.4.0

Heretic notes that KL-divergence and refusal numbers can vary slightly with hardware and library versions.
