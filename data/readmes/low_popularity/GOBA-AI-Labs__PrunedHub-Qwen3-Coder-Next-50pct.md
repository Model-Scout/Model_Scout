---
license: apache-2.0
base_model: Qwen/Qwen3-Coder-Next
tags:
  - moe
  - pruning
  - expert-pruning
  - mixture-of-experts
  - gguf
  - goba-ai-labs
  - prunedhub
  - moe-stream
  - layer-adaptive-pruning
  - coding
  - reasoning
model_name: PrunedHub Qwen3-Coder-Next-50pct
pipeline_tag: text-generation
language:
  - en
  - ja
  - zh
  - ko
---

# PrunedHub Qwen3-Coder-Next-50pct — MoE-Stream Edition

**50% Expert Pruning — 80B → 24 GB** while retaining 93.5% of original quality.

Half of all MoE experts removed from [Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next) using GOBA-AI-Labs' proprietary calibration-based expert optimization, achieving extreme compression with minimal quality loss.

> **Inference Engine**: This model uses **layer-adaptive pruning** (different expert counts per layer) and requires [moe-stream](https://github.com/GOBA-AI-Labs/moe-stream) for inference. llama.cpp does not currently support the `experts_per_layer` metadata format.

## Model Details

| Property | Value |
|----------|-------|
| Base Model | Qwen/Qwen3-Coder-Next |
| Architecture | Hybrid MoE (DeltaNet + Attention) |
| Original Size | 45 GB (Q4_K_M) |
| **Pruned Size** | **24.4 GB** (Q4_K_M) |
| Experts per Layer | **Layer-adaptive** (226–259, avg ~250, from 512) |
| MoE Layers | 48 |
| Routing | Top-8 |
| Quantization | Q4_K_M |
| Inference Engine | **[moe-stream](https://github.com/GOBA-AI-Labs/moe-stream)** (required) |
| License | Apache 2.0 |

## Benchmark Results

| Benchmark | Original (512 experts) | **50% Pruned (~256 experts)** | Delta |
|-----------|----------------------|----------------------------|-------|
| **MMLU** (0-shot, 100Q) | 77% | **72%** | -5pp |
| **HumanEval** (50Q) | 74% | **72%** | -2pp |
| **LCB Easy** (pass@1, 30Q) | — | **83.3%** | — |

**93.5% of original MMLU quality retained** with 50% of all experts removed.

## Size Comparison

| Metric | Original | 50% Pruned | Savings |
|--------|----------|-----------|---------|
| File Size (Q4_K_M) | 45 GB | **24.4 GB** | **-45.8%** |
| Total Experts | 24,576 | **12,015** | -51.1% |
| Layers | 48 | 48 | — |

## Why This Matters

- **45 GB → 24 GB**: The original model requires 48+ GB RAM. This pruned version fits in 24 GB, making it accessible on consumer hardware
- **Outperforms Q2 quantization**: At similar size (~24 GB), Q2 quantization typically degrades quality by 15-20pp. Our expert pruning loses only 5pp
- **Expert pruning > aggressive quantization**: Removing redundant computation paths preserves model capability better than reducing numerical precision

## Usage

This model requires [moe-stream](https://github.com/GOBA-AI-Labs/moe-stream) for inference due to its layer-adaptive expert structure.

### Install

```bash
git clone https://github.com/GOBA-AI-Labs/moe-stream
cd moe-stream
cargo build --release --features metal,accelerate

# Download model
huggingface-cli download goba-ai-labs/PrunedHub-Qwen3-Coder-Next-50pct \
  --local-dir models/
```

### CLI Inference

```bash
# Text generation
./target/release/moe-stream models/PrunedHub-Qwen3-Coder-Next-50pct-Q4_K_M.gguf 512 \
  --prompt "def fibonacci(n):" --stream \
  --preload-gates --preload-attn
```

### OpenAI-Compatible HTTP Server

```bash
# Start server
./target/release/moe-stream-server \
  --model models/PrunedHub-Qwen3-Coder-Next-50pct-Q4_K_M.gguf --port 11434

# Test with curl
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"local","messages":[{"role":"user","content":"Write a Python function to sort a linked list"}],"stream":true}'
```

### Python

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="unused")
response = client.chat.completions.create(
    model="local",
    messages=[{"role": "user", "content": "Implement binary search in Rust"}],
    stream=True
)
for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

### Why not llama.cpp?

This model uses **layer-adaptive pruning**, meaning each layer retains a different number of experts. The per-layer expert counts are stored in the `experts_per_layer` GGUF metadata field, which llama.cpp does not currently support. moe-stream reads this metadata and correctly routes tokens to the available experts in each layer.

## Methodology

- **Calibration-based importance scoring**: Expert importance is measured through actual inference behavior on diverse workloads (academic text, code, mathematics), not just weight magnitude. This is critical at 50% pruning where static analysis would cause severe quality degradation
- **Layer-adaptive expert allocation**: Each of the 48 MoE layers retains a dynamically determined number of experts. Some layers are more sensitive to pruning than others — adaptive allocation preserves quality where it matters most
- **Expert pruning vs quantization**: At ~24 GB, aggressive quantization (Q2/Q3) would degrade all computations uniformly. Expert pruning instead removes entire redundant computation paths while keeping the remaining experts at full Q4 precision, preserving reasoning capability
- **Cross-architecture validated**: The same methodology has been validated on GPT-OSS-20B (lossless at 12.5% pruning) and Qwen3-30B-A3B (near-lossless at 20% pruning), demonstrating generalization across MoE architectures

## Inference Engine: moe-stream

[moe-stream](https://github.com/GOBA-AI-Labs/moe-stream) is a Rust-based MoE inference engine by GOBA-AI-Labs.

| Feature | Details |
|---------|---------|
| Inference Modes | GPU Resident / GPU Hybrid / SSD Streaming (auto-selected) |
| GPU Support | Apple Metal / NVIDIA CUDA |
| Quantization | Q2K-Q8K, MXFP4, F16, F32 (13 formats) |
| API | OpenAI-compatible HTTP / JSONL / MCP |
| Special | Q4 Quantized MatMul (+79% speedup), Dynamic K |

## Citation

```bibtex
@misc{goba-ai-labs-prunedhub-qwen3-coder-next-50pct,
  title={PrunedHub Qwen3-Coder-Next-50pct: Extreme MoE Compression via Expert Pruning},
  author={GOBA-AI-Labs},
  year={2026},
  url={https://huggingface.co/GOBA-AI-Labs/PrunedHub-Qwen3-Coder-Next-50pct}
}
```

## Links

- [GOBA AI Labs](https://goba-ai-labs.github.io) — project website
- [moe-stream](https://github.com/GOBA-AI-Labs/moe-stream) — inference engine (required)
- [GOBA-AI-Labs on HuggingFace](https://huggingface.co/GOBA-AI-Labs)
- [Base Model: Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next)
- [PrunedHub GPT-OSS-20B-28x](https://huggingface.co/GOBA-AI-Labs/PrunedHub-GPT-OSS-20B-28x) — llama.cpp compatible
- [Support GOBA-AI-Labs on Ko-fi](https://ko-fi.com/gobaailabs)
