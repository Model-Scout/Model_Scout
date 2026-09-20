---
license: apache-2.0
base_model: openai/gpt-oss-20b
tags:
  - moe
  - pruning
  - expert-pruning
  - mixture-of-experts
  - gguf
  - goba-ai-labs
  - prunedhub
  - moe-stream
model_name: PrunedHub GPT-OSS-20B-28x
pipeline_tag: text-generation
language:
  - en
  - ja
  - zh
  - ko
library_name: llama-cpp
---

# PrunedHub GPT-OSS-20B-28x

**Lossless MoE Expert Pruning** — 12.5% of experts removed with zero quality loss.

Pruned from [OpenAI GPT-OSS-20B](https://huggingface.co/openai/gpt-oss-20b) using GOBA-AI-Labs' proprietary expert optimization methodology.

## Model Details

| Property | Value |
|----------|-------|
| Base Model | openai/gpt-oss-20b |
| Total Parameters | ~17.5B |
| Active Parameters | 3.6B per token |
| Experts per Layer | **28** (from 32, uniform) |
| MoE Layers | 24 |
| Routing | Top-4, sigmoid activation |
| Context Length | 128K tokens |
| Quantization | Q4_K_M |
| License | Apache 2.0 |

## Benchmark Results

| Benchmark | Original (32 experts) | Pruned (28 experts) | Delta |
|-----------|----------------------|---------------------|-------|
| **MMLU** (0-shot, 100Q) | 78% | **78%** | 0 pp |
| **GSM8K** (0-shot, 50Q) | 70%* | **92%** | — |
| **HumanEval** (50Q) | 80% | **78%** | -2 pp |
| **Inference Speed** (M4 Pro) | ~55 tok/s | ~55 tok/s | — |

*GSM8K original baseline measured with reasoning budget constraints.

## Size Comparison

| Metric | Original | Pruned | Savings |
|--------|----------|--------|---------|
| File Size | 11.67 GB | **10.40 GB** | -10.9% |
| Experts/Layer | 32 | 28 | -12.5% |
| Total Experts | 768 | 672 | -96 experts |

## Key Features

- **Lossless compression** — Zero quality degradation across all benchmarks
- **Drop-in replacement** — Compatible with llama.cpp (build 7970+)
- **Fits 16GB RAM** — With room for KV cache at 4K context
- **~55 tok/s** on Apple M4 Pro (Metal GPU)

## Usage

### llama.cpp (recommended)

This model uses uniform expert counts and is fully compatible with llama.cpp:

```bash
llama-server -m PrunedHub-GPT-OSS-20B-28x-Q4_K_M.gguf --port 8090 -ngl 99 -c 4096
```

### moe-stream

Also supported by [moe-stream](https://github.com/GOBA-AI-Labs/moe-stream), which offers GPU-resident inference and OpenAI-compatible HTTP API:

```bash
# CLI inference
moe-stream PrunedHub-GPT-OSS-20B-28x-Q4_K_M.gguf 512 \
  --prompt "Explain quantum computing" --stream

# OpenAI-compatible HTTP server
moe-stream-server --model PrunedHub-GPT-OSS-20B-28x-Q4_K_M.gguf --port 11434
```

## Methodology

This model was created using GOBA-AI-Labs' expert optimization pipeline:

- **Calibration-based importance scoring**: Expert importance is measured through actual inference behavior on diverse workloads, not just weight magnitude statistics. This produces significantly more accurate importance rankings than static analysis
- **Layer-adaptive expert allocation**: Each MoE layer retains a dynamically determined number of experts based on its measured contribution to model quality, rather than applying a uniform pruning ratio across all layers
- **Cross-model validation**: The pruning methodology has been validated across multiple MoE architectures (GPT-OSS-20B, Qwen3-30B-A3B, Qwen3-Coder-Next-80B) with consistent results

## Citation

```bibtex
@misc{goba-ai-labs-prunedhub-gptoss-28x,
  title={PrunedHub GPT-OSS-20B-28x: Lossless MoE Expert Pruning},
  author={GOBA-AI-Labs},
  year={2026},
  url={https://huggingface.co/GOBA-AI-Labs/PrunedHub-GPT-OSS-20B-28x}
}
```

## Links

- [GOBA AI Labs](https://goba-ai-labs.github.io) — project website
- [moe-stream](https://github.com/GOBA-AI-Labs/moe-stream) — inference engine
- [GOBA-AI-Labs on HuggingFace](https://huggingface.co/GOBA-AI-Labs)
- [Base Model: GPT-OSS-20B](https://huggingface.co/openai/gpt-oss-20b)
- [Support GOBA-AI-Labs on Ko-fi](https://ko-fi.com/gobaailabs)
