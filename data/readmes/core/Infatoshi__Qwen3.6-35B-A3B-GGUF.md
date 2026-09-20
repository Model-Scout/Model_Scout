---
license: apache-2.0
base_model: Qwen/Qwen3.6-35B-A3B
base_model_relation: quantized
language:
- en
- zh
- multilingual
pipeline_tag: image-text-to-text
library_name: gguf
tags:
- gguf
- llama.cpp
- qwen3_5_moe
- multimodal
- vision
- moe
---

# Qwen3.6-35B-A3B-GGUF

GGUF conversions of [`Qwen/Qwen3.6-35B-A3B`](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) for llama.cpp.

Sparse MoE: 35B total / 3B active (256 experts + 1 shared, top-8 routed). Hybrid Gated-DeltaNet + Gated-Attention layers (3:1), 262K native context. Includes vision projector for image/video input.

## Files

| File | Size | Target HW |
|---|---|---|
| `Qwen3.6-35B-A3B-Q4_K_M.gguf` | 20 GB | Single 24GB GPU (3090/4090/5090/A5000) |
| `Qwen3.6-35B-A3B-Q5_K_M.gguf` | 23 GB | 32GB+ VRAM or partial offload |
| `Qwen3.6-35B-A3B-Q8_0.gguf` | 34 GB | 40GB+ VRAM (A6000/A100) or CPU |
| `Qwen3.6-35B-A3B-BF16.gguf` | 65 GB | CPU or multi-GPU |
| `Qwen3.6-35B-A3B-mmproj-BF16.gguf` | 862 MB | Required for vision input |

## Benchmarks (RTX 3090, bs=1, llama.cpp build b1-94ca829)

| Quant | Offload | Prefill | Decode | wikitext-2-raw PPL |
|---|---|---|---|---|
| Q4_K_M | 41/41 GPU | 329.7 t/s | 153.9 t/s | 6.676 ± 0.043 |
| Q5_K_M | 36/41 GPU | 159.9 t/s | 82.9 t/s | — |

Q5_K_M / Q8_0 / BF16 do not fit a single 24GB GPU at usable context.

## Usage

### Text

```bash
llama-cli -m Qwen3.6-35B-A3B-Q4_K_M.gguf -ngl 99 -c 8192 -p "Your prompt"
```

### Vision (image/video)

```bash
llama-mtmd-cli -m Qwen3.6-35B-A3B-Q4_K_M.gguf \
  --mmproj Qwen3.6-35B-A3B-mmproj-BF16.gguf \
  --image path/to/image.jpg -p "Describe this image"
```

## Notes

- Architecture: `Qwen3_5MoeForConditionalGeneration` (`qwen3_5_moe`)
- Converter: llama.cpp `convert_hf_to_gguf.py` (built-in support)
- At bs=1 decode, the GPU is kernel-launch bound; prefill or batched serving will show higher utilization
- For long context (>262K), see base model's YaRN config
