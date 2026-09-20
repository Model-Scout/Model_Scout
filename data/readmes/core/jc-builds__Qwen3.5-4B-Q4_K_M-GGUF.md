---
license: apache-2.0
language:
  - en
  - zh
  - ja
  - ko
  - fr
  - de
  - es
  - pt
  - ru
  - ar
  - it
  - tr
  - nl
  - hi
tags:
  - qwen
  - qwen3.5
  - gguf
  - on-device
  - ios
  - mobile
  - thinking
  - hybrid-attention
  - deltanet
model_name: Qwen3.5-4B Q4_K_M GGUF
base_model: Qwen/Qwen3.5-4B
quantized_by: jc-builds
pipeline_tag: text-generation
---

# Qwen3.5-4B Q4_K_M GGUF

> **4-bit quantized GGUF** of [Qwen/Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) optimized for **on-device iOS inference** via [llama.cpp](https://github.com/ggml-org/llama.cpp).

| Property | Value |
|---|---|
| **Parameters** | 4 billion |
| **Quantization** | Q4_K_M (4-bit, medium quality) |
| **File Size** | 2.6 GB |
| **Context Window** | 262,144 tokens (native) |
| **Architecture** | Hybrid Gated DeltaNet + Attention |
| **License** | Apache 2.0 |
| **Languages** | 201 languages/dialects |

## Key Features

- **Thinking Mode**: Outputs `<think>...</think>` tags for chain-of-thought reasoning
- **Hybrid Architecture**: 3:1 ratio of Gated DeltaNet (linear attention) to full softmax attention, enabling near-constant memory usage
- **Natively Multimodal**: Trained with early vision fusion (vision encoder available separately)
- **Massive Context**: 262K native, extendable to 1M+ with YaRN
- **On-Device Optimized**: Designed for mobile and edge deployment

## Benchmarks

### MMLU-Pro: Qwen3.5-4B vs Competitors

![MMLU-Pro Comparison](mmlu_pro_4b.png)

The 4B model scores **79.1 on MMLU-Pro**, dramatically outperforming Phi-4-mini (52.8), Qwen2.5-3B (44.7), Llama-3.2-3B (39.2), and Mistral-3B (35.3).

### Qwen3.5-4B vs Qwen3-30B (7.5x larger)

![4B vs 30B](4b_vs_30b.png)

Despite being **7.5x smaller**, the 4B model matches or beats Qwen3-30B on GPQA Diamond, IFEval, HMMT math, and tool use benchmarks.

### On-Device Inference Speed

![Speed Comparison](speed.png)

### Vision Capabilities

![Vision Benchmarks](vision.png)

Both 4B and 9B models outperform the dedicated Qwen3-VL-30B vision model on most benchmarks.

### Full Benchmark Table

| Benchmark | Qwen3.5-4B | Qwen3-30B | Qwen3-80B |
|---|---|---|---|
| **MMLU-Pro** | 79.1 | 80.9 | 82.7 |
| **MMLU-Redux** | 88.8 | 91.4 | 92.5 |
| **GPQA Diamond** | 76.2 | 73.4 | 77.2 |
| **IFEval** | 89.8 | 88.9 | 88.9 |
| **HMMT Feb 25** | 74.0 | 63.1 | 73.7 |
| **LiveCodeBench v6** | 55.8 | 66.0 | 68.7 |
| **BFCL-V4 (Tool Use)** | 50.3 | 42.4 | - |
| **MMMU (Vision)** | 77.6 | - | - |
| **C-Eval** | 85.1 | 87.4 | 89.7 |

## Device Compatibility

| Device | RAM | Compatible | Speed |
|---|---|---|---|
| iPhone 16 Pro / Pro Max | 8 GB | Yes | ~30-38 tok/s |
| iPhone 16 / 16e | 8 GB | Yes | ~28-35 tok/s |
| iPhone 15 Pro / Pro Max | 8 GB | Yes | ~28-38 tok/s |
| iPhone 15 / 14 Pro | 6 GB | Marginal | ~15-20 tok/s |
| iPhone 14 and older | 4-6 GB | Not recommended | - |
| iPad Pro (M-series) | 8-16 GB | Yes | ~35-45 tok/s |
| Mac (Apple Silicon) | 8+ GB | Yes | ~40-60 tok/s |

## Usage

### With llama.cpp

```bash
# Download
huggingface-cli download jc-builds/Qwen3.5-4B-Q4_K_M-GGUF Qwen3.5-4B-Q4_K_M.gguf

# Run (with thinking mode)
./llama-cli -m Qwen3.5-4B-Q4_K_M.gguf -p "What is the sum of the first 100 prime numbers?" -ngl 99
```

### With Ollama

```bash
ollama run qwen3.5:4b
```

### In HaploAI (iOS)

This model is available directly in the [HaploAI](https://apps.apple.com/app/haploai/id6503772307) iOS app (v1.18+). Download it from the model selection page.

## Prompt Format

Uses ChatML format:

```
<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
Hello!<|im_end|>
<|im_start|>assistant
```

### Thinking Mode

The model uses `<think>` tags for reasoning:

```
<|im_start|>assistant
<think>
Let me work through this step by step...
</think>
The answer is 42.
```

## Architecture Details

Qwen3.5 introduces a novel **hybrid Gated DeltaNet + Gated Attention** architecture:

- **3:1 ratio**: 3 layers of Gated DeltaNet (linear attention) per 1 layer of full softmax attention
- **32 total layers**: 8 blocks x (3 DeltaNet + 1 Attention)
- **Near-constant memory**: DeltaNet layers maintain bounded memory independent of sequence length
- **GQA**: 16 query heads, 4 KV heads for attention layers
- **RoPE**: `theta=10,000,000` with YaRN extension to 1M+ tokens

## Credits

- **Original model**: [Qwen/Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) by Alibaba Cloud
- **GGUF conversion**: [Unsloth](https://huggingface.co/unsloth/Qwen3.5-4B-GGUF)
- **Quantization**: Q4_K_M via llama.cpp
- **Optimized for iOS**: [jc-builds](https://huggingface.co/jc-builds)
