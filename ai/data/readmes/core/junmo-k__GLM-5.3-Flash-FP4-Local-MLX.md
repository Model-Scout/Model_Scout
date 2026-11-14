---
license: other
license_name: nvidia-open-model-agreement
license_link: LICENSE
base_model: nvidia/GLM-5.3-Flash-FP4-Local
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
---

# GLM-5.3-Flash-FP4-Local-MLX

An MLX repack of [nvidia/GLM-5.3-Flash-FP4-Local](https://huggingface.co/nvidia/GLM-5.3-Flash-FP4-Local) (rev `76348ddb`), NVIDIA's quantization-aware-distilled (QAD) NVFP4 build of [zai-org/GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) (320B total, about 18B active), for MLX/oMLX on Apple Silicon. It retains NVIDIA's QAD NVFP4 routed experts.

**On our held-out set, NLL is 0.91% lower than a round-to-nearest MLX build with the same bit layout (4-bit experts, 8-bit other layers), and 3.53% lower than uniform 4-bit MLX. Temperature-0 prose decode runs at 0.737x its speed, and active MLX memory after load, including MTP, is 4.92 GiB higher.** The table below compares the two models on the same engine. The checkpoint is about 174.33 GiB and runs on [oMLX](https://github.com/jundot/omlx) [v0.7.1](https://github.com/jundot/omlx/releases/tag/v0.7.1) or later.

| At a glance | This model / uniform 4-bit |
|---|---|
| Held-out NLL vs same bit layout, round-to-nearest | 1.66846 / 1.68380, -0.91%, 95% [-1.19%, -0.62%] |
| Held-out NLL vs uniform 4-bit (lower is better) | 1.66846 / 1.72947, -3.53%, 95% [-3.92%, -3.14%] |
| Decode, temperature 0, prose / code | Prose: 70.9 / 96.2 tok/s (0.737x); code: 75.6 / 96.7 tok/s (0.782x) |
| Peak wired memory, median across rounds | 199.1 / 196.5 GB |
| Measured setup | M5 Ultra 256GB, oMLX + [PR #4661](https://github.com/jundot/omlx/pull/4661), MLX 0.32.4, mlx-vlm 0.7.8 |

NLL and speed figures for this repository were measured with this repository's weights. Not affiliated with NVIDIA or Z.AI.

## Requirements

Requires [oMLX](https://github.com/jundot/omlx) [v0.7.1](https://github.com/jundot/omlx/releases/tag/v0.7.1) or later, which includes [PR #4661](https://github.com/jundot/omlx/pull/4661) and its expert-offload follow-up. Measured on an Apple M5 Ultra (256GB) with MLX 0.32.4 and mlx-vlm 0.7.8. Not tested: stock mlx-vlm outside oMLX, Macs with other memory sizes, vision, and the full long-context range.

## Quality

The baseline is a local copy of [pipenetwork/GLM-5.3-Flash-MLX-4bit](https://huggingface.co/pipenetwork/GLM-5.3-Flash-MLX-4bit), a standard affine 4-bit, group-64 conversion from the same GLM model family, with only 33 indexer modules at 8-bit. Both sides use the PR engine with identical inference source, libraries and evaluation windows. This model's NLL comes from an earlier run on a pre-squash build of the same PR whose inference source was verified identical to `04678f78e` (only one test line differs). The new 4-bit and Piecrust NLL runs and all speed measurements use `04678f78e`. This compares the complete models, including the QAD checkpoint, non-expert precision and repack format; it does not isolate the effect of a 4-bit algorithm alone.

Held-out NLL uses two disjoint sets of 120 teacher-forced 512-token windows that were not used for calibration. The 10 categories are English, code, reasoning, chat, tool calling, Chinese, Korean and three categories from private Korean/English working notes. Windows are paired across models; intervals are 95% window bootstrap with 10,000 resamples. Private text is not released. These numbers measure prediction loss on these windows, not conversation preference or a general benchmark score.

| Set | Baseline NLL | This model NLL | Change | 95% window-bootstrap interval |
|---|---:|---:|---:|---|
| A (120 windows) | 1.70105 | 1.64144 | -3.50% | [-4.11%, -2.92%] |
| B (120 windows) | 1.75789 | 1.69548 | -3.55% | [-4.07%, -3.05%] |
| A+B (240 windows) | 1.72947 | 1.66846 | -3.53% | [-3.92%, -3.14%] |

NLL is lower in 218 of 240 windows and 10 of 10 categories. Category point estimates are not a ranking of general intelligence or safety.

Most of the gap to uniform 4-bit comes from bit layout rather than from the checkpoint: uniform 4-bit also stores attention, shared experts and the other non-expert layers at 4 bits, while this model keeps them at 8 bits or MXFP8. To separate the two, the same 240 windows were measured on oMLX v0.7.1 for three checkpoints:

| Checkpoint | Experts | Other layers | NLL | Active memory after load | vs this model |
|---|---|---|---:|---:|---:|
| This model (QAD) | NVFP4 | MXFP8 / 8-bit | 1.66846 | 174.33 GiB (with MTP) | baseline |
| [Same bit layout, round-to-nearest](https://huggingface.co/pipenetwork/GLM-5.3-Flash-MLX-mixed-4_8bit) (rev `d43ea8b4`) | 4-bit affine | 8-bit affine | 1.68380 | 169.59 GiB (no MTP) | +0.92% |
| [Uniform 4-bit, round-to-nearest](https://huggingface.co/pipenetwork/GLM-5.3-Flash-MLX-4bit) (rev `f94fd5d1`) | 4-bit affine | 4-bit affine | 1.72947 | 165.51 GiB (no MTP) | +3.66% |

Against the same bit layout, this model is lower on 163 of 240 windows (95% bootstrap interval of the difference -1.19% to -0.62%) and in all 10 categories, most in tool calling (-2.46%) and reasoning (-1.57%), least in Chinese (-0.04%). That remaining gap is what the QAD checkpoint adds over plain round-to-nearest at the same bits. A calibrated PTQ method such as GPTQ at the same bits was not measured and may narrow it. For speed, one representative cell was measured on the same engine with MTP enabled (adaptive maximum depth 3, oMLX server, single request, prose, temperature 0, 512 output tokens, ABBA with two rounds per arm): this model 67.8 tok/s, the same-bit-layout build 78.9 tok/s (0.86x). That build ships without an MTP head, so the 4-bit MTP head from the uniform 4-bit build was attached for this measurement; its draft acceptance was 74.2% versus 71.8% for this model's own head. Peak system wired memory was 195.7 GB versus 196.3 GB.

## Speed and memory

Uniform 4-bit and this model were measured on the same engine and M5 Ultra (256GB), ABBA x2. Both use MTP with an adaptive maximum depth of 3, at most 12 concurrent requests, top_p 0.95 and temperatures 0/1 as indicated. The uniform 4-bit model uses the existing MTP overlay. Output budgets are 512 tokens, or 16 tokens for prefill cells, with request seed 20261019. Prefill lengths are exactly 8,192 and 32,768 input tokens as reported by the server. Each round starts with a cold load and a warm-up; figures are medians of four valid rounds per model. Order and per-round inputs are fixed, with no prefill cache reuse.

| Metric | Uniform 4-bit + MTP | This model + MTP | FP4 / 4-bit |
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

MTP draft acceptance was 74.80% (10,784/14,418) for uniform 4-bit and 75.14% (8,279/11,018) for this model. Adaptive depth changes the depth distribution behind these rates, so acceptance alone does not explain the speed gap. Per-request tokens/cycle and per-depth accepted/drafted counts are preserved in the raw logs.

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

NVIDIA Open Model Agreement (see `LICENSE` and `NOTICE`). GLM-5.3-Flash by Z.ai is MIT-licensed.

## Acknowledgements

NVIDIA for the QAD checkpoint, Z.ai for GLM-5.3-Flash, FlashInfer / Local Inference Lab for the CSF reference codec, and [mlx-serve](https://github.com/ddalcu/mlx-serve) for the Apple Silicon execution precedent.
