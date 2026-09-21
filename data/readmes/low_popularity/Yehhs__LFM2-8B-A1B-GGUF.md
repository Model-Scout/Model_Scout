---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
pipeline_tag: text-generation
tags:
- liquid
- lfm2
- edge
- moe
- llama.cpp
- gguf
base_model:
- LiquidAI/LFM2-8B-A1B
new_version: LiquidAI/LFM2.5-8B-A1B-GGUF
---

<center>
<div style="text-align: center;">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png" 
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
</div>
<div style="display: flex; justify-content: center; gap: 0.5em;">
<a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> • <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> • <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> • <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
</div>
</center>

<br>

# LFM2-8B-A1B-GGUF

LFM2 is a new generation of hybrid models developed by [Liquid AI](https://www.liquid.ai/), specifically designed for edge AI and on-device deployment. It sets a new standard in terms of quality, speed, and memory efficiency. 

We're releasing the weights of our first MoE based on LFM2, with 8.3B total parameters and 1.5B active parameters.

- LFM2-8B-A1B is the best on-device MoE in terms of both **quality** (comparable to 3-4B dense models) and **speed** (faster than Qwen3-1.7B).
- **Code and knowledge** capabilities are significantly improved compared to LFM2-2.6B.
- Quantized variants fit comfortably on high-end **phones, tablets, and laptops**.

Find more information about LFM2-8B-A1B in our [blog post](https://www.liquid.ai/blog/).

## 🏃 How to run LFM2

Example usage with [llama.cpp](https://github.com/ggml-org/llama.cpp):

```
llama-cli -hf LiquidAI/LFM2-8B-A1B-GGUF
```