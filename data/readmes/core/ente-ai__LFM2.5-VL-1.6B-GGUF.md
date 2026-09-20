---
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
- ja
- ko
- fr
- es
- de
- it
- pt
- ar
- zh
pipeline_tag: image-text-to-text
tags:
- liquid
- edge
- lfm2.5-vl
- lfm2.5
- edge
- llama.cpp
- gguf
base_model:
- LiquidAI/LFM2.5-VL-1.6B
---

<div align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png" alt="Liquid AI" style="width: 100%; max-width: 100%;">
</div>
<div style="display: flex; justify-content: center; gap: 0.5em;">
<a href="https://playground.liquid.ai/chat?model=lfm2.5-vl-1.6b"><strong>Try LFM</strong></a> • <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> • <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> • <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
</div>

<br>

# LFM2.5-VL-1.6B

Find more details in the original model card: https://huggingface.co/LiquidAI/LFM2.5-VL-1.6B

## 🏃 How to run LFM2.5-VL-1.6B

Example usage with [llama.cpp](https://github.com/ggml-org/llama.cpp):

```bash
llama-cli \
  -hf LiquidAI/LFM2.5-VL-3B-GGUF \
  --temp 0.1 \
  --min-p 0.15 \
  --repeat-penalty 1.05
```

Then you can type `/image <IMAGE PATH>` to add an image to the chat, then ask `What is in the image?` or any other question about the image.

## 📬 Contact

- Got questions or want to connect? [Join our Discord community](https://discord.com/invite/liquid-ai)
- If you are interested in custom solutions with edge deployment, please contact [our sales team](https://www.liquid.ai/contact).
