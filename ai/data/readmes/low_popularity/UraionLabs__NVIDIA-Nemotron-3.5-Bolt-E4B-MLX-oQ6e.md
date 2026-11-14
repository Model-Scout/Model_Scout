---
license: other
license_name: openmdw-1.1
license_link: https://openmdw.ai/license/1-1/
base_model: nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16
base_model_relation: quantized
library_name: mlx
pipeline_tag: text-generation
datasets:
- nvidia/nemotron-post-training-v3
- nvidia/nemotron-pre-training-datasets
language:
- en
- es
- fr
- de
- it
- ja
- ar
- bg
- cs
- da
- el
- et
- fi
- hi
- hr
- hu
- id
- ko
- lt
- lv
- nl
- "no"
- pl
- pt
- ro
- ru
- sk
- sl
- sv
- th
- tr
- uk
- vi
- zh
tags:
- mlx
- mlx-vlm
- mlx-lm
- safetensors
- apple-silicon
- mac
- metal
- nvidia
- nemotron
- nemotron-3.5
- nemotron-bolt
- gemma4
- gemma-4
- e4b
- quantized
- 6-bit
- mixed-precision
- imatrix
- oq
- oqe
- oq6e
- omlx
- reasoning
- tool-calling
- function-calling
- conversational
- on-device
- edge-ai
- voice-assistant
- uraionlabs
---

<div align="center">

<img src="assets/banner.png" alt="Nemotron 3.5 Bolt E4B for MLX, by Uraion Labs" width="100%"/>

<br/>

