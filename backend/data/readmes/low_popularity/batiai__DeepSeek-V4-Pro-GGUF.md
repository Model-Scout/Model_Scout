---
language:
  - en
  - zh
  - ko
license: mit
tags:
  - gguf
  - deepseek
  - deepseek-v4
  - quantized
  - batiai
  - 1.6t
  - moe
  - frontier
  - flagship
  - reasoning
  - early-access
base_model: deepseek-ai/DeepSeek-V4-Pro
pipeline_tag: text-generation
library_name: bati.cpp
---

# DeepSeek V4-Pro GGUF — BatiAI Frontier

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-macOS%20AI%20Automation-blue?style=for-the-badge&logo=apple"></a>
  <a href="https://github.com/batiai/bati.cpp"><img src="https://img.shields.io/badge/Inference-bati.cpp-purple?style=for-the-badge"></a>
  <a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"><img src="https://img.shields.io/badge/source-deepseek--ai-orange?style=for-the-badge"></a>
</p>

> ⚠️ **Early Access — requires `bati.cpp` to run.** DeepSeek V4-Pro is the **1.6 trillion parameter
> flagship** of the DeepSeek V4 series, released 2026-05-06. It is **not yet supported by
> `ggml-org/llama.cpp` master**. This GGUF was converted with [`batiai/bati.cpp`](https://github.com/batiai/bati.cpp) v0.1.2 —
> BatiAI's own inference fork. Inference requires the same library. **Ollama is not yet
> compatible** (will auto-update once mainline merges V4 support).

## Why DeepSeek V4-Pro?

The largest open-weights frontier model available in GGUF form. Top-tier on coding,
reasoning, and agentic benchmarks per DeepSeek's official release.

- **1.6 trillion total parameters** / **49B activated per token** (largest open-weights LLM as of 2026-05)
- **DeepSeek-V4-Pro-Max** (extended reasoning) closes the gap with frontier closed-source models on reasoning + agentic tasks
- **Hybrid Attention**: Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA) — 27% inference FLOPs and 10% KV cache vs DeepSeek-V3.2 at 1M context
- **Manifold-Constrained Hyper-Connections (mHC)** — strengthens residual paths for signal propagation across 61 layers
- **Muon Optimizer** training — faster convergence, greater stability
- **1M context window** native
- **32T+ tokens pretrained** + two-stage post-training (independent domain experts → on-policy distillation)
- **MIT license** — fully open

## Quick Start

> ⚠️ This is a workstation/cluster model. Even Mac Studio M3 Ultra 512GB cannot fit Q3.
> Plan for 768GB+ unified memory or multi-Ultra cluster / 8×A100 80GB / H100 node.

```bash
# Q3_K_M (smallest, 698GB — 768GB+ unified memory)
hf download batiai/DeepSeek-V4-Pro-GGUF --include "*Q3_K_M*"

# Q4_K_M (balanced, 900GB — 1TB+ recommended)
hf download batiai/DeepSeek-V4-Pro-GGUF --include "*Q4_K_M*"
```

> **Higher quants (Q5_K_M 1.12TB / Q8_0 1.67TB)** are archived offline (regenerable from the
> Q8_0 base via `--allow-requantize`). They are not hosted here to keep storage lean — open a
> Discussion if you need them and we'll restore on request.

## Available Quants

| Quant | Size | Shards | Min RAM | Target Hardware |
|-------|-----:|-------:|--------:|-----------------|
| **Q3_K_M** | **698 GB** | 17 × ~43 GB | **768 GB** | M3 Ultra 512GB cluster, 8×A100 80GB |
| **Q4_K_M** | **900 GB** | 21 × ~43 GB | **1 TB** | 2× M3 Ultra 512GB, 16×A100 |
| _Q5_K_M_ | _1.12 TB_ | _26 shards_ | _1.2 TB_ | _archived offline — restore on request_ |
| _Q8_0_ | _1.67 TB_ | _38 shards_ | _1.8 TB_ | _NAS archive (base) — restore on request_ |

