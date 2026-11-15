---
language:
- en
- zh
- ko
- ja
license: mit
base_model: zai-org/GLM-5.1
tags:
- glm
- glm-5.1
- moe
- quantized
- fp8
- float8

pipeline_tag: text-generation
library_name: transformers
model_name: GLM-5.1-FP8-Dynamic
quantized_by: mconcat
---

# GLM-5.1-FP8-Dynamic

FP8 dynamic quantized version of [zai-org/GLM-5.1](https://huggingface.co/zai-org/GLM-5.1).

This checkpoint preserves the GLM-5.1 MoE + MLA + DSA architecture from the BF16 source, with all Linear weights quantized to FP8 E4M3 for ~2x compression.

## Quantization Strategy

Per-channel FP8 E4M3 weight quantization with dynamic per-token activation scaling:

| Precision | Layers |
|-----------|--------|
| **FP8 E4M3** | All Linear weights: MLA projections, MLP gate/up/down, expert projections, DSA indexer |
| **BF16** | `lm_head`, `embed_tokens`, MoE router gates, norms |

Architecture match with the BF16 source:

- `model_type=glm_moe_dsa`
- `78` layers (3 dense + 75 MoE, `first_k_dense_replace=3`)
- `n_routed_experts=256`, `num_experts_per_tok=8`, `n_shared_experts=1`

- `max_position_embeddings=202752`
- `hidden_size=6144`, `moe_intermediate_size=2048`
- `vocab_size=154880`

## Calibration

- 512 self-calibration samples generated from GLM-5.1 via OpenRouter (top-tier provider routing)
- 8 diverse categories: math, code, logic, analysis, creative writing, general knowledge, agentic/tool-calling, Korean
- Activation statistics collected layer-by-layer for per-channel FP8 scale computation

## Usage

### SGLang

```bash
python3 -m sglang.launch_server --model mconcat/GLM-5.1-FP8-Dynamic \
  --tensor-parallel-size 8 \
  --dtype bfloat16 \
  --trust-remote-code \
  --mem-fraction-static 0.80
```

### vLLM

```bash
vllm serve mconcat/GLM-5.1-FP8-Dynamic \
  --tensor-parallel-size 8 \
  --dtype bfloat16 \
  --trust-remote-code
```


## Compatibility

| Framework | Supported | Notes |
|-----------|-----------|-------|
| vLLM >= 0.19.0 | Yes | Requires `glm_moe_dsa` + compressed-tensors support |
| SGLang >= 0.5.10 | Yes | Requires GLM-5.1 architecture support |
| transformers >= 5.4.0 | Yes | Direct loading with `device_map="auto"` |

## Notes

- This is a 754B MoE model (~40B active per token). Requires multi-GPU setup for inference (8x 80GB+ GPUs recommended).
- FP8 E4M3 provides ~2x compression over BF16 with minimal quality degradation.
- Compatible with Hopper (SM90) and Blackwell GPUs.
- Dynamic activation scaling — scales computed at inference time, not baked into the checkpoint.
- GLM-5.1 does not ship MTP weights despite `num_nextn_predict_layers=1` in config.

## Blackwell SM120 Patch (RTX PRO 6000 / Workstation GPUs)

If running on Blackwell workstation GPUs (SM 12.0), vLLM 0.19.0 requires patches for FlashMLA sparse attention support:

```bash
# Patch 1: FlashMLA ops - add SM120 to sparse support check
FLASHMLA_OPS=$(python -c "import vllm, os; print(os.path.join(os.path.dirname(vllm.__file__), 'v1/attention/ops/flashmla.py'))") && \
sed -i 's/is_device_capability_family(90)\s*or current_platform.is_device_capability_family(100)/is_device_capability_family(90) or current_platform.is_device_capability_family(100) or current_platform.is_device_capability_family(120)/' "$FLASHMLA_OPS"

# Patch 2: FlashMLA sparse backend - add SM12 to capability check
FLASHMLA_SPARSE=$(python -c "import vllm, os; print(os.path.join(os.path.dirname(vllm.__file__), 'v1/attention/backends/mla/flashmla_sparse.py'))") && \
sed -i 's/return capability.major in \[9, 10\]/return capability.major in [9, 10, 12]/' "$FLASHMLA_SPARSE"

# Patch 3: FlashMLA dense backend (if exists)
FLASHMLA_DENSE=$(python -c "import vllm, os; print(os.path.join(os.path.dirname(vllm.__file__), 'v1/attention/backends/mla/flashmla.py'))") && \
sed -i 's/return capability.major in \[9, 10\]/return capability.major in [9, 10, 12]/' "$FLASHMLA_DENSE" 2>/dev/null || true
```

These patches add SM120 (Blackwell workstation) to the supported compute capability list for GLM-5.1's DSA sparse attention.

## Quantization Process

- **Tool**: Custom layer-by-layer pipeline with native `torch.float8_e4m3fn` dtype
- **Hardware**: Single NVIDIA RTX PRO 6000 Blackwell (96 GB), processed one layer at a time
- **Time**: ~319 minutes for 78 layers
- **Calibration**: 256 samples, per-module activation statistics with MoE expert input hooks