[![Uraion Labs](https://img.shields.io/badge/Uraion%20Labs-uraionlabs.com-050505?style=flat-square&labelColor=E45A1A)](https://uraionlabs.com)
[![Base](https://img.shields.io/badge/base-NVIDIA%20Nemotron%203.5%20Bolt%20E4B-050505?style=flat-square&labelColor=222222)](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16)
[![Runtime](https://img.shields.io/badge/runtime-MLX%20%C2%B7%20Apple%20Silicon-050505?style=flat-square&labelColor=222222)](https://github.com/ml-explore/mlx)
[![Quant](https://img.shields.io/badge/quant-oQ6e%20%C2%B7%207.3%20GB-050505?style=flat-square&labelColor=222222)](#pick-a-size)
[![License](https://img.shields.io/badge/license-OpenMDW--1.1-050505?style=flat-square&labelColor=222222)](https://openmdw.ai/license/1-1/)

</div>

# Nemotron 3.5 Bolt E4B · MLX oQ6e

[NVIDIA Nemotron 3.5 Bolt E4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) quantized for Apple Silicon with MLX: **7.3 GB, mixed precision, 6-bit base with sensitive layers at higher bits**, imatrix-calibrated.

It peaks at **8.1 GB** of memory with a 1K-token prompt. On chat output, its next-token distribution has a mean KL divergence of **0.0045** from BF16, and its top-1 token matches BF16 **98.0%** of the time.

Bolt E4B is NVIDIA's post-train of Gemma 4 E4B for fast local assistants. It has 8B parameters, about 4B effective per token, 64K context, switchable reasoning, a conversational mode for voice, and tool calling. All model credit goes to NVIDIA. See [their card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) for training, benchmarks, and safety.

## Pick a size

Five sizes, same calibration. All measured on the same machine, same text, same settings ([method](#how-we-measured)).

| Repo | Size | Peak memory | KLD vs BF16 ↓ | Top-1 match ↑ | PPL ↓ | Min Mac | |
|---|---:|---:|---:|---:|---:|---|---|
| [oQ8e](https://huggingface.co/UraionLabs/NVIDIA-Nemotron-3.5-Bolt-E4B-MLX-oQ8e) | 8.9 GB | 9.7 GB | 0.0011 | 99.2% | 1.261 | 16 GB | Reference. Closest to BF16. |
| **[oQ6e](https://huggingface.co/UraionLabs/NVIDIA-Nemotron-3.5-Bolt-E4B-MLX-oQ6e)** ← this repo | 7.3 GB | 8.1 GB | 0.0045 | 98.0% | 1.264 | 16 GB | High fidelity. |
| [oQ5e](https://huggingface.co/UraionLabs/NVIDIA-Nemotron-3.5-Bolt-E4B-MLX-oQ5e) | 6.3 GB | 7.1 GB | 0.0116 | 97.0% | 1.271 | 16 GB | High fidelity. |
| [oQ4e](https://huggingface.co/UraionLabs/NVIDIA-Nemotron-3.5-Bolt-E4B-MLX-oQ4e) | 5.6 GB | 6.4 GB | 0.0330 | 94.9% | 1.301 | 16 GB | **Recommended default.** |
| [oQ3e](https://huggingface.co/UraionLabs/NVIDIA-Nemotron-3.5-Bolt-E4B-MLX-oQ3e) | 4.8 GB | 5.6 GB | 0.1584 | 89.2% | 1.486 | 16 GB | Smallest. Noticeable loss; test on your task. |
| [BF16 (NVIDIA)](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) | 16.0 GB | 16.6 GB | 0 | 100% | 1.260 | 32 GB | Source model. |

**Which one?** oQ4e is the best balance for most Macs. oQ5e and up are within 1% of BF16 perplexity. Pick oQ3e only if every 0.8 GB counts.

**Why nothing smaller?** We also built oQ3.5, oQ2.7, oQ2.5 and oQ2. None was worth shipping. In our measurements oQ3.5 scored worse than oQ3 while being larger, and the 2-bit levels we scored nearly doubled perplexity. The BF16 vision/audio encoders and the large per-layer embedding table also put a floor of about 4 GB under every build, so going lower saves less than you'd expect.

All five are in the [collection](https://huggingface.co/collections/UraionLabs/nemotron-35-bolt-e4b-mlx-oqe-6adbaedba171e319748162ae).

## Quickstart

**oMLX** (Apple Silicon server, OpenAI-compatible):

```bash
omlx serve UraionLabs/NVIDIA-Nemotron-3.5-Bolt-E4B-MLX-oQ6e --port 8000
```

**LM Studio:** search for `NVIDIA-Nemotron-3.5-Bolt-E4B-MLX-oQ6e` in the model browser, or run `lms get UraionLabs/NVIDIA-Nemotron-3.5-Bolt-E4B-MLX-oQ6e`.

**mlx-vlm** (Python):

```bash
pip install -U mlx-vlm
```

```python
from mlx_vlm import load, generate
from mlx_vlm.prompt_utils import apply_chat_template

model, processor = load("UraionLabs/NVIDIA-Nemotron-3.5-Bolt-E4B-MLX-oQ6e")
prompt = apply_chat_template(
    processor, model.config,
    "Plan a 3-day trip to Kyoto on a budget.",
    num_images=0,
    enable_thinking=True,        # False for direct answers
)
print(generate(model, processor, prompt, max_tokens=2048, temperature=1.0, top_p=0.95).text)
```

**mlx-lm** works too (text only):

```bash
pip install -U mlx-lm
mlx_lm.chat --model UraionLabs/NVIDIA-Nemotron-3.5-Bolt-E4B-MLX-oQ6e
mlx_lm.server --model UraionLabs/NVIDIA-Nemotron-3.5-Bolt-E4B-MLX-oQ6e --port 8080
```

### Model controls

These come from NVIDIA's chat template. Pass them as chat-template arguments, as in the mlx-vlm example above, or in `chat_template_kwargs` with an OpenAI-compatible server.

| Control | Effect |
|---|---|
| `enable_thinking=True` (default) | Reasons before answering. |
| `enable_thinking=False` | Direct answers, lower latency. |
| `conversational_mode=True` | Short, low-formatting replies for voice and chat UIs. Works with either thinking setting and with tools. |
| `preserve_thinking=True` | Keeps earlier reasoning in multi-turn history. |

NVIDIA recommends **temperature 1.0, top_p 0.95** in both modes. `generation_config.json` also sets top_k 64.

## What oQe is, and what we fixed

oQ is the mixed-precision quantizer in [oMLX](https://github.com/jundot/omlx) by [Jundot](https://huggingface.co/Jundot). It measures how sensitive each layer is, then gives sensitive layers more bits. oQe adds an **importance matrix**: activation statistics from calibration text, used to weight the rounding error of every quantized weight. The calibration set is oMLX's built-in `oqe_code_multilingual`, 128 samples × 512 tokens.

When we quantized this model with oMLX 0.7.2, we found two problems specific to Gemma-4-based checkpoints. Both are fixed in every repo here:

1. **The imatrix was collected but never applied.** The collector stores statistics under mlx-vlm module paths (`language_model.model.layers.N.*`), but the quantizer looks them up by checkpoint name (`model.language_model.layers.N.*`). All 343 lookups missed, so the output was plain oQ with an "e" in the name. We patched the lookup to try both names. Now **343 of 343** calibrated layers are applied. The 39 tensors that remain uncalibrated are expected: the k/v projections in KV-shared layers 24–41 never run, and the embedding and multimodal projectors have no text activations to measure.
2. **Mixed-precision outputs don't load in mlx-vlm.** The per-layer bit overrides in `config.json` are written under checkpoint names, but mlx-vlm resolves them by module path. The higher-bit layers get built at the base bit width, and loading fails with `Expected shape (2560, 256) but received shape (2560, 320)`. We rewrote the override keys to module paths. Weights are unchanged.

## What we changed for oQ4e and oQ3e

Measured on chat output, this model holds up well down to 5 bits and then falls off a cliff at 4. To find out why, we rebuilt oQ4 several ways and scored each against BF16. Each "+" row is a separate build starting from "oQ4e, imatrix applied":

| oQ4 build | Size | KLD vs BF16 ↓ | Top-1 match ↑ | PPL ↓ |
|---|---:|---:|---:|---:|
| oQ4, imatrix not applied (oMLX 0.7.2 as shipped) | 5.4 GB | 0.189 | 89.1% | 1.532 |
| oQ4e, imatrix applied | 5.4 GB | 0.078 | 92.6% | 1.359 |
| + embeddings / output head at 8-bit | 5.7 GB | 0.074 | 92.9% | 1.353 |
| + embeddings and per-layer embeddings at 8-bit | 7.1 GB | 0.073 | 92.9% | 1.350 |
| + MLPs at 8-bit (LM Studio's Gemma 4 rule) | 6.8 GB | 0.068 | 92.9% | 1.342 |
| **+ attention and per-layer gates at 8-bit (shipped)** | 5.6 GB | 0.033 | 94.9% | 1.301 |

Three results stand out:

- **The imatrix fix matters.** On the same bit allocation, the working imatrix cuts divergence by more than half.
- **Attention is where the 4-bit loss comes from.** Holding the attention projections (q/k/v/o) and the small per-layer input gates at 8-bit halves the divergence again, for 0.2 GB.
- **The other usual suspects don't help much.** Pinning the MLPs (the rule LM Studio uses for Gemma 4 E4B) or the embeddings costs far more size for far less gain.

So **oQ4e and oQ3e keep attention and per-layer gates at 8-bit.** oQ5e, oQ6e and oQ8e use oQ's standard allocation, which already lands within 1% of BF16.

## How we measured

- **Fidelity:** BF16 answered 40 varied chat prompts (coding, reasoning, tool use, writing, and five languages; half with thinking on) at NVIDIA's recommended sampling. Each quant then read those exact conversations, and we compared its next-token distribution to BF16's over the 9,621 response tokens: mean KL(BF16 ‖ quant), top-1 agreement, and perplexity. This measures fidelity on the kind of text the model actually produces.
- **Why not WikiText?** We tried it. Raw encyclopedia text is far from what this chat-tuned model expects (BF16 perplexity is in the hundreds), so its near-tie predictions exaggerate differences between quants and misorder them.
- **Memory:** peak unified memory in mlx-vlm 0.7.8 (MLX 0.32.4) with a ~1K-token prompt, vision and audio encoders loaded. Text-only runtimes such as mlx-lm use about 1 GB less.
- **Speed:** not published yet. We'll add tokens/sec measurements in a later update.
- **Load check:** every file in each repo was checksum-verified against our local build, and each build was loaded and run with stock PyPI `mlx-vlm` 0.7.10 and `mlx-lm` 0.32.2.

These are fidelity numbers against BF16, not task benchmarks. For task accuracy, see NVIDIA's [benchmark table](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16#benchmarks). It includes their own Q4_K_M results, which track BF16 closely.

## Files

| File | Notes |
|---|---|
| `model*.safetensors` | MLX quantized weights. Vision and audio encoders are kept at BF16, as in the source checkpoint. |
| `config.json` | Per-layer bit allocation under `quantization` |
| `chat_template.jinja`, `tokenizer*`, `generation_config.json`, `processor_config.json` | Unchanged from NVIDIA |
| `oq_imatrix_report.json` | Which tensors received imatrix weighting |
| `LICENSE`, `bias.md`, `explainability.md`, `privacy.md`, `safety.md` | NVIDIA's license and model-card notices, unchanged |

## Limitations

- **Text is the supported modality.** NVIDIA lists Bolt E4B as text-in, text-out. The Gemma 4 vision and audio encoders are still in the checkpoint and load in mlx-vlm, but NVIDIA doesn't document or evaluate them for this model, and neither do we.
- **Context:** 64K tokens, as upstream.
- **oQ3e** loses measurably more than the others (see the table). Check it on your own task before relying on it.
- **Fidelity numbers don't depend on hardware.** Memory figures will differ slightly by runtime and context length.
- **Behavior:** quantization doesn't change the chat template, safety tuning or intended use. NVIDIA's [card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) and the notice files in this repo cover bias, safety and privacy.

## License & attribution

**Model:** NVIDIA Nemotron 3.5 Bolt E4B by NVIDIA Corporation, under the [OpenMDW License Agreement, version 1.1](https://openmdw.ai/license/1-1/). A copy is in [`LICENSE`](LICENSE). NVIDIA post-trained it from [Google Gemma 4 E4B](https://huggingface.co/google/gemma-4-E4B-it), which is under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

**Quantization:** [oMLX](https://github.com/jundot/omlx) oQe by Jundot, run by Uraion Labs with the fixes and the 8-bit attention rule described above. Weights were quantized only. Nothing was retrained or merged.

Uraion Labs is not affiliated with or endorsed by NVIDIA or Google.

If you use this model, please cite NVIDIA's [technical report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB-Technical-Report.pdf).

---

<div align="center">

<b>Uraion Labs</b> · Frontier reasoning. Specialized execution. Persistent memory.<br/>
<a href="https://uraionlabs.com">uraionlabs.com</a> · <a href="https://huggingface.co/collections/UraionLabs/nemotron-35-bolt-e4b-mlx-oqe-6adbaedba171e319748162ae">all sizes</a>

</div>
