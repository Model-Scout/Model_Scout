---
library_name: mlx
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
- it
pipeline_tag: text-generation
tags:
- liquid
- lfm2.5
- edge
- mlx
base_model: LiquidAI/LFM2.5-230M
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

# LFM2.5-230M-MLX-bf16

MLX export of [LFM2.5-230M](https://huggingface.co/LiquidAI/LFM2.5-230M) for Apple Silicon inference.

LFM2.5-230M is a compact multilingual model built on LiquidAI's hybrid architecture, combining convolutional and attention layers for efficient long-context processing.

## Model Details

| Property | Value |
|----------|-------|
| Parameters | 230M |
| Precision | bf16 |
| Size | 438 MB |
| Context Length | 128K |

## Use with mlx

```bash
pip install mlx-lm
```

```python
from mlx_lm import load, generate
from mlx_lm.sample_utils import make_sampler

model, tokenizer = load("LiquidAI/LFM2.5-230M-MLX-bf16")

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

- [LFM2.5-230M-MLX-bf16](https://huggingface.co/LiquidAI/LFM2.5-230M-MLX-bf16) (438 MB)
- [LFM2.5-230M-MLX-8bit](https://huggingface.co/LiquidAI/LFM2.5-230M-MLX-8bit) (233 MB)
- [LFM2.5-230M-MLX-6bit](https://huggingface.co/LiquidAI/LFM2.5-230M-MLX-6bit) (178 MB)
- [LFM2.5-230M-MLX-5bit](https://huggingface.co/LiquidAI/LFM2.5-230M-MLX-5bit) (159 MB)
- [LFM2.5-230M-MLX-4bit](https://huggingface.co/LiquidAI/LFM2.5-230M-MLX-4bit) (139 MB)

## License

This model is released under the [LFM 1.0 License](LICENSE).
