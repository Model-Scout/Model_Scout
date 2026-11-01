---
library_name: transformers
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
- ar
- zh
pipeline_tag: image-text-to-text
tags:
- liquid
- lfm2
- lfm2-vl
- edge
- lfm2.5-vl
- lfm2.5
- mlx
base_model: LiquidAI/LFM2.5-1.2B-Base
---

# mlx-community/LFM2.5-VL-1.6B-4bit
This model was converted to MLX format from [`LiquidAI/LFM2.5-VL-1.6B`]() using mlx-vlm version **0.3.10**.
Refer to the [original model card](https://huggingface.co/LiquidAI/LFM2.5-VL-1.6B) for more details on the model.
## Use with mlx

```bash
pip install -U mlx-vlm
```

```bash
python -m mlx_vlm.generate --model mlx-community/LFM2.5-VL-1.6B-4bit --max-tokens 100 --temperature 0.0 --prompt "Describe this image." --image <path_to_image>
```
