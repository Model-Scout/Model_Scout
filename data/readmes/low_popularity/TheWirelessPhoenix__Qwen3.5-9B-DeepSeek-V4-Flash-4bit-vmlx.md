---
base_model: Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash
tags:
- text-generation-inference
- transformers
- unsloth
- qwen3_5
- reasoning
- distillation
- deepseek
- deepseek-v4
- sft
- long-cot
- chain-of-thought
- efficient-inference
- agent
- multilingual
- mlx
license: apache-2.0
language:
- en
- zh
- ko
- ja
- es
- ru
pipeline_tag: image-text-to-text
datasets:
- Jackrong/DeepSeek-V4-Distill-8000x
library_name: mlx
---

# TheWirelessPhoenix/Qwen3.5-9B-DeepSeek-V4-Flash-4bit-vmlx

This model was converted to MLX format from [`Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash`](https://huggingface.co/Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash)
using mlx-vlm version **0.6.8**.
Refer to the [original model card](https://huggingface.co/Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash) for more details on the model.

## Use with mlx

```bash
pip install -U mlx-vlm
```

```bash
python -m mlx_vlm.generate --model TheWirelessPhoenix/Qwen3.5-9B-DeepSeek-V4-Flash-4bit-vmlx --max-tokens 100 --temperature 0.0 --prompt "Describe this image." --image <path_to_image>
```
