---
library_name: gguf
license: other
license_name: lfm1.0
license_link: LICENSE
pipeline_tag: image-text-to-text
tags:
- liquid
- lfm3
- gguf
- llama.cpp
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
base_model: LiquidAI/LFM3-VL-2B
---

<div align="center">
  <img
    src="https://huggingface.co/LiquidAI/LFM3-1.7B/resolve/main/assets/liquid-ai-banner.webp"
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: block; margin: 0;"
  />
  <div align="center" style="display: flex; justify-content: center; align-items: center; gap: 1.25em; margin: 8px 0 1.7rem; padding: 0; line-height: 1.3;">
    <a href="https://console.liquid.ai/dashboard" style="display: inline-flex; align-items: center; gap: 6px;"><img src="https://huggingface.co/LiquidAI/LFM3-1.7B/resolve/main/assets/icons/api.svg" width="16" height="16" alt="" aria-hidden="true" style="display: block; flex: 0 0 16px; width: 16px; height: 16px; margin: 0;" /><strong>API</strong></a>
    <a href="https://playground.liquid.ai/" style="display: inline-flex; align-items: center; gap: 6px;"><img src="https://huggingface.co/LiquidAI/LFM3-1.7B/resolve/main/assets/icons/try.svg" width="16" height="16" alt="" aria-hidden="true" style="display: block; flex: 0 0 16px; width: 16px; height: 16px; margin: 0;" /><strong>Try</strong></a>
    <a href="https://docs.liquid.ai/lfm/getting-started/welcome" style="display: inline-flex; align-items: center; gap: 6px;"><img src="https://huggingface.co/LiquidAI/LFM3-1.7B/resolve/main/assets/icons/docs.svg" width="16" height="16" alt="" aria-hidden="true" style="display: block; flex: 0 0 16px; width: 16px; height: 16px; margin: 0;" /><strong>Docs</strong></a>
    <a href="https://www.liquid.ai/blog/lfm3" style="display: inline-flex; align-items: center; gap: 6px;"><img src="https://huggingface.co/LiquidAI/LFM3-1.7B/resolve/main/assets/icons/blog.svg" width="16" height="16" alt="" aria-hidden="true" style="display: block; flex: 0 0 16px; width: 16px; height: 16px; margin: 0;" /><strong>Blog</strong></a>
  </div>
</div>

# LFM3-VL-2B-GGUF

GGUF version of [LFM3-VL-2B](https://huggingface.co/LiquidAI/LFM3-VL-2B) for local inference on CPUs and GPUs.

Find architecture and usage details in the [original model card](https://huggingface.co/LiquidAI/LFM3-VL-2B).

## Use with llama.cpp
<hr style="margin: -0.7em 0 1.2em 0; border: 0; border-top: 1px solid rgba(127, 127, 127, 0.3);" />

Support for LFM3-VL in [llama.cpp](https://github.com/ggml-org/llama.cpp) is in review in [ggml-org/llama.cpp#31252](https://github.com/ggml-org/llama.cpp/pull/31252), without video input for now. We will update this card when a llama.cpp release supports it. Add a quantization tag to pick a file. With `-hf`, llama.cpp also downloads the vision projector.

```bash
llama-cli -hf LiquidAI/LFM3-VL-2B-GGUF:Q4_0 \
  --temp 0.1 --top-p 1.0 --top-k 50 --min-p 0.0 --repeat-penalty 1.1 \
  --no-reasoning-preserve
```

Type `/image <IMAGE PATH>` in the chat to add an image. More options in the [llama.cpp guide](https://docs.liquid.ai/deployment/on-device/llama-cpp).

## QAD Q4_0 GGUF
<hr style="margin: -0.7em 0 1.2em 0; border: 0; border-top: 1px solid rgba(127, 127, 127, 0.3);" />

The Q4_0 build in this repository is the Quantization-Aware Distillation (QAD) checkpoint,
[`LFM3-VL-2B-QAD-Q4_0.gguf`](https://huggingface.co/LiquidAI/LFM3-VL-2B-GGUF/blob/main/LFM3-VL-2B-QAD-Q4_0.gguf).
It was trained to recover the accuracy lost to Q4_0 quantization.

```bash
llama-cli -hf LiquidAI/LFM3-VL-2B-GGUF \
  --hf-file LFM3-VL-2B-QAD-Q4_0.gguf \
  --temp 0.1 --top-p 1.0 --top-k 50 --min-p 0.0 --repeat-penalty 1.1 \
  --no-reasoning-preserve
```
