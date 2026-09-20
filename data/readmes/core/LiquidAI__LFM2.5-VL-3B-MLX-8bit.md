---
library_name: mlx
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
tags:
- liquid
- lfm2
- lfm2-vl
- edge
- lfm2.5
- lfm2.5-vl
- mlx
- mlx_vlm
base_model: LiquidAI/LFM2.5-VL-3B
---

<div align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png" alt="Liquid AI" style="width: 100%; max-width: 100%;">

  <p>
    <a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> •
    <a href="https://docs.liquid.ai/lfm"><strong>Documentation</strong></a> •
    <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> •
    <a href="https://www.liquid.ai/blog/"><strong>Blog</strong></a>
  </p>
</div>

# LFM2.5-VL-3B-MLX-8bit

MLX export of [LFM2.5-VL-3B](https://huggingface.co/LiquidAI/LFM2.5-VL-3B) for Apple Silicon inference.

LFM2.5-VL-3B is a vision-language model built on the LFM2.5-2.6B backbone with a SigLIP2 NaFlex vision encoder (400M).
It supports OCR, document comprehension, multilingual vision understanding, bounding box prediction, and function calling.

## Quickstart

```bash
uv run --with mlx-vlm mlx_vlm.generate --model LiquidAI/LFM2.5-VL-3B-MLX-8bit --max-tokens 100 --temperature 0.2 --image https://placecats.com/neo/300/200 --prompt "how many animals are in the picture?"
```

```python
from mlx_vlm import apply_chat_template, generate, load
from mlx_vlm.utils import load_image

model, processor = load("LiquidAI/LFM2.5-VL-3B-MLX-8bit")

image = load_image("https://placecats.com/neo/300/200")

messages = [
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "text", "text": "What do you see in this image?"},
        ],
    }
]
prompt = apply_chat_template(
    processor,
    model.config,
    messages,
    add_generation_prompt=True,
    num_images=1,
)

result = generate(
    model,
    processor,
    prompt,
    [image],
    temp=0.2,
    top_k=50,
    repetition_penalty=1.0,
    verbose=True,
)
print(result.text)
```
