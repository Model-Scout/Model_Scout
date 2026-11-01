---
language:
  - en
  - es
  - fr
  - de
  - ja
  - it
  - pt
  - zh
  - ar
  - da
  - ko
  - nl
  - pl
  - ru
  - sv
license: other
license_name: nvidia-nemotron-open-model-license
license_link: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license/
base_model: nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16
pipeline_tag: text-generation
tags:
  - gguf
  - nemotron-3
  - moe
  - local
  - quantized
  - padded
---

# Nemotron 3 Nano 30B A3B — pirola padded, IQ3_XXS (fork-only GGUF)

A **13.37 GiB** GGUF of `NVIDIA-Nemotron-3-Nano-30B-A3B` that fits **fully on a
16 GB GPU at 262,144 context** — smaller and higher precision than any published
quant of this model (the best public option, bartowski's 18.09 GB IQ2_XXS, does
not fit the card at all).

## First padded build for this family — verified 2026-08-12

A full audit of Hugging Face, GitHub and the web (100 % enumeration: 7,106 repos /
668 Nemotron GGUF files; 105 repos / 235 Cascade-2-30B-A3B GGUF files; every
llama.cpp issue/PR/commit; every relevant discussion) established the following
facts:

- **No other padded or genuine sub-4-bit GGUF exists** for `Nemotron-3-Nano-30B-A3B`
  or `Nemotron-Cascade-2-30B-A3B`. This file is the only one.
- Every published "sub-4-bit named" GGUF of these two models is pinned at
  **16.5–18.1 GB** (effective 4.6–5.2 bpw): the expert dims (1856/2688, not
  256-divisible) silently fall back to IQ4_NL in `llama-quantize`'s
  `tensor_type_fallback`. The quantizers documented this themselves (bartowski,
  unsloth, AesSedai). Even IQ1_M (1.56 bpw) builds are ~17.9 GB — files do not
  shrink with bit-depth below the floor.
- The only sub-18 GB llama.cpp files for these models are 4-bit FP formats
  (ROCmFP4 15.73 GB; NVFP4/MXFP4 ≈16.7–17.9 GB) — not sub-4-bit and not padded.
- The smaller JANG build (Cascade-2, ~10 GB) is **MLX-only** (Apple Silicon): MLX
  group quantization (group 32/64, no 256-divisibility constraint) — not padded and
  not a llama.cpp GGUF.
- The zero-padding *idea* was floated in a draft, never-merged llama.cpp PR
  (`708-145/llama.cpp#33`, Dec 2025) and an unsloth discussion; **no file was ever
  produced from it**. This repo is the first working realization: padded weights +
  padded imatrix + loader patch, developed 2026-08-10.

**⚠️ Critical: this file requires a fork build of llama.cpp.** The model's expert
weights have their reduction axes zero-padded to 256-divisible widths, which stock
llama.cpp refuses to load. The patch is included in this repo (`nemotron-expert-padding.patch`).
Do **not** point a stock llama-server at it.

## What was done

Nemotron-3 expert tensors are `hidden_size` 2688 and `moe_intermediate_size` 1856 —
neither divides 256, and 1856 doesn't divide 128 either. `llama-quantize.cpp`
tests `ncols % ggml_blck_size(type)` and **silently falls back**, so every K-quant
and IQ-quant was locked out and the smallest stock build was 17.5 GiB — too big
for 16 GB.

The fix zero-pads the reduction axes:

| tensor | original | padded |
|---|---|---|
| `ffn_up_exps` reduction axis | 2688 | **2816** |
| `ffn_down_exps` (expert FF width) | 1856 | **2048** |
| shared-expert FF width | 3712 | **3840** |

This is **exact**, not approximate: the MoE activation is `relu²`, and `relu²(0) = 0`,
so padded rows contribute exactly zero. The padded BF16 master quantizes to IQ3_XXS
experts with no quality loss from the padding itself.

This is "Variant B" padding: `up_exps` is padded too, which needs the 4th patch
hunk (per-expert output views sized from the padded input width). Variant B is
smaller and higher quality than Variant A (A pins `up_exps` at ≥4.5 bpw because
its unpadded width only admits block-32 types).

## Files

| file | purpose |
|---|---|
| `Nemotron-3-Nano-30B-A3B-pirola-IQ3_XXS.gguf` | the quantized model (14,358,879,744 bytes) |
| `nemotron-expert-padding.patch` | **required** — 4 hunks / 3 files, applies to llama.cpp ~b9591 |
| `pad_gguf.py` | reproduction: zero-pads the GGUF tensors (the "Variant B" script) |
| `pad_imatrix.py` | pads the imatrix (must match the padded geometry) |
| `verify_pad.py` | verifies padding correctness |
| `imatrix-padded.gguf` | the padded imatrix used for this quantization |
| `serve-nemotron.sh` | validated serve script (see below) |

### sha256

```
cdaae25ffaa4f17a5ad4617040d5271a54fe61e6bc10ff5366f2c697a3bda16c  Nemotron-3-Nano-30B-A3B-pirola-IQ3_XXS.gguf
```

## Serving

**You must build llama.cpp from the included patch.** Stock llama.cpp refuses the
file with `... has wrong shape; expected 2688,2048,128, got 2816,2048,128`.

This GGUF was built and validated with llama.cpp compiled **for sm_120 (NVIDIA
RTX 5080, Blackwell)** — the CUDA target is hard-coded into the build:

```bash
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp && git checkout b9591            # or any commit ~b9591
git apply /path/to/nemotron-expert-padding.patch
cmake -B build -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=120   # sm_120 = RTX 5080
cmake --build build --config Release -j
```

