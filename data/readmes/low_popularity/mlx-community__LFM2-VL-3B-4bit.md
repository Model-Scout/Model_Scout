---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
- ja
- fr
- es
- de
- it
- pt
- ar
- zh
- ko
pipeline_tag: image-text-to-text
tags:
- liquid
- lfm2
- lfm2-vl
- edge
- mlx
---

# mlx-community/LFM2-VL-3B-4bit
This model was converted to MLX format from [`LiquidAI/LFM2-VL-3B`]() using mlx-vlm version **0.3.4**.
Refer to the [original model card](https://huggingface.co/LiquidAI/LFM2-VL-3B) for more details on the model.
## Use with mlx

```bash
pip install -U mlx-vlm
```

```bash
python -m mlx_vlm.generate --model mlx-community/LFM2-VL-3B-4bit --max-tokens 100 --temperature 0.0 --prompt "Describe this image." --image <path_to_image>
```
