---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model:
  - LiquidAI/LFM2.5-24B-A2B
base_model_relation: finetune
pipeline_tag: text-generation
library_name: gguf
language:
  - en
  - ar
  - zh
  - fr
  - de
  - ja
  - ko
  - es
  - pt
  - it
  - vi
  - th
  - id
  - hi
  - ru
  - pl
tags:
  - gguf
  - llama.cpp
  - abliterated
  - heretic
  - lfm2
  - lfm2moe
  - moe
  - liquid
---

# LFM2.5-24B-A2B-Abliterated — GGUF

An abliterated build of [`LiquidAI/LFM2.5-24B-A2B`](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B),
produced with [Heretic](https://github.com/p-e-w/heretic), then converted to GGUF and quantized. The base is a 23.97B-parameter Mixture-of-Experts (`lfm2moe`, 64 experts, top-4, ~2.45B
active) with a hybrid backbone: 40 blocks = 30 double-gated short-conv + 10 GQA attention.

> **Modification notice** (LFM Open License §4(b)). These files are modified derivatives of
> `LiquidAI/LFM2.5-24B-A2B`. 926 weight tensors were altered by directional ablation to reduce
> refusal behavior — 896 per-expert `down_proj` (`w2`) and 30 attention/short-conv `out_proj` — then
> converted to GGUF and quantized. **Liquid AI did not produce, endorse, or review this build, and
> its behavior is not theirs.**

## Read this before using it

LFM2.5 is a pure reasoning model — its chat template always opens a `<think>` block, with no
non-thinking mode. Heretic scores refusals with the think block skipped (`--response-prefix
'</think>\n\n'`), or its markers (`illegal`, `harmful`, …) fire on *reasoning* text even when the
model complies — so the selected trial's **19/60** is a scoring artefact, not the served effect.

