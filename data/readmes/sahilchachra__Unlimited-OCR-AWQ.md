---
license: mit
base_model: baidu/Unlimited-OCR
base_model_relation: quantized
pipeline_tag: image-text-to-text
library_name: transformers
tags:
  - awq
  - int4
  - w4a16
  - compressed-tensors
  - llm-compressor
  - ocr
  - deepseek-ocr
  - vision-language
  - multimodal
  - image-text-to-text
  - moe
  - quantized
  - document-parsing
language:
  - multilingual
---

# Unlimited-OCR — AWQ (W4A16)

AWQ 4-bit (W4A16) quantization of [**baidu/Unlimited-OCR**](https://huggingface.co/baidu/Unlimited-OCR),
a 3B vision-language OCR model that pushes **DeepSeek-OCR** one step further (one-shot,
long-horizon document parsing). This repo quantizes the **DeepSeek-V2 MoE text decoder** with
activation-aware scaling (AWQ) while keeping the vision tower in BF16, so it stays a drop-in
`transformers` model.

> ⚠️ **Runtime requirements.** This is custom remote code, so load with
> **`trust_remote_code=True`**, **`transformers` 4.57.x**, and **`compressed-tensors`** installed.
> W4A16 (int4) runs on any CUDA GPU; `compressed-tensors` handles the 4-bit unpacking at load.

## This quant

| | |
|---|---|
| **Scheme** | `W4A16` · int4 symmetric · group 128 · `pack-quantized` |
| **Method** | **AWQ** (`llm-compressor`) — activation-aware, text-calibrated |
| **Calibration** | 64 × 512-token general-text sequences (text-only forward) |
| **Quantized** | text-decoder Linears (attention q/k/v/o, all experts + shared `gate/up/down`, dense `gate/up`) |
| **Kept in BF16** | vision tower (`sam_model`, `vision_model`), projector, token embeddings, `lm_head`, the MoE **router gate**, all norms, and the single dense layer-0 `down_proj` (width 6848 not divisible by group 128) |
| **Quantized by** | [sahilchachra](https://huggingface.co/sahilchachra) |

## Quick start

```bash
pip install "transformers==4.57.3" compressed-tensors accelerate torch torchvision \
            einops addict easydict matplotlib pillow
```

```python
import torch
from transformers import AutoModel, AutoTokenizer

repo = "sahilchachra/Unlimited-OCR-AWQ"
tok = AutoTokenizer.from_pretrained(repo, trust_remote_code=True)
model = AutoModel.from_pretrained(repo, trust_remote_code=True,
                                  dtype=torch.bfloat16, device_map="cuda").eval()

text = model.infer(
    tok,
    prompt="<image>\n<|grounding|>Convert the document to markdown.",
    image_file="document.png", output_path="./out",
    base_size=1024, image_size=1024, crop_mode=False,   # "base" mode
    save_results=True, eval_mode=True,
)
print(text)
```

## Prompting guide

Unlimited-OCR uses the **DeepSeek-OCR** prompt vocabulary. The prompt **must contain `<image>`**;
prefix it with `<|grounding|>` whenever you also want **bounding boxes** for what was read.

| Task | Prompt |
|---|---|
| **Document → Markdown** (layout-aware, with boxes) | `<image>\n<|grounding|>Convert the document to markdown.` |
| **Plain text OCR** (just the text, no layout) | `<image>\nFree OCR.` |
| **OCR with bounding boxes** | `<image>\n<|grounding|>OCR this image.` |
| **Native Unlimited-OCR parse** | `<image>document parsing.` |
| **Parse a figure / chart / diagram** | `<image>\nParse the figure.` |
| **Describe the image** (general VQA) | `<image>\nDescribe this image in detail.` |
| **Find specific text** (referring grounding) | `<image>\n<|grounding|>Locate <|ref|>Total Due<|/ref|> in the image.` |
| **Multi-page / PDF** | `<image>Multi page parsing.` via `model.infer_multi(...)` |

### Resolution modes
- **base** — `base_size=1024, image_size=1024, crop_mode=False`. Good default for normal pages.
- **gundam** — `base_size=1024, image_size=640, crop_mode=True`. Tiles the page; use for dense
  or large/high-resolution documents.

### Understanding the output (grounding tokens)

With `<|grounding|>`, the model interleaves the recognized text with detection boxes:

```
<|det|>title [37, 64, 464, 132]<|/det|>INVOICE #2026-0623
<|det|>text  [37, 194, 350, 247]<|/det|>Bill To: Sahil Chachra
<|det|>text  [37, 483, 329, 543]<|/det|>Total Due: $44.00
```

Each `[x1, y1, x2, y2]` is the bounding box (top-left → bottom-right) of that span, in the
coordinate space of the model's input image. Drop the `<|det|>...<|/det|>` tags if you only want
text, or parse them to overlay boxes / rebuild layout. Without `<|grounding|>` you get plain text
(or Markdown) with no box tags.

## Serving

The original model ships an **SGLang** wheel and a vLLM path (see the
[base model card](https://huggingface.co/baidu/Unlimited-OCR)). W4A16 / `compressed-tensors`
weights load directly in runtimes with compressed-tensors support (e.g. vLLM); otherwise use the
`transformers` snippet above.

## About the model

- **Architecture:** `UnlimitedOCRForCausalLM` (DeepSeek-OCR architecture) — a *DeepEncoder*
  vision tower (**SAM-ViT-B + CLIP-L/14**, 1024×1024 input, 16× downsample) → linear projector →
  **DeepSeek-V2 MoE** text decoder (12 layers, hidden 1280, **64 routed + 2 shared experts**,
  6 experts/token; layer 0 dense).
- **Task:** multilingual OCR / document parsing — single image, multi-page, and PDF
  (one-shot long-horizon parsing).
- **License:** MIT (inherited from the base model).

## How this was made

Unlimited-OCR is custom remote code whose forward only runs the vision tower when images are
passed, so AWQ calibration feeds **text only** (`images=None`), exercising the pure DeepSeek-V2
decoder. Per-layer AWQ mappings were built from the live module tree (attention
`input_layernorm→q,k,v` and `v→o`; MoE `post_attention_layernorm→` every expert + shared-expert
`gate/up`, plus per-expert `up→down`). The fx-based "sequential" pipeline can't trace this custom
model, so the **basic** pipeline (real end-to-end forward + activation hooks) was used.

## Verified

Loaded in `transformers` and run on a test document — OCR output matches BF16, e.g.:
```
<|det|>title [37, 64, 464, 130]<|/det|>INVOICE #2026-0623
<|det|>text  [37, 480, 329, 540]<|/det|>Total Due: $44.00
```

## Limitations

- 4-bit weights trade a little accuracy for size; for the highest fidelity use the original BF16
  model. For OCR, this AWQ build is effectively lossless on tested documents.
- The vision encoder and MoE router stay BF16 (small, accuracy-sensitive).
- English-/multilingual-text centric; verify critical fields on hard scans.

## Other formats

- **NVFP4:** [sahilchachra/Unlimited-OCR-NVFP4](https://huggingface.co/sahilchachra/Unlimited-OCR-NVFP4)
- **GGUF (llama.cpp):** [sahilchachra/Unlimited-OCR-GGUF](https://huggingface.co/sahilchachra/Unlimited-OCR-GGUF)
- **MLX:** [sahilchachra/unlimited-ocr-8bit-mlx](https://huggingface.co/sahilchachra/unlimited-ocr-8bit-mlx)

## Credits

Base model [baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR) (MIT), built on
[DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR). Quantized with
[llm-compressor](https://github.com/vllm-project/llm-compressor). License: MIT.
