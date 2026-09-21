---
base_model: InternScience/Agents-A1
language:
  - en
  - zh
  - hi
  - ar
  - ru
  - ja
  - ko
  - nl
  - fr
  - es
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
tags:
  - gptq
  - int4
  - symmetric
  - moe
  - agentic
  - auto-round
  - marlin
  - sglang
  - vllm
---

# Agents-A1-GPTQ-INT4-Sym

Symmetric INT4 GPTQ quantization of [InternScience/Agents-A1](https://huggingface.co/InternScience/Agents-A1), a 35B Mixture-of-Experts agentic model with 256 experts and hybrid Mamba/attention architecture.


## Why this quant?

The community AWQ-INT4 release (`cyankiwi/Agents-A1-AWQ-INT4`) uses **asymmetric** INT4 quantization via the `compressed-tensors` format. SGLang's compressed-tensors MoE path only supports **symmetric** weight-only quantization for the Marlin MoE kernel — the `_is_wNa16_group_channel` gate in `get_moe_scheme()` requires `symmetric=True`. Asymmetric quants fail this check and fall through to the W8A8 detection path, which crashes with `AttributeError: 'NoneType' object has no attribute 'num_bits'` because `input_activations` is `None` in weight-only quantization.

This model was re-quantized with **symmetric** GPTQ to be Marlin-compatible, matching the format used by the working `palmfuture/Qwen3.6-35B-A3B-GPTQ-Int4` model (which uses `sym=True`, `group_size=128`).

## Quantization Details

| Parameter | Value |
|-----------|-------|
| **Base model** | InternScience/Agents-A1 (BF16, ~65 GB) |
| **Algorithm** | AutoRound (sign gradient descent) |
| **Recipe** | `auto-round-best` (1000 iterations per block) |
| **Export format** | GPTQ (`auto_gptq`) |
| **Bits** | 4 |
| **Group size** | 128 |
| **Symmetric** | true |
| **DescAct** | false |
| **Weight-only** | true (W4A16, no activation quantization) |
| **Calibration dataset** | ultrachat_200k |
| **Calibration samples** | 512 |
| **Sequence length** | 2048 |
| **Learning rate** | 0.001 |
| **Tool** | [AutoRound](https://github.com/intel/auto-round) v0.14.0 |
| **Hardware** | 4× NVIDIA RTX 3090 (24 GB each) |
| **Quantization time** | ~18 hours |
| **Output size** | ~22 GB (6 safetensors shards) |

### Ignored layers (kept in BF16/FP16)

These layers are excluded from quantization for quality and Marlin kernel compatibility:

- `.*attn.*` — attention projections (hybrid linear/full attention)
- `.*mlp\.gate$` — MoE router (must NOT be quantized for Marlin MoE kernel)
- `.*shared_expert.*` — shared expert MLP
- `.*mtp.*` — multi-token prediction head
- `.*visual.*` — vision encoder (not needed for text-only serving)
- `lm_head` — output projection
- `model.language_model.embed_tokens` — token embeddings

**Result:** 30,720 of 31,181 layers quantized to INT4. All 256 MoE expert projections per layer (gate_proj, up_proj, down_proj × 256 experts × 40 layers) are quantized.

## Model Architecture

| Parameter | Value |
|-----------|-------|
| Architecture | `Qwen3_5MoeForConditionalGeneration` |
| Total parameters | ~35B |
| Active parameters per token | ~3B |
| Hidden size | 2048 |
| Layers | 40 |
| Routed experts | 256 (8 active per token) |
| Shared experts | 1 |
| MoE intermediate size | 512 |
| Max context | 262,144 |
| Vocabulary | 248,320 |
| Attention | Hybrid (full attention every 4th layer, linear/Mamba otherwise) |
| Vision | Built-in vision encoder (ViT depth 27, hidden 1152) |

## Deployment

### SGLang

```bash
python -m sglang.launch_server \
  --model-path compute1/Agents-A1-GPTQ-INT4-Sym \
  --served-model-name agents-a1 \
  --trust-remote-code \
  --quantization moe_wna16 \
  --tensor-parallel-size 2 \
  --context-length 262144 \
  --mem-fraction-static 0.87 \
  --reasoning-parser qwen3 \
  --tool-call-parser qwen3_coder \
  --enable-hierarchical-cache \
  --enable-mixed-chunk \
  --dtype float16 \
  --host 0.0.0.0 \
  --port 8000
```

### vLLM

```bash
vllm serve compute1/Agents-A1-GPTQ-INT4-Sym \
  --served-model-name agents-a1 \
  --trust-remote-code \
  --tensor-parallel-size 2 \
  --max-model-len 262144 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder
```

## Recommended Sampling Parameters

From the original model card:

- `temperature`: 0.85
- `top_p`: 0.95
- `top_k`: 20
- `min_p`: 0.0
- `presence_penalty`: 1.1
- `repetition_penalty`: 1.0

## VRAM Requirements

Measured on 2× RTX 3090 (24 GB each) with TP=2, `--quantization moe_wna16`, `--mem-fraction-static 0.87`, `--dtype float16`:

| Component | Per-GPU | Notes |
|-----------|---------|-------|
| Model weights (INT4 GPTQ) | 10.53 GB | 256 experts × 40 layers, packed int32 |
| KV cache (float16) | 5.02 GB | 525,638 tokens |
| Mamba SSM state | 4.52 GB | conv_state 0.10 GB + ssm_state 4.42 GB |
| CUDA graphs | 0.20 GB | batch sizes [1, 2, 4, 8, 12] |
| Other overhead | 2.99 GB | init + workspace + buffers |
| **Total used** | **~23.3 GB** | |
| **Free headroom** | **~0.7 GB** | |

The model fits on 2× RTX 3090 (24 GB each). For additional KV cache headroom, `--kv-cache-dtype fp8_e5m2` can be used to double KV token capacity.

Quantization was performed on 4× RTX 3090 with pipeline parallelism, using ~68 GB peak RAM and ~16 GB peak VRAM on the primary GPU.

## Acknowledgements

- [InternScience](https://huggingface.co/InternScience) for the original Agents-A1 model
- [Intel AutoRound team](https://github.com/intel/auto-round) for the quantization toolkit
- Model card adapted from the [original model card](https://huggingface.co/InternScience/Agents-A1)

## License

Apache-2.0, inherited from InternScience/Agents-A1.