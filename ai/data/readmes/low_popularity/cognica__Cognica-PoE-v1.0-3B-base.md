---
license: apache-2.0
language:
  - en
  - ko
  - zh
  - ja
  - es
  - fr
tags:
  - causal-lm
  - poe
  - product-of-experts
  - per-stage-head
  - local-learning
  - chinchilla
  - nanochat
  - pretraining
  - early-exit
  - speculative-decoding
  - asymmetric-stages
library_name: transformers
pipeline_tag: text-generation
---

# Cognica-PoE-v1.0-3B-base

A **3.02B parameter** causal language model pretrained from scratch with **Product of Experts (PoE) per-stage-head** local learning. The model has 4 PoE stages with **asymmetric layer counts (16, 6, 5, 5)** — stage 0 (16 layers, ~50% of trunk) acts as a high-capacity general-LM backbone, while stages 1-3 (6+5+5 deeper layers) refine specialty knowledge. **Each PoE stage has its own additive lm_head** that composes with the shared base lm_head:

```
logits_k = lm_head(x_k) + lm_head_stages[k](x_k)    for k in 0..3
```

Inference aggregates per-stage log-softmax distributions (Bayesian PoE, uniform mean / `alpha=0.0`).

This is a **mid-training research release**. Final training plan is 83,923 steps (~66B tokens, Chinchilla ratio ~22). Multiple checkpoints are released as branches `step-XXXXX` (see "Checkpoints" below). `main` tracks the latest.

## TL;DR

- **3.02B params**: 2.08B transformer trunk + 0.54B value-embeds + 0.34B lm_head_stages + 0.07B wte
- **Architecture**: depth=32, n_embd=2048, n_head=16, n_kv_head=8 (**GQA 2:1**), head_dim=128, intermediate_size=12800, max_seq_len=2048
- **PoE**: K=4 stages, asymmetric `poe_stage_layers=(16, 6, 5, 5)`, boundaries at layers `[15, 21, 26, 31]`, `poe_mode=flat`, `poe_alpha=0.0` (uniform stage mean)
- **Per-stage heads**: 4 independent additive lm_head_stages composing with shared lm_head
- **Training**: DistMuonAdamW (ZeRO-2), total_batch=786,432 tokens/step, ~66B target tokens, Chinchilla ratio ~22, FA2, bf16 compute / fp32 weights, `case_aug_prob=0.15`
- **Dataset**: frontier_v1 mix (63B tokens), 11 sources covering English / multilingual / code / math / books / chat
- **Tokenizer**: 32,768 BPE vocab, BOS-prepend protocol (see "Inference" below)
- Standard HF `AutoModelForCausalLM` + `AutoTokenizer` with `trust_remote_code=True`
- **WAND p99 bounds are now per-checkpoint, stored in `config.json`** (auto-calibrated; class-constant fallback only)

## Architecture details

| Field | Value |
|---|---|
| `num_hidden_layers` | 32 |
| `hidden_size` | 2048 |
| `intermediate_size` | 12800 |
| `num_attention_heads` | 16 |
| `num_key_value_heads` | 8 (GQA 2:1) |
| `head_dim` | 128 |
| `max_position_embeddings` | 2048 |
| `vocab_size` | 32768 |
| `window_pattern` | SSSL (3 short + 1 long sliding-window per 4 layers; final layer always full) |
| `rope_theta` | 100,000 |
| `hidden_act` | relu_squared |
| `rms_norm_eps` | 1e-6 |
| `tie_word_embeddings` | False |
| `poe_mode` | flat |
| `poe_alpha` | 0.0 |
| `poe_stage_layers` | `[16, 6, 5, 5]` |
| `per_stage_head` | True |
| `poe_head_count` | 4 |
| `poe_wand_p99_bounds_per_stage_head` | per-checkpoint (auto-calibrated, see "WAND bounds" below) |

### Stage layout

| Stage | Layer range (0-indexed) | Layers | Approx. trunk-compute share |
|---|---|---|---|
| 0 | [0, 15] | 16 | 50% |
| 1 | [16, 21] | 6 | ~19% (cumulative 69%) |
| 2 | [22, 26] | 5 | ~16% (cumulative 84%) |
| 3 | [27, 31] | 5 | ~16% (cumulative 100%) |

Stage 0 is intentionally deep enough to function as a standalone capable LM. The asymmetric layout (50% / 19% / 16% / 16%) is itself a research variable: see the "Diversity vs layout" note below.

## Training

| Field | Value |
|---|---|
| Optimizer | DistMuonAdamW (ZeRO-2; reduce_scatter zero-padded for `vocab=32768 % world_size != 0`) |
| `total_batch_size` | 786,432 tokens / step |
| `num_iterations` | 83,923 (target) |
| target tokens | ~65.99B (Chinchilla ratio ~21.85) |
| `matrix_lr` | 0.015 |
| `embedding_lr` | 0.3 |
| `unembedding_lr` | 0.008 |
| `weight_decay` | 0.28 |
| `warmup_steps` | 1,000 |
| `warmdown_ratio` | 0.65 |
| `case_aug_prob` | 0.15 (80% lower / 20% upper at sample time) |
| Compute | 3-node A100 80GB (12 GPUs), DDP TCP cross-zone us-central1-c |
| Compute dtype | bf16 |
| Weight dtype | fp32 |

### Dataset (frontier_v1 mix, 63.07B tokens, 848 sharded parquets)

| Source | Share |
|---|---:|
| FineWeb-Edu | 33.5% |
| DCLM-Baseline | 24.1% |
| Stack v2 (codeparrot/github-code-clean mirror) | 15.7% |
| Wikipedia | 5.2% |
| CulturaX (ko, zh, ja, es, fr) | 5.2% |
| ProofPile-2 | 4.2% |
| OpenWebMath | 4.2% |
| Gutenberg (PG-19 separate) | 4.2% |
| PG-19 | 2.1% |
| UltraChat | 1.0% |
| OpenHermes-2.5 | 0.6% |

## Checkpoints

Each ckpt is a separate branch named `step-XXXXX`. The `main` branch tracks the latest released checkpoint (**currently `step-83923` — final, training complete**).

| Branch | Step | Training % | Val BPB (training-eval, 40M tokens, 12 ranks) |
|---|---:|---:|---:|
| `step-2000`  |  2,000 |  2.4% | 0.987 |
| `step-4000`  |  4,000 |  4.8% | 0.955 |
| `step-6000`  |  6,000 |  7.2% | 0.949 |
| `step-8000`  |  8,000 |  9.5% | 0.944 |
| `step-10000` | 10,000 | 11.9% | 0.936 |
| `step-12000` | 12,000 | 14.3% | 0.932 |
| `step-14000` | 14,000 | 16.7% | 0.932 |
| `step-16000` | 16,000 | 19.1% | 0.928 |
| `step-18000` | 18,000 | 21.4% | 0.922 |
| `step-20000` | 20,000 | 23.8% | 0.923 |
| `step-22000` | 22,000 | 26.2% | 0.923 |
| `step-24000` | 24,000 | 28.6% | 0.923 |
| `step-26000` | 26,000 | 31.0% | 0.922 |
| `step-28000` | 28,000 | 33.4% | 0.919 |
| `step-30000` | 30,000 | 35.8% | 0.914 |
| `step-32000` | 32,000 | 38.1% | 0.903 |
| `step-34000` | 34,000 | 40.5% | 0.905 |
| `step-36000` | 36,000 | 42.9% | 0.896 |
| `step-38000` | 38,000 | 45.3% | 0.896 (training-log s37500=0.894 was lower) |
| `step-40000` | 40,000 | 47.7% | 0.890 |
| `step-42000` | 42,000 | 50.0% | 0.885 |
| `step-44000` | 44,000 | 52.4% | 0.883 |
| `step-46000` | 46,000 | 54.8% | 0.879 |
| `step-48000` | 48,000 | 57.2% | 0.875 |
| `step-50000` | 50,000 | 59.6% | 0.866 |
| `step-52000` | 52,000 | 62.0% | 0.859 (skipped analysis; HF auto-publish only) |
| `step-54000` | 54,000 | 64.4% | 0.855 |
| `step-56000` | 56,000 | 66.7% | 0.849 |
| `step-58000` | 58,000 | 69.1% | 0.847 |
| `step-60000` | 60,000 | 71.5% | 0.840 |
| `step-62000` | 62,000 | 73.9% | 0.832 |
| `step-64000` | 64,000 | 76.3% | 0.830 |
| `step-66000` | 66,000 | 78.6% | 0.824 |
| `step-68000` | 68,000 | 81.0% | 0.815 |
| `step-70000` | 70,000 | 83.4% | 0.807 |
| `step-72000` | 72,000 | 85.8% | 0.803 |
| `step-74000` | 74,000 | 88.2% | 0.798 |
| `step-76000` | 76,000 | 90.6% | 0.794 |
| `step-78000` | 78,000 | 92.9% | 0.790 |
| `step-80000` | 80,000 | 95.3% | 0.784 |
| `step-82000` | 82,000 | 97.7% | 0.778 |
| `step-83923` | 83,923 | **100.0% (final)** | 0.773 |
| `main`       | latest |  — | tracks step-83923 |

