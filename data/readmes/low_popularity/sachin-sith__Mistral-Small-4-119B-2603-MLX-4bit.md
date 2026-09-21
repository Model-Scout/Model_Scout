---
license: apache-2.0
base_model: mistralai/Mistral-Small-4-119B-2603
language:
  - en
  - fr
  - de
  - es
  - pt
  - it
  - ja
  - ko
  - zh
library_name: mlx
tags:
  - mlx
  - mistral
  - moe
  - mla
  - 4-bit
  - quantized
  - apple-silicon
pipeline_tag: text-generation
---

# Mistral Small 4 119B — MLX 4-bit

4-bit quantized [MLX](https://github.com/ml-explore/mlx) version of [mistralai/Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) for inference on Apple Silicon.

## Model Details

| Property | Value |
|---|---|
| Base model | [mistralai/Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) |
| Architecture | MoE + MLA (Multi-head Latent Attention) |
| Total parameters | 119B |
| Active parameters | 6.5B per token (128 experts, 4 active) |
| Quantization | 4-bit (~4.5 bits per weight) |
| Model size on disk | ~62 GB |
| Context length | 256K tokens |
| Multimodal | Text + image input, text output |
| Languages | 24+ (en, fr, de, es, pt, it, ja, ko, zh, and more) |
| License | Apache 2.0 |

## Requirements

- Apple Silicon Mac with 64GB+ unified memory (128GB recommended)
- Python 3.10+
- `mlx-lm` with Mistral4 architecture support

### Important: mlx-lm compatibility

As of 2026-03-21, the stable `mlx-lm` pip release does **not** support `model_type: mistral4`. You need mlx-lm from the main branch or a patched version.

```bash
# Option 1: Install from main (once Mistral4 support is merged)
pip install git+https://github.com/ml-explore/mlx-lm.git

# Option 2: Install stable + manually add mistral4.py
pip install mlx-lm
# Then add mistral4.py to mlx_lm/models/ and update mistral3.py
```

## Usage

```python
from mlx_lm import load, generate

model, tokenizer = load("sachin-sith/Mistral-Small-4-119B-2603-MLX-4bit")

messages = [{"role": "user", "content": "Explain quantum computing in simple terms."}]
text = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
response = generate(model, tokenizer, prompt=text, max_tokens=256)
print(response)
```

## Conversion Details

Mistral Small 4 uses a novel architecture not yet supported in the stable mlx-lm release. A custom `mistral4.py` model implementation was created, handling:

- **MLA (Multi-head Latent Attention)**: Compressed KV cache via latent projections (`q_lora_rank=1024`, `kv_lora_rank=256`, `qk_nope_head_dim=64`, `qk_rope_head_dim=64`)
- **MoE with shared experts**: 128 routed experts + 1 shared expert, top-4 routing with softmax gate
- **FP8 dequantization**: Original weights are FP8 with per-tensor scalar scale factors
- **Fused expert weight splitting**: `gate_up_proj` split into separate `gate_proj` and `up_proj`
- **KV projection splitting**: `kv_b_proj` split into `embed_q` and `unembed_out` for MLA

## Also Available

- [Mistral-Small-4-119B-2603-MLX-8bit](https://huggingface.co/sachin-sith/Mistral-Small-4-119B-2603-MLX-8bit) — 8-bit version (~118 GB)

## Original Model

- [mistralai/Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)
