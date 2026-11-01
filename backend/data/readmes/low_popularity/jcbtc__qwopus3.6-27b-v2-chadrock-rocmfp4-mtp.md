---
license: apache-2.0
base_model:
- Jackrong/Qwopus3.6-27B-v2
- Jackrong/Qwopus3.6-27B-v2-MTP-GGUF
base_model_relation: quantized
datasets:
- Jackrong/Claude-opus-4.6-TraceInversion-9000x
- Jackrong/Claude-opus-4.7-TraceInversion-5000x
language:
- en
- zh
- ko
- ru
- ja
- es
library_name: llama.cpp
pipeline_tag: image-text-to-text
tags:
- qwopus3.6
- qwen3.6
- qwen35
- 27b
- model-size-27b
- dense
- gguf
- mtp
- rocm
- rocmfp4
- llama.cpp
- amd
- ryzen-ai-max-395
- strix-halo
- vision
- multimodal
- image-text-to-text
- tool-calling
- coding
---

![Qwopus3.6 27B v2 Chadrock ROCmFP4 MTP](assets/chadrock27b.png)

# Qwopus3.6 27B v2 Chadrock ROCmFP4 MTP

Qwopus3.6 Chadrock is a ROCmFP4/MTP GGUF build of `Jackrong/Qwopus3.6-27B-v2`, tuned for AMD Ryzen AI Max+ 395 / Strix Halo systems.

This model keeps the Qwopus3.6 27B v2 behavior people like, then puts it through Charlie's AMD-focused ROCmFP4 + MTP runtime path. The result is a compact 14 GB GGUF that runs with native draft-MTP on Strix Halo and posts a better HumanEval result than the original local Qwopus3.6 27B v2 Q5 row.

