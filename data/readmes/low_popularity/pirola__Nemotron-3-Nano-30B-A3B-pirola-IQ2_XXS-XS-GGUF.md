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

# Nemotron 3 Nano 30B A3B — pirola padded, IQ2_XXS/IQ2_XS (fork-only GGUF)

A **9.98 GiB** GGUF of `NVIDIA-Nemotron-3-Nano-30B-A3B` that serves **262,144
context at q4_0 KV within an 11,392 MiB footprint** — comfortably under a **12 GB
RTX 5000-class GPU** (896 MiB margin), with coding ability statistically
indistinguishable from the full 13.37 GiB pirola-IQ3_XXS build.

This is the same Variant B zero-padding as [`pirola/Nemotron-3-Nano-30B-A3B-pirola-IQ3_XXS-GGUF`](https://huggingface.co/pirola/Nemotron-3-Nano-30B-A3B-pirola-IQ3_XXS-GGUF),
quantized lower to fit 12 GB cards.

**⚠️ Critical: this file requires a fork build of llama.cpp.** The model's expert
weights have their reduction axes zero-padded to 256-divisible widths, which stock
llama.cpp refuses to load. The patch is included (`nemotron-expert-padding.patch`).

## Quantization recipe

Zero-pad the reduction axes (exact: the MoE activation is `relu²`, and `relu²(0)=0`):

| tensor | original | padded |
|---|---|---|
| `ffn_up_exps` reduction axis | 2688 | **2816** |
| `ffn_down_exps` (expert FF width) | 1856 | **2048** |
| shared-expert FF width | 3712 | **3840** |

Per-tensor types (chosen by dry-run + validated head-to-head; imatrix = the padded
Unsloth-derived imatrix `imatrix-padded.gguf`):

| group | type | bpw |
|---|---|---|
| `ffn_up_exps` | **IQ2_XXS** | 2.06 |
| `ffn_down_exps` | **IQ2_XS** | 2.31 |
| shared-expert FF | Q6_K / Q5_0 / Q4_K (as pirola-IQ3_XXS) | — |
| attention / SSM | Q4_K / Q5_0 / F32 (as pirola-IQ3_XXS) | — |
| output | Q8_0 | — |

The **down** projection is kept one step higher (IQ2_XS) than the up (IQ2_XXS) —
measured: a Q8_0-base variant with IQ2_XXS on both was *worse* (PPL 8.15 vs 8.08)
and had less VRAM headroom. Down is where MoE quality lives.

## Measured quality — head-to-head vs the 13.37 GiB pirola-IQ3_XXS incumbent

All cells at identical protocol (temp 1.0 / top_p 1.0, thinking ON, 8192 cap for
coding; temp 0.6 / top_p 0.95 for agentic). RTX 5080, sm_120 build.

| metric | **this file (IQ2_XXS/XS)** | pirola-IQ3_XXS | verdict |
|---|---|---|---|
| MBPP-sanitized (427) | **89.23 %** (381/427) | 90.40 % (386/427) | McNemar p=0.383 — n.s. |
| HumanEval (164) | **97.56 %** (160/164) | 94.51 % (155/164) | McNemar p=0.227 — n.s. |
| Agentic gate (5 seeds, thinking-on) | **5/5** | 5/5 | tie |
| MBPP cap-hits | **2** | 7 | better |
| wikitext-2 PPL (`-c 4096 --chunks 40`) | 8.0765 ± 0.074 | 6.9728 ± 0.062 | +1.10 |
| **VRAM @ 262,144 / q4_0 KV, full window** | **11,392 MiB** | 14,862 MiB | **fits 12 GB** |

**Bottom line: statistically indistinguishable from the 13.37 GiB build on every
coding cell, at 3.5 GB less VRAM.** The +1.10 PPL cost of 2.4 bpw experts does not
surface in pass@1 or agentic ability.

## Files

| file | purpose |
|---|---|
| `Nemotron-3-Nano-30B-A3B-pirola-IQ2_XXS-XS.gguf` | the quantized model (10,717,175,296 bytes) |
| `nemotron-expert-padding.patch` | **required** — 4 hunks / 3 files, applies to llama.cpp ~b9591 |
| `pad_gguf.py` | reproduction: zero-pads the GGUF tensors (Variant B) |
| `pad_imatrix.py` | pads the imatrix (must match the padded geometry) |
| `imatrix-padded.gguf` | the padded Unsloth-derived imatrix used for this quantization |
| `verify_pad.py` | verifies padding correctness |
| `serve-nemotron.sh` | validated serve script |
| `parts/part-000` … `parts/part-019` | split-download fallback (20 chunks) reassembling to the same GGUF above — use if the direct download stalls |

### sha256

```
c6363afc6a9c9d77efa4df0587f52c67c0f3dbc8b5a0efec10b8ba0c6a103152  Nemotron-3-Nano-30B-A3B-pirola-IQ2_XXS-XS.gguf
```

## Serving

**You must build llama.cpp from the included patch.** Stock llama.cpp refuses the
file. This GGUF was built and validated with llama.cpp compiled **for sm_120
(NVIDIA RTX 5080, Blackwell)** — the CUDA target is hard-coded into the build:

```bash
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp && git checkout b9591            # or any commit ~b9591
git apply /path/to/nemotron-expert-padding.patch
cmake -B build -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=120   # sm_120 = RTX 5080
cmake --build build --config Release -j
```

Set `-DCMAKE_CUDA_ARCHITECTURES` to your own GPU's compute capability (e.g. `89`
for RTX 40-series Ada) if you are not on a 5080 — the patch and the quantization
are architecture-independent; only the CUDA kernels are compiled per capability.

