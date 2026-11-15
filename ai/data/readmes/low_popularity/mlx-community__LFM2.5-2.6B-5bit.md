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

# mlx-community/LFM2.5-2.6B-5bit

This model was converted to MLX format from [`LiquidAI/LFM2.5-2.6B`](https://huggingface.co/LiquidAI/LFM2.5-2.6B)
using mlx-vlm version **0.6.10**.
Refer to the [original model card](https://huggingface.co/LiquidAI/LFM2.5-2.6B) for more details on the model.

## Use with mlx

```bash
pip install -U mlx-vlm
```

```bash
python -m mlx_vlm.generate --model mlx-community/LFM2.5-2.6B-5bit --max-tokens 100 --temperature 0.0 --prompt "Describe this image." --image <path_to_image>
```