All quants signed by BatiAI (`general.author=BatiAI`, `general.url=https://flow.bati.ai`).

> **Note**: IQ-quants (IQ3_XXS / IQ4_XS) are tracked in `bati.cpp` v0.2.0. They require
> imatrix calibration, and `llama-imatrix` currently segfaults during V4 model context init
> in the fork. Will be added once that path is fixed (or once mainline llama.cpp merges
> DeepSeek V4 support). K-quants above use `bati.cpp` v0.1.2's integer-tensor pass-through
> patch + `--allow-requantize` from a Q8_0 base.

## Hardware Reality Check

| Your System | Q3 (698GB) | Q4 (900GB) | Q5 (1.06TB) | Q8 (1.67TB) |
|-------------|:----------:|:----------:|:-----------:|:-----------:|
| Mac 128GB | ❌ | ❌ | ❌ | ❌ |
| Mac 192GB | ❌ | ❌ | ❌ | ❌ |
| Mac 256GB | ❌ | ❌ | ❌ | ❌ |
| Mac M3 Ultra 512GB | ⚠️ heavy swap (impractical) | ❌ | ❌ | ❌ |
| **2× M3 Ultra (1TB cluster)** | ✅ | ✅ tight | ❌ | ❌ |
| **4× M3 Ultra cluster** | ✅ | ✅ | ✅ | ⚠️ |
| **8× A100 80GB (640GB total)** | ⚠️ tight | ❌ | ❌ | ❌ |
| **8× H100 80GB (640GB total)** | ⚠️ tight | ❌ | ❌ | ❌ |
| **8× H200 141GB (1.1TB total)** | ✅ Fast | ✅ Fast | ✅ tight | ❌ |
| **DGX H200 / H100 node 1TB+** | ✅ Fast | ✅ Fast | ✅ | ⚠️ |
| **Multi-node H100/H200 cluster** | ✅ | ✅ | ✅ | ✅ |