Set `-DCMAKE_CUDA_ARCHITECTURES` to your own GPU's compute capability (e.g. `89`
for RTX 40-series Ada, `90` for H100) if you are not on a 5080 — the patch and the
quantization are architecture-independent; only the CUDA kernels are compiled per
compute capability.

> **Toolchain caveat:** NVCC 13.2 miscompiles the i-quant sign-table CUDA kernels
> (`iq1_s`/`iq2_s`/`iq3_s` — `test-backend-ops test -o MUL_MAT` fails against
> `5e-4`; see ggml-org#21255, unslothai#4849). If you are on CUDA ≥13.2, rebuild
> against CUDA 13.0 before trusting any IQ output. 13.0 passes all gates.

### Exact serve flags (validated operating point)

```
llama-server \
  -m Nemotron-3-Nano-30B-A3B-pirola-IQ3_XXS.gguf \
  --host 127.0.0.1 --port 8189 \
  -ngl 99 -np 1 --flash-attn on \
  -c 262144 -ctk q4_0 -ctv q4_0 \
  --jinja --alias nemotron \
  --temp 0.6 --top-p 0.95
```

Measured at this operating point (RTX 5080 16 GB, fully resident, `-ngl 99`):
14,858–14,862 MiB VRAM used (~1,120 MiB free). Do not raise `-np`, `-c`, or the KV
cache type without re-measuring. `serve-nemotron.sh` wraps this (start/stop/status,
PID file, log).

Pi / OpenAI-compatible clients:

```json
{ "baseUrl": "http://127.0.0.1:8189/v1", "api": "openai-completions",
  "models": [{ "id": "nemotron", "contextWindow": 262144, "maxTokens": 32768, "reasoning": true }] }
```

## Sampling guidance (from NVIDIA's card for this family)

| mode | temperature | top_p |
|---|---|---|
| **Tool calling / agentic** | **0.6** | **0.95** |
| Reasoning / single-shot benchmarks | 1.0 | 1.0 |

The served default above is **0.6 / 0.95** (tool calling). Set 1.0/1.0 per-request
for reasoning work. Thinking is on by default; disable per-request with
`"chat_template_kwargs": {"enable_thinking": false}`.

`tool_choice: "required"` is silently ignored under the `peg-native` chat format —
prompt for tool calls instead. Set `parallel_tool_calls: false` defensively.

## Measured quality (local, 16 GB RTX 5080, WSL2)

All benchmarks are local runs on this exact file with the exact flags above
(thinking ON unless noted).

| metric | value |
|---|---|
| MBPP-sanitized, temp 1.0/1.0 | **90.40 %** (386/427) |
| MBPP-sanitized, temp 0.6/0.95 | **88.52 %** (378/427) — statistically indistinguishable (McNemar p=0.15) |
| HumanEval, temp 1.0/1.0 | **94.51 %** (155/164) |
| HumanEval, temp 0.6/0.95 | **95.12 %** (156/164) — McNemar p=1.00 |
| NIAH (needle-in-a-haystack) | **40/40** at 32k / 131k / 262k context |
| wikitext-2 PPL (`-c 4096 --chunks 40`) | **6.9728 ± 0.062** |
| Prefill @ 262k | 3,833–3,884 t/s |
| Decode @ 16k / 131k / 262k | ~246 / ~132 / **85.8 t/s** |
| Agentic loop (tool calling, thinking ON, 5 seeds) | **5/5**, zero cap-hits |

Caveats: MBPP at n=427 has a binomial SE of ~±1.5 pp near 88 % — differences under
~2 pp are not meaningful. All numbers are from a fully-resident single-request
(`-np 1`) run.

## Provenance

- **Base model:** `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16` (NVIDIA, Sep–Dec
  2025; post-training cutoff 2025-11-28). Architecture `nemotron_h_moe`
  (Mamba2 + MoE hybrid; ~35.4 B declared params, ~29.4 B real MoE params).
- **License:** NVIDIA Open Model License
  (https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license/).
  Verify compliance for commercial use before distributing.
- **Quantization imatrix:** derived from Unsloth's model-specific calibration file
  (`unsloth_calibration_Nemotron-3-Nano-30B-A3B.txt`, 80 chunks), padded to the
  padded geometry with `pad_imatrix.py`. Full imatrix coverage, no `has no data`
  warnings.
- **Quantized with:** `llama-quantize` from the patched fork. Actual tensor census
  of this file: experts `down`/`up` **IQ3_XXS** (3.46 bpw over real params), shared
  expert FF `Q6_K`/`Q5_0`/`Q4_K`, attention `F32`/`Q5_0`/`Q4_K`/`Q8_0` (SSM params
  largely F32 — expected for the Mamba2 hybrid), output `Q8_0`. Serving uses
  **q4_0 KV** (quality-neutral vs f16, verified; see the 2026-08-11 sampling study).
- **Padding lineage:** the technique was developed 2026-08-10; see the "First
  padded build for this family" section above for the prior-art audit.

## Reproduction

```bash
# 1. pad a downloaded BF16 master
python pad_gguf.py --in master.gguf --out master-padded-BF16.gguf   # variant B
# 2. pad the imatrix to match
python pad_imatrix.py --in imatrix.gguf --out imatrix-padded.gguf
# 3. quantize with the patched fork
llama-quantize master-padded-BF16.gguf Nemotron-3-Nano-30B-A3B-pirola-IQ3_XXS.gguf IQ3_XXS \
  --imatrix imatrix-padded.gguf
```

`verify_pad.py` asserts the padded tensors are exactly zero outside the original
width (it is what the padding correctness gate ran).
