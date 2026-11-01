---
license: other
license_name: nvidia-open-model-agreement
license_link: LICENSE
base_model: Piecrust/GLM-5.3-Flash-FP4-Abliterated
base_model_relation: quantized
library_name: mlx
pipeline_tag: image-text-to-text
language:
  - en
  - ko
  - zh
tags:
  - mlx
  - apple-silicon
  - glm
  - glm-5.3
  - moe
  - nvfp4
  - mxfp8
  - qad
  - mtp
  - uncensored
  - abliterated
---

# GLM-5.3-Flash-FP4-Local-Piecrust-Abliterated-MLX

An MLX repack of [Piecrust/GLM-5.3-Flash-FP4-Abliterated](https://huggingface.co/Piecrust/GLM-5.3-Flash-FP4-Abliterated) (rev `5c15d091`) for MLX/oMLX. It keeps NVIDIA QAD FP4-Local's routed experts unchanged and includes the rank-1 refusal-direction edit to 44 matrices (`self_attn.o_proj` and `mlp.shared_experts.down_proj`, layers 15-36). This does not guarantee compliance with every request.

**Held-out NLL is 3.18% lower than uniform 4-bit MLX, with a +0.36% NLL cost against the [non-abliterated FP4-Local](https://huggingface.co/junmo-k/GLM-5.3-Flash-FP4-Local-MLX).** The edit cost was +0.46% on the older engine; the new measurements are distinguished below. The checkpoint is about 174.33 GiB and runs on [oMLX](https://github.com/jundot/omlx) [v0.7.1](https://github.com/jundot/omlx/releases/tag/v0.7.1) or later.

NLL for this repository was measured with this repository's Piecrust weights. The speed and memory figures below were **measured with the non-abliterated FP4-Local**. The two have the same tensor formats and sizes, but identical MTP acceptance or generation speed has not been established. Not affiliated with NVIDIA, Z.AI, Piecrust or Huihui.

## Requirements

Requires [oMLX](https://github.com/jundot/omlx) [v0.7.1](https://github.com/jundot/omlx/releases/tag/v0.7.1) or later, which includes [PR #4661](https://github.com/jundot/omlx/pull/4661) and its expert-offload follow-up. Measured on an Apple M5 Ultra (256GB) with MLX 0.32.4 and mlx-vlm 0.7.8. Not tested: stock mlx-vlm outside oMLX, Macs with other memory sizes, vision, and the full long-context range.

## Quality against uniform 4-bit

The baseline is a local copy of [pipenetwork/GLM-5.3-Flash-MLX-4bit](https://huggingface.co/pipenetwork/GLM-5.3-Flash-MLX-4bit), a standard affine 4-bit, group-64 conversion from the same GLM model family, with only 33 indexer modules at 8-bit. Both sides use the PR engine with identical inference source, libraries and evaluation windows. The non-abliterated FP4-Local NLL comes from an earlier run on a pre-squash build of the same PR whose inference source was verified identical to `04678f78e` (only one test line differs). The new 4-bit and Piecrust NLL runs and all speed measurements use `04678f78e`. This compares the complete models, including the QAD checkpoint, non-expert precision and repack format; it does not isolate the effect of a 4-bit algorithm alone.

Held-out NLL uses two disjoint sets of 120 teacher-forced 512-token windows that were not used for calibration. The 10 categories are English, code, reasoning, chat, tool calling, Chinese, Korean and three categories from private Korean/English working notes. Windows are paired across models; intervals are 95% window bootstrap with 10,000 resamples. Private text is not released. These numbers measure prediction loss on these windows, not conversation preference or a general benchmark score.

| Set | Baseline NLL | This model NLL | Change | 95% window-bootstrap interval |
|---|---:|---:|---:|---|
| A (120 windows) | 1.70105 | 1.64763 | -3.14% | [-3.78%, -2.52%] |
| B (120 windows) | 1.75789 | 1.70136 | -3.22% | [-3.76%, -2.70%] |
| A+B (240 windows) | 1.72947 | 1.67449 | -3.18% | [-3.58%, -2.77%] |

NLL is lower in 204 of 240 windows and 10 of 10 categories. Category point estimates are not a ranking of general intelligence or safety.

### Edit cost against non-abliterated FP4-Local

| Set | Baseline NLL | This model NLL | Change | 95% window-bootstrap interval |
|---|---:|---:|---:|---|
| A (120 windows) | 1.64144 | 1.64763 | +0.38% | [+0.13%, +0.62%] |
| B (120 windows) | 1.69548 | 1.70136 | +0.35% | [+0.14%, +0.55%] |
| A+B (240 windows) | 1.66846 | 1.67449 | +0.36% | [+0.21%, +0.53%] |

The earlier run on oMLX `6feea9f9` and MLX 0.32.3 measured a combined edit cost of +0.46% (95% [+0.30%, +0.63%]). The table above uses the current PR engine and MLX 0.32.4; the two environments are not pooled.

## Speed and memory

Uniform 4-bit and the non-abliterated FP4-Local model were measured on the same engine and M5 Ultra (256GB), ABBA x2. Both use MTP with an adaptive maximum depth of 3, at most 12 concurrent requests, top_p 0.95 and temperatures 0/1 as indicated. The uniform 4-bit model uses the existing MTP overlay. Output budgets are 512 tokens, or 16 tokens for prefill cells, with request seed 20261019. Prefill lengths are exactly 8,192 and 32,768 input tokens as reported by the server. Each round starts with a cold load and a warm-up; figures are medians of four valid rounds per model. Order and per-round inputs are fixed, with no prefill cache reuse.

| Metric | Uniform 4-bit + MTP | Non-abliterated FP4-Local + MTP | FP4 / 4-bit |
|---|---:|---:|---:|
| Prefill, 8,192 tokens (tok/s) | 2,248.9 | 2,063.7 | 0.918 |
| Prefill, 32,768 tokens (tok/s) | 2,358.8 | 2,145.7 | 0.910 |
| Decode, temperature 0, prose (tok/s) | 96.2 | 70.9 | 0.737 |
| Decode, temperature 0, code (tok/s) | 96.7 | 75.6 | 0.782 |
| Decode, temperature 1, prose (tok/s) | 93.4 | 68.0 | 0.728 |
| Decode, temperature 1, code (tok/s) | 92.0 | 72.8 | 0.791 |
| Aggregate, 1 concurrent (tok/s) | 89.8 | 68.8 | 0.767 |
| Aggregate, 8 concurrent (tok/s) | 127.5 | 111.7 | 0.877 |
| Median of per-round peak wired memory (GB) | 196.5 | 199.1 | 1.013 |

Aggregate throughput is total generated tokens divided by elapsed time from the first request's start to the last response's completion, including TTFT. Decode speed is the server usage metric for the generation phase. System-wide peak wired memory (GB) and active MLX memory (GiB) are different measures. The highest wired memory observed across all rounds was 199.2 GB for uniform 4-bit and 200.0 GB for FP4. Active MLX memory after NLL load was 169.41 GiB for uniform 4-bit with its MTP overlay and 174.33 GiB for FP4 with its stored MTP. Those active-memory figures do not include the server's generation-time KV and buffer use.

MTP draft acceptance was 74.80% (10,784/14,418) for uniform 4-bit and 75.14% (8,279/11,018) for non-abliterated FP4-Local. Adaptive depth changes the depth distribution behind these rates, so acceptance alone does not explain the speed gap. Per-request tokens/cycle and per-depth accepted/drafted counts are preserved in the raw logs.

## Compared with JK v4

[JK v4](https://huggingface.co/junmo-k/GLM-5.3-Flash-UNCENSORED-JK-oQ3.5e) is our earlier 158 GiB uncensored GLM-5.3-Flash build for MLX (oQ3.5e GPTQ, from a dealignai derivative). The trade-off is quality versus speed and memory: this model has lower NLL, while JK v4 decodes faster and needs less memory.

These numbers come from a separate paired run on an older engine (oMLX `6feea9f9`, MLX 0.32.3, mlx-vlm 0.7.7), measured on this checkpoint itself, so do not mix them with the tables above. NLL uses the same 240 windows. Speed is ABBA x2 with MTP on: 4 JK v4 rounds and 3 valid rounds for this model.

| Metric | JK v4 | This model | Ratio |
|---|---:|---:|---:|
| Held-out NLL, A+B (240 windows) | 1.69950 | 1.67460 | -1.47%, 95% [-1.84%, -1.10%] |
| Prefill 8K / 32K (tok/s) | 2,087 / 2,179 | 1,946 / 2,116 | 0.93 / 0.97 |
| Decode, temperature 0, prose / code (tok/s) | 85.1 / 83.8 | 68.4 / 74.0 | 0.80 / 0.88 |
| Aggregate, 1 / 8 concurrent (tok/s) | 85.5 / 126.8 | 65.1 / 110.6 | 0.76 / 0.87 |
| Peak wired memory (GB) | 185.4 | 198.1 | +12.7 GB |
| MLX active memory after load (GiB) | 158.2 | 174.3 | +16.2 GiB |

The two models remove refusals with different methods, and refusal behavior was not compared. NLL and speed do not tell you which one answers more requests.

## Layout and conversion scope

The checkpoint is about 174.33 GiB. Routed experts and MXFP8 matrices preserve the source values. Other matrices, including FP8 block formats that MLX cannot represent directly, use the re-encoding, dequantization or precision changes listed below.

| Part | Stored as | Conversion |
|---|---|---|
| Routed experts, layers 3-44 and the MTP layer (`gate_proj` / `up_proj` / `down_proj`) | MLX `nvfp4` (E2M1, E4M3 scale per 16) plus `weight_scale_2` per expert (f32) | NVIDIA's trained NVFP4 values are unchanged byte for byte. CSF block scales are decoded with the FlashInfer reference codec. |
| KDA attention projections, dense MLPs (layers 0-2), `lm_head`, MTP attention, MTP shared expert, MTP indexer | MLX `mxfp8` (E4M3, E8M0 scale per 32) | Source MXFP8 values unchanged |
| Shared experts (layers 3-44), DSA `q_a_proj` / `q_b_proj` / `kv_a_proj_with_mqa` / `o_proj` | 8-bit affine, group 64 | FP8 128x128 blocks are dequantized and re-encoded. |
| DSA `kv_b_proj` | BF16, split into `embed_q` / `unembed_out` | Split to match oMLX's load-time layout |
| Vision tower | BF16 | Source NVFP4 / MXFP8 values are dequantized. |
| Embeddings, routers, KDA state parameters, hyper-connections and other parameters | Source precision (BF16 / F32) | Unchanged |
| RMSNorm weights stored as F32 in the source | BF16 | Narrowed so oMLX's 16-bit fused paths apply |

Each MoE layer's routed experts sit in their own `*-experts.safetensors` file.

## Checks and measurement scope

Earlier conversion checks found exact agreement between 36 sampled routed-expert matrices and an independent decode of the source, and exact agreement for MXFP8 values and the `kv_b_proj` split. With PR #4661, all 129 loaded expert scales (backbone and MTP) matched the source exactly. The NLL runs cover every window in both sets, and the speed comparison has four valid rounds per model. Vision performance, the full long-context range and stock mlx-vlm outside oMLX were not covered here.

## License

NVIDIA Open Model Agreement (see `LICENSE` and `NOTICE`). GLM-5.3-Flash by Z.ai and the Huihui refusal-direction edit are MIT-licensed.

## Acknowledgements

NVIDIA for the QAD checkpoint, Z.ai for GLM-5.3-Flash, FlashInfer / Local Inference Lab for the CSF reference codec, and [mlx-serve](https://github.com/ddalcu/mlx-serve) for the Apple Silicon execution precedent, plus Piecrust and Huihui for the refusal-direction edit.
