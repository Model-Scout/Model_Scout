---
library_name: gguf
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- ar
- zh
- en
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
pipeline_tag: image-text-to-text
base_model: LiquidAI/LFM2.5-VL-3B
tags:
- liquid
- lfm2
- lfm2-vl
- edge
- lfm2.5
- lfm2.5-vl
- gguf
- llama.cpp
---

<div align="center">
  <img
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png"
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
  <div style="display: flex; justify-content: center; gap: 0.5em; margin-bottom: 1em;">
    <a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> •
    <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> •
    <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> •
    <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
  </div>
</div>

# LFM2.5-VL-3B-GGUF

LFM2.5 is a new generation of hybrid models developed by [Liquid AI](https://www.liquid.ai/), specifically designed for edge AI and on-device deployment. It sets a new standard in terms of quality, speed, and memory efficiency.

Find more details in the original model card: https://huggingface.co/LiquidAI/LFM2.5-VL-3B

## 🏃 How to run LFM2.5-VL-3B

Example usage with [llama.cpp](https://github.com/ggml-org/llama.cpp):

```bash
llama-cli \
  -hf LiquidAI/LFM2.5-VL-3B-GGUF \
  --temp 0.2 \
  --top-k 50 \
  --repeat-penalty 1.0
```

Then you can type `/image <IMAGE PATH>` to add an image to the chat, then ask `What is in the image?` or any other question about the image.
