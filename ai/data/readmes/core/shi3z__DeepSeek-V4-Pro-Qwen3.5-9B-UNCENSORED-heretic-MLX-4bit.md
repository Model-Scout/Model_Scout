---
license: apache-2.0
language:
- en
- zh
- ko
- ja
- es
- ru
library_name: mlx
pipeline_tag: text-generation
base_model: xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic
tags:
- mlx
- 4-bit
- qwen3_5
- uncensored
- heretic
---

# DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic (MLX 4-bit)

MLX 4-bit quantization of [xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic)
(itself derived from [Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B](https://huggingface.co/Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B)). Licensed under Apache-2.0 like the original; all credit for the model goes to the original authors.

- Quantization: 4-bit, group size 64 (about 4.5 bits per weight), 4.7 GB
- Converted with `mlx-lm` 0.32.2 (`mlx_lm.convert`, quantized on CPU)
- **Text-only**: the vision tower and the MTP (speculative decoding) weights were not carried over
- Uncensored ("heretic"/abliterated) variant. Use at your own risk.

## Usage
```bash
pip install -U mlx-lm
python -m mlx_lm generate --model shi3z/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-MLX-4bit --prompt "Hello"
```

To use it as the backend for Claude Code, see https://github.com/shi3z/mightyCode