**Bottom line**: V4-Pro is **not** a consumer Mac model. For Mac users with ≤256GB, use
[`batiai/DeepSeek-V4-Flash-GGUF`](https://huggingface.co/batiai/DeepSeek-V4-Flash-GGUF)
(284B-A13B, 127-282 GB) for the same architecture family in actually-runnable sizes.

## How to run inference (build `bati.cpp`)

```bash
# 1. Clone + build BatiAI's inference library
git clone https://github.com/batiai/bati.cpp.git
cd bati.cpp
cmake -B build -DGGML_CUDA=ON               # Linux (recommended for V4-Pro scale)
# or: cmake -B build -DGGML_METAL=ON         # macOS (multi-Ultra cluster only)
cmake --build build -j 16 --target llama-cli llama-gguf-split llama-server

# 2. Download a quant + merge shards (Q3 example, 698GB → single GGUF)
hf download batiai/DeepSeek-V4-Pro-GGUF \
    --include "*Q3_K_M*" --local-dir ./v4-pro
build/bin/llama-gguf-split --merge \
    ./v4-pro/deepseek-ai-DeepSeek-V4-Pro-Q3_K_M-00001-of-00017.gguf \
    ./v4-pro/merged-Q3_K_M.gguf

# 3. Inference (CLI, single-node minimum spec)
build/bin/llama-cli \
    -m ./v4-pro/merged-Q3_K_M.gguf \
    -cnv -ngl 99 -c 8192 \
    --reasoning on --reasoning-budget 8192

# 4. Or run as a server (recommended for production)
build/bin/llama-server \
    -m ./v4-pro/merged-Q3_K_M.gguf \
    -ngl 99 -c 32768 --port 8080
```

## Reasoning mode (DeepSeek-V4-Pro-Max)

DeepSeek-V4-Pro's "Max" mode uses **extended reasoning budget** for hardest tasks. Enable via:

```bash
build/bin/llama-cli -m merged.gguf --reasoning on --reasoning-budget 32768 -c 65536
```

DeepSeek-V4-Flash-Max approaches Pro-level reasoning with a larger budget, but for pure
knowledge tasks and the most complex agentic workflows, Pro retains a clear lead per the
official release notes.

## Model details

- **Source**: [deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- **Architecture**: 1.6T total / 49B active MoE — 61 layers, 7168 hidden, 384 routed experts (top-6), 1 KV head
- **Attention**: CSA + HCA hybrid (1M native context)
- **Optimizer**: Muon (training)
- **Innovation**: Manifold-Constrained Hyper-Connections (mHC) for residual signal propagation
- **Original precision**: FP4 + FP8 mixed (FP4 expert weights, FP8 attention) — `quantization_config` MXFP4 spec
- **This GGUF**: Q8_0 dequantization base → K-quants via `--allow-requantize`
- **License**: MIT

## Quantization story (1.6T = engineering exercise)

V4-Pro is the largest open-weights model in BatiAI's catalog and required significant
infrastructure tuning. Documented for future 1T+ MoE work:

- **Source size**: 805 GB safetensors (FP4 mixed precision)
- **Q8_0 dequantized**: 1.67 TB (2.07× FP4→Q8 expansion factor)
- **K-quants from Q8 base** via `--allow-requantize` (avoids BF16 intermediate)
- **Memory peak**: ~1.3 TB RAM+swap during convert (single 503GB-RAM machine + 1.2TB swap)
- **Disk allocation**: NFS overflow to NAS — convert outfile directly to network storage
  to escape the 4TB local SSD limit (Q8 base + safetensors > 2.5 TB combined active size)
- **Convert tool**: `bati.cpp` v0.1.2 `convert_hf_to_gguf.py` (FP4 → Q8 direct path, no BF16)
- **K-quants pipeline**: `llama-quantize --allow-requantize` from Q8 first shard

This GGUF is the **second public V4-Pro quantization** after `teamblobfish/DeepSeek-V4-Pro-GGUF`,
and the first with **BatiAI metadata signing** + full Q3/Q4/Q5/Q8 K-quant matrix.

## What happens after mainline merges V4

When `ggml-org/llama.cpp` master merges DeepSeek V4 support:

1. Rebuild with mainline + run imatrix calibration (wikitext-2, 200 chunks — projected ~24 hours for 1.6T MoE)
2. Add **IQ3_XXS, IQ4_XS** quants (better quality at same/smaller size than Q3/Q4 K-quants)
3. Run real-hardware benchmarks (M3 Ultra cluster + H200 cluster)
4. `bati.cpp`'s V4 support transitions to read-only archive (users migrate to mainline)

Watch this repo or the upstream [DeepSeek V4 llama.cpp tracking issue](https://github.com/ggml-org/llama.cpp/issues/) for the update.

## BatiAI signing

All GGUFs in this repo carry:
- `general.author = BatiAI`
- `general.url = https://flow.bati.ai`

## About `bati.cpp`

[`batiai/bati.cpp`](https://github.com/batiai/bati.cpp) is BatiAI's own inference library —
a `llama.cpp`-based fork focused on Apple Silicon, frontier-model early access, and BatiAI's
quantization standard. Built on top of [`ggml-org/llama.cpp`](https://github.com/ggml-org/llama.cpp)
and [`antirez/llama.cpp-deepseek-v4-flash`](https://github.com/antirez/llama.cpp-deepseek-v4-flash)
(all MIT). See `bati.cpp`'s `ATTRIBUTION.md` for full credits.

## License

Inherits the source model license: **MIT**.

## About BatiFlow

[BatiFlow](https://flow.bati.ai) — free on-device AI automation for Mac.

<!-- BENCH-START -->
*Benchmarks will be added once Mac M3 Ultra cluster / H200 node measurements complete.*
<!-- BENCH-END -->
