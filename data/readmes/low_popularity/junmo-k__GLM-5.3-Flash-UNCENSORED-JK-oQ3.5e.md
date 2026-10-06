---
license: mit
base_model: dealignai/GLM-5.3-Flash-UNCENSORED-FP8
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
  - mixed-precision
  - oq
  - imatrix
  - gptq
  - mtp
  - uncensored
  - abliterated
---

# GLM-5.3-Flash-UNCENSORED-JK-oQ3.5e

**JK** is a custom mixed-precision MLX build of [dealignai/GLM-5.3-Flash-UNCENSORED-FP8](https://huggingface.co/dealignai/GLM-5.3-Flash-UNCENSORED-FP8) (rev `d5822b06`, a weight-level uncensoring of [zai-org/GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash), 320B total / about 18B active). It was quantized with [oMLX](https://github.com/jundot/omlx) oQ on an Apple M5 Ultra (256GB) to fit long-context work on that machine: **158 GiB on disk, about 15 GiB smaller than an oQ4e build of the same weights.** Vision and the MTP draft head are kept.

This is **v3** (2026-10-05). It keeps the v2 bit layout and re-quantizes every routed expert with an expert-wise GPTQ fitted to each expert's own routed inputs, which lowers held-out NLL by 0.19% against v2 at the same size and speed. v2 remains available at the [`v2` tag](https://huggingface.co/junmo-k/GLM-5.3-Flash-UNCENSORED-JK-oQ3.5e/tree/v2) and v1 at the [`v1` tag](https://huggingface.co/junmo-k/GLM-5.3-Flash-UNCENSORED-JK-oQ3.5e/tree/v1).

Not affiliated with Z.AI or dealignai.

## Versions

| Version | Date | Revision | Change |
|---|---|---|---|
| v3 | 2026-10-05 | `main` | Routed experts (all 42 MoE layers and the MTP head) re-quantized with expert-wise GPTQ at the v2 bit layout. |
| v2 | 2026-10-02 | `v2` | Attention and dense MLPs 8 to 6 bits, `lm_head` 8 to 6, embeddings 8 to 4. The space goes to 4 more MoE layers with 4-bit expert `gate_proj` / `up_proj` (14 to 18). |
| v1 | 2026-10-01 | `v1` | First release. |

To get an earlier version: `hf download junmo-k/GLM-5.3-Flash-UNCENSORED-JK-oQ3.5e --revision v2` (or `v1`).

## Layout

| Part | v3 bits | v2 bits | v1 bits |
|---|---|---|---|
| Routed experts `gate_proj` / `up_proj`, 18 most sensitive MoE layers (4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 26, 27, 32, 35, 37, 39) | 4 | 4 (18 layers) | 4, except layers 6, 10, 12, 14 at 3 |
| Routed experts `gate_proj` / `up_proj`, the other 24 MoE layers | 3 | 3 | 3 |
| Routed experts `down_proj`, all 42 MoE layers | 4 | 4 | 4 |
| Attention (except the DSA indexer), dense MLPs (layers 0-2) | 6 | 6 | 8 |
| `lm_head` | 6 | 6 | 8 |
| Embeddings | 4 | 4 | 8 |
| Shared experts, DSA indexer | 8 | 8 | 8 |
| MTP head: routed experts / `eh_proj` / everything else | 4 / BF16 / 8 | 4 / BF16 / 8 | 4 / BF16 / 8 |

All quantized weights are affine with group size 64, and the vision tower stays in BF16. About 4.23 bits per weight overall (v2: 4.23, v1: 4.22). Per-module bits are recorded in `config.json` (`quantization`).

## Expert GPTQ (v3)

v1 and v2 quantize routed experts with oQe: round-to-nearest with imatrix-weighted scale search. v3 keeps the same bits and replaces only the routed-expert weights, re-quantized from the FP8 source with GPTQ.

- **Per-expert Hessians.** Stock GPTQ builds one Hessian from all inputs of a switch layer and shares it across the 288 experts. v3 builds a Hessian per expert from the tokens actually routed to it, weighted by the squared routing weight, so the error that matters is the error in the expert's contribution to the layer output. `gate_proj` and `up_proj` share inputs and are solved together; `down_proj` is solved afterwards on the SwiGLU output of the already-quantized `gate_proj` / `up_proj`.
- **Sparse experts.** Some experts see only a few thousand calibration tokens. To keep their Hessians well conditioned, each expert's Hessian is blended with the layer's pooled input covariance at a weight of 4,096 virtual tokens. On two probe layers this lowered the held-out error ratio (against v2) from 0.71-0.78 to 0.63-0.66.
- **Grid.** Scales and biases follow the MLX affine group-64 format and are rounded to their stored BF16 values before the error is propagated, so the correction follows the grid the weights are stored on. Each group's clip range is searched on the diagonal of the Hessian. No act-order (it would fight the group-64 layout).
- **Inputs.** Expert inputs and routing were captured from v2 itself, so each layer sees the distribution produced by the quantized layers above it: 1,024 windows x 512 tokens from the same calibration mix as the imatrix, excluding every window that overlaps the held-out sets. Only aggregate second-order statistics enter the quantization; no text is stored in the weights.
- **Local error.** On held-out set A, with routing fixed, the MoE block output error relative to v2 was 0.564 for 3-bit layers, 0.680 for 4-bit layers and 0.555 for the MTP head (lower is better).

## How the bits were placed

Every token reads all of the attention, dense MLP, shared-expert and `lm_head` weights (6.1, 0.63, 1.05 and 0.63 GiB in v1), but only 8 of the 288 routed experts in each MoE layer (143.7 GiB in total). At a fixed size, the bits of these always-read weights set most of the decode speed, so v2 lowers them and spends the space on routed experts.

The MoE layers that get 4-bit `gate_proj` / `up_proj` were ranked on a uniform 4-bit copy of the base model: each layer's expert `gate_proj` / `up_proj` was re-quantized to 3 bits with routing held fixed, and the relative squared error of that MoE block's output was measured (32 windows x 512 tokens). End-to-end KL against the reference was not used for ranking: it is dominated by routing changes, and even re-quantizing a layer at the same 4 bits moved it by 0.045 nats while NLL stayed within +-0.004. v1 takes the top 14 layers of this ranking and v2 the top 18.

Candidates of about the same size were compared by held-out NLL against v1 and by decode speed. NLL used two disjoint sets (A and B) of 120 windows x 512 tokens each, 12 from each of the 10 categories of the calibration mix. 64 of the 512 imatrix windows used for v1 and v2 partly overlap these sets (found after v2 was released); the v3 GPTQ calibration excludes every overlapping window. Speeds come from separate screening runs on the M5 Ultra.

| Candidate | NLL vs v1, set A | NLL vs v1, set B | Tok/s greedy / sampled / 30K ctx |
|---|---|---|---|
| v1: attention and dense MLPs at 8 bits, 14 layers | reference | reference | 70.7 / 63.2 / 77.4 |
| 6 bits, 14 layers | +0.23% | | 73.5 / 66.9 / 77.7 |
| 6 bits, 17 layers | +0.05% | -0.18% | 74.1 / 67.3 / 78.3 |
| 5 bits, 19 layers | -0.04% | | 70.9 / 66.1 / 78.6 |
| **6 bits, `lm_head` 6, embeddings 4, 18 layers (v2)** | **-0.53%** | **-0.14%** | **74.8 / 66.9 / 78.3** |
| 4 bits, `lm_head` 6, embeddings 4, 21 layers | +1.24% | +1.23% | 75.8 / 69.7 / 81.3 |

The bit counts in this table refer to attention and dense MLPs. Shared experts and the DSA indexer stayed at 8 bits in every candidate. The -0.53% on set A shrank to -0.14% on set B, so v2's NLL should be read as equal to v1 within noise, not as a clear gain. 5 bits did not speed up greedy decoding, and 4 bits cost about 1.2% NLL on both sets.

Also tried and dropped: 8-bit routed experts in the MTP head (+0.9 points of acceptance, 95% interval -0.3 to +2.2, for +3.6 GiB), 4 MTP draft tokens instead of 3 (no clear gain), moving bits between `down_proj` and `gate_proj` / `up_proj` (differences within simulation error), and simulated pruning of rarely used experts (with 16 experts removed per layer, KL to the original rose from 0.111 to 0.132).

## Calibration (oQe imatrix)

512 windows x 512 tokens sampled from a 1.84M-token mix: the oMLX built-in oQe corpus (60%), private agent-session transcripts (20%), nightly session digests (10%) and technical notes (10%), with family-related content and secret-like lines removed. Only aggregate per-channel activation statistics enter the quantization; no text is stored in the weights. Every routed expert received tokens (5th percentile 2,179 tokens per expert). The MTP head has no imatrix entries and uses plain rounding. v1 and v2 use the same imatrix. v3 uses the same imatrix for every non-expert tensor, and the GPTQ calibration described above for routed experts.

## Evaluation

v2 and v3 side by side in the same run on the M5 Ultra (2026-10-05), with the same runtime and settings (oMLX, MTP with 3 draft tokens, alternating rounds):

| | v2 | v3 |
|---|---|---|
| Held-out NLL, set A / set B (120 windows x 512 tokens each) | reference | −0.11% / −0.27% |
| Both sets, 95% interval | | −0.19%, [−0.48%, +0.10%] |
| Tok/s greedy / sampled / 30K ctx | 82.3 / 79.5 / 93.1 | 84.5 / 79.8 / 93.9 |
| Server memory in use | 162.1 GiB | 162.1 GiB |
| MTP acceptance | 74.8% | 74.4% |
| Functional checks | pass | pass |
| Six short reasoning problems at high effort | 6/6 | 6/6 |
| Chinese or Japanese characters in Korean answers | 0 | 0 |

- The NLL gain is small and consistent in direction: v3 was better on 137 of 240 windows (sign test p = 0.033), with the largest gain in reasoning text and a small loss in chat text. The 95% interval of the mean difference still includes zero.
- Speed and memory are the same as v2 within run-to-run noise.
- Functional checks: short summaries at low reasoning effort, `chat_template_kwargs`, a sensitive request at low and high effort (answered), vision, and tool calling.

## Usage

GLM-5.3-Flash (`glm5_next`: hybrid linear and sparse MLA attention, hyper-connections, DSA indexer, MTP head) needs a runtime that supports this architecture. JK was built and tested with oMLX on Apple Silicon (GLM-5.3 branch, with MTP enabled and 3 draft tokens). Support in stock `mlx-lm` / `mlx-vlm` has not been verified.

The chat template is the one from the base GLM-5.3-Flash release. The dealignai template differs only in the `clear_thinking` default (`true` there, `false` here).

## Responsible use

This model inherits dealignai's removal of safety refusals. It may produce content that the original model would refuse. You are responsible for how you use it and for complying with applicable laws.

## License

MIT, as the upstream [zai-org/GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) and [dealignai/GLM-5.3-Flash-UNCENSORED-FP8](https://huggingface.co/dealignai/GLM-5.3-Flash-UNCENSORED-FP8). See `LICENSE`.
