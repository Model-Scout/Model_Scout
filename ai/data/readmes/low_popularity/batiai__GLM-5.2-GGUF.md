---
language:
  - en
  - zh
  - ko
license: other
license_name: mit
license_link: https://huggingface.co/zai-org/GLM-5.2/blob/main/LICENSE
tags:
  - gguf
  - glm
  - zai-org
  - quantized
  - batiai
  - mixture-of-experts
  - frontier
  - 744b
  - swe-bench
  - dsa
base_model: zai-org/GLM-5.2
pipeline_tag: text-generation
library_name: llama.cpp
---

# GLM-5.2 GGUF — Quantized by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-on--device%20AI-blue?style=for-the-badge&logo=apple" alt="BatiFlow"></a>
  <a href="https://huggingface.co/zai-org/GLM-5.2"><img src="https://img.shields.io/badge/source-zai--org-orange?style=for-the-badge" alt="zai-org"></a>
</p>

> IQ2_XS / IQ3_XXS / Q3_K_M quantization of **zai-org/GLM-5.2** (744B total / 40B active MoE).
> Quantized directly from official Z.AI weights by [BatiAI](https://bati.ai).

## Why GLM-5.2?

- **744B parameters** (40B active) — frontier MoE with **Deep Sparse Attention (DSA)**
- Latest in Z.AI's GLM-5 series — successor to GLM-5.1, the **#1 open-source model on SWE-Bench Pro**
- **256 routed experts + 1 shared expert** (top-8 routing + DSA indexer) — extreme sparsity
- **78 transformer blocks** (3 dense + 75 MoE) with hybrid attention/FFN routing
- **1M token context** (`max_position_embeddings=1048576`, RoPE θ=8M)
- **MIT license** — fully permissive for commercial use, fine-tuning, redistribution
- Released by **Z.AI / Zhipu AI** — same lineage as ChatGLM / GLM-4 / GLM-5.1

## Quick Start

```bash
# IQ2_XS (smallest — 214 GiB, dynamic 2.44bpw, fits Mac Studio 256GB)
hf download batiai/GLM-5.2-GGUF --include "*IQ2_XS*"

# IQ3_XXS (273 GiB — needs Mac 384GB+ / server)
hf download batiai/GLM-5.2-GGUF --include "*IQ3_XXS*"

# Q3_K_M (highest-fidelity offered — 337 GiB, needs 384GB+ unified RAM)
hf download batiai/GLM-5.2-GGUF --include "*Q3_K_M*"
```

## Available Quantizations

| Quant | Total Size | Shards | Min RAM | Target Hardware |
|-------|-----------|--------|---------|-----------------|
| **IQ2_XS** ⭐ | **230 GB / 214 GiB** (measured) | 5 @ 48 GB max | **~256 GB** | **Mac Studio 256GB** / server |
| **IQ3_XXS** | **293 GB / 273 GiB** (measured) | 7 @ 48 GB max | **~320 GB** | M3 Ultra 384–512GB / H100 node |
| **Q3_K_M** | **361 GB / 337 GiB** (measured) | 8 @ 48 GB max | **~384 GB** | M3 Ultra 512GB / H100 node |

> **IQ2_XS** uses a **dynamic recipe** — routed experts at IQ2_XS (2.31 bpw) while attention / router / shared-expert / DSA indexer / MTP block are protected at Q4–Q6 → effective **2.44 bpw**. This opens the **256GB Mac Studio tier** that IQ3_XXS / Q3_K_M (512GB-class) cannot reach. Q3_K_M is also the imatrix-source build (kept in RAM cache during calibration). All sizes above are **measured**. **IQ4_XS (~376 GB, 512GB-class)** overlaps IQ3/Q3's hardware tier, so it is **archived on NAS and re-uploadable on request** rather than shipped by default.

> **⚠️ High-RAM only** — the smallest build (**IQ2_XS, 214 GiB**) needs **Mac Studio 256GB+**; IQ3_XXS / Q3_K_M need 384–512GB. **It does not fit a 192GB Mac.** 16–192GB Mac users should use `batiai/qwen3.6-35b` or `batiai/minimax-m2.7` instead.

## Hardware Reality Check

| Your System | IQ2_XS (214 GiB) | IQ3_XXS (273 GiB) | Q3_K_M (337 GiB) |
|---|---|---|---|
| Mac ≤192GB | ❌ Won't fit | ❌ | ❌ |
| **Mac 256GB** | ✅ **Usable** (~30GB headroom) | ❌ Won't fit | ❌ |
| Mac 384GB | ✅ Comfortable | ✅ Usable | ✅ Tight |
| **Mac M3 Ultra 512GB** | ✅ Comfortable | ✅ Comfortable | ✅ Usable |
| **2× M3 Ultra (cluster)** | ✅ Fast | ✅ Fast | ✅ Fast |
| **8× A100 80GB (640GB)** | ✅ Fast | ✅ Fast | ✅ Fast |
| **H100 node** | ✅ Fast | ✅ Fast | ✅ Fast |

Numbers based on MoE activation pattern — 40B active params × 2 bytes (Q4 active) ≈ 80GB runtime, plus shard buffers + KV cache. Going below the min RAM forces SSD paging which destroys throughput.

## Special Engineering Notes

GLM-5.2 uses **Deep Sparse Attention (DSA)** — a per-layer "indexer" tensor selects the top-K key positions for sparse attention. The config marks 21 of 78 layers as `full` indexer (layers 0–2 plus every 4th from layer 6: 6, 10, 14, … 74); the remaining 57 are `shared`. This hybrid layout required two fixes during quantization:

1. **DSA indexer tensors not in imatrix** — `--tensor-type indexer=q5_k` override (these tensors are not exercised by the forward pass used for imatrix, so they have no calibration data and are kept at Q5_K)
2. **MTP / NextN block (blk.78) imatrix gap** — GLM-5.2 ships `num_nextn_predict_layers=1`, so the multi-token-prediction block lands at `blk.78` (= `num_hidden_layers`, derived dynamically by the pipeline as `LAST_BLK=NLAYERS=78`). It is not used in the forward pass and has no imatrix data; `--tensor-type blk.78=q5_k` keeps it at higher precision.

Both flags are baked into our quantization pipeline (`scripts/runtime/glm52-pipeline.sh`). The fallback Q5_K layers add a negligible amount to file size but prevent low-bit IQ-quants from bailing on missing imatrix data. The entire pipeline runs on NAS (`/mnt/nas`, 1.51 TB) under bati.cpp.

## What BatiAI's Quantization Delivers

| | BatiAI | typical 3rd-party |
|---|---|---|
| **Source** | Direct from official Z.AI weights | Often re-quantized from other GGUFs |
| **Quantization flow** | safetensors → Q8_0 → Q3_K_M / IQ3_XXS / IQ4_XS with imatrix (wikitext-2-raw, 200 chunks) | Varies |
| **imatrix** | ✅ 200 chunks (quality saturation), measured over Q3_K_M in RAM cache | Often skipped or fewer chunks |
| **DSA indexer handling** | ✅ Q5_K override documented | Often unaddressed → garbage low-bit |
| **MTP / last-block imatrix gap** | ✅ Workaround applied (blk.78=q5_k) | Often causes bail-out or quality loss |
| **BatiAI signature** | ✅ `general.author=BatiAI`, `general.url=https://flow.bati.ai` | ✗ |

## Model Comparison — BatiAI Lineup

| Your Hardware | Best BatiAI Model | Size |
|---|---|---|
| 16GB Mac | `batiai/gemma4-e4b:q4` | 5GB |
| 24GB Mac | `batiai/gemma4-26b:iq4` | 15GB |
| 48GB Mac | `batiai/qwen3.6-35b:iq4` | 22GB |
| 96GB Mac | `batiai/qwen3.6-35b:q6` | 29GB |
| 128GB Mac | `batiai/minimax-m2.7:iq3` | 82GB |
| 192GB Mac Studio | `batiai/kimi-k2.6:iq3` | 394GB (paged) |
| **M3 Ultra 512GB** | **GLM-5.2 IQ4_XS ⬅ here** | **~376GB** |
| **M3 Ultra 512GB (alt)** | `batiai/kimi-k2.6:iq4` | 546GB (heavy swap) |

GLM-5.2 IQ4_XS at ~376 GB is among the **largest models that run on a single M3 Ultra 512GB** without crippling SSD swap. Kimi K2.6 IQ4 (546GB) would page heavily on the same machine.

## Benchmarks (source model)

<!-- BENCH-START -->
_Benchmark numbers pending. No locally-verified scores yet — values will be populated by `scripts/render-readmes.py` from `bench.sh` results on target hardware. GLM-5.2 is the successor to GLM-5.1 (the #1 open-source model on SWE-Bench Pro); quantization-preserved scores are not asserted until measured._
<!-- BENCH-END -->

> Validating that quantization preserves the source model's quality on Mac M3 Ultra is **pending** (`bench.sh` on target hardware). No unverified scores are listed here.

## Technical Details

- **Original Model**: [zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)
- **Architecture**: `GlmMoeDsaForCausalLM` (`model_type=glm_moe_dsa`) — 744B total / 40B active, **78 blocks (3 dense + 75 MoE)**, 256 routed + 1 shared expert (top-8, `noaux_tc` routing, sigmoid scoring, `routed_scaling_factor=2.5`), DSA hybrid attention with ~21 `full`-indexer layers
- **Dimensions**: hidden 6144, intermediate 12288, MoE intermediate 2048, 64 attn heads / 64 KV heads, head_dim 192 (qk 256 = 192 nope + 64 rope, v 256), kv_lora_rank 512, q_lora_rank 2048, vocab 154880, dtype bfloat16
- **Context**: 1M tokens (`max_position_embeddings=1048576`, `rope_theta=8000000`, interleaved RoPE)
- **MTP**: `num_nextn_predict_layers=1` → NextN block at `blk.78`
- **Original storage**: BF16/FP8 mix (~1.4 TB safetensors)
- **License**: MIT
- **Quantized with**: [bati.cpp](https://github.com/batiai/bati.cpp) (BatiAI's llama.cpp fork — needed for the `glm-dsa` / DSA architecture; hybrid-DSA loader treats the indexer as optional per layer, blk.78 in-place metadata patch)
- **Calibration**: wikitext-2-raw, 200 chunks (quality saturation), imatrix measured over Q3_K_M
- **imatrix overrides**: `--tensor-type indexer=q5_k --tensor-type blk.78=q5_k`
- **Quantized by**: [BatiAI](https://bati.ai)

## Usage

### llama.cpp / bati.cpp

GLM-5.2 currently requires **bati.cpp** (BatiAI's llama.cpp fork) — mainline `ggml-org/llama.cpp` does not yet support the `glm-dsa` (GLM-MoE-DSA) DSA indexer at runtime. Will switch to mainline once full DSA-indexer support lands.

```bash
git clone https://github.com/batiai/bati.cpp.git
cd bati.cpp
cmake -B build -DGGML_METAL=ON   # macOS
# or: cmake -B build -DGGML_CUDA=ON   # Linux
cmake --build build -j --target llama-cli

hf download batiai/GLM-5.2-GGUF --include "*IQ4_XS*" --local-dir ./glm52

# Point at shard 00001 of the IQ4_XS split set (filename pattern below)
build/bin/llama-cli -m ./glm52/zai-org-GLM-5.2-IQ4_XS-00001-of-*.gguf \
    -p "Your prompt" \
    --ctx-size 32768 \
    --n-gpu-layers 99
```

### Ollama

**Not available on Ollama.** Ollama vendors mainline `llama.cpp`, which does not support the `glm-dsa` (GLM-MoE-DSA) DSA indexer at runtime, so these GGUFs cannot load there. Mainline PR #19460 adds the GLM-MoE-DSA architecture but the DSA indexer is a follow-up PR still pending; as of 2026-06-20 `ollama.com/batiai/GLM-5.2` returns 404. Quantization and inference are possible only with `batiai/bati.cpp`. An Ollama build will be revisited once the mainline `glm-dsa` indexer is merged.

### vLLM / TGI

Not directly compatible — these serve FP8/BF16 safetensors. Use original [zai-org/GLM-5.2](https://huggingface.co/zai-org/GLM-5.2) for vLLM.

## About `bati.cpp`

[`batiai/bati.cpp`](https://github.com/batiai/bati.cpp) is BatiAI's llama.cpp-based fork focused on:
- Apple Silicon (Metal) optimization
- Frontier-model early access (V4-Flash, GLM-5.1 / GLM-5.2 DSA, etc.) before mainline merges
- BatiAI quantization standard (signature, imatrix workflow)

Built on top of [`ggml-org/llama.cpp`](https://github.com/ggml-org/llama.cpp) and [`antirez/llama.cpp-deepseek-v4-flash`](https://github.com/antirez/llama.cpp-deepseek-v4-flash) (all MIT). See `bati.cpp/ATTRIBUTION.md` for full credits.

## License

Inherits the source model license: **MIT**. Public (non-gated) — MIT permits commercial use, fine-tuning, and redistribution with no access form required.

## About BatiFlow

[BatiFlow](https://flow.bati.ai) — free on-device AI automation for Mac. 5MB native app, 60+ tools (KakaoTalk, iMessage, Slack, Calendar, Notes, Chrome, file system). Works with all `batiai/*` models.