Measured with **thinking on** — the regime you serve — on a 44-prompt held-out harmful battery
(`bench-ablit.py`, distinct from the optimiser's prompts), UD-IQ3_XXS, temp 0.1:

| | stock | abliterated |
| --- | --- | --- |
| refusal markers | 43/44¹ | 21/44 |
| **hand-sorted** | **44/44 refuse** | **≈34 comply / ≈9 deflect / ≈1 refuse** |

¹ The one stock marker "miss" was itself a refusal, so stock is effectively **44/44**.

Markers mislead both ways, so the 44 were sorted by behaviour: a response that opens with a
disclaimer then delivers the content counts as compliance, and one that pivots to a harmless reading
of the prompt counts as deflection. The buckets (a human read of response openings, ±a few):

- **~34 genuinely comply** with the harmful request.
- **~9 deflect** to a safe reading.
- **~1 clean refusal.**

At **KL 0.169** this is the strongest ablation in this series, yet it cost no measured reasoning
(see below).

## Why int8 / unfused experts (provenance)

The base is **47.9 GB in bf16**, which does not fit a 48 GB GPU, and the next card up costs ~4× as
much. transformers 5 also loads `lfm2_moe` with its 64 experts **fused** into one 3-D parameter, so
stock Heretic + PEFT would silently abliterate attention only, never the experts (22.9B of the 24.0B
parameters).

Both were handled by a shim (`heretic-mps/unfuse_moe.py`, `UNFUSE_INT8=1`): the model is built on
`meta`, the fused experts are **unfused into per-expert int8 linears filled straight from the
checkpoint** (the fused bf16 experts never exist, on GPU or in host RAM — ~25 GB total), and Heretic
searches against that. **Only the search sees int8.** The export merges the chosen trial's deltas
onto the **original bf16** shards (`streaming_merge.py`), so no int8 error reaches the released
weights. The int8 experts were verified against bf16 on real activations before the search (relative
error 0.5–1.0%; padding-batch KL 0.0003).

## The quants

Five GGUFs + the imatrix. The three `UD-*` files **replicate Unsloth's
[`LFM2.5-24B-A2B-GGUF`](https://huggingface.co/unsloth/LFM2.5-24B-A2B-GGUF) layout tensor-for-tensor**
(every per-tensor type cloned from their header; `428 tensors, 0 differ` on each). `Q4_K_M` and
`Q8_0` use llama.cpp's stock mixes, matching the other repos in this series.

| file | size | notes |
| --- | --- | --- |
| `…-UD-IQ2_XXS.gguf` | 7.47 GB | smallest; experts IQ2 |
| `…-UD-IQ3_XXS.gguf` | 8.96 GB | the one benchmarked below; experts IQ2_S/IQ3_S |
| `…-UD-Q3_K_XL.gguf` | 10.95 GB | higher-quality UD mix |
| `…-Q4_K_M.gguf` | 14.53 GB | stock mix |
| `…-Q8_0.gguf` | 25.49 GB | stock mix; near-lossless |
| `…-imatrix.gguf` | 56 MB | see below |

**Unsloth published no imatrix for this model**, and IQ2_XXS / IQ3_XXS cannot be built without one
(it is a hard error, not a warning). So the importance matrix here is **ours**, computed from this
*abliterated* model's own Q8_0 over
[bartowski's `calibration_datav3`](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8).
Only the imatrix rounding differs from Unsloth's files; the tensor types are identical.

## Capability check

Abliteration damage concentrates in **mathematical reasoning** — a cross-architecture study (Young,
2025) puts Heretic's mean GSM8K change at −7.81 pp, with a −18.81 pp (−26.5%) worst case on
Yi-1.5-9B while that model's MMLU and HellaSwag barely moved. At KL 0.169 that risk is the thing to
check, so it was checked.

**GSM8K, paired, n=100, thinking on, identical sampling on both builds (UD-IQ3_XXS):**

| | accuracy |
| --- | --- |
| stock | **98/100** |
| abliterated | **98/100** |

Delta **0.00 pp**. Discordant pairs split **1/1** (one problem each build missed that the other got),
net flips **0**, McNemar exact **p = 1.000**. No truncations on either side. A regression the size
that study reports would need ~19 net flips against this build; there were none.

Caveats: n=100 excludes a *large* regression, not a 2–3 pp one; and **MMLU,
coding, long context, and the 15 non-English languages are unmeasured** — a refusal-direction
ablation could plausibly bite harder on the multilingual side than on English math.

## The selected trial

Heretic's TPE search ran 80 trials and auto-selected **trial 68** off the Pareto front: **19/60**
refusals at **KL 0.1689** (baseline 59/60). Abliteration is **not** bit-reproducible from the recipe
— a re-run lands on a different trial — so the trial's parameters are published for Heretic's
`--reproduce`:

```
direction_index                    = per layer
attn.o_proj.max_weight             = 1.43
attn.o_proj.max_weight_position    = 26.25
attn.o_proj.min_weight             = 1.34
attn.o_proj.min_weight_distance    = 17.11
mlp.down_proj.max_weight           = 1.45
mlp.down_proj.max_weight_position  = 24.65
mlp.down_proj.min_weight           = 0.50
mlp.down_proj.min_weight_distance  = 6.82
```

(`attn.o_proj` covers both `self_attn.out_proj` and the short-conv blocks' `conv.out_proj`;
`mlp.down_proj` is each expert's `feed_forward.w2`. "per layer" means each layer used its own refusal
direction.) More conservative points on the same front, if you want less behaviour change and even
lower divergence: **40/60 @ KL 0.071** (trial 62), **38/60 @ KL 0.075** (trial 61).

## Prompt sets

[Heretic](https://github.com/p-e-w/heretic)'s built-in defaults, unchanged — refusal directions from
the training splits, optimiser scoring on `test[:60]`:

| dataset | used for |
| --- | --- |
| [`mlabonne/harmful_behaviors`](https://huggingface.co/datasets/mlabonne/harmful_behaviors) | refusal directions; optimiser scoring |
| [`mlabonne/harmless_alpaca`](https://huggingface.co/datasets/mlabonne/harmless_alpaca) | refusal directions; KL divergence + refusal control |

The 44-prompt battery in the tables above is a **held-out** harmful set (`bench-ablit.py`), distinct
from the optimiser's prompts. Neither dataset declares a license on the Hub.

## Verifying the build

```
14e78558266e8ec41852810523d5eac6a5bca519c92fa31f120371f50532cef7  LFM2.5-24B-A2B-Abliterated-UD-IQ2_XXS.gguf
f7de3abe93401891580936573d6f7cc289b504f633628bc6f0609e12d4e5d76e  LFM2.5-24B-A2B-Abliterated-UD-IQ3_XXS.gguf
69034a38ff8cc1f147470c021970c4331da13670f9257e6fcf4e4e1425e30cfb  LFM2.5-24B-A2B-Abliterated-UD-Q3_K_XL.gguf
ed9be86be844d32bee1d810278b4f25bd27c36a2f8b096cbddb27c95b03a6b75  LFM2.5-24B-A2B-Abliterated-Q4_K_M.gguf
c3ea9ec2534eb513f20de3e03942309d8d44fb647911876e9bbe83567b4b04af  LFM2.5-24B-A2B-Abliterated-Q8_0.gguf
b32e4b4502691bf7d4203d25af9b9d980a3d6b4d9ecaa8cd906be896d8432403  LFM2.5-24B-A2B-Abliterated-imatrix.gguf
```

## License

**LFM Open License v1.0**, inherited from `LiquidAI/LFM2.5-24B-A2B` — the full text is in `LICENSE`,
copied verbatim from the base model repo (sha256 `4d28ca14…70068c`). Abliteration and quantization
change nothing about it.

This is **not** an Apache/MIT-style license:

- **§5 Commercial Use Limitation** — the commercial rights granted are conditioned on you or your
  legal entity not exceeding the **Threshold**, defined in §1 as **annual revenue of $10,000,000 USD
  or more**. Commercial use by an entity over that threshold is _not licensed_ by this agreement.
- Non-commercial and research use, and use by qualified non-profits for such purposes, are
  unrestricted by §5.
- §3 carries a patent-litigation termination clause; the license grants no trademark rights.

Read `LICENSE` yourself before any commercial deployment — the summary above is orientation, not
legal advice.

## Credits

- [LiquidAI](https://huggingface.co/LiquidAI) — the LFM2.5-24B-A2B base model
- [p-e-w/heretic](https://github.com/p-e-w/heretic) — the abliteration tooling and method
- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) — conversion and quantization
- [unsloth](https://huggingface.co/unsloth) — the UD quant layout these three UD files replicate
- [mlabonne](https://huggingface.co/mlabonne) — `harmful_behaviors` and `harmless_alpaca`
- [bartowski](https://huggingface.co/bartowski) — `calibration_datav3`, used to compute the imatrix

## Tested setup

I've run the IQ3_XXS quant via llama.cpp in [Reika](https://reikacode.com) on an M2 MacBook Air (16GB) at 64k and 131k context, with the default f16 KV cache. This was general use and a few informal evals, not a benchmark.

## Supporting my work

If these quants are useful to you, consider supporting them via [Ko-fi](https://ko-fi.com/alexwkleung). It goes toward local hardware for quantizing and testing larger models. I also build [Reika](https://reikacode.com), a coding agent CLI designed around small local models first.