> **Toolchain caveat:** NVCC 13.2 miscompiles the i-quant sign-table CUDA kernels
> (`iq1_s`/`iq2_s`/`iq3_s`). If you are on CUDA ≥13.2, rebuild against CUDA 13.0
> before trusting any IQ output.

### Exact serve flags (validated operating point)

```
llama-server \
  -m Nemotron-3-Nano-30B-A3B-pirola-IQ2_XXS-XS.gguf \
  --host 127.0.0.1 --port 8189 \
  -ngl 99 -np 1 --flash-attn on \
  -c 262144 -ctk q4_0 -ctv q4_0 \
  --jinja --alias nemotron \
  --temp 0.6 --top-p 0.95
```

Measured: **11,312 MiB after load, 11,392 MiB after a full 250k-token prompt**
(12 GB card = 12,288 MiB; 896 MiB free). Do not raise `-np`, `-c`, or the KV cache
type without re-measuring.

## Sampling guidance

| mode | temperature | top_p |
|---|---|---|
| **Tool calling / agentic** | **0.6** | **0.95** |
| Reasoning / single-shot benchmarks | 1.0 | 1.0 |

Thinking is on by default; disable per-request with
`"chat_template_kwargs": {"enable_thinking": false}`.

## First padded build for this family — verified 2026-08-12

A full audit of Hugging Face, GitHub and the web (100 % enumeration: 7,106 repos /
668 Nemotron GGUF files; 105 repos / 235 Cascade-2-30B-A3B GGUF files; every
llama.cpp issue/PR/commit; every relevant discussion) established the following
facts:

- **No other padded or genuine sub-4-bit GGUF exists** for `Nemotron-3-Nano-30B-A3B`
  or `Nemotron-Cascade-2-30B-A3B` besides this repo and its IQ3_XXS sibling.
- Every published "sub-4-bit named" GGUF of these two models is pinned at
  **16.5–18.1 GB** (effective 4.6–5.2 bpw): the expert dims (1856/2688, not
  256-divisible) silently fall back to IQ4_NL in `llama-quantize`'s
  `tensor_type_fallback`. Even IQ1_M (1.56 bpw) builds are ~17.9 GB.
- The only sub-18 GB llama.cpp files for these models are 4-bit FP formats
  (ROCmFP4 15.73 GB; NVFP4/MXFP4 ≈16.7–17.9 GB) — not sub-4-bit and not padded.
- The smaller JANG build (Cascade-2, ~10 GB) is **MLX-only** (Apple Silicon): MLX
  group quantization (group 32/64, no 256-divisibility constraint) — not padded and
  not a llama.cpp GGUF.
- The zero-padding *idea* was floated in a draft, never-merged llama.cpp PR
  (`708-145/llama.cpp#33`, Dec 2025) and an unsloth discussion; **no file was ever
  produced from it**.

## Provenance

- **Base model:** `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16` (NVIDIA, Sep–Dec
  2025). Architecture `nemotron_h_moe` (Mamba2 + MoE hybrid; ~35.4 B declared params,
  ~29.4 B real MoE params).
- **License:** NVIDIA Open Model License
  (https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-nemotron-open-model-license/).
- **Quantization imatrix:** derived from Unsloth's model-specific calibration file,
  padded to the padded geometry with `pad_imatrix.py`.
- **Padding lineage:** the technique was developed 2026-08-10; see the "First
  padded build" section above for the prior-art audit.