This GGUF will **not run correctly with stock llama.cpp**. You need the pinned [`ciru-ai/ROCmFPX`](https://github.com/ciru-ai/ROCmFPX/tree/7aa484a2f0a504dc612a3d74a068024f3e6d6353) runner because this file uses ROCmFP4 tensor types that upstream llama.cpp does not currently understand.

The model file is already provided here. You do **not** need to rebuild or quantize the model. You only need to build the custom llama server once.

## Why This Mix

Qwopus3.6 27B v2 is already a strong dense local model with vision and tool-use capability. Chadrock adds the AMD runtime piece:

- Qwopus3.6 27B v2 behavior from Jackrong
- native MTP serving
- ROCmFP4 Strix Lean tensor recipe
- AMD ROCm/HIP backend path
- 262K context target
- one-slot draft-MTP profile for real local use

This is not just a smaller file. It is a model/runtime pairing built for Strix Halo.

## Model Lineage

This card follows the upstream tree from Jackrong's Qwopus card, then adds this ROCmFP4 / Chadrock build at the end:

```text
Qwen/Qwen3.6-27B
  -> Jackrong/Qwopus3.6-27B-v2
       datasets:
         - Jackrong/Claude-opus-4.6-TraceInversion-9000x
         - Jackrong/Claude-opus-4.7-TraceInversion-5000x
  -> Jackrong/Qwopus3.6-27B-v2-MTP-GGUF
  -> jcbtc/qwopus3.6-27b-v2-chadrock-rocmfp4-mtp
```

In plain terms: Qwen provides the dense 27B foundation, Jackrong's Qwopus v2 adds the Trace Inversion / curriculum SFT behavior, Jackrong's MTP GGUF provides the MTP source path, and this release converts that line into the Strix-focused ROCmFP4 Chadrock format.

## Technical Metadata

| Field | Value |
| --- | --- |
| model size | `27B` dense |
| architecture | `qwen35` |
| GGUF size label | `27B` |
| direct upstream behavior model | `Jackrong/Qwopus3.6-27B-v2` |
| direct upstream MTP GGUF | `Jackrong/Qwopus3.6-27B-v2-MTP-GGUF` |
| base family | `Qwen/Qwen3.6-27B` |
| local runtime format | ROCmFP4 Chadrock GGUF |

## Headline Benchmarks

All local numbers below were measured on AMD Ryzen AI Max+ 395 / Strix Halo.

### HumanEval

| Model / row | HumanEval base | HumanEval+ |
| --- | ---: | ---: |
| Qwopus3.6 27B v2 Chadrock ROCmFP4 MTP | `159/164 = 96.95%` | `155/164 = 94.51%` |
| Original Qwopus3.6 27B v2 Q5_K_M | `151/164 = 92.07%` | `147/164 = 89.63%` |

That is an `+8 task` improvement on base HumanEval and an `+8 task` improvement on HumanEval+ versus the recorded original Qwopus3.6 27B v2 Q5_K_M row.

### HumanEval Speed

| Metric | Qwopus3.6 Chadrock |
| --- | ---: |
| HumanEval tasks | `164` |
| completion tokens generated | `45,033` |
| cumulative request latency | `1346.8s` |
| mean total-token request speed | `59.08 tok/s` |
| median total-token request speed | `60.04 tok/s` |
| completion-only llama.cpp eval speed | `~33.44 tok/s` |
| peak active completion speed | `~37.14 tok/s` |

The stored original Qwopus3.6 27B v2 Q5_K_M HumanEval run recorded `3834s` generation time. This Chadrock run completed the same 164-task HumanEval codegen workload with about `2.8x` lower recorded request-generation time while also scoring higher.

### BFCL Tool Calling

Qwopus3.6 Chadrock also did well on BFCL v4 non-live tool-calling rows:

| BFCL v4 row | Score |
| --- | ---: |
| non-live overall | `85.88%` |
| simple Python AST | `94.50%` |
| multiple-call AST | `96.00%` |
| parallel-call AST | `86.50%` |
| parallel multiple-call AST | `85.50%` |
| irrelevance detection | `81.67%` |

This is the profile to try if you want a local Strix Halo model that feels fast while still staying sharp on coding and tool-use formats.

## Best Settings / Advanced Setup

For the pinned runner build, copy-paste build commands, request-level speculative controls, and the latest Chadrock ROCmFP4 setup notes, use the advanced Ciru setup page:

**https://llm.ciru.ai/chadrock-rocmfpx/**

The current pinned runner build is:

```text
ciru-ai/ROCmFPX commit: 7aa484a2f0a504dc612a3d74a068024f3e6d6353
historical score tag: chadrock-rocmfp4-mtp-scores-20260621
```

For the fastest current Qwopus3.6 27B v2 Chadrock profile on Strix Halo, use:

```text
backend: Vulkan0 target + Vulkan0 draft
context: 262144
batch / ubatch: 2048 / 512
target KV: q8_0 / q8_0
draft KV: f16 / f16
MTP: draft-mtp, n_max=4, n_min=0, p_min=0.0, p_split=0.20
serving: one slot, metrics on, text-only for speed runs
sampler: temperature=0, top_p=0.95, top_k=20
```

This supersedes the older small-batch ROCm0/q4 launch shape for speed testing.
Keep the projector in the command below when you want image-text behavior; use
text-only serving when benchmarking decode speed.

## Run With llama-server

Build Charlie's custom llama.cpp once, download this GGUF, then run:

```bash
HSA_OVERRIDE_GFX_VERSION=11.5.1 \
GGML_HIP_ENABLE_UNIFIED_MEMORY=1 \
/path/to/rocmfp4-llama/build-strix-rocmfp4/bin/llama-server \
  -m Qwopus3.6-27B-v2-MTP-BF16-to-ROCmFP4-STRIX_LEAN.gguf \
  --mmproj mmproj-F32.mmproj \
  --alias qwopus3.6-27b-v2-chadrock \
  --host 127.0.0.1 \
  --port 8080 \
  --jinja \
  -c 262144 \
  -ngl 999 \
  -fa on \
  -dev ROCm0 \
  -b 512 \
  -ub 512 \
  -t 16 \
  -tb 32 \
  -ctk q4_0 \
  -ctv q4_0 \
  --ctx-checkpoints 0 \

  --checkpoint-every-n-tokens -1 \

  --spec-type draft-mtp \
  --spec-draft-device ROCm0 \
  --spec-draft-ngl all \
  --spec-draft-type-k q4_0 \
  --spec-draft-type-v q4_0 \
  --spec-draft-n-max 4 \
  --spec-draft-n-min 0 \
  --spec-draft-p-min 0.0 \
  --spec-draft-p-split 0.10 \
  --parallel 1 \
  --metrics \
  --no-mmap
```

Use `--parallel 1` for MTP. Multi-slot serving changes the draft-MTP behavior and is not the intended profile.

For text-only use, you may omit `--mmproj`.

For vision use, keep `mmproj-F32.mmproj` beside the main GGUF, but run with MTP off. In practice, that means using the vision projector and removing the `--spec-*` draft-MTP flags from the command.

The projector is a GGUF-format projector file with a `.mmproj` repo extension so Hugging Face's GGUF metadata badge tracks the 27B language model rather than the smaller CLIP projector.

## Build The Required llama.cpp

The GGUF is already provided. You only need to build the custom llama.cpp server once:

```bash
git clone https://github.com/ciru-ai/ROCmFPX.git
cd ROCmFPX
git checkout 7aa484a2f0a504dc612a3d74a068024f3e6d6353
env JOBS=16 scripts/build-strix-rocmfp4-mtp.sh llama-server llama-bench
```

The server binary will be here:

```text
build-strix-rocmfp4/bin/llama-server
```

## About ROCmFP4 / Chadrock

Charlie's ROCmFP4 method adds AMD-focused GGUF tensor formats and backend paths to llama.cpp.

ROCmFP4 is not stock Q4, MXFP4, or NVFP4. It uses custom 4-bit tensor layouts, Codebook10 values, finite unsigned E4M3 scale semantics, tensor-aware Strix presets, ROCm/HIP kernels, Vulkan support, and MTP regression guards.

Why it matters: Strix Halo has a large unified-memory pool, but good local serving still depends on memory bandwidth, tensor layout, KV traffic, and draft-token acceptance. Chadrock is built for that exact hardware shape.

## Files

| File | Size | SHA256 |
| --- | ---: | --- |
| `Qwopus3.6-27B-v2-MTP-BF16-to-ROCmFP4-STRIX_LEAN.gguf` | `14 GB` | `1f1c0a9d63b9b38b06feb4f460f9cb6ed85f001331be713f09e6c2aaff5367e4` |
| `mmproj-F32.mmproj` | `889 MB` | `bf51f62572c6e513659d3fa4989ac846e58fa8c30fb60ecb8112aebb1f3128a3` |

## Credits

- **[Qwen](https://huggingface.co/Qwen)**: `Qwen/Qwen3.6-27B` base model family.
- **[Jackrong](https://huggingface.co/Jackrong)**: `Qwopus3.6-27B-v2`, the Trace Inversion datasets, and the MTP GGUF source.
- **charlie12345 / [@Italianclownz](https://x.com/Italianclownz)**: ROCmFP4 llama.cpp fork, Strix Halo build path, and AMD-focused MTP runtime work.

## Notes

This is an experimental AMD ROCmFP4/MTP build. Performance depends on driver version, clocks, prompt shape, MTP acceptance, and serving flags. The numbers above are local reproducible measurements, not universal llama.cpp claims.