Training-log val BPB new-minimum trajectory: s24500=0.9216 → s26500=0.9205 → s27000=0.9170 → s27500=0.9152 → s29000=0.9150 → s30000=0.9139 → s30500=0.9058 → s32000=0.9029 → s33500=0.9025 → s35000=0.9019 → s35500=0.8957 → s37500=0.8936 → s40000=0.8904 → s41500=0.8856 → s42000=0.8849 → s44000=0.8827 → s44500=0.8777 → s46500=0.8735 → s47000=0.8720 → s48500=0.8686 → s49500=0.8677 → s50000=0.8655 → s50500=0.8645 → s51000=0.8604 → s51500=0.8525 → s54500=0.8542. Warmdown phase began at step 29373; LR decay (`lrm`) is 1.00 at start, 0.85 by step 38000, 0.74 by step 44000, 0.65 by step 50000, 0.59 by step 54000.

Load a specific checkpoint via:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "cognica/Cognica-PoE-v1.0-3B-base",
    revision="step-83923",       # branch name
    trust_remote_code=True,
    torch_dtype="bfloat16",
)
tokenizer = AutoTokenizer.from_pretrained(
    "cognica/Cognica-PoE-v1.0-3B-base",
    revision="step-83923",
    trust_remote_code=True,
)
```

### WAND bounds (per-checkpoint, calibrated)

Each branch's `config.json` carries `poe_wand_p99_bounds_per_stage_head`, calibrated on a 131,072-token val slice using the tight margin-shrinkage metric `range(delta) = max(delta) - min(delta)` (constant-shift invariant). `model.generate_wand(...)` reads this field automatically; the class constant `POE_WAND_P99_BOUNDS_PER_STAGE_HEAD = (3.2557, 1.5259, 1.1327)` is now a fallback only.

| step | bound 0→1 | bound 1→2 | bound 2→3 |
|------|----------:|----------:|----------:|
| 2,000  | 3.7031 | 1.6121 | 0.9499 |
| 4,000  | 3.8367 | 1.7457 | 1.0991 |
| 6,000  | 3.6368 | 1.6811 | 1.0779 |
| 8,000  | 3.7747 | 1.7518 | 1.1965 |
| 10,000 | 3.6264 | 1.6389 | 1.1198 |
| 12,000 | 3.4802 | 1.6259 | 1.1765 |
| 14,000 | 3.2557 | 1.5259 | 1.1327 |
| 16,000 | 3.2375 | 1.5871 | 1.2400 |
| 18,000 | 3.0877 | 1.4975 | 1.1504 |
| 20,000 | 3.3391 | 1.6146 | 1.2223 |
| 22,000 | 3.2850 | 1.5351 | 1.1668 |
| 24,000 | 3.0965 | 1.5135 | 1.2253 |
| 26,000 | 3.2014 | 1.5787 | 1.1850 |
| 28,000 | 3.3545 | 1.6309 | 1.2206 |
| 30,000 | 3.2619 | 1.5749 | 1.1668 |
| 32,000 | 3.1206 | 1.5611 | 1.1859 |
| 34,000 | 3.3211 | 1.6436 | 1.1958 |
| 36,000 | 3.1297 | 1.5429 | 1.1388 |
| 38,000 | 3.5419 | 1.7612 | 1.2951 |
| 40,000 | 3.2932 | 1.6490 | 1.2101 |
| 42,000 | 3.1828 | 1.6904 | 1.2802 |
| 44,000 | 3.5738 | 1.8313 | 1.3495 |
| 46,000 | 3.3461 | 1.7629 | 1.2783 |
| 48,000 | 3.4684 | 1.7783 | 1.3153 |
| 50,000 | 3.3907 | 1.7382 | 1.2635 |
| 54,000 | 3.6491 | 1.8719 | 1.4201 |
| 56,000 | 3.5046 | 1.8724 | 1.3725 |
| 58,000 | 3.8759 | 2.0701 | 1.5092 |
| 60,000 | 3.4080 | 1.8007 | 1.3147 |
| 62,000 | 3.4241 | 1.8028 | 1.3601 |
| 64,000 | 3.3929 | 1.7722 | 1.2997 |
| 66,000 | 3.3416 | 1.7172 | 1.2378 |
| 68,000 | 3.8046 | 2.0047 | 1.4619 |
| 70,000 | 3.4113 | 1.7839 | 1.3367 |
| 72,000 | 3.4601 | 1.8653 | 1.3684 |
| 74,000 | 3.7531 | 2.0426 | 1.4564 |
| 76,000 | 3.7031 | 1.9777 | 1.4586 |
| 78,000 | 3.9050 | 1.9837 | 1.4425 |
| 80,000 | 3.8490 | 1.9599 | 1.4154 |
| 82,000 | 3.8955 | 2.0010 | 1.4470 |
| **83,923 (final)** | 3.9429 | 2.0193 | 1.4479 |

The bound 0→1 decreased s2k → s18k (from peak 3.84 at s4000 to 3.09 at s18000). Subsequent windows produced repeated widening / narrowing cycles: at s20k → s28k all three rose +3-5%, descended through s30k → s36k, widened sharply at s38k (+13~14%), narrowed at s40k (-7%), split at s42k, widened uniformly at s44k (+12-5%), reverted at s46k (-5%), mild moves through s48-s56, widened uniformly at s58k (+10%; bound 1→2 = 2.0701 set a trajectory-wide single-bound high), narrowed substantially at s60k (-12-13% — the s58 widening fully reverts), held essentially flat at s62k (+0.5% / +0.1% / +3.5%), narrowed mildly through s64-s66 (-0.9% to -4.8%), widened uniformly at s68k (+13.85% / +16.74% / +18.10%), narrowed substantially at s70k (-10.34% / -11.01% / -8.56%), mildly re-widened at s72k (+1.43% / +4.56% / +2.37%), widened moderately at s74k (+8.47% / +9.50% / +6.43%), mildly narrowed at s76k (-1.33% / -3.18% / +0.15%), and split at s78k (+5.45% bound 0→1 / +0.30% bound 1→2 / -1.10% bound 2→3). The trajectory is non-monotonic on every measurement window.

## Inference

### Standard HF generate (with BOS prepend — REQUIRED for base ckpts)

This is a base (pretrained) model. The training protocol always prepends `<|bos|>` to the prompt before tokenization. Failing to prepend BOS produces incoherent output:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda" if torch.cuda.is_available() else "cpu"
model = AutoModelForCausalLM.from_pretrained(
    "cognica/Cognica-PoE-v1.0-3B-base",
    trust_remote_code=True,
    dtype=torch.bfloat16,
).to(device).eval()
tokenizer = AutoTokenizer.from_pretrained(
    "cognica/Cognica-PoE-v1.0-3B-base",
    trust_remote_code=True,
)

prompt = "The capital of France is"
input_ids = [tokenizer.bos_token_id] + tokenizer.encode(prompt, add_special_tokens=False)
input_ids = torch.tensor([input_ids], device=device)
out = model.generate(
    input_ids=input_ids,
    max_new_tokens=32,
    do_sample=False,           # greedy; set True + temperature for sampling
)
print(tokenizer.decode(out[0].tolist()))
```

KV cache is enabled by default. `CognicaKVCache` subclasses `transformers.Cache` so HF `generate()` preserves it across decode steps without auto-replacing it with `DynamicCache`. The cache is preallocated to `max_position_embeddings` and lives on the device of the input tensor.

Implementation details:

- **Numerical**: SDPA's prefill (`is_causal=True`, full sequence) and decode (`Tq == 1`, masked) kernels are mathematically equivalent but accumulate bf16 rounding errors in different orders. To prevent that drift from compounding across decode steps and producing different greedy tokens at low-margin branching points, the SDPA call casts `q/k/v` to fp32, runs the kernel, then casts back to bf16. The K/V cache itself stays in bf16 (memory unchanged). On a fixed greedy prompt this gives bit-identical agreement between `use_cache=True` and `use_cache=False` for at least 200 generated tokens.
- **Throughput**: in single-batch (B=1) interactive use, per-decode Python and dispatch overhead dominates the per-step compute savings from the cache. Measured speedup is +3-6 percent (`use_cache=True` vs `use_cache=False`) over 50-500 token runs. To realize the cache's full benefit, batch the decode (`B >= 4`) or use a fused kvcache kernel (FA2's `flash_attn_with_kvcache`, FlashInfer).

### PoE-specific inference (s83923 final measurements, 8-shard val slice 1.05M tokens)

s83923 is the **final** ckpt (lrm at s83923 ≈ 0.05; warmdown complete). Same val slice across s8000..s83923, single A100 80GB, bug-fixed code:

