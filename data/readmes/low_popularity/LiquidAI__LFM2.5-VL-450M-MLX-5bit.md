---
library_name: mlx
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
- lfm2.5-vl
- lfm2.5
- edge
- mlx
base_model: LiquidAI/LFM2.5-VL-450M
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

# LFM2.5-VL-450M-MLX-5bit

MLX export of [LFM2.5-VL-450M](https://huggingface.co/LiquidAI/LFM2.5-VL-450M) for Apple Silicon inference.

LFM2.5-VL-450M is a vision-language model built on the LFM2.5-350M backbone with a SigLIP2 NaFlex vision encoder (86M).
It supports OCR, document comprehension, multilingual vision understanding, bounding box prediction, and function calling.

## Model Details

| Property | Value |
|----------|-------|
| Parameters | 450M |
| Precision | 5-bit |
| Group Size | 64 |
| Size | 0.39 GB |
| Context Length | 32K |
| Vision Encoder | SigLIP2 NaFlex (86M) |
| Native Resolution | up to 512x512 |

## Quickstart

```bash
uv pip install 'mlx-vlm==0.3.9'
```

```python
from mlx_vlm import load, generate
from mlx_vlm.utils import load_image

model, processor = load("LiquidAI/LFM2.5-VL-450M-MLX-5bit")

image = load_image("photo.jpg")

# Apply chat template (required for LFM2.5-VL)
messages = [{"role": "user", "content": [
    {"type": "image"},
    {"type": "text", "text": "What do you see in this image?"},
]}]
prompt = processor.apply_chat_template(messages, add_generation_prompt=True)

result = generate(
    model,
    processor,
    prompt,
    [image],
    temp=0.1,
    min_p=0.15,
    repetition_penalty=1.05,
    verbose=True,
)
print(result.text)
```

### Recommended Sampling Parameters

| Parameter | Value |
|-----------|-------|
| temperature | 0.1 |
| min_p | 0.15 |
| repetition_penalty | 1.05 |

## License

This model is released under the [LFM 1.0 License](LICENSE).
