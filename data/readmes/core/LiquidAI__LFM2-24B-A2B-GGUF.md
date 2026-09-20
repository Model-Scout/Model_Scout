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
- pt
pipeline_tag: text-generation
tags:
- liquid
- lfm2
- edge
- moe
- llama.cpp
- gguf
base_model:
- LiquidAI/LFM2-24B-A2B
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

# LFM2-24B-A2B-GGUF

LFM2 is a family of hybrid models designed for on-device deployment. LFM2-24B-A2B is the largest model in the family, scaling the architecture to 24 billion parameters while keeping inference efficient.

- **Best-in-class efficiency**: A 24B MoE model with only 2B active parameters per token, fitting in 32 GB of RAM for deployment on consumer laptops and desktops.
- **Fast edge inference**: 112 tok/s decode on AMD CPU, 293 tok/s on H100. Fits in 32B GB of RAM with day-one support llama.cpp, vLLM, and SGLang.
- **Predictable scaling**: Quality improves log-linearly from 350M to 24B total parameters, confirming the LFM2 hybrid architecture scales reliably across nearly two orders of magnitude.

![image](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/VhdjtAT5zWTWdVYgW69O0.png)

Find more information about LFM2-24B-A2B in our [blog post](https://www.liquid.ai/blog/).

## How to run LFM2

Example usage with [llama.cpp](https://github.com/ggml-org/llama.cpp):

```
llama-cli -hf LiquidAI/LFM2-24B-A2B-GGUF --conversation \
    --temp 0.1 --top-k 50 --repeat-penalty 1.05
```

## 📬 Contact

- Got questions or want to connect? [Join our Discord community](https://discord.com/invite/liquid-ai)
- If you are interested in custom solutions with edge deployment, please contact [our sales team](https://www.liquid.ai/contact).