| Inference mode | n_layer used | training-objective BPB | renormed PoE BPB (α=0) |
|---|---:|---:|---:|
| Full PoE (`alpha=0`, all 4 stages aggregated) | 32 | **0.724738** | 0.724738 |
| Single stage 0 alone | 16 | 0.727740 | 0.727740 |
| Single stage 1 alone | 22 | 0.725798 | 0.725798 |
| Single stage 2 alone | 27 | 0.725063 | 0.725063 |
| Single stage 3 alone | 32 | **0.724273** | 0.724273 |
| prefix K'=1 (== single s0) | 16 | 0.727740 | — |
| prefix K'=2 | 22 | 0.726103 | — |
| prefix K'=3 | 27 | 0.725363 | — |
| Self-speculative decoding (stage 0 drafts, full verifies) | mixed | (no quality loss by construction) | — |

| metric | s83923 (final) |
|---|---|
| Speculative decoding speedup (m=4, 7 prompts × ~60 tokens) | **1.61x end-to-end** |
| Speculative acceptance α | **0.9852** (s82000=0.9377, +0.0475; **2nd highest in trajectory** after s28000=0.9882) |
| Routing probe at cap=0.020 (regression-rate-bounded) | 85.05% routed (s82000=86.08%, -1.03pp), projected speedup 1.715x |
| Per-stage target accuracy (full K=4) | **0.4860** (s82000=0.4835, +0.0025; **trajectory peak**) |
| Per-stage best (s3) accuracy | **0.4862** (trajectory peak) |
| PoE↔single-s3 BPB crossover gap | +0.000465 (s82000=+0.000441, s80000=+0.000445) |

vs s82000 the local-slice training-objective BPB dropped -0.005308 (full K=4) and -0.005332 (single s3). Sub-0.725 first crossed across the full table.

**Cumulative warmdown phase totals**: full K=4 BPB s30000 → s83923 = -0.133244 (15.5% relative reduction). Per-stage full acc s32000 → s83923 = +0.0580 (5.80 percentage points).

Per-stage target accuracy across last 12 ckpts (s52000 skipped from analysis):

| step | s0 | s1 | s2 | s3 | full |
|---:|---:|---:|---:|---:|---:|
| s32000 | 0.4258 | 0.4279 | 0.4281 | 0.4280 | 0.4280 |
| s34000 | 0.4266 | 0.4279 | 0.4281 | 0.4281 | 0.4280 |
| s36000 | 0.4303 | 0.4311 | 0.4310 | 0.4310 | 0.4311 |
| s38000 | 0.4336 | 0.4342 | 0.4345 | 0.4347 | 0.4347 |
| s40000 | 0.4380 | 0.4394 | 0.4392 | 0.4393 | 0.4394 |
| s42000 | 0.4388 | 0.4403 | 0.4406 | 0.4407 | 0.4407 |
| s44000 | 0.4395 | 0.4400 | 0.4403 | 0.4405 | 0.4403 |
| s46000 | 0.4397 | 0.4407 | 0.4410 | 0.4414 | 0.4410 |
| s48000 | 0.4419 | 0.4427 | 0.4427 | 0.4430 | 0.4429 |
| s50000 | 0.4456 | 0.4466 | 0.4471 | 0.4471 | 0.4470 |
| s54000 | 0.4500 | 0.4512 | 0.4515 | 0.4521 | 0.4515 |
| s56000 | 0.4531 | 0.4542 | 0.4547 | 0.4549 | 0.4546 |
| s58000 | 0.4535 | 0.4547 | 0.4549 | 0.4550 | 0.4550 |
| s60000 | 0.4563 | 0.4570 | 0.4573 | 0.4578 | 0.4573 |
| s62000 | 0.4590 | 0.4599 | 0.4603 | 0.4608 | 0.4602 |
| s64000 | 0.4626 | 0.4634 | 0.4639 | 0.4642 | 0.4639 |
| s66000 | 0.4643 | 0.4652 | 0.4652 | 0.4655 | 0.4651 |
| s68000 | 0.4674 | 0.4685 | 0.4687 | 0.4688 | 0.4687 |
| s70000 | 0.4697 | 0.4706 | 0.4708 | 0.4711 | 0.4708 |
| s72000 | 0.4711 | 0.4720 | 0.4722 | 0.4726 | 0.4721 |
| s74000 | 0.4731 | 0.4741 | 0.4745 | 0.4748 | 0.4745 |
| s76000 | 0.4763 | 0.4775 | 0.4777 | 0.4782 | 0.4776 |
| s78000 | 0.4786 | 0.4798 | 0.4799 | 0.4804 | 0.4801 |
| s80000 | 0.4812 | 0.4820 | 0.4824 | 0.4829 | 0.4824 |
| s82000 | 0.4824 | 0.4830 | 0.4835 | 0.4837 | 0.4835 |
| **s83923** | **0.4844** | **0.4856** | **0.4859** | **0.4862** | **0.4860** |

Cumulative s32 → s82 full acc gain: +0.0555. **0.05 cumulative milestone crossed at s78k**; **0.48 boundary first crossed at s80k** (s2/s3/full = 0.4824 / 0.4829 / 0.4824); s82k continues +0.0011 mild descent.

Sample-level outputs at s78000 (greedy temp=0.0, 60 tokens):
- Capital France: "Paris. It is the largest city in France and the capital of the country. Paris is the seat of the government, the seat of the French Academy, and the seat of the European Union. It is also the seat of the United Nations. Paris is the second largest city in the European Union." (Paris ✓; "largest city in France" ✓; "seat of government" ✓; "seat of French Academy" ✓ — Académie française is in Paris; "seat of European Union" wrong; "seat of UN" wrong; mixed factual quality)
- Gold symbol: "Au. Gold is a soft, malleable, ductile, **highly unreactive ✓**, precious, yellow, ductile, malleable, ..." (Au ✓; **"highly unreactive" ✓ — corrects the s72 "highly reactive" error**; precious + yellow + soft + malleable + ductile correct; output then degenerates into ductile/yellow/malleable repetition loop)
- Friday → tomorrow: "Saturday. If you are a Christian, then you know that the Bible says that God created the world on the sixth day of Creation Week. If you are a Muslim, then you know that the Quran says ... If you are a Jew ..." (Saturday is incorrect — correct is Sunday; religious tangent about Creation Week)
- Opposite hot: "cold. The opposite of cold is hot. ..." (binary loop)
- Planets list: "the bodies that orbit the Sun. The planets are the only bodies in the solar system that have atmospheres. The planets are named after the Roman gods of the Greek pantheon. **The planets are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.**" (**FIRST TIME the response produces a complete and correct modern 8-planet list across the entire trajectory** — Mercury through Neptune, no Pluto, in correct order; "named after the Roman gods of the Greek pantheon" ✓; richest planets output by a wide margin)
- Color: "red. I love the color red. ..." (red + repetition; first non-blue since s70)
- `5x + 3 = 13`: "x is equal to 1.5. ..." (1.5 wrong — correct is 2; closer than s76 "1/3"; cleaner format, no MC, no equation echo loop)

Sample-level outputs at s76000:
- Capital France: "Paris. ... largest city in France / 3rd largest in Europe / 2nd most populous / 2nd most visited after London"
- Gold: Au + atomic number 79 ✓ + comprehensive properties + use list (jewelry/coins/electronics/dentistry/medicine)
- Friday: "Saturday" + Matrix simulation drift
- Planets: "objects that orbit the Sun" generic only
- Algebra: "x = 1/3" single fractional answer (wrong)

s32000 → s78000 pattern across 24 analyzed warmdown checkpoints: per-stage accuracy increased across 22 of 23 2k-step windows (s44 alone broke; s58 was near-flat). Local-slice training-objective BPB descended non-monotonically (s34/s38/s44 produced positive deltas; the rest negative). The s78 planets prompt produced the **first complete and correct modern 8-planet list across the entire trajectory** (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune in correct order; no Pluto). The s76 gold prompt was the first correct atomic number 79 in a comprehensive Au response; s78 corrects the s72 "highly reactive" error to "highly unreactive ✓". Routing crossed the 90% boundary at s76 (90.76% peak at cap=0.020) and pulled back to 83.79% at s78. Cumulative full-stack acc gain s32 → s78 = +0.0521 (0.05 milestone crossed at s78).

## Trajectory and findings (s8000 → s33000)

This is a research release; we publish per-checkpoint experiment data so the trajectory of PoE behavior is externally auditable. The 8-shard local-val BPB and per-checkpoint WAND bounds are first-class artifacts of each branch.

### BPB trajectory

