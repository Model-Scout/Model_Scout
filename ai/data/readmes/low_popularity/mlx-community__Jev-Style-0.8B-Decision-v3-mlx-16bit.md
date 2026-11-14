---
library_name: mlx
pipeline_tag: text-classification
license: apache-2.0
base_model: chaoliangUNSW/Jev-Style-0.8B-Decision-v3
tags:
  - mlx
  - safetensors
  - apple-silicon
  - jev-style
  - qwen3_5_text
  - text-generation
  - decision-model
  - transformers
  - system-one
  - calibration
  - classification
  - long-context
  - multilingual
  - qwen3.5
  - on-device
  - llm-routing
  - guardrails
  - text-classification
  - en
  - zh
  - ar
  - bg
  - de
  - el
  - es
  - fr
  - hi
  - ja
  - ko
  - pt
  - ru
  - sw
  - ta
  - th
  - tr
  - ur
  - vi
  - license:apache-2.0
---

# Jev-Style-0.8B-Decision-v3-mlx-16bit

> 16-bit MLX conversion of [chaoliangUNSW/Jev-Style-0.8B-Decision-v3](https://huggingface.co/chaoliangUNSW/Jev-Style-0.8B-Decision-v3) optimized for Apple Silicon native GPU inference.

**Converted by**: [SirSahOl](https://huggingface.co/SirSahOl)  
**Source Model**: [chaoliangUNSW/Jev-Style-0.8B-Decision-v3](https://huggingface.co/chaoliangUNSW/Jev-Style-0.8B-Decision-v3)  
**Framework**: [MLX](https://github.com/ml-explore/mlx) by Apple  
**Quantization**: 16-bit (Average 16.00 (unquantized bfloat16) bits per weight)  
**Format**: safetensors  
**License**: apache-2.0  

---

## Model Details

*   **Architecture**: Qwen3_5ForCausalLM
*   **Parameters**: 0.8B
*   **Context Length**: 262,144 tokens
*   **Format**: MLX (Apple Silicon native GPU format)
*   **Quantization**: 16-bit (Average 16.00 (unquantized bfloat16) bits per weight)
*   **Active VRAM Footprint**: ~1940 MB (Minimum recommended: 8 GB Unified Memory)

---

## Quick Start

### Installation

```bash
pip install mlx-lm
```

### Usage

#### CLI

```bash
# Chat interactively
mlx_lm.chat --model SirSahOl/Jev-Style-0.8B-Decision-v3-mlx-16bit

# Generate text
mlx_lm.generate --model SirSahOl/Jev-Style-0.8B-Decision-v3-mlx-16bit --prompt "Write a short poem about artificial intelligence."
```

#### Python API (with Chat Template)

```python
from mlx_lm import load, generate

model, tokenizer = load("SirSahOl/Jev-Style-0.8B-Decision-v3-mlx-16bit")

messages = [
    {"role": "user", "content": "Explain quantum superposition in simple terms."}
]
prompt = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)

response = generate(model, tokenizer, prompt=prompt, verbose=True)
print(response)
```

---

## Performance Benchmarks

### Measured Benchmarks (Apple M1)

| Metric | 16-bit |
| :--- | :--- |
| **Tokens/sec** | **29.83** |
| **TTFT** | 33.54 ms |
| **Peak Memory** | 495.8 MB |

> Benchmarked on **Apple M1** with **8GB** unified memory.
> Average over 5 runs with 256 max tokens.

---

## Multi-Quantization Comparison

Evaluate your hardware budget and choose the optimal precision:

| Variant | Disk Size | VRAM Footprint | Target Apple Silicon Hardware | Key Advantage |
| :--- | :--- | :--- | :--- | :--- |
| **[4-bit MLX](https://huggingface.co/SirSahOl/Jev-Style-0.8B-Decision-v3-mlx-4bit)** | ~450 MB | ~490 MB | M1 / M2 / M3 / M4 (8GB+ Unified Memory) | Ultra-compact footprint, maximum generation speed; negligible memory pressure. |
| **[8-bit MLX](https://huggingface.co/SirSahOl/Jev-Style-0.8B-Decision-v3-mlx-8bit)** | ~855 MB | ~900 MB | M1 / M2 / M3 / M4 (8GB+ Unified Memory) | Near-lossless precision with an extremely lightweight footprint. |
| **16-bit MLX** (This Repository) | ~1620 MB | ~1690 MB | M1 / M2 / M3 / M4 (8GB+ Unified Memory) | Full unquantized precision; zero perplexity penalty for reference evaluation. |

---

## Who Should Use This?

| Your Hardware | Recommended Quantization |
|---------------|--------------------------|
| M1/M2/M3/M4 (8GB – 16GB) | **4-bit** — Best balance of speed, low memory, and multitasking capability |
| M1/M2/M3/M4 Pro/Max (18GB – 36GB) | **8-bit** — Higher quality reasoning with comfortable memory headroom |
| M1/M2/M3/M4 Max/Ultra (36GB – 192GB) | **16-bit** — Unquantized full precision, zero quality degradation |

**General guidance:**
- Use **4-bit** if you want to run this model alongside IDEs, browsers, and background development tools.
- Use **8-bit** if you have 16GB+ unified memory and require superior reasoning and code accuracy.
- Use **16-bit** for research, benchmarking, evaluation, or high-end workstation deployments.

---

## Other Quantization Variants

| Variant | Link |
|---------|------|
| 4-bit | [SirSahOl/Jev-Style-0.8B-Decision-v3-mlx-4bit](https://huggingface.co/SirSahOl/Jev-Style-0.8B-Decision-v3-mlx-4bit) |
| 8-bit | [SirSahOl/Jev-Style-0.8B-Decision-v3-mlx-8bit](https://huggingface.co/SirSahOl/Jev-Style-0.8B-Decision-v3-mlx-8bit) |
| 16-bit | [SirSahOl/Jev-Style-0.8B-Decision-v3-mlx-16bit](https://huggingface.co/SirSahOl/Jev-Style-0.8B-Decision-v3-mlx-16bit) |

---

## LM Studio & Local Inference Setup Guide

To prevent runaway loops and ensure correct conversational turn-taking, configure custom stop tokens in your local inference runtime:

1. `<|im_start|>`
2. `<|im_end|>`
3. `<|endoftext|>`

### Prompt Template Formatting

*   **System Prefix**: `<|im_start|>system\n`
*   **System Suffix**: `<|im_end|>\n`
*   **User Prefix**: `<|im_start|>user\n`
*   **Assistant Suffix**: `<|im_end|>\n<|im_start|>assistant\n`

### Ollama Quickstart

```dockerfile
FROM SirSahOl/Jev-Style-0.8B-Decision-v3-mlx-16bit
PARAMETER stop "<|im_start|>"
PARAMETER stop "<|im_end|>"
PARAMETER stop "<|endoftext|>"
PARAMETER temperature 0.7
```

```bash
ollama create jev-style-0.8b-decision-v3-mlx-16bit -f Modelfile
ollama run jev-style-0.8b-decision-v3-mlx-16bit
```

---

## Conversion Details

| Property | Value |
|----------|-------|
| **Source Model** | [chaoliangUNSW/Jev-Style-0.8B-Decision-v3](https://huggingface.co/chaoliangUNSW/Jev-Style-0.8B-Decision-v3) |
| **Quantization** | 16-bit |
| **mlx-lm Version** | 0.31.3 |
| **Conversion Time** | 4.43s |
| **Output Size** | 1.4 GB |
| **Date** | 2026-10-13T00:25:16.703768+00:00 |

### Reproduction

To reproduce this conversion:

```bash
pip install mlx-lm==0.31.3
python3 -m mlx_lm.convert --hf-path /Users/z4/.cache/huggingface/hub/models--chaoliangUNSW--Jev-Style-0.8B-Decision-v3/snapshots/b023d1f9c7858fbf01504577a3bfc349ea5c7385 --mlx-path output/b023d1f9c7858fbf01504577a3bfc349ea5c7385-mlx-16bit
```

---

## Limitations & Known Issues

- 4-bit group-wise quantization introduces minor precision loss compared to unquantized weights; for deep mathematical derivations or precision-critical reasoning, test the 8-bit or 16-bit variants.
- High context sequences (>32K tokens) require sufficient unified memory headroom; ensure unified memory is not overcommitted.
- This is a weight-only MLX conversion designed specifically for Apple Silicon GPUs (M1/M2/M3/M4 series).

---

## License

This model conversion inherits the license of the source model: **apache-2.0**.

See the [original model card](https://huggingface.co/chaoliangUNSW/Jev-Style-0.8B-Decision-v3) for full license details.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-10-13 | Initial conversion |

---

*Converted with [MLX Foundry](https://github.com/SirSahOl/mlx-foundry) — a professional pipeline for converting models to Apple MLX format.*
