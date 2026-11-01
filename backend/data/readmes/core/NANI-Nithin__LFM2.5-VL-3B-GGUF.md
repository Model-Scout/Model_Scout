---
license: other
license_name: lfm-1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-VL-3B
base_model: LiquidAI/LFM2.5-VL-3B
tags:
  - llama.cpp
  - gguf
  - quantized
  - vision
  - multimodal
  - lfm2
  - liquid
  - ocr
  - grounding
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
pipeline_tag: image-text-to-text
library_name: llama.cpp
---

# LFM2.5-VL-3B-GGUF

GGUF quantizations of [LiquidAI/LFM2.5-VL-3B](https://huggingface.co/LiquidAI/LFM2.5-VL-3B) for [llama.cpp](https://github.com/ggml-org/llama.cpp).

LFM2.5-VL-3B is a 3.1B vision-language model for on-device use. It uses the LFM2.5-2.6B language backbone plus a SigLIP2 NaFlex 400M vision encoder, with 32K context. It is strong at screen/UI understanding, OCR with layout, object grounding, and tool use from text or images.

- **Base model:** [LiquidAI/LFM2.5-VL-3B](https://huggingface.co/LiquidAI/LFM2.5-VL-3B)
- **Official GGUF (Liquid):** [LiquidAI/LFM2.5-VL-3B-GGUF](https://huggingface.co/LiquidAI/LFM2.5-VL-3B-GGUF)
- **Docs:** [LFM2.5-VL-3B](https://docs.liquid.ai/lfm/models/lfm25-vl-3b)
- **Architecture:** LFM2.5-VL (dense)
- **Context:** 32,768 tokens
- **Vocab:** 128,000
- **License:** [LFM Open License v1.0](https://huggingface.co/LiquidAI/LFM2.5-VL-3B)

## Recommended quants

| Use case | Quant | Notes |
|---|---|---|
| Best everyday default | `Q4_K_M` | Best size/quality tradeoff |
| Higher quality, still small | `Q5_K_M` | Safer for OCR / grounding |
| Fast / low RAM | `Q3_K_M` or `IQ4_XS` | Use IQ if you have the imatrix quants |
| Near-lossless | `Q6_K` / `Q8_0` | Quality check / archival |
| Full precision | `BF16` | Source GGUF used for quantization |

IQ quants (`IQ2_M`, `IQ3_*`, `IQ4_*`) were built with an importance matrix and are usually better than same-size standard quants at very low bits.

## Available files

**Standard**

- `LFM2.5-VL-3B-BF16.gguf`
- `LFM2.5-VL-3B-Q2_K.gguf`
- `LFM2.5-VL-3B-Q3_K_S.gguf`
- `LFM2.5-VL-3B-Q3_K_M.gguf`
- `LFM2.5-VL-3B-Q3_K_L.gguf`
- `LFM2.5-VL-3B-Q4_0.gguf`
- `LFM2.5-VL-3B-Q4_1.gguf`
- `LFM2.5-VL-3B-Q4_K_S.gguf`
- `LFM2.5-VL-3B-Q4_K_M.gguf`
- `LFM2.5-VL-3B-Q5_K_S.gguf`
- `LFM2.5-VL-3B-Q5_K_M.gguf`
- `LFM2.5-VL-3B-Q6_K.gguf`
- `LFM2.5-VL-3B-Q8_0.gguf`

**I-quants (imatrix)**

- `LFM2.5-VL-3B-IQ2_M.gguf`
- `LFM2.5-VL-3B-IQ3_XXS.gguf`
- `LFM2.5-VL-3B-IQ3_XS.gguf`
- `LFM2.5-VL-3B-IQ3_M.gguf`
- `LFM2.5-VL-3B-IQ4_XS.gguf`
- `LFM2.5-VL-3B-IQ4_NL.gguf`

Use a **recent llama.cpp** build. This is a vision model (`lfm2` / LFM2.5-VL). Older binaries may fail to load it.

## Quick start

```bash
# CLI
llama-cli \
  -hf NANI-Nithin/LFM2.5-VL-3B-GGUF:Q4_K_M \
  --image test_image.jpg \
  -p "What's in this image?" \
  -n 256 \
  --temp 0.2 --top-k 50 --repeat-penalty 1.0

# Local file
llama-cli \
  -m LFM2.5-VL-3B-Q4_K_M.gguf \
  --image test_image.jpg \
  -p "Read all visible text and summarize the document." \
  -n 256 \
  --temp 0.2 --top-k 50 --repeat-penalty 1.0

# Server
llama-server \
  -m LFM2.5-VL-3B-Q4_K_M.gguf \
  -c 4096 \
  --port 8080
```

`--image-max-tokens` controls the image token budget if needed.

## Sampling

Liquid recommends:

- `temperature=0.2`
- `top_k=50`
- `repetition_penalty=1.0`

Good for single-turn, low-latency work: OCR, screenshots, menus/signs, object localization, batch document parsing. Less suitable for long visual reasoning or highly technical blueprint analysis.

## Conversion notes

Converted from the official HF checkpoint with `convert_hf_to_gguf.py` (`bf16`), then quantized with `llama-quantize`. IQ files used `llama-imatrix` + `--imatrix`.

This is an unofficial community quantization. For official GGUF files, use [LiquidAI/LFM2.5-VL-3B-GGUF](https://huggingface.co/LiquidAI/LFM2.5-VL-3B-GGUF).

## License and attribution

Weights follow Liquid AI's **LFM Open License v1.0**. Review the license on the [base model page](https://huggingface.co/LiquidAI/LFM2.5-VL-3B) before commercial use.