| step | training-obj. full K=4 BPB (8 shards) | training-log val BPB (12 ranks) | comment |
|------|--------------------------------------:|-------------------------------:|---------|
| s8,000  | 0.886647 | 0.943905 | early plateau exiting |
| s12,000 | 0.879752 | 0.931519 | mid-training, oscillation begins |
| s14,000 | 0.872835 | 0.931956 | first local low on 8-shard slice |
| s16,000 | 0.878514 | 0.927683 | regression on 8-shard slice (recovery on training-log) |
| s18,000 | 0.877102 | 0.922033 | training-log prior minimum |
| s20,000 | 0.875179 | 0.922640 | 8-shard recovery in progress |
| s22,000 | 0.874345 | 0.923003 | gap to s14k baseline now +0.0015; both slices in agreement |
| s24,000 | 0.866000 | 0.923228 | largest 2k-step drop in trajectory (-0.0083); crossed below prior s14k floor |
| s24,500 | (not run) | 0.921583 | training-log new min |
| s26,000 | 0.863433 | 0.922316 | local slice min through this point; per-stage acc -0.0018; routing 68.26% |
| s26,500 | (not run) | 0.920499 | training-log new min |
| s27,000 | (not run) | 0.917032 | training-log new min |
| s27,500 | (not run) | 0.915166 | training-log new min (5-step streak) |
| s28,000 | 0.858138 | 0.918785 | local slice min through this point; per-stage acc +0.0035; spec α 0.9882; crossover gap +0.000073 |
| s29,000 | (not run) | 0.915006 | training-log new min |
| s30,000 | 0.857982 | 0.913886 | both slices min through this point; first warmdown ckpt (lrm≈0.988); routing 68.39% |
| s30,500 | (not run) | 0.905847 | training-log new min; -0.008 single-step jump |
| s31,000 | (not run) | 0.906107 | small bounce in [0.902, 0.907] band |
| s31,500 | (not run) | 0.906766 | continued |
| s32,000 | 0.847991 | 0.902863 | -0.0100 local slice drop vs s30000; per-stage acc +0.0044 uniform; routing 74.33% (+5.94%); 4 prompts (Friday chain, modern planets, single-integer algebra, antonym graph) produced new output forms vs s30000 |
| s32,500 | (not run) | 0.907459 | reversal at upper band edge |
| s33,000 | (not run) | 0.906124 | oscillation in [0.902, 0.907] band; lrm ≈ 0.94 |
| s33,500 | (not run) | 0.902453 | training-log new min (9th); lrm ≈ 0.93 |
| s34,000 | 0.853621 | 0.904607 | local slice +0.0056 vs s32000; routing -13.11%; algebra prompt produced "A. 2 / B. 3 / C. 4" multiple-choice format |
| s35,000 | (not run) | 0.901891 | training-log new min (10th) |
| s35,500 | (not run) | 0.895684 | training-log new min (11th); first sub-0.9; -0.0062 vs s35000 |
| s36,000 | 0.841936 | 0.895738 | -0.0117 local slice drop vs s34000; per-stage acc +0.003 uniform; routing 67.63%; WAND bounds -5~-6% vs s34000 |
| s37,500 | (not run) | 0.893594 | training-log new min (12th); first sub-0.895 |
| s38,000 | 0.842198 | 0.896005 | local slice +0.000262 vs s36000 (first +Δ this warmdown); per-stage acc +0.0036 uniform; spec α 0.9483 (+0.0189); routing 72.06% (+4.4%); WAND bounds +13~14%; crossover gap +0.000476 → +0.000067 |
| s39,500 | (not run) | 0.891012 | training-log new min (13th) |
| s40,000 | 0.831678 | 0.890430 | local slice -0.010520 vs s38000 (full K=4); training-log -0.005575 (sub-0.89 first); per-stage acc +0.0047 uniform; spec α 0.9822 (+0.0339); routing 73.19% (+1.13%); WAND bounds -7%/-6.4%/-6.6%; crossover gap +0.000346; algebra prompt produced "x is equal to 2" (correct) |
| s41,500 | (not run) | 0.885587 | training-log new min (14th) |
| s42,000 | 0.826550 | 0.884868 | local slice -0.005128 vs s40000 (full K=4); training-log -0.005562 (sub-0.885 first); per-stage acc +0.0013 uniform; spec α 0.9403 (-0.0419); routing 68.90% (-4.29%); WAND bounds split (-3.4% / +2.5% / +5.8%); crossover gap +0.000109 |
| s44,000 | 0.828415 | 0.882684 | local slice +0.001865 vs s42000 (slice/log disagree on direction at s44); training-log -0.002184; per-stage acc s0 +0.0007 / s1-s3 -0.0002~-0.0003; spec α 0.9294 (-0.0109); routing cap=0.020 77.57% (+8.67%, surpasses s32000 prior peak 74.33%); WAND bounds widened uniformly (+12.3% / +8.3% / +5.4%); crossover gap +0.000038 |
| s44,500 | (not run) | 0.877723 | training-log new min; -0.0050 single-step drop |
| s46,000 | 0.827073 | 0.878585 | local slice -0.001342 vs s44000 (reverts s44 +Δ); training-log -0.004099; per-stage acc +0.0002~+0.0009 (monotonic increase resumes; s32→s46 cumulative full acc gain +0.0130); spec α 0.9294 (unchanged); routing cap=0.020 70.97% (-6.60%, reverts s44 jump); WAND bounds reverted (-6.4% / -3.7% / -5.3%); crossover gap +0.000158 |
| s46,500 | (not run) | 0.873460 | training-log new min |
| s47,000 | (not run) | 0.871953 | training-log new min |
| s48,000 | 0.821333 | 0.874640 | local slice -0.005740 vs s46000; training-log -0.003945; per-stage acc +0.0016~+0.0022; spec α 0.9320 (+0.0026); routing cap=0.020 79.18% (+8.21%, NEW trajectory peak); WAND bounds mildly widened (+3.7% / +0.9% / +2.9%); crossover gap +0.000303 |
| s48,500 | (not run) | 0.868639 | training-log new min |
| s49,500 | (not run) | 0.867675 | training-log new min |
| s50,000 | 0.811991 | 0.865501 | local slice -0.009342 vs s48000; training-log -0.009139; per-stage acc +0.0037~+0.0044 (largest single-step acc gain through s50); spec α 0.9852 (+0.0532, second-highest in trajectory after s28000=0.9882); routing cap=0.020 77.33% (-1.85% vs s48 peak); WAND bounds mildly narrowed (-2.2% / -2.3% / -3.9%); crossover gap +0.000107 |
| s51,500 | (not run) | 0.852479 | training-log new min; -0.0079 single-step drop (largest 500-step descent in trajectory) |
| s52,000 | (not run) | 0.858810 | epoch 1 ended around this region; pq_idx wrapped to 0 entering epoch 2 |
| s54,000 | 0.801717 | 0.855220 | first ckpt analyzed in epoch 2; local slice -0.010274 vs s50000 (cumulative s48→s54 full K=4: -0.019616); training-log -0.010281; per-stage acc +0.0044~+0.0050 (LARGEST single-step acc gain in trajectory; **0.45 boundary first crossed** at s3=0.4521); spec α 0.9566; routing cap=0.020 73.57%; WAND bounds widened uniformly (+7.6% / +7.7% / +12.4%); crossover gap +0.000023 (LOWEST in entire trajectory) |
| s55,500 | (not run) | 0.851502 | training-log new min |
| s56,000 | 0.795069 | 0.849220 | local slice -0.006648 vs s54000 (sub-0.80 first crossed on full K=4); training-log -0.005978 (0.85 boundary first crossed); per-stage acc +0.0028~+0.0032 (0.455 boundary first crossed at s3=0.4549); spec α 0.9430; routing cap=0.020 79.77% (+6.20%, NEW trajectory peak); WAND bounds mildly narrowed (-4.0% / +0.0% / -3.4%); crossover gap +0.000359 |
| s58,000 | 0.792391 | 0.844465 | local slice -0.002678 vs s56000 (smallest single-step descent since s44→s46); per-stage acc +0.0001~+0.0005 (smallest gain since s32→s34, essentially flat); spec α 0.8784 (-0.0646, lowest since s20000=0.9086); WAND bounds widened uniformly (+10.6% / +10.6% / +10.0%; bound 1→2=2.0701 trajectory single-bound high); crossover gap +0.000194; multiple sample-level regressions co-occur |
| s60,000 | 0.785370 | 0.840422 | local slice -0.007021 vs s58000 (descent rate recovers); training-log -0.004043; per-stage acc +0.0023~+0.0028 (resumes growth); spec α 0.9402 (+0.0618, recovers from s58 low); routing cap=0.020 80.92% (+4.16%, NEW trajectory peak surpassing s56=79.77%); WAND bounds substantially narrowed (-12.1% / -13.0% / -12.9%, s58 widening fully reverts); crossover gap +0.000553 |
| s60,500 | (not run) | 0.834882 | training-log new min; -0.0055 single-step drop |
| s61,000 | (not run) | 0.833518 | training-log new min |
| s62,000 | 0.779053 | 0.832344 | local slice -0.006317 vs s60000 (**sub-0.78 first crossed**); training-log -0.008078; per-stage acc +0.0027~+0.0030 (**0.46 boundary first crossed**); spec α 0.9795 (third-highest in trajectory); routing cap=0.020 77.43%; WAND bounds essentially flat; crossover gap +0.000471 |
| s63,000 | (not run) | 0.829964 | training-log new min (sub-0.83 first) |
| s64,000 | 0.772334 | 0.825504 | local slice -0.006719 vs s62000; per-stage acc +0.0034~+0.0037 (s32→s64 cumulative full acc gain +0.0359); spec α 0.9483; routing cap=0.020 80.51%; WAND bounds mildly narrowed |
| s64,500 | (not run) | 0.823171 | training-log new min (sub-0.824) |
| s66,000 | 0.769515 | (s65500=0.823685; s66000 not yet observed at probe time) | local slice -0.002819 vs s64000 (smaller magnitude; descent rate decelerating); per-stage acc +0.0012~+0.0018 (s32→s66 cumulative full acc gain +0.0371); spec α 0.9738 (+0.0255, recovers toward s62 third-place); routing cap=0.020 83.21% (+2.70%, **NEW trajectory peak** surpassing prior s60=80.92%); WAND bounds mildly narrowed (-1.5% / -3.1% / -4.8%); crossover gap +0.000553 |
| s68,000 | 0.761794 | 0.814863 | local slice -0.007721 vs s66000 (largest single-window descent of warmdown phase); training-log -0.009; per-stage acc +0.0031~+0.0036 (s32→s68 cumulative full acc gain +0.0407); spec α 0.9162 (-0.0576; sits between s60=0.9402 and s58 trajectory low 0.8784); routing cap=0.020 82.07% (-1.14pp; below s66 peak); WAND bounds widened uniformly (+13.85% / +16.74% / +18.10%); crossover gap +0.000326 |
| s70,000 | 0.757416 | 0.806862 | local slice -0.004378 vs s68000 (moderate descent); training-log -0.008; per-stage acc +0.0021~+0.0023 (**0.47 boundary first crossed**; s32→s70 cumulative full acc gain +0.0428); spec α 0.9139 (-0.0023, basically flat-low; the s68 drop did not recover); routing cap=0.020 83.45% (+1.38pp, **NEW trajectory peak** surpassing prior s66=83.21%); WAND bounds narrowed uniformly (-10.34% / -11.01% / -8.56%, fully reverts s68 widening); crossover gap +0.000268 |
| s72,000 | 0.755075 | 0.802531 | local slice -0.002341 vs s70000 (mild descent); training-log -0.004; per-stage acc +0.0013~+0.0015 (s32→s72 cumulative full acc gain +0.0441); **spec α 0.9708 (+0.0569, sharp recovery from s68/s70 low pair; the s58 single-window recovery pattern repeats with two-window delay across s68→s72)**; routing cap=0.020 84.31% (+0.86pp, **NEW trajectory peak** surpassing prior s70=83.45%); WAND bounds mildly re-widened (+1.43% / +4.56% / +2.37%, well below s68 widened regime); crossover gap +0.000306 |
| s74,000 | 0.749713 | 0.797773 | local slice -0.005362 vs s72000 (moderate descent; sub-0.75 first crossed); training-log -0.005; per-stage acc +0.0020~+0.0024 (s32→s74 cumulative full acc gain +0.0465); spec α 0.9484 (-0.0224, pulls back from s72 recovery but stays well above s68/s70 low pair); routing cap=0.020 86.52% (+2.21pp, **NEW trajectory peak** surpassing prior s72=84.31%); WAND bounds widened moderately (+8.47% / +9.50% / +6.43%, second-largest single-window since s58); crossover gap +0.000204 (lowest since s50-s54 era); algebra prompt produced first "Explanation: 5x = 13 - 3" algebraic-step structure since s62 |
| s76,000 | 0.741818 | 0.793753 | local slice -0.007895 vs s74000 (largest single-window descent since s66→s68 -0.0077; sub-0.745 first crossed); training-log -0.004; per-stage acc +0.0031~+0.0034 (s32→s76 cumulative full acc gain +0.0496); spec α 0.9568 (+0.0084, mild recovery); routing cap=0.020 90.76% (+4.24pp, **NEW trajectory peak** and **90% boundary first crossed**); WAND bounds mildly narrowed (-1.33% / -3.18% / +0.15%); crossover gap +0.000403; gold prompt produced first **atomic # 79 ✓** embedded in comprehensive Au + properties + use list response across the trajectory; France prompt produced best multi-fact response across the trajectory with no internal contradictions |
| s78,000 | 0.738087 | 0.789612 | local slice -0.003731 vs s76000 (mild descent; sub-0.74 first crossed); training-log -0.004; per-stage acc +0.0022~+0.0025 (s32→s78 cumulative full acc gain +0.0521; **0.05 cumulative milestone first crossed**); spec α 0.9190 (-0.0378, pulls back from s76 mild recovery); routing cap=0.020 83.79% (-6.97pp, major pullback from s76 trajectory peak); WAND bounds split (+5.45% bound 0→1 / +0.30% bound 1→2 / -1.10% bound 2→3); crossover gap +0.000365; **planets prompt produced first complete and correct modern 8-planet list across the entire trajectory** (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune; no Pluto; "named after Roman gods of Greek pantheon" ✓); gold prompt corrected s72 "highly reactive" error to "highly unreactive ✓" |
| s80,000 | 0.732713 | 0.783510 | local slice -0.005374 vs s78000 (moderate descent; sub-0.735 / sub-0.733 first crossed); training-log -0.006; per-stage acc +0.0022~+0.0026 (s32→s80 cumulative full acc gain +0.0544; **0.48 boundary first crossed**); spec α 0.9483 (+0.0293, recovers from s78 pullback); routing cap=0.020 87.66% (+3.87pp, recovers but below s76 peak); WAND bounds mildly narrowed (-1.43% / -1.20% / -1.88%); crossover gap +0.000445; **France prompt produced richest factual output across trajectory** (Paris + largest + north + Seine + culture/art/fashion + museums/parks/monuments, no errors); **Gold prompt added transition metals classification ✓** for first time across trajectory; planets and algebra prompts regressed (s78 8-planet breakthrough not retained; algebra back to "x is 5" pattern from s64 era) |

