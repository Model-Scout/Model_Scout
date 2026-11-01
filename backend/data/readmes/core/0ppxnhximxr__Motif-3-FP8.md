---
library_name: transformers
pipeline_tag: text-generation
language:
- en
- ko
license: mit
base_model: Motif-Technologies/Motif-3
base_model_relation: quantized
tags:
- motif
- motif-3
- mixture-of-experts
- moe
- fp8
- block-fp8
- e4m3
- vllm
- multilingual
---

# Motif-3 FP8

This is an **unofficial, community-made FP8 quantization** of the released [Motif-Technologies/Motif-3](https://huggingface.co/Motif-Technologies/Motif-3) checkpoint, not Motif-3-Beta. The exact source revision is [`1695f5aa6d97cccc8623a03f93c9c7d5fbb14d45`](https://huggingface.co/Motif-Technologies/Motif-3/commit/1695f5aa6d97cccc8623a03f93c9c7d5fbb14d45).

The recipe follows the expert-only 128x128 block-E4M3 layout used for [0ppxnhximxr/Motif-3-Beta-FP8](https://huggingface.co/0ppxnhximxr/Motif-3-Beta-FP8), while applying it independently to the official Motif-3 weights.

## Summary

- Architecture: 314B-parameter decoder-only MoE, approximately 13.2B active parameters per token
- Quantization: routed-expert projection weights only, FP8 E4M3, 128x128 blocks, W8A16
- Quantized weights: `gate_up_proj` and `down_proj` in all 51 MoE layers
- Quantized tensors: 102
- Quantized parameters: 308,029,685,760
- Scale format: FP32 inverse scales stored as `<weight_name>_scale_inv`
- Dequantization: `W ≈ W_fp8 * scale_inv`
- Checkpoint tensor size: 629,683,551,500 bytes to 321,729,326,780 bytes, a 48.91% reduction

Embeddings, the language-model head, attention, routers, shared experts, dense layers, MTP layers, normalization layers, and all other non-target tensors remain in their original precision.

## Precision compared with the original checkpoint

The following table measures **weight-space fidelity**, not downstream benchmark accuracy. The FP8 statistics were accumulated over every value in all 102 quantized tensors. “Original” is the exact BF16 checkpoint used as the quantization source.

| Metric | Original Motif-3 | This FP8 checkpoint | Interpretation |
|---|---:|---:|---|
| Checkpoint tensor size | 629,683,551,500 bytes (586.44 GiB) | 321,729,326,780 bytes (299.63 GiB) | 48.91% smaller |
| Routed-expert projection precision | BF16 | FP8 E4M3 + FP32 scale per 128x128 block | Expert-only W8A16 |
| Quantized parameters | 0 | 308.03B | 102 tensors across 51 MoE layers |
| Mean cosine similarity | 1.000000 | **0.999650** | 99.9650% directional similarity |
| Minimum tensor cosine similarity | 1.000000 | **0.999650** | Minimum over the 102 target tensors |
| Mean relative RMSE | 0% | **2.6455%** | Mean over the 102 target tensors |
| Maximum relative RMSE | 0% | **2.6458%** | Maximum over the 102 target tensors |
| Maximum absolute weight error | 0 | **0.06808** | Maximum observed element error |
| NaN or Inf after dequantization | 0 | **0** | No non-finite values observed |
| Non-target tensor equality | Reference | **Bit-exact to reference** | Verified for non-quantized tensors |

Cosine similarity is not “model accuracy.” A paired BF16-versus-FP8 benchmark suite has not yet been completed, so no task-accuracy retention percentage is claimed here.

## Validation

The checkpoint was validated in four ways:

1. The source repository was downloaded at the pinned revision and all 167 source files passed local checksum/presence verification.
2. The output index contains 2,338 tensors: the original 2,236 tensors plus exactly 102 FP32 inverse-scale tensors.
3. Three representative 128x128 blocks from each quantized tensor were recomputed from the official BF16 source. All 306 sampled blocks matched the converter's FP8 values and scales exactly.
4. The quantizer output was cross-checked against vLLM's block-FP8 cast with `use_ue8m0=False`; sampled values and scales matched exactly.

The local FP8 tensors were also compared with the Beta-FP8 checkpoint and were different, confirming that these are quantized official Motif-3 weights rather than copied Beta weights.

## Quantization environment

Quantization was performed on 2026-08-10 UTC with the included [`quantization/quantize_motif_fp8.py`](./quantization/quantize_motif_fp8.py).

| Component | Environment |
|---|---|
| Host OS | Ubuntu 24.04, Linux 6.8.0-1046-nvidia, EXT4 |
| CPU / RAM | Intel Xeon Platinum 8480+ / 885 GiB RAM |
| GPU host | 4x NVIDIA H100 80GB HBM3, NVLink NV18 |
| Quantization device | `cuda:0` (one H100 80GB) |
| NVIDIA driver | 580.178.04 |
| CUDA toolkit / PyTorch CUDA | 13.0 / 12.4 |
| Python | 3.12.3 |
| PyTorch | 2.5.1+cu124 |
| Transformers | 4.55.4 |
| Safetensors | 0.8.0 |
| Flash Attention | 2.7.4.post1 |
| Hugging Face Hub / hf-xet | 0.36.2 / 1.6.0 |
| Source download client | Hugging Face Hub 1.27.0 / hf-xet 1.6.0 |
| Source download mode | `HF_XET_HIGH_PERFORMANCE=1` |
| Quantization wall time | Approximately 7.1 minutes summed across 155 shards |

The complete numerical summary is in [`quantization_recipe.json`](./quantization_recipe.json).

## Serving with vLLM

### Important compatibility note

This checkpoint stores arbitrary FP32 inverse scales. The pinned Motif vLLM image supports online block-FP8 conversion from BF16 but does not directly load this serialized layout without a small runtime patch. The reproducible patch and Dockerfile used for the smoke tests are included in [`serving/`](./serving/).

The patch is intentionally pinned to:

```text
ghcr.io/motiftechnologies/vllm:v0.20.2-motif3.rc3
```

Build the serving image:

```bash
git clone https://huggingface.co/0ppxnhximxr/Motif-3-FP8
cd Motif-3-FP8
docker build -t motif-vllm:direct-fp8 serving
```

The following conservative command matches the tested 4x H100 80GB topology. It uses CPU/UVA offload because the model and usable KV cache do not comfortably fit in 4x 80GB without it.

```bash
docker run --rm --gpus all --ipc=host --shm-size=64g \
  -p 8080:8080 \
  -e HF_XET_HIGH_PERFORMANCE=1 \
  -e VLLM_USE_DEEP_GEMM_E8M0=0 \
  -v "$HOME/.cache/huggingface:/root/.cache/huggingface" \
  motif-vllm:direct-fp8 \
  vllm serve 0ppxnhximxr/Motif-3-FP8 \
    --trust-remote-code \
    --hf-overrides '{"quantization_config":{"quant_method":"modelopt_blockfp8","direct_load":true}}' \
    --tensor-parallel-size 4 \
    --enable-expert-parallel \
    --dtype bfloat16 \
    --cpu-offload-gb 4.2 \
    --gpu-memory-utilization 0.98 \
    --max-model-len 512 \
    --block-size 128 \
    --enable-auto-tool-choice \
    --tool-call-parser motif \
    --reasoning-parser motif \
    --host 0.0.0.0 --port 8080
```

Check the endpoint:

```bash
curl http://127.0.0.1:8080/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "0ppxnhximxr/Motif-3-FP8",
    "messages": [{"role": "user", "content": "대한민국의 수도를 한 문장으로 답해줘."}],
    "temperature": 0,
    "max_tokens": 64
  }'
```

The 512-token context limit above was used only for the constrained H100 smoke test. It is not the model's architectural limit. Larger context lengths need substantially more KV-cache memory and were not validated on this topology. The upstream Motif-3 card recommends H200 or B200-class deployments for the full model.

## Quantization reproduction

After downloading the pinned BF16 source, run:

```bash
python quantization/quantize_motif_fp8.py \
  --src /path/to/Motif-3 \
  --dst /path/to/Motif-3-FP8 \
  --device cuda:0
```

The converter quantizes only tensors ending in:

```text
.moe.experts.gate_up_proj
.moe.experts.down_proj
```

Each `[expert, output, input]` tensor is divided into 128x128 blocks. For each block, it stores E4M3 values and an FP32 inverse scale computed from `amax / 448`.

## Limitations

- No full downstream benchmark parity run against the original BF16 model has been completed.
- The reported fidelity values measure weights, not task accuracy or perplexity.
- Long-context behavior was not evaluated.
- Direct loading currently requires the included patch against the exact pinned Motif vLLM image.
- Generic Transformers loading is not a supported inference path for this serialized FP8 layout.
- CPU/UVA offload makes 4x H100 80GB serving possible but can reduce throughput.

For architecture details, intended use, training data, safety considerations, and the original benchmark results, see the [official Motif-3 model card](https://huggingface.co/Motif-Technologies/Motif-3).

## License and attribution

The upstream Motif-3 checkpoint is published under the MIT license. This repository contains a quantized transformation of those weights. Motif-3 was created by [Motif Technologies](https://motiftech.io); this community repository is not an official Motif Technologies release.
