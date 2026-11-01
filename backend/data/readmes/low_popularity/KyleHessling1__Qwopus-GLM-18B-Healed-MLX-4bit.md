---
license: apache-2.0
base_model:
  - KyleHessling1/Qwopus-GLM-18B-Healed
  - Jackrong/Qwopus3.5-9B-v3.5
  - Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1
tags:
  - mlx
  - mlx-4bit
  - quantized
  - apple-silicon
  - merge
  - frankenmerge
  - qwen3.5
  - reasoning
  - text-generation
  - conversational
  - unsloth
  - agent
  - tool-use
  - chain-of-thought
library_name: mlx
model_type: qwen3_5
pipeline_tag: text-generation
language:
  - en
  - zh
  - ko
  - ja
  - fr
  - de
  - es
---

# Qwopus-GLM-18B-Healed — MLX 4-bit

**Apple Silicon / MLX 4-bit quantization** of the healed Qwopus-GLM-18B frankenmerge. Ready to run on Macs with the [MLX](https://github.com/ml-explore/mlx) framework via [`mlx-lm`](https://github.com/ml-explore/mlx-lm).

- **Source (BF16):** [KyleHessling1/Qwopus-GLM-18B-Healed](https://huggingface.co/KyleHessling1/Qwopus-GLM-18B-Healed)
- **Q4_K_M GGUF (llama.cpp):** [KyleHessling1/Qwopus-GLM-18B-Merged-GGUF](https://huggingface.co/KyleHessling1/Qwopus-GLM-18B-Merged-GGUF)

## Quickstart

```bash
pip install -U "mlx-lm>=0.31.2"
```

```python
from mlx_lm import load, generate

model, tokenizer = load("KyleHessling1/Qwopus-GLM-18B-Healed-MLX-4bit")
print(generate(model, tokenizer, prompt="The capital of France is", max_tokens=64))
```

Or from the CLI:

```bash
python3 -m mlx_lm generate \
  --model KyleHessling1/Qwopus-GLM-18B-Healed-MLX-4bit \
  --prompt "Write a haiku about Apple Silicon." \
  --max-tokens 128
```

Runs comfortably on a 16–24 GB unified-memory Mac (M-series).

## Quantization

| Property | Value |
|---|---|
| **Method** | MLX affine quantization (`mlx_lm.convert -q`) |
| **Bits / weight** | 4 (effective **4.502** after non-quantized layers) |
| **Group size** | 64 |
| **Non-quant dtype** | bfloat16 |
| **Output size** | **~8.4 GB** (2 safetensor shards) |
| **Quantizer version** | `mlx-lm` 0.31.2 / `mlx` 0.31.1 |

Reproducible from the BF16 source with:

```bash
python3 -m mlx_lm convert \
  --hf-path KyleHessling1/Qwopus-GLM-18B-Healed \
  --mlx-path ./Qwopus-GLM-18B-Healed-MLX-4bit \
  -q --q-bits 4 --q-group-size 64
```

## Base Model

A **64-layer frankenmerge** of two of [Jackrong's](https://huggingface.co/Jackrong) Qwen3.5-9B finetunes, healed with a 1000-step QLoRA fine-tune:

- **Layers 0–31:** [Jackrong/Qwopus3.5-9B-v3.5](https://huggingface.co/Jackrong/Qwopus3.5-9B-v3.5) (Opus reasoning distill)
- **Layers 32–63:** [Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1](https://huggingface.co/Jackrong/Qwen3.5-9B-GLM5.1-Distill-v1) (GLM-5.1 reasoning distill)
- **Heal training:** 1000 steps QLoRA (rank 64) on Jackrong's training data to smooth the layer boundary

### Architecture

| Property | Value |
|---|---|
| **Parameters** | ~18B |
| **Layers** | 64 (32 + 32) |
| **Hidden Size** | 4096 |
| **Attention Heads** | 16 (4 KV heads, GQA) |
| **Attention Type** | Hybrid (linear + full, every 4th layer) |
| **Context Length** | 262,144 tokens |
| **Source Precision** | BF16 |

### Capability Suite (from base model)

Beats Qwen 3.6-35B-A3B MoE on a 44-test capability suite at less than half the VRAM:

| | Qwopus-GLM-18B (healed) | Qwen 3.6-35B MoE |
|---|---|---|
| **Score** | **40/44 (90.9%)** | 38/44 (86.4%) |
| **Tool Calling** | 6/6 | 6/6 |
| **Agentic** | 4/4 | 4/4 |
| **Programming** | 12/15 | 12/15 |

Frontend stress tests: **62/63 checks passed** across 6 complex HTML/CSS/JS generation tasks with perfectly balanced braces/parens and zero garbled output.

> Note: benchmarks were measured on the BF16 base / Q4_K_M GGUF. The MLX 4-bit weights are a separate quantization and have not been independently re-benchmarked — expect quality within normal 4-bit quantization variance.

## Known Issues

- The tokenizer emits a Mistral-regex warning on load (inherited from the source repo). Benign for Qwen tokenization in practice.

## Credits

All credit for the source models goes to **[Jackrong](https://huggingface.co/Jackrong)**. The heal training used his published datasets. See the [full merge documentation](https://huggingface.co/KyleHessling1/Qwopus-GLM-18B-Merged-GGUF/blob/main/MERGE_PROCESS.md) for the complete technical workflow.

MLX quantization by [@KyleHessling1](https://huggingface.co/KyleHessling1) using [mlx-lm](https://github.com/ml-explore/mlx-lm).

## License

Apache 2.0 (inherited from source models)

## Contact

Questions, issues, or cool projects? Reach out on X: [@KyleHessling1](https://x.com/KyleHessling1)