Local-slice training-objective BPB across the warmdown ckpts: 0.857982 (s30k) → 0.847991 (s32k) → 0.853621 (s34k) → 0.841936 (s36k) → 0.842198 (s38k) → 0.831678 (s40k) → 0.826550 (s42k) → 0.828415 (s44k) → 0.827073 (s46k) → 0.821333 (s48k) → 0.811991 (s50k) → 0.801717 (s54k) → 0.795069 (s56k) → 0.792391 (s58k) → 0.785370 (s60k) → 0.779053 (s62k) → 0.772334 (s64k) → 0.769515 (s66k) → 0.761794 (s68k) → 0.757416 (s70k) → 0.755075 (s72k) → 0.749713 (s74k) → 0.741818 (s76k) → 0.738087 (s78k) → 0.732713 (s80k) → 0.730046 (s82k) → **0.724738 (s83923, final)**. Non-monotonic (s32→s34 +Δ, s38 +Δ, s44 +Δ). Through s83923 the cumulative drop from s30000 is **-0.133244** (15.5% relative reduction).

### Sample-level concept oscillation under monotone BPB improvement

Greedy continuations on a fixed 7-prompt probe set track concept-level retention separately from BPB:

| capability | s78000 | s76000 | s74000 | s72000 | s70000 | s68000 | s66000 | s64000 | s62000 | s60000 | s58000 | s56000 | s54000 | s50000 | s48000 | s46000 | s44000 | s42000 | s40000 | s38000 | s36000 | s34000 | s32000 | s30000 | s28000 | s26000 | s24000 | s22000 | s20000 | s18000 | s16000 | s14000 |
|------------|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| `gold` symbol → `Au` | ✓ Au + soft/malleable/ductile + **"highly unreactive" ✓** + precious + yellow (then property repetition) | ✓ Au + atomic # 79 ✓ + soft/yellow/lustrous/malleable/ductile + uses (jewelry/coins/electronics/dentistry/medicine) | ✓ Au + soft/yellow/malleable/ductile + "easily cut with knife" ✓ | ✓ Au + soft/yellow/malleable/ductile + "highly reactive" wrong | ✓ Au + clean sentence repetition | ✓ Au + self-referential definition loop | ✓ Au + correct properties (soft/malleable/ductile/conductor) | ✓ Au + Wikipedia fact list (atomic # "19" wrong) | ✓ Au + 5 properties + Latin "aurum" | ✓ Au + "A and U" decomposition | ✗ "A" only | ✓ Au + sentence repetition (4th stable) | ✓ Au + sentence repetition (3rd stable) | ✓ Au + sentence repetition (stable) | ✓ Au + sentence repetition (no swap) | ✓ Au + 79-reference + jewelry | ✗ "79" only | ✗ "A" only + soft/malleable | ✓ Au + soft/malleable/jewelry | ✓ Au + "Au" loop | Au + yellow + soft/malleable | Au + ✗ "abundant" | ✓ + soft/malleable | ✓ but "abundant" wrong | ✓ + industries | ✓ + properties | ✓ | ✓ | ✓ | ✗ "24" | ✓ | ✗ |
| `gold` atomic number → 79 | (avoided in s78 sample) | **✓ "79" embedded in comprehensive Au response** | (avoided) | (avoided) | (avoided) | (avoided) | (avoided) | ✗ "19" (wrong; potassium's number) | (avoided) | (avoided) | (avoided; truncated) | (avoided) | (avoided) | (avoided) | (avoided) | (s46 produced 79 within Au response) | (s44 produced 79 alone) | (avoided) | (avoided) | (avoided) | (avoided) | (avoided) | (avoided) | (avoided) | ✓ "79" | (avoided) | ✗ "24" | - | - | - | - | - |
| Friday→tomorrow → Sunday | ✗ "Saturday" + religious Creation Week drift | ✗ "Saturday" + Matrix simulation drift | ✗ "Saturday" + bizarre "rest of the week" meta-language | ✗ "Monday" + initial Mon↔Fri loop then clean +1-day chain Fri→Sat→Sun→Mon→Tue | ✗ "Saturday" + alternating yesterday→today/tomorrow chain (+1/+2 confusion) | ✗ "Saturday" + alternating-frame all→Saturday | ✗ "Monday" + Internet topic drift | ✗ "Friday" + circular self-ref | ✗ "Saturday" + first logically correct +1-day chain | ✗ "Saturday" + chain logic broken | ✗ "Saturday" + alternating-framing | ✗ "Saturday" + clean self-repetition | ✗ "Monday" + mixed-framing | ✗ "Saturday" + correct +1-day chain | ✗ "Wednesday" + correct +1-day chain | ✗ "Saturday" + weekend continuation | ✗ "Tuesday" + bizarre temporal | ✗ "Saturday" + "100 years old" | ✗ "Saturday" + reverse-chain | ✓ "Sunday" + Sunday-school drift | ✗ narrative drift | ✗ + narrative drift | ✗ first ans, +1-day chain | ✗ infinite loop | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ |
| Full planet list (Mercury…) | **✓ Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune (modern 8, no Pluto, correct order) + named after Roman gods of Greek pantheon ✓** | ✗ "objects orbit the Sun" generic | ✗ "Sun is the star at the center" | ✗ "objects orbit Sun + Sun is center of solar system" | ✗ "only objects with solid surface" (factually wrong) | ✗ "objects orbit Sun + classified terrestrial/gas giants" generic | ✗ "objects that orbit the sun" generic (regression) | ✗ terrestrial/gas-giants split + first names: Mercury/Venus/Earth/Mars/Moon (Moon wrong) | ✗ "Jupiter largest at farthest" | ✗ "near/far from Sun" structure | ✗ "all in same orbit" | ✗ inner/outer/rocky/gas-giants taxonomy (no names) | ✗ "named after gods/goddesses" | ✗ "most common objects in universe" | ✗ "closest to sun, most massive" | ✗ "named after Greek god of sky" | ✗ "most diverse in universe" | ✗ "most massive bodies" | ✗ "orbit the sun" generic | ✗ "state of flux" | ✗ Sun/Moon included; Pluto/Venus/Mercury absent | ✗ Pluto re-added + ice/water | ✓ modern 8 (no Pluto) | ✗ Sun+Moon+Pluto+Belt | ✓ full 9 + Charon | ✗ Earth dropped | full 9 | 9+Charon+belt | inner 4 | full 9 | partial | partial |
| Math `5x + 3 = 13` → x = 2 | "x is equal to 1.5" single fractional answer (wrong; closer to 2 than s76 "1/3") | "x is equal to 1/3" single fractional answer (wrong) | 5-option MC w/ "Explanation: 5x = 13 - 3" — first algebraic-step structure since s62 (truncated) | 4-option MC duplicate "A.5 B.3 C.5 D.3" (correct value 2 absent) | "two solutions x=1 and x=13" (both wrong; 13 as one solution) | 5-option MC fractional choices A=1/3..E=1/4 (correct value 2 absent; D and E duplicate "2/3") | 5-option MC "A.1 B.2 C.3 D.4 E.5" (correct B=2 enumerated, not selected) | "x is 5. The answer is 5." (coefficient confusion) | "5x = 13-3 / 5x = 8 / x = 8/5 / x = 1" (first algebraic-step) | "A.3/B.4/C.5/D.6 / The answer is C." MC | "A.1.5/.../D.4.5 / The answer is B. 2.5" MC | "method of substitution" instruction | "A.3/B.4/.../H.10" 8-option MC | "x is 3" | "x is equal to 13/5" (treats 5x=13) | "x is 3" | "5 times as big as 3" + echo | "5x+3=13" echo | **"x is equal to 2"** (correct) | "x = 1" | "x is:" truncated | "A. 2 / B. 3 / C. 4" choices | "3" single integer | "multiple of 13" | "5x+3" circular | MC D=75 | "a square" | "13 times bigger" | "5","3" | "prime" | "3.5" | "factor 13" |
| Capital of France → Paris | ✓ Paris + largest in France ✓ + seat of govt ✓ + seat of French Academy ✓ (+ seat of EU/UN wrong, 2nd largest in EU debatable) | ✓ Paris + largest in France ✓ + 3rd in Europe + 2nd populous + 2nd visited after London (best multi-fact) | ✓ Paris + cascading wrong superlatives (1st/2nd/3rd contradicting) | ✓ Paris + north + Île-de-France + seat of govt + largest city + 10th in world | ✓ Paris + "largest city / most populous / Paris region / north" multi-fact | ✓ Paris + sentence repetition only (Île-de-France/Seine lost) | ✓ Paris + **Île-de-France ✓ + Seine ✓ + north** (richest factual output yet) | ✓ Paris + "capital of EU" loop | ✓ Paris + factual world-capital fragments | ✓ Paris + "capital of the world" loop | ✓ Paris + Hauts-de-Seine | ✓ Paris + Seine-et-Marne | ✓ Paris + sentence | ✓ Paris + "French Empire" | ✓ Paris + sentence | ✓ Paris + degenerate "Paris, Paris" loop | ✓ Paris + "south / 2nd largest" | ✓ Paris + "Europe/world largest" | ✓ Paris + "world capital" | ✓ Paris + "EU / largest city" | ✓ Paris + spurious extras | ✗ "French Republic" | ✓ + "most important city" | ✓ + UK/US loop | ✓ "Paris" | ✗ "south of France" | ✗ "2nd largest world" | - | - | - | - | - |
| Favorite color | red + "I love the color red" repetition | blue + "I love the color blue" repetition | blue + "I love the color blue" repetition | blue + "I love the color blue" repetition | red + "looks/feels/makes me feel" multi-clause | blue + "feel/think" two-clause alternation | blue + "I love the way" multi-clause | blue + multi-sense description | blue + "I love the way" loop | blue + clothing/household nouns | blue + clothing nouns | red + "I love the way" loop | red + "I love the way" loop | blue + "blue-eyed monster" | blue + "sky/water/clouds" | blue + "sky/ocean" | purple + "beautiful and mysterious" | blue + "I love blue" loop | red + "movie" loop | red + "I love red" loop | blue + "calming/soothing" | blue + "blue friends" | blue (positive) | red (dark) | blue | black | red | - | - | - | - | - |
| Antonym graph (hot→) | cold/hot binary loop | cold/hot binary loop | cold/hot binary loop | hot/cold/warm/cool multi-hop chain | cold/hot binary loop | cold/hot binary loop | cold/hot binary loop | cold/hot binary loop | cold/hot binary loop | cold/hot binary loop | cold/hot binary loop | cold/hot binary loop | cold/hot binary loop | cold/hot binary loop | cold/hot binary loop | cold/heat binary loop | cold/hot binary loop | cold/hot binary loop | cold/hot binary loop | cold/hot/dry/wet/windy chain | cold/hot binary | cold/cold loop | cold/warm/dry/moist/wet chain | cold↔hot loop | - | - | - | - | - | - | - | - |

Specific factual tokens swing in and out of top-1 between checkpoints even as token-averaged BPB improves. This is the long-tail-vs-frequent-token tradeoff: BPB is dominated by the bulk of frequent-token predictions, where a small calibration sharpening can hide rare-token rank shifts.

Sample-level output changes through s30000: s24000 produced wrong "atomic number 24" (gold prompt); s26000 produced "south of France" (capital prompt) and dropped Earth from the planet list; s30000 added Sun/Moon/Kuiper Belt to the planet list and looped on the Friday prompt.

At s32000 the four prompts produced new output forms versus prior checkpoints:
- Calendar: "Saturday" first-answer (still incorrect) followed by a +1-day chain continuation ("Saturday → Sunday → Monday → ...").
- Planets: 8-planet list (Mercury through Neptune), no Pluto, no Sun/Moon.
- Algebra `5x + 3 = 13`: "3" single integer. Truth is 2.
- Antonym: "hot/cold/warm/dry/moist/wet" multi-token continuation.

At s40000 the algebra prompt produced "x is equal to 2" — first checkpoint to produce the correct answer. Subsequent checkpoints produced an equation echo (s42), "5 times as big as 3" (s44), "x is 3" (s46/s50), "x is equal to 13/5" (s48), and an 8-option multiple-choice format A-H without 2 in the choices (s54). The gold-symbol prompt evolved Au+properties (s40) → "A" (s42) → "79" (s44) → "Au+79-ref+properties" (s46) → stable "Au + sentence repetition" (s48 / s50 / s54). The Friday prompt at s48/s50/s54 produces an incorrect first-answer (Wednesday/Saturday/Monday) but the continuation produces a +1-day chain across 7 days at s48/s50, with mixed-framing chain at s54. Color choice across s38-s54: red/red/blue/purple/blue/blue/red.

The dataloader is sequential (`pq_idx` advances monotonically through 848 shards); s44000 has seen pq_idx ≈ 719. The same prompt set will be re-run at s50000, s83923.

### Speculative-decoding acceptance trend

| step | E2 acceptance α | end-to-end speedup |
|------|----------------:|-------------------:|
| s8000  | 0.9539 | 1.54x |
| s12000 | 0.9539 | 1.54x |
| s14000 | 0.9652 | 1.55x |
| s16000 | 0.9853 | 1.59x |
| s18000 | 0.9375 | 1.52x |
| s20000 | 0.9086 | 1.48x |
| s22000 | 0.9511 | 1.54x |
| s24000 | 0.9824 | 1.58x |
| s26000 | 0.9737 | 1.59x |
| s28000 | 0.9882 | 1.60x |
| s30000 | 0.9824 | 1.58x |
| s32000 | 0.9348 | 1.52x |
| s34000 | 0.9320 | 1.51x |
| s36000 | 0.9294 | 1.51x |
| s38000 | 0.9483 | 1.53x |
| s40000 | 0.9822 | 1.57x |
| s42000 | 0.9403 | 1.54x |
| s44000 | 0.9294 | 1.52x |
| s46000 | 0.9294 | 1.52x |
| s48000 | 0.9320 | 1.51x |
| s50000 | 0.9852 | 1.59x |
| s54000 | 0.9566 | 1.56x |
| s56000 | 0.9430 | 1.54x |
| s58000 | 0.8784 | 1.45x |
| s60000 | 0.9402 | 1.52x |
| s62000 | 0.9795 | 1.58x |
| s64000 | 0.9483 | 1.53x |
| s66000 | 0.9738 | 1.58x |
| s68000 | 0.9162 | 1.50x |
| s70000 | 0.9139 | 1.50x |
| s72000 | 0.9708 | 1.58x |
| s74000 | 0.9484 | 1.54x |
| s76000 | 0.9568 | 1.56x |
| s78000 | 0.9190 | 1.51x |
| s80000 | 0.9483 | 1.54x |
| s82000 | 0.9377 | 1.53x |
| **s83923** | **0.9852** | **1.61x** |

Drafter acceptance is non-monotone across the trajectory: declined s16k → s20k, rose through s22k → s28k (peak 0.9882 at s28k), drifted s32-s36 (0.93 range), rose through s38k-s50k with intermittent dips, dropped to 0.8784 at s58k (lowest since s20k), recovered through s60-s62, oscillated through s64-s78 with the s68/s70 low pair (0.9162 / 0.9139) standing out as a localized regime change followed by partial recovery (s72=0.9708, s74=0.9484, s76=0.9568, s78=0.9190). End-to-end speedup has been 1.45-1.69x across all 31 measured checkpoints.

### Confidence-aware routing trend

| step | routed @ cap=0.020 | projected speedup |
|------|-------------------:|------------------:|
| s8000  | 59.94% | 1.416x |
| s12000 | 63.70% | 1.454x |
| s14000 | 63.37% | 1.450x |
| s16000 | 63.07% | 1.447x |
| s18000 | 66.04% | 1.478x |
| s20000 | 67.05% | 1.489x |
| s22000 | 61.21% | 1.428x |
| s24000 | 67.35% | 1.493x |
| s26000 | 68.26% | 1.503x |
| s28000 | 62.45% | 1.441x |
| s30000 | 68.39% | 1.504x |
| s32000 | 74.33% | 1.573x |
| s34000 | 61.22% | 1.429x |
| s36000 | 67.63% | 1.496x |
| s38000 | 72.06% | 1.546x |
| s40000 | 73.19% | 1.559x |
| s42000 | 68.90% | 1.510x |
| s44000 | 77.57% | 1.613x |
| s46000 | 70.97% | 1.533x |
| s48000 | 79.18% | 1.634x |
| s50000 | 77.33% | 1.610x |
| s54000 | 73.57% | 1.564x |
| s56000 | 79.77% | 1.642x |
| s58000 | 76.76% | 1.603x |
| s60000 | 80.92% | 1.657x |
| s62000 | 77.43% | 1.611x |
| s64000 | 80.51% | 1.652x |
| s66000 | 83.21% | 1.688x |
| s68000 | 82.07% | 1.673x |
| s70000 | 83.45% | 1.692x |
| s72000 | 84.31% | 1.704x |
| s74000 | 86.52% | 1.736x |
| s76000 | 90.76% | 1.801x |
| s78000 | 83.79% | 1.697x |
| s80000 | 87.66% | 1.753x |
| s82000 | 86.08% | 1.729x |
| **s83923** | **85.05%** | **1.715x** |

Position-level top-1 routing fraction (cap=0.020) and speculative acceptance α track different slices of the trunk's confidence distribution: routing reads margin at boundary positions; spec acceptance reads step-by-step alignment between stage 0 and full-stack. Through s40000 they have moved in different directions in some windows and the same direction in others. The late-trajectory routing fraction progressed s40k=73% → s60k=81% → s76k=91% (peak) → s78k=84% — stage 0 alone suffices for 84-91% of positions within a 2% accuracy regression budget across the late warmdown, with the s76 peak followed by a s78 pullback. Speculative acceptance α has been more volatile (0.88-0.99 range) but remains in a regime where 4-token speculative draft delivers consistent 1.45-1.69x end-to-end speedup.

### Stage diversity probe — early vs late trajectory

#### Early trajectory: s14000 head decomposition

Inference-time analysis of `lm_head_stages[k].weight` at s14000 (results essentially unchanged at s20000):

- **SVD top-1 alignment**: stages s1, s2, s3 dominant left singular vectors are mutually identical (cosine ≈ 1.000); stage s0 is anti-aligned (cosine ≈ -0.98). The 4 stages collapse into a 2-cluster structure {s0} vs {s1, s2, s3}.
- **Gram-Schmidt orthogonalization**: 77.2% of s1, 91.8% of s2, 92.0% of s3 weight projects onto the span of earlier stages. Only ~38% of total per-stage parameter budget carries unique information.
- **Single-stage perturbation symmetry**: turning OFF any single stage (β_k = 0) costs a uniform +0.0025-0.0030 BPB, regardless of `k` — operationally interchangeable.
- **β scaling sweep**: the trained β = 1 inference rule is BPB-optimal but factual-recall-suboptimal. β = 2 recovers ~2× the gold-as-Au probability at +0.05 BPB cost; β = 0 (drop the stage delta entirely) costs +0.10 BPB.

#### Late trajectory: s76000 head decomposition

Re-running the same probes at s76000 (90.6% trained):

- **SVD top-1 alignment**: cluster structure shifted from `{s0} vs {s1, s2, s3}` (s14k) to **depth-tier `{s0, s1} vs {s2, s3}`** (s76k). Pairwise dominant-singular-vector cosines: s0↔s1 = +0.977 (aligned), s2↔s3 = +0.997 (aligned), {s0,s1}↔{s2,s3} = -0.97 to -0.99 (anti-aligned). Stage 1 has migrated from the s1/s2/s3 cluster (early) into alignment with s0 (late). The boundary now corresponds to trunk depth: shallow tier (s0 at depth 16, s1 at depth 22) vs deep tier (s2 at depth 27, s3 at depth 32).
- **Gram-Schmidt orthogonalization**: unique residual norms grew from s14k {s1=22.8%, s2=8.2%, s3=8.0%} to s76k **{s1=21.1%, s2=11.8%, s3=11.3%}**. Total unique parameter budget increased from ~38% (s14k) to **~44% (s76k)**. Stages s2 and s3 each gained ~3 percentage points of unique content; stage s1 lost ~2pp.
- **Top-singular-vector token list**: s0 and s1 both load on suffix-like tokens ('TION', 'ATE', 'EAR', 'IAL', 'BER'); s2 and s3 load on shorter morpheme fragments ('UN', 'IT', 'PER', 'TH', 'EV', 'AL'). The shallow tier emphasizes longer suffix completions; the deep tier emphasizes finer morphemic refinement.

**Reading**: at s14000 the stages-as-experts story was degenerate — only stage 0 carried distinct signal and stages 1-3 were mutually redundant. By s76000 the structure has reorganized into a depth-tier specialization: shallow stages {s0, s1} cluster together and deep stages {s2, s3} cluster together, with non-trivial unique content in each later head (s2 / s3 each ~11% unique vs ~8% earlier). This is consistent with the late-trajectory routing improvement (cap=0.020 fraction routed to stage 0 went from 73% at s40k to 91% at s76k): the shallow tier becomes confident enough to handle most positions, while the deep tier specializes on the residual ~9-15% where extra refinement is needed. The PoE↔single-s3 crossover gap remains small (+0.0002 to +0.0005) — meaning the geometric-mean aggregation gives a measurable but modest improvement over the deepest single stage at every point in the trajectory. See `cognica/Cognica-PoE-v1.0-1.3B-base` (4 symmetric stages of 6 layers, shared `lm_head` only) for the diversity-vs-layout disambiguation.

### Diversity vs layout

The asymmetric (16, 6, 5, 5) layout *itself* is a hypothesis on the input variable side: stage 0's 50% trunk share gives stages 1-3 only shallow depth (5-6 layers each) on top of an already-refined representation, which structurally biases them toward refining stage 0's output rather than producing independent evidence. Whether the absence of diversity is *caused* by this layout or by the PoE training signal itself can be cleanly separated by comparing against the 1.3B symmetric (4×6, shared head) release. Result of that comparison will be added when measured.

## Advanced PoE inference helpers

All four PoE-specific inference modes are exposed directly on `CognicaPoEForCausalLM`. They re-forward the full prefix each decode step (no KV cache); wall-clock speedups come from reduced trunk depth.

```python
import torch

# 1. Single-stage prediction (uses head k at boundary k only).
logits = model.forward_stage(input_ids, stage=3)        # (B, T, V) float32

# 2. PoE-aggregated log-probabilities over the first K' stages.
log_p = model.forward_aggregated(input_ids, max_stages=2)  # log-softmax shape (B, T, V)

# 3. Generation with prefix pruning (K' <= K stages, asymmetric trunk depth).
out = model.generate_prefix(input_ids, max_stages=1, max_new_tokens=64)
# K'=1 on (16,6,5,5) -> 16 trunk layers (~2.2x decode speedup)

# 4. Single-stage generation.
out = model.generate_stage(input_ids, stage=0, max_new_tokens=64)

# 5. WAND adaptive depth (Jeong 2026 Section 5.3). p99 bounds are now read
#    from config.json (`poe_wand_p99_bounds_per_stage_head`); the class
#    constant is fallback only. Override per call via `p99_bounds=...`.
out, stages_used = model.generate_wand(
    input_ids, max_new_tokens=64, safety=1.0,
    return_stages_used=True,
)

# 6. Self-speculative decoding (zero-extra-training accelerator).
out, accept_rate = model.generate_speculative(
    input_ids, max_new_tokens=64,
    draft_stage=0, k_draft=4, return_acceptance=True,
)

# 7. Parallel stage composition (Jeong 2026 Section 6.5.5).
out = model.generate_parallel_composition(
    input_ids, stages=(2, 3), stage_weights=(1.0, 1.0), max_new_tokens=64,
)
```

Implementation notes for this release (`per_stage_head=True`):
- `forward_stage(stage=k)` returns logits using `lm_head(x_k) + lm_head_stages[k](x_k)` at boundary `k`. Each stage head was trained additively on top of the shared `lm_head`.
- `generate_speculative` verifier uses the full PoE aggregate over all K stages. Greedy match by construction guarantees output identity with `model.generate(...)`.
- `generate_wand` runs in cumulative-PoE log-prob space; the p99 bound must be expressed in that same scale (config.json carries this per-checkpoint).

## Limitations

- **Final release** (s83923 / 100.00% complete; **training finished 2026-05-07 12:31 KST**): all 27 published checkpoints (s2000, s4000, ..., s82000, s83923) remain available as separate branches for trajectory analysis. The `main` branch tracks the final ckpt s083923.
- **Calendar prompt** ("yesterday → tomorrow"): first-answer outputs have been "Sunday" (s14000 only), narrative drifts (s16-s30), "Saturday" (s32, s40-s42, s46, s50, s56-s62, s68, s70, s74, s76, s78), "Tuesday" (s44), "Sunday" (s38), "Wednesday" (s48), "Monday" (s54, s66, s72), "Friday" (s64). At s62k the chain continuation was the first to be logically correct; at s72k the chain stabilized into a clean +1-day chain. From s74k onward the response drifts into topic tangents (rest-of-the-week meta-language at s74, Matrix at s76, Creation Week at s78) — the calendar prompt remains a persistently unsolved factual probe.
- **Math prompt** `5x+3=13` (correct: x=2): outputs include "factor 13" / "a square" / multiple-choice formats / circular / "multiple of 13" / "3" / "1" / "x is equal to 2" (s40, only correct so far) / "5x+3=13" echo / "5 times as big as 3" / "x is 3" (s46/s50) / "x is equal to 13/5" (s48) / 8-option MC A-H (s54) / "method of substitution" instruction (s56) / 4-option MC self-asserted "B. 2.5" (s58) / 4-option MC "C" (s60) / first algebraic-step structure with arithmetic error (s62) / "x is 5" coefficient confusion (s64) / 5-option MC including B=2 enumerated but not selected (s66) / 5-option MC with fractional choices A=1/3..E=1/4 (s68) / "two solutions x=1 and x=13" (s70) / 4-option MC duplicate "A.5 B.3 C.5 D.3" (s72) / 5-option MC negative integers w/ "Explanation: 5x = 13 - 3" (s74) / "x is equal to 1/3" single fractional answer (s76) / "x is equal to 1.5" single fractional answer (s78; closer to correct value 2 than s76 1/3 but still wrong).
- **Planets prompt**: at s56k inner/outer/rocky/gas-giants taxonomy first appeared. At s60k near/far structural language. At s62k ordering-by-distance with "Jupiter largest". At s64k the response listed actual planet names for the first time but with "terrestrial / gas giants" categorical split where terrestrial = "Mercury, Venus, Earth, Mars, and the Moon" (Moon wrongly included). At s66-s76 the response oscillated between generic "objects orbit the Sun" framings and incorrect categorical claims. **At s78k the response produced the first complete and correct modern 8-planet list across the entire trajectory**: "The planets are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune" + "named after the Roman gods of the Greek pantheon" ✓.
- **s58000 reorganization signals (transient)**: spec α dropped sharply (-0.0646), WAND p99 widened uniformly (+10%), per-stage acc gain decelerated, gold/planets prompts regressed. At s60k–s64k these signals reverted: spec α rose to 0.9402, 0.9795, then 0.9483; WAND narrowed and held; per-stage acc resumed +0.002~0.004 growth; gold/planets prompts produced richer / structured outputs.
- **s68000 signal mismatch (fully recovered by s72000)**: at s68 largest local-slice BPB descent of the warmdown phase (-0.0077 full K=4) co-occurred with largest spec α drop since s56→s58 (-0.0576) and uniform WAND widening (+14~18%). At s70 WAND fully reverted, routing set new peak 83.45%, BPB descent continued, per-stage acc crossed 0.47, but spec α stayed flat at 0.9139. **At s72 spec α recovered sharply (+0.0569 → 0.9708)**, routing set another peak 84.31%. The s58→s60 single-window recovery pattern played out across s68→s72 with a two-window delay.
- **s74000 → s78000 progression**: at s74 BPB descended moderately, spec α pulled back, WAND widened moderately, sample regressed on France and Antonym. At s76 BPB descent resumed strongly (-0.0079), per-stage acc gained +0.003, routing crossed the 90% boundary (90.76% peak), gold prompt produced first correct atomic # 79 ✓ in a comprehensive Au response, France prompt produced best multi-fact response. At s78 BPB continued (-0.0037; sub-0.74 first crossed), per-stage acc crossed the 0.05 cumulative milestone (s32→s78 = +0.0521), routing pulled back to 83.79%, and **the planets prompt produced the first complete and correct modern 8-planet list across the entire trajectory** (Mercury through Neptune, no Pluto). Gold prompt corrected the s72 "highly reactive" error to "highly unreactive" ✓.
- **Stage diversity at the (16, 6, 5, 5) asymmetric layout**: PoE↔single-s3 crossover gap stays in [+0.000067, +0.000553] across all measured checkpoints — the PoE renormalized aggregate is close to the single-best-stage value at every point. The early-trajectory finding ("stages-as-experts degenerate at s14000") is partially superseded by the late-trajectory measurement: at s76000 the head SVD shows a depth-tier cluster structure `{s0, s1} vs {s2, s3}` and unique parameter budget grew from ~38% to ~44%. See "Stage diversity probe" section above for the early-vs-late comparison.
- **The model is a base (pretrained) checkpoint** — chat / SFT fine-tuning is not included in this release.

## License

Apache 2.0. See `LICENSE` and `NOTICE`.

## Citation

If you use this release, please cite the companion paper for the PoE per-stage-head methodology:

```
@misc{jeong2026poe,
  author = {Jeong, Jaepil},
  title  = {Product of Experts as Scalable Local Learning: Modular Construction at 1.3B Parameters},
  year   = {2026},
  doi    = {10.5281/zenodo.19547653},
  publisher = {Zenodo},
}
```

A 3B-specific paper is in preparation.

## Related models

- [`cognica/Cognica-PoE-v1.0-1.3B-base`](https://huggingface.co/cognica/Cognica-PoE-v1.0-1.3B-base) — 1.3B PoE per-stage release with shared `lm_head` (no per-stage additive heads), 4 symmetric stages of 6 layers, ClimbMix dataset.
- [`cognica/Cognica-BP-v1.0-1.3B-base`](https://huggingface.co/cognica/Cognica-BP-v1.0-1.3B-base) — Backprop baseline, same compute / dataset / tokenizer as 1.3B PoE.
