---
license: apache-2.0
base_model: Qwen/Qwen3-30B-A3B
tags:
  - nvfp4
  - fp4
  - quantized
  - llm-compressor
  - rtn
  - moe
  - vllm
pipeline_tag: text-generation
base_model_relation: quantized
library_name: transformers
language:
- en
- ko
---

# Qwen3-30B-A3B-NVFP4-RTN

NVFP4 (4-bit weights and activations) quantization of `Qwen/Qwen3-30B-A3B`, produced with
**llm-compressor** using a **round-to-nearest** oneshot over 1,024 calibration samples.
**18.11 GB** on disk against the 56.89 GB bf16 original, a 3.14x reduction.

This is the **cheap** half of a deliberate pair. `ThakiCloud/Qwen3-30B-A3B-NVFP4-GPTQ` is the
identical model at the identical bit width and file size, built with GPTQ instead. Both are
published so the trade is visible rather than asserted.

## Quality (measured, not inherited)

Single B200, **vLLM 0.27.1**, **lm-eval 0.4.12**, full sets, no `--limit`.
MMLU n=14,042 (loglikelihood); GSM8K-CoT n=1,319, 8-shot (generative).

| build | recipe | quantize time | MMLU | GSM8K (strict) |
|---|---|---|---|---|
| `Qwen/Qwen3-30B-A3B` (bf16) | — | — | **0.7779** | 0.8741 |
| **this model** | llm-compressor, RTN | 5,271 s | 0.7676 (−1.03pp) | 0.8999 |
| `ThakiCloud/Qwen3-30B-A3B-NVFP4-GPTQ` | llm-compressor, GPTQ | 23,730 s | **0.7743** (−0.36pp) | 0.8878 |
| `RedHatAI/Qwen3-30B-A3B-NVFP4` | RTN | — | 0.7675 (−1.04pp) | 0.8939 |

**This build loses about 1pp of MMLU** (z = −2.2, borderline significant). The GPTQ sibling
does not (−0.36pp, z = −0.8). GPTQ costs 4.5x the quantization time, and that 1pp is what it
buys. Both timings come from `quantize_meta.json`, which ships in this repo. For a lot of deployments 1pp of MMLU is not worth 5.1 extra GPU-hours; for some it is.
The pair exists so that is your call and not ours.

**This build reproduces `RedHatAI/Qwen3-30B-A3B-NVFP4` to within 0.01pp MMLU** (0.7676 vs
0.7675), which is how we established that their NVFP4 is RTN and not GPTQ. If you were
choosing between this and theirs on quality, they are the same checkpoint in every way we can
measure; theirs is 1.23 GB smaller.

**We do not claim quantization improves math.** GSM8K comes out above bf16 for every 4-bit
build in the table, consistently in sign, but z runs 1.1 to 2.1 over 1,319 generative samples
and is not separable from sampling noise. The defensible claim is **no measurable degradation
on GSM8K**.

## Kernel path (the part most FP4 cards leave out)

A 4-bit checkpoint can hold NVFP4 weights and still expand them to bf16 for every matmul —
slower than bf16, saving only memory. So we assert the kernel rather than assume it:

```
Using 'FLASHINFER_TRTLLM' NvFp4 MoE backend     # B200, no fallback warning
```

Verified on B200 (SM100) with vLLM 0.27.1, with no `does not have native support for FP4`
warning in the serving log.

⚠️ **Blackwell only.** On Hopper (H200/H100) vLLM falls back to weight-only Marlin emulation,
which we measured at roughly **0.85x of bf16**. NVFP4 is not a speed win on SM90; FP8 is the
format that wins there.

## Serving energy

Single B200, decode-dominant workload, GPU power only (host and cooling excluded):

| build | tok/J |
|---|---|
| bf16 | 27.4 |
| **this model** | **46.8** |

⚠️ That run was **not** saturated (GPU utilisation 54 to 85 percent on 29-token prompts), so
we withdraw its throughput claim and quote only the power gap, which is the defensible part.

## Usage

```bash
vllm serve ThakiCloud/Qwen3-30B-A3B-NVFP4-RTN --max-model-len 8192
```

Check the serving log for the backend line above. `MARLIN` or a native-support warning means
you are measuring emulation, not FP4.

## Scope

One model, one recipe, one engine version, one GPU generation for the kernel claim. Quality
was measured on MMLU and GSM8K only; code, multilingual and long-context behaviour are
unevaluated and unclaimed.
