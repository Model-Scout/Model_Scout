---
license: mit
language:
- zh
- en
- fr
- es
- ru
- de
- ja
- ko
library_name: mlx
base_model: zai-org/GLM-OCR
pipeline_tag: image-text-to-text
tags:
- mlx
---

# EZCon/GLM-OCR-mlx

This model was converted to MLX format from [`zai-org/GLM-OCR`](https://huggingface.co/zai-org/GLM-OCR)
using mlx-vlm version **0.6.12**.
Refer to the [original model card](https://huggingface.co/zai-org/GLM-OCR) for more details on the model.

## Use with mlx

```bash
pip install -U mlx-vlm
```

```bash
python -m mlx_vlm.generate --model EZCon/GLM-OCR-mlx --max-tokens 100 --temperature 0.0 --prompt "Describe this image." --image <path_to_image>
```
