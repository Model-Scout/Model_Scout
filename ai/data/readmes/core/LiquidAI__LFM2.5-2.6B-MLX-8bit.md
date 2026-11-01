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
pipeline_tag: text-generation
tags:
- liquid
- lfm2.5
- edge
- mlx
base_model: LiquidAI/LFM2.5-2.6B
---

<div align="center">
  <img
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png"
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
  <div style="display: flex; justify-content: center; gap: 0.5em; margin-bottom: 1em;">
    <a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> &bull;
    <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> &bull;
    <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> &bull;
    <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
  </div>
</div>
<br>

# LFM2.5-2.6B-MLX-8bit

MLX export of [LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B) for Apple Silicon inference.

LFM2.5-2.6B is a compact multilingual model built on LiquidAI's hybrid architecture, combining convolutional and attention layers for efficient long-context processing.

## Model Details

| Property | Value |
|----------|-------|
| Parameters | 2.6B |
| Precision | 8-bit |
| Group Size | 64 |
| Size | 2.67 GB |
| Context Length | 131072 |

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate
from mlx_lm.sample_utils import make_sampler

model, tokenizer = load("LiquidAI/LFM2.5-2.6B-MLX-8bit")

response = generate(
    model,
    tokenizer,
    prompt="The capital of France is",
    max_tokens=100,
    sampler=make_sampler(temp=0.7),
    verbose=True,
)
```

## Other Precisions

- [LFM2.5-2.6B-MLX-bf16](https://huggingface.co/LiquidAI/LFM2.5-2.6B-MLX-bf16) (5.02 GB)
- [LFM2.5-2.6B-MLX-8bit](https://huggingface.co/LiquidAI/LFM2.5-2.6B-MLX-8bit) (2.67 GB)
- [LFM2.5-2.6B-MLX-6bit](https://huggingface.co/LiquidAI/LFM2.5-2.6B-MLX-6bit) (2.04 GB)
- [LFM2.5-2.6B-MLX-5bit](https://huggingface.co/LiquidAI/LFM2.5-2.6B-MLX-5bit) (1.76 GB)
- [LFM2.5-2.6B-MLX-4bit](https://huggingface.co/LiquidAI/LFM2.5-2.6B-MLX-4bit) (1.47 GB)
- [LFM2.5-2.6B-MLX-mxfp8](https://huggingface.co/LiquidAI/LFM2.5-2.6B-MLX-mxfp8) (2.59 GB)
- [LFM2.5-2.6B-MLX-mxfp4](https://huggingface.co/LiquidAI/LFM2.5-2.6B-MLX-mxfp4) (1.46 GB)
- [LFM2.5-2.6B-MLX-nvfp4](https://huggingface.co/LiquidAI/LFM2.5-2.6B-MLX-nvfp4) (1.53 GB)

## License

This model is released under the [LFM 1.0 License](LICENSE).
